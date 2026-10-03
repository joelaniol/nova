# `nova.emulation_use_device`

Applies a named device preset (viewport, DPR, touch capabilities, and user agent) in a single atomic call.

---

## 1. Overview

`nova.emulation_use_device` is the Playwright `devices["..."]` equivalent for Nova. It atomically configures screen metrics, touch emulation, device pixel ratio, and realistic user agent headers across 113 mobile, tablet, and desktop presets.

* **Security Tier:** Tier 2 (Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `device` | `string` | Yes | — | `iPhone 8`, `iPhone SE`, `iPhone X`, `iPhone XR`, `iPhone 11`, `iPhone 12 Mini`, `iPhone 12`, `iPhone 12 Pro`, `iPhone 13 Mini`, `iPhone 13`, `iPhone 13 Pro`, `iPhone 13 Pro Max`, `iPhone 14`, `iPhone 14 Plus`, `iPhone 14 Pro`, `iPhone 14 Pro Max`, `iPhone 15`, `iPhone 15 Plus`, `iPhone 15 Pro`, `iPhone 15 Pro Max`, `iPhone 16`, `iPhone 16 Pro`, `iPhone 16 Pro Max`, `Pixel 2`, `Pixel 2 XL`, `Pixel 3`, `Pixel 3 XL`, `Pixel 4`, `Pixel 4a`, `Pixel 4 XL`, `Pixel 5`, `Pixel 6`, `Pixel 6 Pro`, `Pixel 7`, `Pixel 7 Pro`, `Pixel 8`, `Pixel 8 Pro`, `Pixel 9`, `Pixel 9 Pro`, `Pixel 9 Pro XL`, `Pixel Fold`, `Galaxy S8`, `Galaxy S9+`, `Galaxy S10`, `Galaxy S20`, `Galaxy S21`, `Galaxy S22`, `Galaxy S23`, `Galaxy S24`, `Galaxy S24 Ultra`, `Galaxy Note 20`, `Galaxy A54`, `Galaxy Z Flip 5`, `Galaxy Z Flip 6`, `Galaxy Z Fold 5`, `Galaxy Z Fold 6`, `OnePlus 11`, `OnePlus Nord 3`, `Xiaomi 13`, `Xiaomi 14`, `Redmi Note 12`, `Poco F5`, `Sony Xperia 1`, `Nothing Phone 2`, `Moto G Power`, `Moto Edge 40`, `Huawei P30`, `Huawei Mate 40 Pro`, `Honor Magic 5`, `Oppo Find X5`, `Vivo X90`, `Realme GT`, `Asus ROG Phone 6`, `Pixel 9 Pro Fold`, `Motorola Razr 40`, `Honor Magic V2`, `Oppo Find N3`, `OnePlus Open`, `iPad Mini`, `iPad (gen 7)`, `iPad (gen 10)`, `iPad Air`, `iPad Pro 11`, `iPad Pro 12.9`, `Galaxy Tab S4`, `Galaxy Tab S6 Lite`, `Galaxy Tab S7`, `Galaxy Tab S8`, `Galaxy Tab S8 Ultra`, `Galaxy Tab S9`, `Galaxy Tab A8`, `Galaxy Tab A9`, `Amazon Fire 7`, `Amazon Fire HD 8`, `Amazon Fire HD 10`, `Amazon Fire Max 11`, `Pixel Tablet`, `Lenovo Tab P11`, `Lenovo Tab P12`, `Xiaomi Pad 6`, `OnePlus Pad`, `Nexus 7`, `Nexus 9`, `Nexus 10`, `Desktop Chrome`, `Desktop Chrome HiDPI`, `Desktop Edge`, `Desktop Firefox`, `Desktop Safari`, `Laptop`, `Desktop 1080p`, `Desktop 1440p`, `Desktop 4K` | Device preset id. See the tool description for viewport sizes. |

Capability bundle: `device_emulation` (load it with `nova.tools_bundle(bundle='device_emulation')`).
<!-- /generated:parameters -->

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
