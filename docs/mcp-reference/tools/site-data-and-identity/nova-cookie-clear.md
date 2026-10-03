# `nova.cookie_clear`

Clears cookies across the target profile, with optional domain filtering.

---

## 1. Overview

`nova.cookie_clear` purges cookies from the target sandbox container. When `domain` is specified, only matching cookies are removed; omitting `domain` clears all cookies in the profile.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 3 (Batch Cookie Clearance)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | No | `null` | Optional domain scope. When set, only cookies whose domain matches this value or is a subdomain of it are deleted (e.g. 'example.com' matches '.example.com' and 'sub.example.com'). Omit to clear ALL cookies (profile-wide). |
| **`targetId`** | `string` | Yes | `null` | Tab or sandbox ID. Required. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.cookie_clear",
  "arguments": {
    "targetId": "tab-1",
    "domain": "example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cleared 14 cookies for domain example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "clearedDomain": "example.com",
    "clearedCount": 14
  }
}
```

---

## 4. Operational Best Practices

* **Targeted Purging:** Always provide `domain` to avoid logging out users from unrelated services sharing the same sandbox profile.

---

## 5. Related Tools

* [`nova.cookie_delete`](nova-cookie-delete.md)
* [`nova.cache_clear`](nova-cache-clear.md)
