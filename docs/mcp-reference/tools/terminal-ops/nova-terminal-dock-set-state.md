# `nova.terminal_dock_set_state`

Sets the visual presentation of the Nova terminal dock to expanded, collapsed, or hidden.

---

## 1. Overview

`nova.terminal_dock_set_state` toggles the visible dock state. When set to `hidden` or `collapsed`, all active shell sessions continue running in the background without termination.

* **Security Tier:** Tier 2 (UI Control)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `state` | `string` | Yes | — | `expanded`, `collapsed`, `hidden` | Requested dock state. 'expanded' shows the full dock, 'collapsed' leaves only the tab strip, and 'hidden' hides the dock while preserving running sessions. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_dock_set_state",
  "arguments": {
    "state": "hidden"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Terminal dock state set to hidden."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "success",
    "reasonCode": null,
    "requestedState": "hidden",
    "previousState": "expanded",
    "state": "hidden"
  }
}
```

---

## 4. Operational Best Practices

* **Permission Gate:** Agent control must be enabled in Settings > Terminal (`TerminalAgentCanControlDock`). If disabled, fails with `terminal_dock_agent_control_disabled`.
* **No Data Loss:** Hiding the dock does NOT kill user sessions.

---

## See Also

* [`nova.terminal_dock_get_state`](nova-terminal-dock-get-state.md) - Query current dock state.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
