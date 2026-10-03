# `nova.proxy_remove`

Deletes a proxy profile and resets any sandbox bindings back to the global default.

---

## 1. Overview

`nova.proxy_remove` deletes a proxy profile and removes its encrypted credentials. Any sandboxes assigned to the deleted profile are automatically reset to `global`.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Cleanup)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`profileId`** | `string` | Yes | `none` | Proxy profile ID to delete. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_remove",
  "arguments": {
    "profileId": "prx-de-socks5"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy profile 'prx-de-socks5' removed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "prx-de-socks5",
    "removed": true
  }
}
```

---

## 4. Operational Best Practices

* **Automatic Fallback:** Sandboxes never fail closed upon profile deletion; they seamlessly fall back to global proxy routing.

---

## See Also

* [`nova.proxy_list`](nova-proxy-list.md) - List profiles.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
