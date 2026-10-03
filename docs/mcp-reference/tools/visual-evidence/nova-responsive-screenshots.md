# `nova.responsive_screenshots`

> **Captures responsive screenshots across multiple breakpoint widths (mobile, tablet, desktop) in parallel.**

* **Capability Bundle:** `visual_evidence`
* **Security Tier:** Tier 2 (Responsive Auditing)
* **Core Feature Guide:** [Visual Evidence & Auditing](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.responsive_screenshots` sets device emulations across specified widths (e.g. 375, 768, 1280, 1920) and captures visual evidence for each viewport in a single invocation.

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
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_responsive_screenshots",
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
      "text": "Captured 3 responsive screenshots."
    }
  ],
  "structuredContent": {
    "ok": true,
    "screenshots": [
      {
        "width": 375,
        "uri": "nova://screenshot/resp-375"
      },
      {
        "width": 768,
        "uri": "nova://screenshot/resp-768"
      },
      {
        "width": 1280,
        "uri": "nova://screenshot/resp-1280"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Cross-Device QA:** Rapidly verify mobile navigation collapses and responsive flex wraps in one operation.

---

## 5. Related Tools

* [`nova.capture_screenshot`](nova-capture-screenshot.md)
* [`nova.emulation_set_device_metrics`](../device-emulation/nova-emulation-set-device-metrics.md)
