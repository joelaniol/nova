# Nonce Sentinel Detection & PowerShell Exit Code Resolution

In a traditional flat subprocess (`Process.Start`), the operating system notifies the caller when the process terminates by closing stdout and providing an integer exit code. However, in an interactive terminal session (ConPTY), the underlying shell process (`powershell.exe`) remains alive between commands.

To enable synchronous command execution via [`nova.terminal_run_command`](../../../../mcp-reference/tools/terminal-ops/nova-terminal-run-command.md), Nova implements a **Dynamic Cryptographic Nonce Sentinel Protocol**, **Sliding-Window Tail Scanning**, and **PowerShell Exit Code Disambiguation**.

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Autonomous Agent
    participant Nova as Nova Terminal Engine
    participant Shell as Interactive PowerShell (ConPTY)

    Agent->>Nova: nova.terminal_run_command(sessionId="term_123", command="git status")
    Nova->>Nova: Generate 16-hex nonce: "7a8b9c0d1e2f3a4b"
    Nova->>Shell: Inject: git status; <sentinel_payload>
    Note over Shell: Shell executes "git status", streams stdout/stderr
    Shell-->>Nova: Raw PTY Byte Chunks (Channel 2)
    Nova->>Nova: Sliding-Window Scan (256-byte overlap)
    Shell-->>Nova: Emits Sentinel: "\nNOVAEXIT_7a8b9c0d1e2f3a4b_0\n"
    Nova->>Nova: Match Nonce Sentinel! Extract Exit Code = 0
    Nova-->>Agent: {"exitCode": 0, "output": "On branch main...", "durationMs": 420}
```

---

## 1. The Dynamic Nonce Sentinel Protocol

When an agent submits a command, Nova does not send the raw command string alone. Instead, it appends an automated exit-capture trailer containing a fresh, cryptographically random nonce:

```powershell
<user_command>; $__ec = if ($LASTEXITCODE -ne $null) { $LASTEXITCODE } else { if ($?) { 0 } else { 1 } }; Write-Host "`nNOVAEXIT_7a8b9c0d1e2f3a4b_$__ec"
```

### Why a Dynamic Nonce is Essential
1. **Preventing Accidental Hits:** If an agent runs a script that inspects Nova's documentation or prints logs containing the string `NOVAEXIT`, a static sentinel would trigger premature completion.
2. **Freshness Guarantee:** The 16-character hexadecimal nonce is minted uniquely for each command invocation (`Guid.NewGuid().ToString("N")[..16]`). The scanner ignores any output that does not match the active command's exact nonce.

---

## 2. Sliding-Window Tail Scanning (256-Byte Overlap)

Data emitted by ConPTY arrives across named pipe chunks of arbitrary sizes (from 1 byte to 64 KB depending on OS scheduling):

```
Buffer Chunk 1: [ ... 4090 bytes of git status output ... N O V A E X ]
Buffer Chunk 2: [ I T _ 7 a 8 b 9 c 0 d 1 e 2 f 3 a 4 b _ 0 \n ]
                               ▲
                      Chunk Boundary Split!
```

### The Boundary Split Hazard
If a scanner inspects each buffer chunk independently, a sentinel that straddles the boundary between Chunk 1 and Chunk 2 will never match, causing the tool to hang until execution timeouts expire.

### Nova's Overlap Buffer Architecture
Nova maintains a rolling 256-byte tail window:
* Before scanning incoming Chunk $N$, Nova prepends the last 256 bytes from Chunk $N-1$.
* The search window always contains sufficient contiguous bytes to capture the full sentinel pattern (`~35 bytes`), regardless of where network or pipe packet boundaries fall.
* Once detected, the sentinel trailer is cleanly excised from the returned output text, presenting clean, professional logs to the calling agent.

---

## 3. PowerShell Exit Code Disambiguation (`$LASTEXITCODE` vs. `$?`)

PowerShell uses two distinct mechanisms to track execution success:
1. **`$LASTEXITCODE`:** Captures the numeric exit code returned by native Windows executables (`git.exe`, `cargo.exe`, `python.exe`, `dotnet.exe`).
2. **`$?`:** A boolean (`$true` / `$false`) indicating whether the *immediately preceding* PowerShell cmdlet or statement succeeded.

### The Pitfall
* Built-in PowerShell cmdlets (such as `Get-ChildItem`, `Set-Location`, or `Remove-Item`) **do not update `$LASTEXITCODE`**.
* If a native command fails (setting `$LASTEXITCODE = 1`), and a subsequent PowerShell cmdlet succeeds, inspecting only `$LASTEXITCODE` will mistakenly report failure.
* Conversely, if an earlier command succeeded (`$LASTEXITCODE = 0`) and a subsequent cmdlet fails, inspecting only `$LASTEXITCODE` will report false success.

### Nova's Unified Resolution Logic
Nova's sentinel wrapper evaluates both indicators:

```powershell
$__ec = if ($LASTEXITCODE -ne $null) { $LASTEXITCODE } else { if ($?) { 0 } else { 1 } }
```

* If a native executable was run, its exact integer exit code (e.g., `0`, `1`, `127`) is preserved.
* If a pure PowerShell cmdlet was run, its boolean status is mapped deterministically to standard POSIX convention: `$true \rightarrow 0$`, `$false \rightarrow 1$`.

---

## 4. Related Documentation

* [Command Execution Overview](../README.md)
* [Concurrency Gates & Non-Destructive Timeouts](../concurrency-gate-and-timeouts/README.md)
* [IPC Named Pipe Wire Protocol](../../ipc-wire-protocol/README.md)
* [Terminal Run Command Tool Reference](../../../../mcp-reference/tools/terminal-ops/nova-terminal-run-command.md)
