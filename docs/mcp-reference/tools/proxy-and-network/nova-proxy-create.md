# `nova.proxy_create`

Creates a new proxy profile with host, port, protocol, and optional credentials.

---

## 1. Overview

`nova.proxy_create` defines a new proxy configuration in Nova (up to 12 profiles). Supports HTTP, HTTPS, SOCKS4, and SOCKS5 protocols with custom bypass lists.

* **Security Tier:** Tier 2 (Configuration)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | Display name for the proxy profile. |
| `protocol` | `string` | No | `"http"` | — | Protocol: 'http', 'https', 'socks4', or 'socks5'. Default: 'http'. |
| `host` | `string` | Yes | — | — | Proxy hostname or IP address. Accepts 'host:port' or 'protocol://host:port' endpoint format. |
| `port` | `integer` | Yes | — | 1–65535 | Port number (1–65535). |
| `bypassList` | `string` | No | — | — | Semicolon-separated list of domains/IPs to bypass the proxy (e.g. 'localhost;127.0.0.1;*.internal'). |
| `username` | `string` | No | — | — | Username for proxy authentication (HTTP/HTTPS only; SOCKS auth is not supported by Chromium). |
| `enabled` | `boolean` | No | `true` | — | Whether the profile is enabled. Default: true. |
| `isGlobalDefault` | `boolean` | No | `false` | — | Set as the global default proxy for normal browser tabs. Only one profile can be global default. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
<!-- /generated:parameters -->

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
