# Terminal & Console Execution Troubleshooting

This guide resolves common execution failures, timeouts, concurrency blocks, and named pipe connection issues across Nova's integrated terminal dock and programmatic MCP terminal tools (`nova.terminal_*`).

---

## Quick Symptom Checker

| Symptom / Error Code | Root Cause | Primary Resolution |
| :--- | :--- | :--- |
| `command_rejected` ("Another terminal_run_command is still running...") | Concurrency Gate active on that session. | Wait for the previous command, read progress with `nova.terminal_read`, or open a separate session via `nova.terminal_open`. |
| `command_rejected` ("The previous terminal_run_command... ended before its command finished...") | A prior command timed out or was cancelled, and is still running in the background. | Read output via `nova.terminal_read`, or send `nova.terminal_send_key(sessionId=..., key='Ctrl+C')` to interrupt it. |
| `command_rejected` ("Multi-line commands are not supported...") | The command string contains embedded newline characters (`\r` or `\n`). | Send single-line commands with `nova.terminal_run_command`, or send raw multi-line scripts using `nova.terminal_write`. |
| Tool times out after 30 seconds (`timedOut: true`) | The command took longer than `timeoutSeconds` to output its completion sentinel. | Increase `timeoutSeconds` (up to 3600), or inspect ongoing progress via `nova.terminal_read`. |
| Named pipe connection fails (`protocol_version`) | Nova was updated while an older `NovaBrowser.TerminalRunner.exe` is still active. | Close Nova, terminate old runner processes in Task Manager, or click **Reinstall runner** in Settings. |
| Runner terminates with exit code `3` | Windows console handle acquisition failed. | Ensure TerminalRunner is executed in a standard desktop logon session capable of allocating a console handle. |

---

## 1. Concurrency Blocks & Rejected Commands (`command_rejected`)

Nova's terminal subsystem enforces strict safeguards against typing collisions. When a command is rejected, inspect the specific error message:

### 1.1 "Another terminal_run_command is still running in this session"
* **Cause:** A single terminal session behaves like a physical console: typing two commands at the same time causes keystrokes to interleave, garbling inputs and corrupting execution output. Nova enforces a strict single-command gate (`SemaphoreSlim(1, 1)`) per session.
* **Resolution:**
  1. Poll the running command's output using `nova.terminal_read(sessionId='<id>')`.
  2. If parallel execution is required, spawn a dedicated terminal session using `nova.terminal_open()` with its own working directory.

### 1.2 "The previous terminal_run_command ended before its command finished... and is still running"
* **Cause:** A previous call to `nova.terminal_run_command` reached its timeout deadline or was cancelled by the client. **The shell process does not die on timeout.** The shell continues running the long-running task in the background. Nova sets an internal `PendingRunMarker` to prevent subsequent commands from being blindly typed into a busy process (e.g. accidentally typing a build command into an interactive confirmation prompt).
* **Resolution:**
  1. Inspect whether the task finished by calling `nova.terminal_read(sessionId='<id>')`.
  2. If the task is hanging or needs to be aborted, send an interrupt signal:
     ```json
     {
       "name": "nova.terminal_send_key",
       "arguments": {
         "sessionId": "term-session-1",
         "key": "Ctrl+C"
       }
     }
     ```
     Sending `Ctrl+C` clears the pending run marker, returning the shell prompt to an idle state.

### 1.3 "Multi-line commands are not supported by run_command"
* **Cause:** `nova.terminal_run_command` works by appending an automated completion sentinel (`NOVAEXIT_<nonce>`) to capture the command's exit code. If a command string contains embedded newlines (`\r` or `\n`), intermediate lines execute before the sentinel is submitted, causing ambiguous exit code attribution.
* **Resolution:**
  * For sequential commands, execute them one by one or join them on a single line using PowerShell operators (`;` or `&&`).
  * For raw multiline scripts or interactive input blocks, use `nova.terminal_write`:
    ```json
    {
      "name": "nova.terminal_write",
      "arguments": {
        "sessionId": "term-session-1",
        "data": "Get-Process | Where-Object CPU -gt 10\r"
      }
    }
    ```

---

## 2. Command Timeouts & Hanging Background Shells

### Symptoms
* An agent runs a command (e.g. `npm install` or `docker build`), and the tool call returns `{ "timedOut": true, "exitCode": null }`.
* Subsequent commands are blocked.

### Key Behavioral Guarantee: Shell Processes Survive Timeouts
Reaching `timeoutSeconds` terminates only the waiting RPC tool call; **it does not terminate the underlying process.** The compilation or build script continues running inside `NovaBrowser.TerminalRunner.exe`.

