# `nova.terminal_run_command`

Executes a single command line in an existing session and waits synchronously for its completion.

---

## 1. Overview

`nova.terminal_run_command` submits a command to an active ConPTY session, monitors execution via an end-of-command sentinel, and returns both output and numeric exit code. If execution exceeds `timeoutSeconds`, the session remains open with `reasonCode: "command_timeout"`.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 2 (Execute)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`sessionId`** | `string` | Yes | `none` | Session identifier from `nova.terminal_open`. |
| **`command`** | `string` | Yes | `none` | Single-line command to run. Embedded newlines are rejected (`command_rejected`). |
| **`timeoutSeconds`** | `integer` | No | `30` | Maximum seconds to wait (1 - 3600). |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional metadata with execution intent. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_run_command",
  "arguments": {
    "sessionId": "term-a8f9c1d0",
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
      "text": " M public/docs/mcp-reference/tool-catalog.md"
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term-a8f9c1d0",
    "output": " M public/docs/mcp-reference/tool-catalog.md\r\n",
    "exitCode": 0
  }
}
```

---

## 4. Operational Best Practices

* **Single-Line Only:** Do not send multi-line scripts in `command`. Use temporary script files or pipe commands.
* **Timeout Recovery:** If `reasonCode: "command_timeout"` is returned, the command is still running. You can check output using `nova.terminal_read` or terminate it via `nova.terminal_send_key(key="Ctrl+C")`.

---

## See Also

* [`nova.terminal_open`](nova-terminal-open.md) - Open a new session.
* [`nova.terminal_read`](nova-terminal-read.md) - Read scrollback output.
* [`nova.terminal_send_key`](nova-terminal-send-key.md) - Send Ctrl+C to abort.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
