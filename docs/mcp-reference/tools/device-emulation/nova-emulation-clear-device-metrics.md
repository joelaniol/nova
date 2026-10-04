# `nova.emulation_clear_device_metrics`

Clears viewport device metrics overrides, restoring normal window-sized rendering.

---

## 1. Overview

`nova.emulation_clear_device_metrics` clears any active `Emulation.setDeviceMetricsOverride` on the target tab, returning the layout and CSS viewport to standard host window proportions.

* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `device_emulation` (load it with `nova.tools_bundle(bundle='device_emulation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Device viewport metrics cleared. No tracked touch or user-agent override remains."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "cleared": {
      "viewport": true,
      "touch": false,
      "userAgent": false
    },
    "remainingDeviceAxes": null,
    "note": "Device viewport metrics cleared. No tracked touch or user-agent override remains."
  }
}
```

If touch or a user-agent override is still active on the tab, the text and `note` instead read
"Device viewport metrics cleared. Touch/user-agent overrides are separate CDP axes: disable touch
with `nova.emulation_set_touch(enabled=false)`; a tab-local user-agent override remains until the
tab is closed/reopened or replaced with `nova.emulation_set_user_agent`." and `remainingDeviceAxes`
reports which of `touch`/`userAgentOverridden` is still set.

---

## 4. Operational Best Practices

* **Does Not Clear UA or Touch:** Clearing device metrics does NOT revert touch emulation or user agent overrides — those are separate CDP axes. Disable touch explicitly with `nova.emulation_set_touch(enabled=false)`; a user-agent override remains until the tab is closed/reopened or replaced with `nova.emulation_set_user_agent`.

---

## See Also

* [`nova.emulation_set_device_metrics`](nova-emulation-set-device-metrics.md) - Set custom metrics.
* [`nova.emulation_clear_media`](nova-emulation-clear-media.md) - Clear media feature overrides.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
