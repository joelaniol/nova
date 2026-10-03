# `nova.terminal_list`

Lists all open agent-owned terminal sessions with status, shell type, and exit codes.

---

## 1. Overview

`nova.terminal_list` queries the terminal session manager for active background sessions created by agents. It excludes the user's interactive dock terminals to maintain clear security and control boundaries.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 1 (Safe)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier to filter sessions. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
        "sessionId": "term-a8f9c1d0",
        "shell": "powershell.exe",
        "running": true,
        "exitCode": null,
        "createdAtUtc": "2026-10-02T20:15:30.1234567Z"
      },
      {
        "sessionId": "term-b2c3d4e5",
        "shell": "powershell.exe",
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
