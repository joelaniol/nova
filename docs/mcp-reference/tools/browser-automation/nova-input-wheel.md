# `nova.input_wheel`

> **Dispatches a physical mouse wheel scroll event at specific coordinates with deltaX and deltaY.**

* **Security Tier:** Tier 2 (Physical Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_wheel` delivers raw wheel events at a chosen location, enabling zooming in maps, canvas panning, or scrolling nested scrollable panels.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `x` | `number` | Yes | — | — | Viewport X coordinate (CSS px) where the wheel event is dispatched. |
| `y` | `number` | Yes | — | — | Viewport Y coordinate (CSS px) where the wheel event is dispatched. |
| `deltaX` | `number` | No | `0` | — | Horizontal scroll delta in pixels. |
| `deltaY` | `number` | Yes | — | — | Vertical scroll delta in pixels. Positive = scroll down. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_wheel",
  "arguments": {
    "targetId": "tab-1",
    "x": 500,
    "y": 400,
    "deltaY": 250
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Dispatched mouse wheel event (deltaY: 250)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "deltaX": 0,
    "deltaY": 250
  }
}
```

---

## 4. Operational Best Practices

* **Map Zoom:** Position cursor over map canvas before issuing small deltaY increments to zoom.
* **Prefer scroll_smart:** Use `nova.scroll_smart` for normal page scrolling.

---

## 5. Related Tools

* [`nova.scroll_smart`](nova-scroll-smart.md)
* [`nova.scroll_by`](nova-scroll-by.md)
