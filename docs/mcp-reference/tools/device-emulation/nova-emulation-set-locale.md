# `nova.emulation_set_locale`

Emulates browser locale, timezone, and geolocation coordinates for testing localized content.

---

## 1. Overview

`nova.emulation_set_locale` sets the browser language headers, IANA timezone, and GPS coordinates for internationalization and geolocation testing.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (Locale Emulation)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`locale`** | `string` | No | `null` | BCP-47 locale tag (e.g. `"de-DE"`, `"ja-JP"`, `"en-GB"`). Sets `navigator.language` and `Accept-Language`. |
| **`timezone`** | `string` | No | `null` | IANA timezone identifier (e.g. `"Europe/Berlin"`, `"America/New_York"`, `"Asia/Tokyo"`). |
| **`latitude`** | `number` | No | `null` | GPS latitude (-90 to 90). Requires `longitude`. |
| **`longitude`** | `number` | No | `null` | GPS longitude (-180 to 180). Requires `latitude`. |
| **`accuracy`** | `number` | No | `1` | Geolocation accuracy in meters. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
