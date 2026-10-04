# `nova.input_move`

> **Moves the mouse cursor to specified viewport coordinates with a single mouse-move event.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_move` dispatches a single mouse-move event to the target coordinates through the DevTools input pipeline — there is no movement curve or intermediate steps. It still triggers CSS `:hover` states, tooltips, and `mouseenter`/`mouseover` listeners, since the browser treats the pointer as having arrived at that position.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `x` | `number` | Yes | — | — | Mouse X coordinate in CSS pixels (viewport-relative). |
| `y` | `number` | Yes | — | — | Mouse Y coordinate in CSS pixels (viewport-relative). |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_move",
  "arguments": {
    "targetId": "tab-1",
    "x": 620,
    "y": 180
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Mouse moved to (620,180)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "x": 620,
    "y": 180,
    "actionDispatched": true
  }
}
```

There is no top-level `ok` field; `actionDispatched: true` confirms the move event was sent.

---

## 4. Operational Best Practices

* **Hover Reveals:** Move cursor over navigation dropdown menus before clicking hidden child links.

---

## 5. Related Tools

* [`nova.input_click`](nova-input-click.md)
* [`nova.click_selector`](nova-click-selector.md)
