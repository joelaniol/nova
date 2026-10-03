# `nova.proxy_set_password`

Stores or clears encrypted proxy authentication credentials using Windows DPAPI.

---

## 1. Overview

`nova.proxy_set_password` encrypts proxy passwords using Windows Data Protection API (DPAPI). The plaintext secret is never returned in any MCP response or written to plaintext configuration files.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Credential Management)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`profileId`** | `string` | Yes | `none` | Proxy profile ID. |
| **`password`** | `string` | No | `null` | Password to store. Pass `null` or empty string to clear stored password. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_set_password",
  "arguments": {
    "profileId": "prx-us-east",
    "password": "super_secret_proxy_pass"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Password stored for proxy profile 'prx-us-east'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "prx-us-east",
    "passwordConfigured": true
  }
}
```

---

## 4. Operational Best Practices

* **Security Hygiene:** Never store passwords directly in `nova.proxy_create` or commit them in code.

---

## See Also

* [`nova.proxy_create`](nova-proxy-create.md) - Create profile.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
