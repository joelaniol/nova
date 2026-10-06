# `nova.cookie_list`

Lists cookies for the target tab's profile with metadata (domain, path, flags, expiry).

---

## 1. Overview

`nova.cookie_list` inspects the cookie jar belonging to the target tab's sandbox profile. By default, it returns metadata only (names, domains, paths, expiration timestamps, Secure/HttpOnly/SameSite flags) with plaintext values redacted to prevent token leakage.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Tab or sandbox ID whose profile to read, or 'active' / 'activeBrowserTab'. All browser tabs share one cookie store, so any browser tab returns the same cookies; a sandbox has its own. The response's scope names the profile that was read. |
| `uri` | `string` | No | — | — | Optional URI filter. Only returns cookies that apply to this URI. Without: all cookies in the profile. |
| `nameFilter` | `string` | No | — | — | Optional substring match on cookie name. |
| `domainFilter` | `string` | No | — | — | Optional exact domain match (case-insensitive, leading dot stripped). Required when includeValues=true. |
| `includeValues` | `boolean` | No | `false` | — | Include actual cookie values in response. Default: false (metadata only). When true, requires permission, domainFilter, and may trigger HIGH-IMPACT secret-read policy because values may contain session tokens and secrets. |
| `maxEntries` | `integer` | No | `100` | 1–500 | Max cookies to return. Default: 100, max: 500. |
| `cursor` | `string` | No | — | — | Pagination cursor from a previous response's nextCursor field. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `site_data_management` (load it with `nova.tools_bundle(bundle='site_data_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.cookie_list",
  "arguments": {
    "targetId": "tab-1",
    "domainFilter": ".example.com",
    "includeValues": false
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Listed 2 cookies (total: 2) for sandbox:tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "cookies": [
      {
        "cookieId": "a1b2c3d4...",
        "name": "session_id",
        "domain": ".example.com",
        "path": "/",
        "expiresUtc": "2026-10-09T20:00:00Z",
        "isSession": false,
        "httpOnly": true,
        "secure": true,
        "sameSite": "Lax"
      },
      {
        "cookieId": "e5f6a7b8...",
        "name": "theme",
        "domain": ".example.com",
        "path": "/",
        "expiresUtc": null,
        "isSession": true,
        "httpOnly": false,
        "secure": false,
        "sameSite": "None"
      }
    ],
    "scope": {
      "profileId": "tab-1",
      "profileScope": "sandbox:tab-1",
      "isSharedProfile": false
    },
    "totalCount": 2,
    "hasMore": false,
    "nextCursor": null,
    "includeValues": false
  }
}
```

When `includeValues: true`, each entry also carries a `value` field with the plaintext cookie value.

---

## 4. Operational Best Practices

* **Security Redaction:** Plaintext values are redacted by default; only request `includeValues: true` when explicitly transferring session authentication.
* **Domain Filtering:** Always supply `domainFilter` or `uri` on busy profiles with hundreds of tracking cookies.

---

## 5. Related Tools

* [`nova.cookie_set`](nova-cookie-set.md)
* [`nova.cookie_delete`](nova-cookie-delete.md)
* [`nova.cookie_clear`](nova-cookie-clear.md)
