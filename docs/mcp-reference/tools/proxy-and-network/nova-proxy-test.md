# `nova.proxy_test`

Executes an active network diagnostic probe through a proxy profile to verify connectivity and external IP.

---

## 1. Overview

`nova.proxy_test` sends a probe request through the specified proxy server, measuring TCP handshake time, SSL negotiation latency, and detecting whether credentials are valid.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 1 (Safe Diagnostics)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`profileId`** | `string` | Yes | `none` | Proxy profile ID to test. |
| **`probeUrl`** | `string` | No | `https://api.ipify.org` | Test URL for connectivity probe. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_test",
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
      "text": "Probe succeeded: 198.51.100.25 (78ms)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "prx-us-east",
    "success": true,
    "latencyMs": 78,
    "externalIp": "198.51.100.25",
    "error": null
  }
}
```

---

## 4. Operational Best Practices

* **Test Before Switch:** Always run `nova.proxy_test` before switching live sandboxes to ensure credentials and connectivity are functional.

---

## See Also

* [`nova.proxy_switch`](nova-proxy-switch.md) - Switch active proxy.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
