# `nova.emulation_set_device_metrics`

Overrides the viewport dimensions, device scale factor (DPR), and mobile layout behavior for a tab.

---

## 1. Overview

`nova.emulation_set_device_metrics` invokes Chrome DevTools Protocol `Emulation.setDeviceMetricsOverride` to resize the browser rendering viewport independently of host window bounds.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `width` | `integer` | Yes | — | 100–10000 | Viewport width in CSS pixels (e.g. 375 for iPhone, 1920 for desktop). |
| `height` | `integer` | Yes | — | 100–10000 | Viewport height in CSS pixels (e.g. 812 for iPhone X, 1080 for desktop). |
| `deviceScaleFactor` | `number` | No | `1` | 0.1–8 | Device pixel ratio / DPI multiplier (e.g. 2.0 for Retina, 3.0 for high-DPI mobile). Affects rendering resolution. |
| `mobile` | `boolean` | No | `false` | — | If true, emulate mobile viewport behavior (viewport meta tag, touch scrolling, mobile layout). Effective layout width still depends on the page's own <meta viewport>; without it, the browser uses a ~980px layout viewport. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_set_device_metrics",
  "arguments": {
    "width": 375,
    "height": 667,
    "deviceScaleFactor": 2,
    "mobile": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Device metrics override applied: 375x667 @ 2x (mobile=True)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "width": 375,
    "height": 667,
    "deviceScaleFactor": 2,
    "mobile": true,
    "devToolsOpen": false
  }
}
```

---

## 4. Operational Best Practices

* **Visual Outlines:** Pair with `nova.emulation_set_viewport_frame` so you can visually distinguish the emulated device frame from empty window space.
* **Responsive Testing:** Use together with `nova.measure_elements` and `nova.detect_overflow` to diagnose mobile clipping issues.

---

## See Also

* [`nova.emulation_clear_device_metrics`](nova-emulation-clear-device-metrics.md) - Revert viewport overrides.
* [`nova.emulation_use_device`](nova-emulation-use-device.md) - Use named device preset.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
