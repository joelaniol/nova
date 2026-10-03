# `nova.terminal_close`

Terminates an agent-owned terminal session and cleans up its process tree and temporary directory.

---

## 1. Overview

`nova.terminal_close` gracefully shuts down the PTY and forcefully terminates any remaining child processes in the session tree. Subsequent calls referencing the session ID return `terminal_not_found`.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 2 (Destructive)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`sessionId`** | `string` | Yes | `none` | Session ID to close. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_close",
  "arguments": {
    "sessionId": "term-a8f9c1d0"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Terminal session 'term-a8f9c1d0' closed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term-a8f9c1d0",
    "closed": true
  }
}
```

---

## 4. Operational Best Practices

* **Always Close Sessions:** Unclosed sessions hold ConPTY pipe handles and temporary directories on disk. Always close sessions once tasks complete.

---

## See Also

* [`nova.terminal_open`](nova-terminal-open.md) - Open a new terminal session.
* [`nova.terminal_list`](nova-terminal-list.md) - List active sessions.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
