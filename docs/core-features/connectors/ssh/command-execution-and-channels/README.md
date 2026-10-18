# SSH Command Execution & Channel Isolation

The SSH command execution subsystem allows autonomous agents to execute remote diagnostics, deployment scripts, and batch system commands over SSH-2 (RFC 4251–4254). Nova enforces a strict channel-isolation model, cryptographic host-key verification, output flood protection, empirical exit status accounting, and operation-level idempotency.

```mermaid
flowchart TD
    subgraph AgentCall["Agent Invocation"]
        RunCall["nova.ssh_run\n(command / commands, timeouts, idempotency)"]
    end

    subgraph SecurityGate["Security & Policy Gate"]
        HostKeyGate["Host-Key Verification Gate\n(Settings Human Confirmation Required)"]
        ExecGate["Capability: 'process.exec'\n(Explicit Grant Stage)"]
        MutatingPolicy["MutatingRemote Confirmation Policy"]
    end

    subgraph ExecutionEngine["SSH Execution Engine"]
        ChannelManager["SSH-2 Channel Manager\n(Isolated Exec Channels)"]
        BatchController["Batch Controller\n(Sequential execution, stopOnError)"]
        OutputCapture["Output Capture & Flood Engine\n(Head/Tail 256 KB, 64 MB ceiling, SHA-256)"]
        SecretRedactor["Secret Redactor\n(Hashes, PEM Keys, Passwords)"]
        Ledger["Idempotency Ledger\n(operationId, 24h Retention)"]
    end

    subgraph RemoteHost["Remote SSH Server"]
        RemoteDaemon["sshd Daemon"]
        Process1["Process 1: /bin/sh -c '...'"]
        Process2["Process 2: /bin/sh -c '...'"]
    end

    RunCall --> Ledger --> HostKeyGate --> ExecGate --> MutatingPolicy --> ChannelManager
    ChannelManager --> BatchController
    BatchController --> Process1 --> OutputCapture
    BatchController --> Process2 --> OutputCapture
    OutputCapture --> SecretRedactor --> Ledger
```

---

## 1. The Channel Isolation Model

In SSH-2, command execution occurs within dedicated `session` channels via the `exec` request type. Nova implements strict channel boundaries:

```mermaid
sequenceDiagram
    participant Agent as Autonomous Agent
    participant Nova as Nova SSH Runner
    participant Server as Remote SSH Server

    Note over Agent,Server: Single TCP & SSH Transport Handshake
    Agent->>Nova: nova.ssh_run(commands=["cd /var/www", "ls -la"])
    
    Note over Nova,Server: Command 1 in Channel 0
    Nova->>Server: SSH_MSG_CHANNEL_OPEN (session 0)
    Server-->>Nova: SSH_MSG_CHANNEL_OPEN_CONFIRMATION
    Nova->>Server: SSH_MSG_CHANNEL_REQUEST ("exec", "cd /var/www")
    Server-->>Nova: Channel 0 Output & Exit Status 0
    Nova->>Server: SSH_MSG_CHANNEL_CLOSE (session 0)

    Note over Nova,Server: Command 2 in Channel 1 (Independent State!)
    Nova->>Server: SSH_MSG_CHANNEL_OPEN (session 1)
    Server-->>Nova: SSH_MSG_CHANNEL_OPEN_CONFIRMATION
    Nova->>Server: SSH_MSG_CHANNEL_REQUEST ("exec", "ls -la")
    Server-->>Nova: Channel 1 Output & Exit Status 0 (Runs in default HOME!)
    Nova->>Server: SSH_MSG_CHANNEL_CLOSE (session 1)

    Nova-->>Agent: Consolidated Batch Results
```

### Critical Channel Invariants

1. **State Independence:** Each command line in a `commands` batch runs in its own distinct SSH channel. Working directory (`cd`), environment variables (`export FOO=bar`), and shell options do **NOT** carry over to subsequent commands in the array.
2. **Compound Execution Pattern:** To run dependent commands, combine them into a single command line joined with standard shell operators:
   ```json
   {
     "command": "cd /var/www && npm install && npm run build"
   }
   ```
3. **No Interactive Shell / No PTY:** `nova.ssh_run` does not allocate a pseudo-terminal. Interactive commands requiring a TTY (such as interactive password prompts or text editors) will block or fail. For interactive programs or continuous shell input, use [Interactive PTY Terminals](../interactive-pty-terminals/README.md).

---

## 2. Host-Key Verification & Capability Stages

Remote command execution involves elevated trust and requires multiple independent policy gates:

### The Host-Key Verification Gate
To prevent Man-in-the-Middle (MitM) attacks, Nova mandates host-key trust:
* **Zero Blind Trust:** When connecting to a remote host for the first time, Nova captures the server's public key fingerprint.
* **Human Operator Authorization:** Host keys must be reviewed and confirmed by an operator in Nova Settings. **Agents cannot confirm or modify host keys via MCP tools.**
* **Tampering Detection:** If a known host key changes, Nova flags `ssh_host_key_changed` and terminates the connection before transmitting any credentials or commands.

### Capability Stages
Command execution requires the dedicated **`process.exec`** capability stage:
* The `process.exec` grant is independent of the file-transfer `full` grant: being authorized to upload files via SFTP does not silently authorize executing arbitrary commands.
* If `process.exec` is unset, interactive runs prompt once ("Always" persists the grant). Unattended runs (such as scheduled tasks) fail closed until the grant is configured.

---

## 3. Output Bounding, Flood Protection & Secret Redaction

To prevent agent context flooding and host memory exhaustion caused by noisy commands (such as package builds or verbose logs), Nova enforces dual-layer stream management:

