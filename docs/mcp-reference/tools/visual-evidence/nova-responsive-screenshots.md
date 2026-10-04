# `nova.responsive_screenshots`

> **Sweeps multiple viewport widths one at a time, capturing a screenshot at each and restoring the tab's original viewport afterwards.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.responsive_screenshots` applies a CDP device-metrics override at each requested width (e.g. 375, 768, 1280, 1920) in turn — not in parallel — waits briefly for layout to settle, and captures one screenshot per width, each delivered as a `nova://screenshot/...` resource (reference mode) so a multi-breakpoint sweep stays token-cheap. After the sweep, Nova restores the tab's pre-sweep viewport emulation (or clears the override if there was none) and reports `viewportRestored: true` only when the after-restore layout/visual-viewport metrics verifiably match the pre-sweep snapshot (a vertical-scrollbar-gutter width change is tolerated; height, scroll position, and scale are not).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `widths` | `array` of `integer` | Yes | — | — | Viewport widths to sweep (1-8). Each gets one screenshot. Required. |
| `height` | `integer` | No | `900` | 200–4000 | Viewport height in CSS pixels applied at every breakpoint. |
| `deviceScaleFactor` | `number` | No | `1` | 0.1–8 | Device pixel ratio applied at every breakpoint. |
| `mobile` | `boolean` | No | `false` | — | Emulate mobile viewport behavior at every breakpoint. |
| `fullPage` | `boolean` | No | `false` | — | Capture the full scrollable page at each width instead of just the viewport. |
| `format` | `string` | No | — | `png`, `jpeg`, `auto` | Image format for all shots. Defaults to the tool-intent profile. |
| `quality` | `integer` | No | — | 1–100 | JPEG quality (1-100) when format is jpeg. |

Capability bundles: `device_emulation`, `visual_evidence`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.responsive_screenshots",
  "arguments": {
    "targetId": "tab-1",
    "widths": [
      375,
      768,
      1280
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Captured 3 responsive screenshot(s)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "count": 3,
    "fullPage": false,
    "breakpoints": [
      { "width": 375, "height": 900, "resourceUri": "nova://screenshot/<id-375>", "mimeType": "image/jpeg", "bytes": 38120, "captured": true },
      { "width": 768, "height": 900, "resourceUri": "nova://screenshot/<id-768>", "mimeType": "image/jpeg", "bytes": 41650, "captured": true },
      { "width": 1280, "height": 900, "resourceUri": "nova://screenshot/<id-1280>", "mimeType": "image/jpeg", "bytes": 52300, "captured": true }
    ],
    "viewportRestored": true,
    "viewportRestore": { "restored": true, "status": "ok", "reasonCode": null, "attempts": 1 }
  }
}
```

Each `breakpoints[]` entry also carries `readabilityRisk` and an `evidenceGuidance` block (same shape as `nova.capture_screenshot`'s). `viewportRestored: false` means the restore CDP call failed or the after-restore viewport still differs from the pre-sweep one; `viewportRestore.reasonCode` explains why (`restore_cdp_call_failed`, `viewport_metrics_unavailable`, or `viewport_restore_drift`).

---

## 4. Operational Best Practices

* **Cross-Device QA:** Verify mobile navigation collapses and responsive flex wraps across breakpoints in one call — each width is still captured in sequence, so budget roughly `widths.length × (~150ms reflow settle + one screenshot capture)`.
* **Always check `viewportRestored`:** A `false` value means the tab may be left at the last swept viewport; read `viewportRestore` for the reason before trusting the tab's current layout state.

---

## 5. Related Tools

* [`nova.capture_screenshot`](nova-capture-screenshot.md)
* [`nova.emulation_set_device_metrics`](../device-emulation/nova-emulation-set-device-metrics.md)
