# `nova.terminal_run_command`

Executes a single command line in an existing session and waits synchronously for its completion.

---

## 1. Overview

`nova.terminal_run_command` submits a command to an active ConPTY session, monitors execution via an end-of-command sentinel, and returns both output and numeric exit code. If execution exceeds `timeoutSeconds`, the session remains open with `reasonCode: "command_timeout"`.

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sessionId` | `string` | Yes | — | — | Session id from terminal_open. |
| `command` | `string` | Yes | — | — | Command line to run (e.g. 'dir', 'git status'). Single line only — embedded newlines are rejected (command_rejected); use terminal_write for raw multi-line input. |
| `timeoutSeconds` | `integer` | No | — | 1–3600 | Max seconds to wait for completion. Default 30. |
| `agentId` | `string` | No | — | — | Accepted for compatibility and ignored: terminal sessions are addressed by sessionId and are not bound to a tab or a tab claim. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `terminal_ops` (load it with `nova.tools_bundle(bundle='terminal_ops')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_run_command",
  "arguments": {
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "command": "git status --short",
    "timeoutSeconds": 15
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": " M src/main.py"
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "output": " M src/main.py\r\n",
    "exitCode": 0
  }
}
```

---

## 4. Operational Best Practices

* **Single-Line Only:** Do not send multi-line scripts in `command`. Use temporary script files or pipe commands.
* **Timeout Recovery:** If `reasonCode: "command_timeout"` is returned, the command is still running. You can check output using `nova.terminal_read` or terminate it via `nova.terminal_send_key(key="Ctrl+C")`.
* **No Commands That Ask for Input:** Completion is detected by a marker line typed after the command. A program that reads input (a confirmation prompt, `Read-Host`, a REPL such as `python`) reads that line as its answer, and the call times out. Drive such programs with `nova.terminal_write` and `nova.terminal_read`.
* **One Command per Session at a Time:** A second `nova.terminal_run_command` on the same session while the first is still running is rejected with `reasonCode: "command_rejected"`. Use a second session for parallel work.

---

## See Also

* [`nova.terminal_open`](nova-terminal-open.md) - Open a new session.
* [`nova.terminal_read`](nova-terminal-read.md) - Read scrollback output.
* [`nova.terminal_send_key`](nova-terminal-send-key.md) - Send Ctrl+C to abort.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
