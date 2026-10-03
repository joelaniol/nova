# `nova.emulation_use_device`

Applies a named device preset (viewport, DPR, touch capabilities, and user agent) in a single atomic call.

---

## 1. Overview

`nova.emulation_use_device` is the Playwright `devices["..."]` equivalent for Nova. It atomically configures screen metrics, touch emulation, device pixel ratio, and realistic user agent headers across 113 mobile, tablet, and desktop presets.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`device`** | `string` | Yes | `none` | Named device preset identifier (e.g. `"iPhone 15"`, `"Pixel 8 Pro"`, `"Galaxy S24"`, `"iPad Air"`, `"Desktop 1080p"`). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs` or `"active"`. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_use_device",
  "arguments": {
    "device": "iPhone 15",
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Applied device preset 'iPhone 15' (393x852 @ 3x, touch=True)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "device": "iPhone 15",
    "label": "iPhone 15",
    "width": 393,
    "height": 852,
    "deviceScaleFactor": 3,
    "mobile": true,
    "hasTouch": true,
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "platform": "iPhone"
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Consistency:** Automatically derives and syncs `navigator.userAgentData` (Sec-CH-UA Client Hints) for Chromium devices so bot detectors see consistent platform signals.
* **Resetting Presets:** Viewport can be cleared using `nova.emulation_clear_device_metrics`, and touch via `nova.emulation_set_touch(enabled=false)`.
* **Desktop Presets:** When applying desktop presets (`Desktop Chrome`, `Desktop 1080p`), Nova disables touch and preserves native browser user agent strings.

---

## See Also

* [`nova.emulation_set_device_metrics`](nova-emulation-set-device-metrics.md) - Configure custom dimensions.
* [`nova.emulation_clear_device_metrics`](nova-emulation-clear-device-metrics.md) - Revert to normal viewport.
* [`nova.emulation_set_touch`](nova-emulation-set-touch.md) - Toggle touch input.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
