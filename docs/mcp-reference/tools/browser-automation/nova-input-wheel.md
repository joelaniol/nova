# `nova.input_wheel`

> **Dispatches a physical mouse wheel scroll event at specific coordinates with deltaX and deltaY.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_wheel` dispatches a single wheel event with the given `deltaX`/`deltaY` at the chosen viewport coordinates, enabling zooming in maps, canvas panning, or scrolling nested scrollable panels. Nova then measures whether the page actually moved (window scroll position and, where detected, a scroll container under the pointer) and reports that in the response — a dispatched event with no observed movement is not silently treated as success.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Wheel at (500,400) deltaY=250."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "message": null,
    "x": 500,
    "y": 400,
    "deltaX": 0,
    "deltaY": 250,
    "changed": true,
    "movementVerified": true,
    "warnings": [],
    "actionDispatched": true,
    "scrollEvidence": {
      "beforeWindowX": 0,
      "beforeWindowY": 1200,
      "afterWindowX": 0,
      "afterWindowY": 1450,
      "evidenceSource": "window",
      "underPointerHeadroom": false
    }
  }
}
```

### Status and `reasonCode` When Nothing Moved
* `status: "noop"`, `reasonCode: "input_wheel.at_boundary"` — the page is already at the scroll edge in the requested direction; this is reported as **success**, not a failure.
* `status: "no_effect"`, `reasonCode: "input_wheel.no_effect"` — the event was dispatched but no movement was observed anywhere; the page likely handles wheel input itself or scrolls a container Nova could not detect under the pointer.
* `status: "dispatched_unverified"`, `reasonCode: "input_wheel.iframe_unverified"` or `"input_wheel.evidence_unavailable"` — the event was sent, but movement could not be confirmed (e.g. dispatched into an opaque cross-origin frame).

---

## 4. Operational Best Practices

* **Map Zoom:** Position cursor over map canvas before issuing small deltaY increments to zoom.
* **Prefer scroll_smart:** Use `nova.scroll_smart` for normal page scrolling.

---

## 5. Related Tools

* [`nova.scroll_smart`](nova-scroll-smart.md)
* [`nova.scroll_by`](nova-scroll-by.md)
