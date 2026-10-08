# `nova.proxy_set_password`

Stores or clears encrypted proxy authentication credentials using Windows DPAPI.

---

## 1. Overview

`nova.proxy_set_password` encrypts proxy passwords using Windows Data Protection API (DPAPI). The plaintext secret is never returned in any MCP response or written to plaintext configuration files.

* **Core Architecture Guide:** [Proxy Routing](../../../core-features/network/proxy/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | ID of the proxy profile. |
| `password` | `string or null` | No | — | — | Password to store. Omit or null to clear the stored password. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_set_password",
  "arguments": {
    "profileId": "proxy-2",
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
      "text": "Password stored for proxy 'US East SOCKS5'."
    }
  ],
  "structuredContent": {
    "success": true,
    "profileId": "proxy-2",
    "hasPassword": true
  }
}
```
Passing `password: null` (or omitting it) clears the stored password instead and returns `"hasPassword": false`.

---

## 4. Operational Best Practices

* **Security Hygiene:** Never store passwords directly in `nova.proxy_create` or commit them in code.

---

## See Also

* [`nova.proxy_create`](nova-proxy-create.md) - Create profile.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
