# `nova.terminal_write`

Writes raw characters to the session stdin without appending an implicit newline.

---

## 1. Overview

`nova.terminal_write` feeds raw bytes or strings directly into the ConPTY stdin stream. It does not wait for command completion or output generation.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 2 (Execute)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`sessionId`** | `string` | Yes | `none` | Session identifier. |
| **`data`** | `string` | Yes | `none` | Text to write to stdin verbatim. Include `\r` to submit a line. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_write",
  "arguments": {
    "sessionId": "term-a8f9c1d0",
    "data": "npm test\r"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Wrote 9 char(s) to 'term-a8f9c1d0'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term-a8f9c1d0",
    "charsWritten": 9
  }
}
```

---

## 4. Operational Best Practices

* **CRLF Submission:** Because this is a raw PTY write, a command line requires a trailing carriage return (`\r` or `\r\n`) to be executed by PowerShell.
* **Prefer `run_command`:** For linear command execution, `nova.terminal_run_command` is much safer because it waits for the exit code and sentinel.

---

## See Also

* [`nova.terminal_send_key`](nova-terminal-send-key.md) - Send control key combinations.
* [`nova.terminal_read`](nova-terminal-read.md) - Read scrollback output.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
