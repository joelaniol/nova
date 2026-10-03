# `nova.terminal_send_key`

Sends a named control key or key combination to the active terminal session.

---

## 1. Overview

`nova.terminal_send_key` transmits special keyboard events to the ConPTY input pipe, allowing agents to interrupt running jobs, navigate interactive menus, or confirm prompts.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 2 (Control)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sessionId` | `string` | Yes | — | — | Session id from terminal_open. |
| `key` | `string` | Yes | — | — | Key name (e.g. 'Enter', 'Ctrl+C', 'ArrowUp'). |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_send_key",
  "arguments": {
    "sessionId": "term-a8f9c1d0",
    "key": "Ctrl+C"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sent 'Ctrl+C' to 'term-a8f9c1d0'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term-a8f9c1d0",
    "key": "Ctrl+C"
  }
}
```

---

## 4. Operational Best Practices

* **Cancel Runaway Commands:** Send `Ctrl+C` to abort a command that has timed out or entered an infinite loop.
* **Clear Terminal Screen:** Send `Ctrl+L` to reset the visible screen buffer during interactive sessions.

---

## See Also

* [`nova.terminal_write`](nova-terminal-write.md) - Write raw characters to stdin.
* [`nova.terminal_close`](nova-terminal-close.md) - Forcefully terminate session.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
