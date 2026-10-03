# `nova.emulation_set_viewport_frame`

Configures the visual outline rendered around an emulated device viewport in the host UI.

---

## 1. Overview

`nova.emulation_set_viewport_frame` styles the visible border outline around a device-emulated page within the Nova window, making empty surrounding area clearly recognizable during human or visual agent reviews.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 1 (Host UI Appearance)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `enabled` | `boolean` | No | — | — | Whether the outline is drawn at all. Omit to keep the current setting. |
| `color` | `string` | No | — | — | Outline color as '#RRGGBB' or '#AARRGGBB' (6-digit values are treated as fully opaque), or 'default' to restore Nova's accent color. Omit to keep the current color. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_set_viewport_frame",
  "arguments": {
    "enabled": true,
    "color": "#FF35CCE6"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Viewport frame updated (enabled=True, color=#FF35CCE6)."
    }
  ],
  "structuredContent": {
    "enabled": true,
    "effectiveColor": "#FF35CCE6",
    "changed": true,
    "enabledChanged": true,
    "colorChanged": false
  }
}
```

---

## 4. Operational Best Practices

* **Host-Only Rendering:** This outline is rendered in Nova's native XAML composition layer and does not touch or affect the page DOM or WebViews.

---

## See Also

* [`nova.emulation_set_device_metrics`](nova-emulation-set-device-metrics.md) - Set viewport dimensions.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
