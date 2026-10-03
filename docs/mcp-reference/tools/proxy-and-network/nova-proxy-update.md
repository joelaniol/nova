# `nova.proxy_update`

Updates host, port, protocol, or bypass list of an existing proxy profile.

---

## 1. Overview

`nova.proxy_update` performs partial updates on an existing proxy profile without altering omitted fields or resetting stored credentials.

* **Security Tier:** Tier 2 (Configuration)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | ID of the proxy profile to update. |
| `name` | `string` | No | — | — | New display name. |
| `protocol` | `string` | No | — | — | New protocol: 'http', 'https', 'socks4', or 'socks5'. |
| `host` | `string` | No | — | — | New hostname or IP address. |
| `port` | `integer` | No | — | 1–65535 | New port number (1–65535). |
| `bypassList` | `string` | No | — | — | New bypass list (semicolon-separated). Empty string clears. |
| `username` | `string` | No | — | — | New username. Empty string clears. |
| `enabled` | `boolean` | No | — | — | Enable or disable the profile. |
| `isGlobalDefault` | `boolean` | No | — | — | Set or unset as global default. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
<!-- /generated:parameters -->

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
