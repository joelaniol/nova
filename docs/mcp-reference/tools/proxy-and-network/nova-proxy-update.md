# `nova.proxy_update`

Updates host, port, protocol, or bypass list of an existing proxy profile.

---

## 1. Overview

`nova.proxy_update` performs partial updates on an existing proxy profile without altering omitted fields or resetting stored credentials.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Configuration)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`profileId`** | `string` | Yes | `none` | Proxy profile identifier. |
| **`name`** | `string` | No | `unchanged` | New display name. |
| **`host`** | `string` | No | `unchanged` | New hostname/IP. |
| **`port`** | `integer` | No | `unchanged` | New port. |
| **`protocol`** | `string` | No | `unchanged` | New protocol. |
| **`username`** | `string` | No | `unchanged` | New username. |
| **`bypassList`** | `string` | No | `unchanged` | New bypass list. |
| **`enabled`** | `boolean` | No | `unchanged` | Enable/disable. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_update",
  "arguments": {
    "profileId": "prx-de-socks5",
    "port": 1085
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy profile 'prx-de-socks5' updated."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "prx-de-socks5",
    "updated": true
  }
}
```

---

## 4. Operational Best Practices

* **Hot Swapping:** If the profile is actively assigned to an open sandbox, call `nova.proxy_switch` afterwards to re-initialize affected WebViews.

---

## See Also

* [`nova.proxy_list`](nova-proxy-list.md) - List proxy profiles.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
