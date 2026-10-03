# `nova.emulation_clear_locale`

Clears all locale, timezone, and geolocation overrides, reverting to host system settings.

---

## 1. Overview

`nova.emulation_clear_locale` removes active timezone and geolocation overrides and restores the browser's default language preferences.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (Locale Reset)
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
  "name": "nova.emulation_clear_locale",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Locale and geolocation overrides cleared."
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

* **Revert After Test:** Always revert locale overrides after testing region-specific checkout or currency displays.

---

## See Also

* [`nova.emulation_set_locale`](nova-emulation-set-locale.md) - Set locale overrides.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
