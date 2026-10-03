# `nova.proxy_status`

Queries real-time connectivity status, latency, and external IP for a proxy profile.

---

## 1. Overview

`nova.proxy_status` runs a non-destructive health probe against a proxy profile or the active global proxy, reporting visual health states (`healthy`, `slow`, `degraded`, `failed`, `disconnected`).

* **Security Tier:** Tier 1 (Safe Diagnostics)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | No | — | — | Proxy profile ID. Omit to query the active global default proxy. |
| `targetId` | `string` | No | — | — | Target ID (sandbox ID or 'browser-tabs') to get status for a specific tab scope. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_status",
  "arguments": {
    "profileId": "prx-us-east"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy prx-us-east is healthy (latency=85ms, externalIp=198.51.100.25)."
    }
  ],
  "structuredContent": {
    "profileId": "prx-us-east",
    "status": "healthy",
    "latencyMs": 85,
    "externalIp": "198.51.100.25",
    "connected": true
  }
}
```

---

## 4. Operational Best Practices

* **IP Verification:** Check `externalIp` to ensure the outbound connection is correctly routed before accessing geo-restricted targets.

---

## See Also

* [`nova.proxy_test`](nova-proxy-test.md) - Run deep diagnostic probe.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
