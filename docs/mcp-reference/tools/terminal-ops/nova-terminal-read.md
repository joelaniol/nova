# `nova.terminal_read`

Reads the recent raw output tail of a terminal session scrollback buffer.

---

## 1. Overview

`nova.terminal_read` extracts the most recent output from a running or exited session. The output may contain ANSI escape codes, progress markers, and sensitive environment data.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 1 (Read / Sensitive)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`sessionId`** | `string` | Yes | `none` | Session ID returned by `nova.terminal_open`. |
| **`maxBytes`** | `integer` | No | `16384` | Maximum bytes to read from the tail (256 - 200,000). |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_read",
  "arguments": {
    "sessionId": "term-a8f9c1d0",
    "maxBytes": 8192
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "PS C:\\Work> git status\nOn branch main\nnothing to commit"
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term-a8f9c1d0",
    "output": "PS C:\\Work> git status\nOn branch main\nnothing to commit",
    "totalBytes": 2450,
    "truncated": false,
    "running": true,
    "exitCode": null
  }
}
```

---

## 4. Operational Best Practices

* **Understanding `truncated`:** `truncated: true` indicates that output was permanently evicted from the circular scrollback buffer due to size limits, not that `maxBytes` was reached.
* **Sensitive Content:** Output may contain credentials or sensitive system information; do not log terminal scrollbacks to public sinks.

---

## See Also

* [`nova.terminal_write`](nova-terminal-write.md) - Write raw text to stdin.
* [`nova.terminal_run_command`](nova-terminal-run-command.md) - Run a command and capture output.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
