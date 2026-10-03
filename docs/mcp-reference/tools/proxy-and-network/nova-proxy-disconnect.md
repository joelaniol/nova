# `nova.proxy_disconnect`

Manually disconnects the proxy for a target scope, blocking all HTTP(S) traffic as an emergency kill switch.

---

## 1. Overview

`nova.proxy_disconnect` acts as an emergency network kill switch. It severs the proxy route and blocks all outgoing HTTP(S) requests until `nova.proxy_reconnect` succeeds, preventing IP leaks.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Kill Switch)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | Yes | `none` | Tab or sandbox ID to disconnect. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_disconnect",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy disconnected for tab-1 (traffic blocked)."
    }
  ],
  "structuredContent": {
    "status": "disconnected",
    "isDisconnected": true,
    "targetId": "tab-1"
  }
}
```

---

## 4. Operational Best Practices

* **Leak Prevention:** Use if proxy latency spikes or if you suspect proxy degradation to prevent background traffic from falling back to real IPs.

---

## See Also

* [`nova.proxy_reconnect`](nova-proxy-reconnect.md) - Reconnect proxy.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
