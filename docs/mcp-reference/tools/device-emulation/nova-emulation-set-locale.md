# `nova.emulation_set_locale`

Emulates browser locale, timezone, and geolocation coordinates for testing localized content.

---

## 1. Overview

`nova.emulation_set_locale` sets the browser language headers, IANA timezone, and GPS coordinates for internationalization and geolocation testing.

* **Security Tier:** Tier 2 (Locale Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `locale` | `string` | No | — | — | BCP-47 locale, e.g. 'de-DE', 'ja-JP', 'ar-EG'. Sets navigator.language/languages + Accept-Language header (NOT Intl number/date formatting — see tool description). |
| `timezone` | `string` | No | — | — | IANA timezone id, e.g. 'Europe/Berlin', 'America/New_York', 'Asia/Tokyo'. |
| `latitude` | `number` | No | — | -90–90 | Geolocation latitude. Requires longitude. |
| `longitude` | `number` | No | — | -180–180 | Geolocation longitude. Requires latitude. |
| `accuracy` | `number` | No | `1` | ≥ 0 | Geolocation accuracy in meters (default 1). Only used when latitude+longitude are set. |

Capability bundle: `device_emulation` (load it with `nova.tools_bundle(bundle='device_emulation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_set_locale",
  "arguments": {
    "locale": "ja-JP",
    "timezone": "Asia/Tokyo",
    "latitude": 35.6762,
    "longitude": 139.6503
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Locale override applied: locale=ja-JP, timezone=Asia/Tokyo, geo=35.6762,139.6503."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "locale": "ja-JP",
    "timezone": "Asia/Tokyo",
    "geolocation": {
      "latitude": 35.6762,
      "longitude": 139.6503,
      "accuracy": 1
    }
  }
}
```

---

## 4. Operational Best Practices

* **Paired Coordinates:** `latitude` and `longitude` must both be provided when testing geolocation.
* **Timezone Testing:** Timezone overrides affect `Intl.DateTimeFormat` and JavaScript `Date` constructor outputs.

---

## See Also

* [`nova.emulation_clear_locale`](nova-emulation-clear-locale.md) - Clear locale and geo overrides.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