### Resolution Workflow:
1. **Never immediately re-run the same command.** Re-running creates duplicate processes and locks workspace files.
2. **Monitor execution progress:** Call `nova.terminal_read(sessionId='<id>')` periodically. If the byte offset advances, the task is actively progressing.
3. **Configure higher timeout bounds:** For known long-running operations (such as container image builds or extensive end-to-end test suites), specify an explicit timeout up to 3600 seconds (1 hour):
   ```json
   {
     "name": "nova.terminal_run_command",
     "arguments": {
       "sessionId": "term-session-1",
       "command": "dotnet test --no-build",
       "timeoutSeconds": 300
     }
   }
   ```

---

## 3. Terminal Runner Disconnects & Handshake Failures

TerminalRunner operates as an independent external process (`NovaBrowser.TerminalRunner.exe`) communicating over a duplex named pipe (`novabrowser-terminal-runner-{profileId}`).

### 3.1 Protocol Version Mismatches (`protocol_version`)
* **Symptom:** Terminal initialization fails, or `nova.terminal_open` returns an error stating that the terminal runner version does not match Nova.
* **Cause:** Nova AI Workspace was updated to a newer version, but a background `NovaBrowser.TerminalRunner.exe` process from the previous installation is still running in memory, holding active sessions.
* **Resolution:**
  1. Close Nova.
  2. Open Windows Task Manager and end any remaining `NovaBrowser.TerminalRunner.exe` processes.
  3. Start Nova again. Nova will automatically launch the updated runner executable.

### 3.2 Authorization Failures (`unauthorized`)
* **Symptom:** The runner immediately closes pipe connections with error code `unauthorized`.
* **Cause:** The capability secret token stored in `%LOCALAPPDATA%\NovaBrowser` does not match the token passed by the client during the `hello` handshake.
* **Resolution:**
  * Open Nova and navigate to **Menu → Settings → AI & agents → Setup**.
  * Click **Reinstall runner**. Nova will refresh its internal authentication tokens and re-synchronize the launcher binaries.

### 3.3 Exit Code 3 on Startup (`ConsoleBootstrap.ConsoleMode.Failed`)
* **Symptom:** `NovaBrowser.TerminalRunner.exe` terminates immediately with exit code `3`.
* **Cause:** ConPTY requires an active Win32 console handle (`AllocConsole` / `AttachConsole`). If the process is launched inside a restricted non-interactive Windows service or headless session without desktop window station access, console allocation fails.
* **Resolution:** Ensure Nova and TerminalRunner are executed within a standard interactive Windows user logon session.

---

## 4. Slow Consumer View-Drop & Buffer Reconnection

### Symptoms
* An interactive terminal dock tab stops updating output during high-volume logging, while the underlying process continues running.
* Background logs show that a session attachment was cancelled.

### Cause: The 32-Frame Bounded Output Channel
To prevent runaway memory consumption when a process outputs data faster than WinUI or an agent can consume it, TerminalRunner limits its output queue to 32 frames in flight (`BoundedChannelFullMode.DropWrite`). If Nova falls behind, the runner cancels the view attachment to protect system stability.

### Resolution:
1. **The underlying shell is unharmed.** The in-memory ring buffer continues recording all console output.
2. **Re-attaching to the stream:**
   * In the desktop UI: Minimizing and re-expanding the terminal dock reconnects the view and replays recent history.
   * Over MCP: Call `nova.terminal_read(sessionId='<id>', maxBytes=65536)` to fetch the latest output tail.

---

## 5. Development Server Continuity & The 24-Hour Orphan Policy

### Why Dev Servers Survive Nova Reboots
When you launch a development server (e.g. `npm run dev` or Python web service) inside a terminal workspace, the process lives inside `NovaBrowser.TerminalRunner.exe`. If you close Nova, reload the window, or install an update:
* The runner helper stays alive in the background.
* Your server continues listening on its local port (e.g. `http://localhost:3000`).
* Reopening Nova automatically rediscovers the existing terminal runner and restores the connection.

### The 24-Hour Cleanup Invariant
If Nova is closed and never reopened, the runner maintains live sessions for **up to 24 hours (`OrphanExitGraceHours`)**. After 24 hours of total disconnection from Nova, the runner safely terminates all orphaned sessions and exits, releasing system memory and file handles.

---

## Related Documentation

* **[TerminalRunner Component Architecture](../components/terminal-runner.md)** — In-depth architectural specification of ConPTY, Job Objects, and framing protocols.
* **[Integrated Terminal Dock User Guide](../user-guide/tools/terminal.md)** — Interactive dock layout, workspaces, and keyboard shortcuts.
* **[MCP Terminal Operations Catalog](../mcp-reference/tools/terminal-ops/README.md)** — Parameter reference for all programmatic terminal tools.
* **[Diagnostics & Logs](diagnostics.md)** — Locating crash dumps and process diagnostic logs.
