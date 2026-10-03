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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`width`** | `integer` | Yes | `none` | Viewport width in CSS pixels (100 - 10,000). |
| **`height`** | `integer` | Yes | `none` | Viewport height in CSS pixels (100 - 10,000). |
| **`deviceScaleFactor`** | `number` | No | `1` | DPI multiplier (0.1 - 8.0). Use 2.0 for Retina displays, 3.0 for modern mobile screens. |
| **`mobile`** | `boolean` | No | `false` | Whether to emulate mobile layout viewport and meta viewport tag processing. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
