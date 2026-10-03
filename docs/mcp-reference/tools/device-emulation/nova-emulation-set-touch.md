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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`enabled`** | `boolean` | Yes | `none` | `true` to enable touch emulation; `false` to revert to mouse input. |
| **`maxTouchPoints`** | `integer` | No | `5` | Reported touch points (1 - 10). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
