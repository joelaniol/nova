# `nova.emulation_clear_device_metrics`

Clears viewport device metrics overrides, restoring normal window-sized rendering.

---

## 1. Overview

`nova.emulation_clear_device_metrics` clears any active `Emulation.setDeviceMetricsOverride` on the target tab, returning the layout and CSS viewport to standard host window proportions.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (Emulation Reset)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_clear_device_metrics",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Device metrics override cleared."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "cleared": true
  }
}
```

---

## 4. Operational Best Practices

* **Does Not Clear UA:** Note that clearing device metrics does NOT revert user agent overrides. Use tab restart or explicit `nova.emulation_set_user_agent` to change UA.

---

## See Also

* [`nova.emulation_set_device_metrics`](nova-emulation-set-device-metrics.md) - Set custom metrics.
* [`nova.emulation_clear_media`](nova-emulation-clear-media.md) - Clear media feature overrides.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
