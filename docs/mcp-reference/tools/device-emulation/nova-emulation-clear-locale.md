# `nova.emulation_clear_locale`

Clears all locale, timezone, and geolocation overrides, reverting to host system settings.

---

## 1. Overview

`nova.emulation_clear_locale` removes active locale, timezone, and geolocation overrides set by `nova.emulation_set_locale`, restoring `navigator.language`/`navigator.languages`, the Accept-Language request header, the timezone, and geolocation to their real values.

* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/privacy/fingerprint-and-identity/README.md)

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
      "text": "Locale/timezone/geolocation emulation cleared."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1"
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
