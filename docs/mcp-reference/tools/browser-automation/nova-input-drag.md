# `nova.input_drag`

> **Executes a physical mouse drag-and-drop gesture from source coordinates to destination.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Physical Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_drag` moves the mouse pointer from a starting position to a target position while holding down a specified mouse button.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `startX` | `number` | No | — | — | Preferred start X coordinate (CSS px, viewport-relative). Legacy alias: fromX. If both are provided, values must match. |
| `startY` | `number` | No | — | — | Preferred start Y coordinate (CSS px, viewport-relative). Legacy alias: fromY. If both are provided, values must match. |
| `endX` | `number` | No | — | — | Preferred end X coordinate (CSS px, viewport-relative). Legacy alias: toX. If both are provided, values must match. |
| `endY` | `number` | No | — | — | Preferred end Y coordinate (CSS px, viewport-relative). Legacy alias: toY. If both are provided, values must match. |
| `fromX` | `number` | No | — | — | Legacy alias for startX. Prefer startX. If both are provided, values must match. |
| `fromY` | `number` | No | — | — | Legacy alias for startY. Prefer startY. If both are provided, values must match. |
| `toX` | `number` | No | — | — | Legacy alias for endX. Prefer endX. If both are provided, values must match. |
| `toY` | `number` | No | — | — | Legacy alias for endY. Prefer endY. If both are provided, values must match. |
| `steps` | `integer` | No | `10` | 1–100 | Number of intermediate mouse move steps (more = smoother drag). |
| `button` | `string` | No | `"left"` | `left`, `middle`, `right` | Mouse button held during drag. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_drag",
  "arguments": {
    "targetId": "tab-1",
    "startX": 100,
    "startY": 200,
    "endX": 400,
    "endY": 200,
    "steps": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Dragged from (100, 200) to (400, 200)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "distance": 300
  }
}
```

---

## 4. Operational Best Practices

* **Slider Interaction:** Ideal for dragging volume sliders, range inputs, or Kanban cards.
* **Steps Interpolation:** Increase `steps` parameter for smoother movement recognized by gesture-sensitive UI libraries.

---

## 5. Related Tools

* [`nova.input_drag_humanized`](nova-input-drag-humanized.md)
* [`nova.input_move`](nova-input-move.md)
