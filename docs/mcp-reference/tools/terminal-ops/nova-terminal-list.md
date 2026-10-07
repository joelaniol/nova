# `nova.terminal_list`

Lists all open agent-owned terminal sessions with status, shell type, and exit codes.

---

## 1. Overview

`nova.terminal_list` queries the terminal session manager for active background sessions created by agents. It excludes the user's interactive dock terminals to maintain clear security and control boundaries.

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | — | — | Accepted for compatibility and ignored: terminal sessions are addressed by sessionId and are not bound to a tab or a tab claim. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `terminal_ops` (load it with `nova.tools_bundle(bundle='terminal_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 terminal session(s)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "count": 2,
    "sessions": [
      {
        "sessionId": "term_1a2b3c4d5e6f7a8b",
        "shell": "powershell.exe -NoProfile -NoLogo -NoExit -Command \"Remove-Module PSReadLine -Force -ErrorAction SilentlyContinue\"",
        "running": true,
        "exitCode": null,
        "createdAtUtc": "2026-10-02T20:15:30.1234567Z"
      },
      {
        "sessionId": "term_9f8e7d6c5b4a3210",
        "shell": "powershell.exe -NoProfile -NoLogo -NoExit -Command \"Remove-Module PSReadLine -Force -ErrorAction SilentlyContinue\"",
        "running": false,
        "exitCode": 0,
        "createdAtUtc": "2026-10-02T19:40:12.9876543Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Orphan Detection:** Periodically list sessions to verify completed tasks and clean up exited terminals.
* **Security Boundary:** User dock sessions are strictly filtered out; agents cannot observe or interact with user shell sessions.

---

## See Also

* [`nova.terminal_open`](nova-terminal-open.md) - Open a new terminal session.
* [`nova.terminal_get_state`](nova-terminal-get-state.md) - Get state of a single session.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
