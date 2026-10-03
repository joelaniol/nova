# `nova.terminal_dock_get_state`

Reads the presentation state of the visible terminal dock in the Nova application shell.

---

## 1. Overview

`nova.terminal_dock_get_state` inspects the visual state of the interactive terminal dock inside the Nova desktop window. This is purely UI chrome inspection and does not alter or inspect terminal content.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 1 (Safe)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_dock_get_state",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Terminal dock state: expanded (enabled=True, agentControlAllowed=True)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "state": "expanded",
    "enabled": true,
    "visible": true,
    "collapsed": false,
    "sessionCount": 1,
    "hasActiveSession": true,
    "agentControlAllowed": true,
    "sessionsPreservedByHidden": true
  }
}
```

---

## 4. Operational Best Practices

* **Visual Clearance:** Before taking full-window app screenshots, inspect dock state to know if terminal output is currently occupying bottom viewport space.

---

## See Also

* [`nova.terminal_dock_set_state`](nova-terminal-dock-set-state.md) - Expand, collapse, or hide dock.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
