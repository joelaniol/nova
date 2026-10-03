# `nova.emulation_set_touch`

Enables or disables touch event simulation and sets the maximum touch points reported by the browser.

---

## 1. Overview

`nova.emulation_set_touch` configures CDP touch emulation, switching pointer input events to touch events and updating `navigator.maxTouchPoints`.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (Input Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `enabled` | `boolean` | Yes | — | — | If true, enable touch event emulation (touch events dispatched instead of mouse). If false, disable and revert to mouse input. |
| `maxTouchPoints` | `integer` | No | `5` | 1–10 | Maximum simultaneous touch points reported by navigator.maxTouchPoints. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_set_touch",
  "arguments": {
    "enabled": true,
    "maxTouchPoints": 5
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Touch emulation enabled (maxTouchPoints=5)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "enabled": true,
    "maxTouchPoints": 5
  }
}
```

---

## 4. Operational Best Practices

* **Gesture Support:** When touch is enabled, web applications render mobile UI drawer handles and touch sliders instead of desktop scrollbars.

---

## See Also

* [`nova.emulation_use_device`](nova-emulation-use-device.md) - Preset with automatic touch handling.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
