# `nova.proxy_reconnect`

Reconnects a disconnected proxy and verifies connectivity before unblocking network traffic.

---

## 1. Overview

`nova.proxy_reconnect` runs an immediate health probe against the proxy; traffic is only unblocked if the probe succeeds, guaranteeing that no unencrypted or non-proxied data leaks.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Routing Recovery)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | Yes | `none` | Tab or sandbox ID to reconnect. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_reconnect",
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
      "text": "Proxy reconnected for tab-1 (probe succeeded)."
    }
  ],
  "structuredContent": {
    "status": "reconnected",
    "isDisconnected": false,
    "probeOk": true,
    "targetId": "tab-1"
  }
}
```

---

## 4. Operational Best Practices

* **Fail-Closed Security:** If the probe fails, status reports `probe_failed` and traffic remains strictly blocked.

---

## See Also

* [`nova.proxy_disconnect`](nova-proxy-disconnect.md) - Disconnect proxy.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
