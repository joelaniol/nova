# `nova.terminal_close`

Terminates an agent-owned terminal session and cleans up its process tree and temporary directory.

---

## 1. Overview

`nova.terminal_close` gracefully shuts down the PTY and forcefully terminates any remaining child processes in the session tree. Subsequent calls referencing the session ID return `terminal_not_found`.

* **Security Tier:** Tier 2 (Destructive)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sessionId` | `string` | Yes | — | — | Session id from terminal_open. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `terminal_ops` (load it with `nova.tools_bundle(bundle='terminal_ops')`).
<!-- /generated:parameters -->

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
