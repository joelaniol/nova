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

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `deviceScaleFactor` | `number` | No | Device pixel ratio applied at every breakpoint. |
| `format` | `string` | No | Image format for all shots. Defaults to the tool-intent profile. |
| `fullPage` | `boolean` | No | Capture the full scrollable page at each width instead of just the viewport. |
| `height` | `integer` | No | Viewport height in CSS pixels applied at every breakpoint. |
| `mobile` | `boolean` | No | Emulate mobile viewport behavior at every breakpoint. |
| `quality` | `integer` | No | JPEG quality (1-100) when format is jpeg. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `widths` | `array` | **Yes** | Viewport widths to sweep (1-8). Each gets one screenshot. Required. |

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