```mermaid
graph LR
    subgraph InputStream["Raw SSH Output Stream (Up to 64 MB)"]
        H["Head (First 64 KB)"]
        M["Omitted Middle Data (Counted in sha256)"]
        T["Tail (Last 192 KB)"]
    end

    subgraph Retained["Retained Agent Output (maxOutputBytes = 256 KB)"]
        RH["Preserved Startup Banners & Initial Config"]
        RT["Preserved Tracebacks, Exit Logs & Summaries"]
    end

    H --> RH
    T --> RT
    InputStream -.-> Hash["Continuous SHA-256 Digest"]
```

1. **Head + Tail Retention (`maxOutputBytes`):**
   - Default: **256 KB** per stream (`maxOutputBytes`, range 1 KB to 1 MB).
   - One-quarter is allocated to the stream head (preserving startup banners and initial configuration), and three-quarters is allocated to the stream tail (preserving error messages, stack traces, and exit summaries).
   - The tool output indicates `truncated: true` and reports `omittedBytes`.
2. **Hard Receive Cap (64 MB Flood Limit):**
   - If a runaway process (e.g. `cat /dev/urandom` or an unbuffered loop) generates more than 64 MB, Nova terminates the command with `outcome: "output_limit_exceeded"`.
3. **Continuous SHA-256 Digest:**
   - While streaming and draining data, Nova calculates an incremental SHA-256 hash over the *entire* raw output. Agents can verify whether two runs produced identical output without downloading gigabytes of text.
4. **Automated Secret Redaction (`redactSecrets`):**
   - Automatically sanitizes detected private keys (`-----BEGIN PRIVATE KEY-----`), password hashes, and database connection strings from returned stdout and stderr.

---

## 4. Empirical Exit Status Accounting

Nova never guesses whether a remote command succeeded. The outcome is determined strictly by remote RFC 4254 signals:

| Outcome Code | Description | Success Evaluated As |
| :--- | :--- | :---: |
| `exited` | The server reported an explicit exit status code. | `true` if exitCode in `expectedExitCodes` |
| `signaled` | The process was killed by a remote signal (e.g. SIGKILL, SIGSEGV). | `false` |
| `timed_out` | Nova's `commandTimeoutSeconds` or `overallTimeoutSeconds` expired. | `false` |
| `output_limit_exceeded` | The process exceeded the 64 MB receive limit. | `false` |
| `connection_lost` | The network connection dropped mid-command. | `false` |
| `skipped` | Not started because a previous command in the batch failed and `stopOnError: true`. | `false` |
| `unknown` | The command ran, but the remote server closed the channel without an exit status. | `false` |

---

## 5. Success Markers & Idempotency (`operationId`)

### Success Markers (`expectStdoutRegex`)
To confirm atomic steps without parsing multi-page logs, agents can supply an `expectStdoutRegex`:
* A command is marked `success: true` only if its exit code is expected **and** its retained stdout matches the multiline regex.
* On a matched success, the verbose output body is omitted from the result to conserve context window tokens.

### Idempotency Ledger (`operationId`)
Network hiccups can cause tool calls to disconnect while the remote server is still executing. Supplying an `operationId`:
* Nova registers the operation in an internal idempotency ledger (persisted for 24 hours).
* If an agent repeats the identical call with the same `operationId`, Nova returns the running job or replayed result (`replayed: true`) instead of spawning duplicate commands.

---

## 6. Execution Examples & Schema

### Single Diagnostic Command
```json
// nova.ssh_run
{
  "profileId": "conn_prod_server",
  "command": "systemctl status nginx --no-pager",
  "outputDetail": "compact"
}
```

```json
{
  "content": [
    {
      "type": "text",
      "text": "Command finished with exit code 0."
    }
  ],
  "structuredContent": {
    "profileId": "conn_prod_server",
    "success": true,
    "results": [
      {
        "index": 0,
        "command": "systemctl status nginx --no-pager",
        "outcome": "exited",
        "exitCode": 0,
        "success": true,
        "stdout": "● nginx.service - A high performance web server\n   Loaded: loaded (/lib/systemd/system/nginx.service; enabled)\n   Active: active (running) since Wed 2026-10-14 12:00:00 UTC",
        "stderr": ""
      }
    ]
  }
}
```

### Sequential Batch with `stopOnError`
```json
// nova.ssh_run
{
  "profileId": "conn_prod_server",
  "commands": [
    "git pull origin main",
    "npm run test",
    "systemctl reload node-app"
  ],
  "stopOnError": true,
  "commandTimeoutSeconds": 120
}
```

---

## 7. Practical Agent Recipes

### Recipe 1: Grep Log Search (Non-Zero Exit Allowed)
```json
// Grep returns exit code 1 when no lines match; allow it as expected
// nova.ssh_run
{
  "profileId": "conn_prod_server",
  "command": "grep 'ERROR' /var/log/app.log | tail -n 20",
  "expectedExitCodes": [0, 1]
}
```

### Recipe 2: Provisioning Script via Stdin
```json
// Stream local script directly to remote bash without saving on remote disk
// nova.ssh_run
{
  "profileId": "conn_prod_server",
  "command": "bash -s",
  "stdin": "echo 'Deploying update...'\nmkdir -p /app/data\nchmod 755 /app/data\necho 'Done.'"
}
```

---

## 8. Related Tools & Documentation

* [`nova.ssh_run` Tool Reference](../../../../mcp-reference/tools/connectors-and-mail/nova-ssh-run.md)
* [Background Sessions & Streaming I/O](../background-sessions-and-streaming/README.md)
* [Interactive PTY Terminals](../interactive-pty-terminals/README.md)
* [SSH Architecture Overview](../README.md)
