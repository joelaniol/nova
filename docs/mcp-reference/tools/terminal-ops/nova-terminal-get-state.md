# `nova.terminal_get_state`

Queries lifecycle status, working directory, and exit code for a specific session.

---

## 1. Overview

`nova.terminal_get_state` inspects whether a terminal session is actively running, its working directory, and its process exit code if it has terminated.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 1 (Safe)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`sessionId`** | `string` | Yes | `none` | Session identifier. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_get_state",
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
      "text": "'term-a8f9c1d0': running."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sessionId": "term-a8f9c1d0",
    "shell": "powershell.exe",
    "cwd": "C:\\Projects\\NovaBrowser",
    "running": true,
    "exitCode": null,
    "createdAtUtc": "2026-10-02T20:15:30.1234567Z"
  }
}
```

---

## 4. Operational Best Practices

* **State Check Before Commands:** Check session state to avoid running commands against exited or broken shells.

---

## See Also

* [`nova.terminal_list`](nova-terminal-list.md) - List all active sessions.
* [`nova.terminal_close`](nova-terminal-close.md) - Close session.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
