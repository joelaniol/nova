# `nova.proxy_list`

Lists all configured proxy profiles with connection settings, protocols, and sandbox bindings.

---

## 1. Overview

`nova.proxy_list` inventories all proxy profiles registered in Nova. Passwords are never returned; it reports profile IDs, hostnames, ports, protocols (HTTP, HTTPS, SOCKS4, SOCKS5), active status, and sandbox bindings.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 proxy profile(s) configured."
    }
  ],
  "structuredContent": {
    "profiles": [
      {
        "profileId": "prx-us-east",
        "name": "US Residential SOCKS5",
        "protocol": "socks5",
        "host": "198.51.100.25",
        "port": 1080,
        "username": "agent_user",
        "enabled": true,
        "isGlobalDefault": true,
        "sandboxes": [
          "B"
        ]
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Credential Privacy:** Passwords are encrypted at rest with Windows DPAPI and never disclosed in list responses.

---

## See Also

* [`nova.proxy_status`](nova-proxy-status.md) - Check proxy health and latency.
* [`nova.proxy_switch`](nova-proxy-switch.md) - Assign proxy to sandbox.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
