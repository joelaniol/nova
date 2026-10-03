# `nova.input_drag_humanized`

> **Performs a bot-resilient drag-and-drop gesture along a natural Bézier physics curve with micro-jitters.**

* **Security Tier:** Tier 2 (Physical Input with Physics)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_drag_humanized` simulates human hand kinematics during drag-and-drop, defeating bot-detection heuristics that flag perfectly linear mouse vectors.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `startX` | `number` | No | — | — | Preferred start X coordinate (CSS px). Ignored if selector is set. Legacy alias: fromX. If both are provided, values must match. |
| `startY` | `number` | No | — | — | Preferred start Y coordinate (CSS px). Ignored if selector is set. Legacy alias: fromY. If both are provided, values must match. |
| `endX` | `number` | No | — | — | Preferred end X coordinate (CSS px). Legacy alias: toX. If both are provided, values must match. |
| `endY` | `number` | No | — | — | Preferred end Y coordinate (CSS px). Legacy alias: toY. If both are provided, values must match. |
| `fromX` | `number` | No | — | — | Legacy alias for startX. Prefer startX. Ignored if selector is set. If both are provided, values must match. |
| `fromY` | `number` | No | — | — | Legacy alias for startY. Prefer startY. Ignored if selector is set. If both are provided, values must match. |
| `toX` | `number` | No | — | — | Legacy alias for endX. Prefer endX. If both are provided, values must match. |
| `toY` | `number` | No | — | — | Legacy alias for endY. Prefer endY. If both are provided, values must match. |
| `selector` | `string` | No | — | — | Optional CSS selector for the drag handle element. If set, startX/startY (or legacy fromX/fromY) are derived from the element's center. mousedown is dispatched on this element (not elementFromPoint). |
| `durationMs` | `number` | No | — | 500–10000 | Target drag duration in ms (default: random 1800-2400). Affects interval timing. |
| `jitterPx` | `number` | No | `2` | 0–10 | Vertical jitter amplitude in px (simulates muscle tremor). |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

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
