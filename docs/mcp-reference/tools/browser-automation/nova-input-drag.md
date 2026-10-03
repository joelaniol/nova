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

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `activateIfNeeded` | `boolean` | No | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `button` | `string` | No | Mouse button held during drag. |
| `endX` | `number` | No | Preferred end X coordinate (CSS px, viewport-relative). Legacy alias: toX. If both are provided, values must match. |
| `endY` | `number` | No | Preferred end Y coordinate (CSS px, viewport-relative). Legacy alias: toY. If both are provided, values must match. |
| `fromX` | `number` | No | Legacy alias for startX. Prefer startX. If both are provided, values must match. |
| `fromY` | `number` | No | Legacy alias for startY. Prefer startY. If both are provided, values must match. |
| `restoreActiveTarget` | `boolean` | No | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `startX` | `number` | No | Preferred start X coordinate (CSS px, viewport-relative). Legacy alias: fromX. If both are provided, values must match. |
| `startY` | `number` | No | Preferred start Y coordinate (CSS px, viewport-relative). Legacy alias: fromY. If both are provided, values must match. |
| `steps` | `integer` | No | Number of intermediate mouse move steps (more = smoother drag). |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `toX` | `number` | No | Legacy alias for endX. Prefer endX. If both are provided, values must match. |
| `toY` | `number` | No | Legacy alias for endY. Prefer endY. If both are provided, values must match. |

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
