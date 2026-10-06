# `nova.terminal_close`

Terminates an agent-owned terminal session and cleans up its process tree and temporary directory.

---

## 1. Overview

`nova.terminal_close` gracefully shuts down the PTY and forcefully terminates any remaining child processes in the session tree. Subsequent calls referencing the session ID return `terminal_not_found`.

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sessionId` | `string` | Yes | — | — | Session id from terminal_open. |
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
  "name": "nova.terminal_close",
  "arguments": {
    "sessionId": "term_1a2b3c4d5e6f7a8b"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Terminal session 'term_1a2b3c4d5e6f7a8b' closed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term_1a2b3c4d5e6f7a8b",
    "closed": true
  }
}
```

---

## 4. Operational Best Practices

* **Always Close Sessions:** Unclosed sessions keep their shell process (and its ConPTY handles) running and their temporary working directory in place. Close a session once its task is done to free both.

---

## See Also

* [`nova.terminal_open`](nova-terminal-open.md) - Open a new terminal session.
* [`nova.terminal_list`](nova-terminal-list.md) - List active sessions.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
