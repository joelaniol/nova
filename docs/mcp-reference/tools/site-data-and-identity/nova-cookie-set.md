# `nova.cookie_set`

Sets or updates a cookie in the target sandbox profile's cookie jar.

---

## 1. Overview

`nova.cookie_set` writes or updates a cookie for the target tab's sandbox container. Cookies are identified by the unique tuple `{name, domain, path}`.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Cookie Mutation)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | Yes | `null` | Cookie domain. Must match or be parent of current page host. Required. |
| **`dryRun`** | `boolean` | No | `false` | Validate without writing. Returns wouldCreate/wouldReplace and warnings. |
| **`expires`** | `number` | No | `null` | Expiry as Unix timestamp (seconds since epoch). Omit or set to 0 for a session cookie. Values in the past create an immediately expired cookie (effectively deletes it). |
| **`httpOnly`** | `boolean` | No | `false` | HttpOnly flag. Default: false. |
| **`name`** | `string` | Yes | `null` | Cookie name. Required. |
| **`path`** | `string` | No | `"/"` | Cookie path. Default: '/'. |
| **`sameSite`** | `string` | No | `"Lax"` | SameSite attribute. |
| **`secure`** | `boolean` | No | `false` | Secure flag. Default: false. Required for __Secure- and __Host- prefixes and SameSite=None. |
| **`targetId`** | `string` | Yes | `null` | Tab or sandbox ID. Required. |
| **`value`** | `string` | Yes | `null` | Cookie value. Required. |

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
      "text": "Set cookie 'user_pref' on .example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "name": "user_pref",
    "domain": ".example.com",
    "path": "/",
    "status": "Set"
  }
}
```

---

## 4. Operational Best Practices

* **Dry Run Pre-flight:** Pass `dryRun: true` to validate cookie syntax and security constraints without applying changes.
* **Domain Scoping:** Specify domain with a leading dot (e.g. `.example.com`) if the cookie must cover subdomains.

---

## 5. Related Tools

* [`nova.cookie_list`](nova-cookie-list.md)
* [`nova.cookie_delete`](nova-cookie-delete.md)
