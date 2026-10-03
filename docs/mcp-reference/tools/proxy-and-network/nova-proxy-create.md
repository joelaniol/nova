# `nova.proxy_create`

Creates a new proxy profile with host, port, protocol, and optional credentials.

---

## 1. Overview

`nova.proxy_create` defines a new proxy configuration in Nova (up to 12 profiles). Supports HTTP, HTTPS, SOCKS4, and SOCKS5 protocols with custom bypass lists.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Configuration)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`name`** | `string` | Yes | `none` | Profile display name. |
| **`host`** | `string` | Yes | `none` | Proxy server hostname or IP address. |
| **`port`** | `integer` | Yes | `none` | Proxy port number (1 - 65535). |
| **`protocol`** | `string` | No | `"http"` | Protocol: `"http"`, `"https"`, `"socks4"`, or `"socks5"`. |
| **`username`** | `string` | No | `null` | Authentication username. |
| **`bypassList`** | `string` | No | `"<local>"` | Semicolon-separated host bypass rules. |
| **`isGlobalDefault`** | `boolean` | No | `false` | Set as active browser default. |
| **`enabled`** | `boolean` | No | `true` | Enable profile. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_create",
  "arguments": {
    "name": "EU Germany SOCKS5",
    "protocol": "socks5",
    "host": "198.51.100.80",
    "port": 1080,
    "username": "researcher",
    "bypassList": "<local>;*.corp.internal"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy profile 'EU Germany SOCKS5' (prx-de-socks5) created."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "prx-de-socks5",
    "name": "EU Germany SOCKS5",
    "protocol": "socks5"
  }
}
```

---

## 4. Operational Best Practices

* **Password Security:** Passwords are not accepted in `proxy_create`. Use `nova.proxy_set_password` to store DPAPI-encrypted credentials separately.

---

## See Also

* [`nova.proxy_set_password`](nova-proxy-set-password.md) - Store encrypted proxy password.
* [`nova.proxy_switch`](nova-proxy-switch.md) - Activate proxy.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
