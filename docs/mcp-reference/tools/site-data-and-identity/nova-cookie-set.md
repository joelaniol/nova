# `nova.cookie_set`

Sets or updates a cookie in the target sandbox profile's cookie jar.

---

## 1. Overview

`nova.cookie_set` writes or updates a cookie for the target tab's sandbox container. Cookies are identified by the unique tuple `{name, domain, path}`.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab or sandbox ID. Required. |
| `name` | `string` | Yes | — | — | Cookie name. Required. |
| `value` | `string` | Yes | — | — | Cookie value. Required. |
| `domain` | `string` | Yes | — | — | Cookie domain. Must match or be parent of current page host. Required. |
| `path` | `string` | No | `"/"` | — | Cookie path. Default: '/'. |
| `expires` | `number` | No | — | — | Expiry as Unix timestamp (seconds since epoch). Omit or set to 0 for a session cookie. Values in the past create an immediately expired cookie (effectively deletes it). |
| `httpOnly` | `boolean` | No | `false` | — | HttpOnly flag. Default: false. |
| `secure` | `boolean` | No | `false` | — | Secure flag. Default: false. Required for __Secure- and __Host- prefixes and SameSite=None. |
| `sameSite` | `string` | No | `"Lax"` | `None`, `Lax`, `Strict` | SameSite attribute. |
| `dryRun` | `boolean` | No | `false` | — | Validate without writing. Returns wouldCreate/wouldReplace and warnings. |

Capability bundle: `site_data_management` (load it with `nova.tools_bundle(bundle='site_data_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.cookie_set",
  "arguments": {
    "targetId": "tab-1",
    "name": "user_pref",
    "value": "dark_mode",
    "domain": ".example.com",
    "path": "/",
    "secure": true,
    "sameSite": "Lax"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cookie 'user_pref' created on .example.com/ (sandbox:tab-1)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "dryRun": false,
    "result": "created",
    "cookieId": "a1b2c3d4...",
    "effectiveDomain": ".example.com",
    "effectivePath": "/",
    "scope": {
      "profileId": "tab-1",
      "profileScope": "sandbox:tab-1",
      "isSharedProfile": false
    },
    "warnings": []
  }
}
```

`result` is `"created"` for a new cookie or `"replaced"` when an existing cookie with the same name/domain/path is overwritten.

---

## 4. Operational Best Practices

* **Dry Run Pre-flight:** Pass `dryRun: true` to validate cookie syntax and security constraints without applying changes.
* **Domain Scoping:** Specify domain with a leading dot (e.g. `.example.com`) if the cookie must cover subdomains.

---

## 5. Related Tools

* [`nova.cookie_list`](nova-cookie-list.md)
* [`nova.cookie_delete`](nova-cookie-delete.md)
