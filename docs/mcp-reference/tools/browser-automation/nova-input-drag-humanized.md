# `nova.input_drag_humanized`

> **Performs a bot-resilient drag-and-drop gesture along a natural Bézier physics curve with micro-jitters.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Physical Input with Physics)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_drag_humanized` simulates human hand kinematics during drag-and-drop, defeating bot-detection heuristics that flag perfectly linear mouse vectors.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `durationMs` | `number` | No | Target drag duration in ms (default: random 1800-2400). Affects interval timing. |
| `endX` | `number` | No | Preferred end X coordinate (CSS px). Legacy alias: toX. If both are provided, values must match. |
| `endY` | `number` | No | Preferred end Y coordinate (CSS px). Legacy alias: toY. If both are provided, values must match. |
| `fromX` | `number` | No | Legacy alias for startX. Prefer startX. Ignored if selector is set. If both are provided, values must match. |
| `fromY` | `number` | No | Legacy alias for startY. Prefer startY. Ignored if selector is set. If both are provided, values must match. |
| `jitterPx` | `number` | No | Vertical jitter amplitude in px (simulates muscle tremor). |
| `selector` | `string` | No | Optional CSS selector for the drag handle element. If set, startX/startY (or legacy fromX/fromY) are derived from the element's center. mousedown is dispatched on this element (not elementFromPoint). |
| `startX` | `number` | No | Preferred start X coordinate (CSS px). Ignored if selector is set. Legacy alias: fromX. If both are provided, values must match. |
| `startY` | `number` | No | Preferred start Y coordinate (CSS px). Ignored if selector is set. Legacy alias: fromY. If both are provided, values must match. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `toX` | `number` | No | Legacy alias for endX. Prefer endX. If both are provided, values must match. |
| `toY` | `number` | No | Legacy alias for endY. Prefer endY. If both are provided, values must match. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_drag_humanized",
  "arguments": {
    "targetId": "tab-1",
    "startX": 150,
    "startY": 250,
    "endX": 550,
    "endY": 250,
    "durationMs": 400
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Humanized drag completed over 400ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "curveType": "CubicBezier",
    "jitterApplied": true
  }
}
```

---

## 4. Operational Best Practices

* **Captcha & Verification:** Use on slider captchas or sensitive drag-to-verify security widgets.
* **Physics Realistic:** Velocity profiles automatically decelerate towards the target landing zone.

---

## 5. Related Tools

* [`nova.input_drag`](nova-input-drag.md)
* [`nova.input_move`](nova-input-move.md)
