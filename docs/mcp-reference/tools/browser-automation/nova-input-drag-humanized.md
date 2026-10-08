# `nova.input_drag_humanized`

> **Performs a drag-and-drop gesture with an eased motion path, overshoot, correction moves, and jitter — aimed at drag-based bot checks that flag perfectly linear mouse vectors.**

* **Core Feature Guide:** [Drag & Drop](../../../core-features/browser-interaction/drag-and-drop/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_drag_humanized` runs as a script inside the page: it dispatches a `mousedown`, moves along an eased path (smoothstep easing, not a parametric Bézier curve) with a small random vertical jitter per step, overshoots the end point by 3-8 px, applies 2-3 correction moves back to the target, then dispatches `mouseup`. The events are **synthetic** (`isTrusted: false`; the result reports `mode: "humanized_js"`) — use `nova.input_drag` instead on pages that require trusted input. It drives HTML5 `draggable="true"` surfaces under the same rules as `nova.input_drag`: the start point must sit on a draggable element, and a drop only lands where the page accepts it.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
    "durationMs": 1800
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Humanized drag from (150,250) to (550,250)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "startX": 150,
    "startY": 250,
    "endX": 550,
    "endY": 250,
    "mode": "humanized_js",
    "isTrusted": false,
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "profile": {
      "interval_mean_ms": 54.2,
      "interval_std_ms": 12.8,
      "step_mean_px": 28.4,
      "step_std_px": 9.1,
      "unique_interval_buckets": 6,
      "trusted_ratio": 0,
      "total_moves": 11,
      "duration_ms": 612.4
    },
    "actionDispatched": true
  }
}
```

`profile` is the raw movement-timing report from the in-page script (interval and step statistics), not a fixed-shape "curve type". On failure (e.g. the in-page script threw), `ok` is `false`, `status` is `"failed"`, and `reasonCode` is set (e.g. `input.drag_humanized_failed`).

---

## 4. Operational Best Practices

* **Captcha & Verification:** Use on slider captchas or sensitive drag-to-verify security widgets that analyze pointer timing/jitter, and when `nova.input_drag` fails on them.
* **Trusted-Input Pages:** Skip this tool on pages that explicitly require real (`isTrusted`) input — the events here are synthetic and some pages ignore or reject them.

---

## 5. Related Tools

* [`nova.input_drag`](nova-input-drag.md)
* [`nova.input_move`](nova-input-move.md)
