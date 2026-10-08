# `nova.proxy_list`

Lists all configured proxy profiles with connection settings, protocols, and sandbox bindings.

---

## 1. Overview

`nova.proxy_list` inventories all proxy profiles registered in Nova. Passwords are never returned; it reports profile IDs, hostnames, ports, protocols (HTTP, HTTPS, SOCKS4, SOCKS5), active status, and sandbox bindings.

* **Core Architecture Guide:** [Proxy Routing](../../../core-features/network/proxy/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "1 proxy profile(s) configured."
    }
  ],
  "structuredContent": {
    "profiles": [
      {
        "id": "proxy-2",
        "name": "US East SOCKS5",
        "protocol": "socks5",
        "host": "198.51.100.25",
        "port": 1080,
        "enabled": true,
        "isGlobalDefault": true,
        "bypassList": null,
        "username": "agent_user",
        "hasPassword": true,
        "isUsable": true
      }
    ],
    "sandboxAssignments": [
      {
        "sandboxId": "B",
        "sandboxName": "Sandbox B",
        "proxyMode": "profile",
        "proxyProfileId": "proxy-2"
      }
    ],
    "webRtcLeakProtectionEnabled": false,
    "loggingEnabled": true
  }
}
```
Sandbox assignments are listed separately from profiles, not nested under each profile — a sandbox's stored `proxyMode`/`proxyProfileId` does not currently give it an independent outbound proxy (see [proxy routing guide](../../../core-features/network/proxy/README.md)).

---

## 4. Operational Best Practices

* **Credential Privacy:** Passwords are encrypted at rest with Windows DPAPI and never disclosed in list responses.

---

## See Also

* [`nova.proxy_status`](nova-proxy-status.md) - Check proxy health and latency.
* [`nova.proxy_switch`](nova-proxy-switch.md) - Assign proxy to sandbox.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
