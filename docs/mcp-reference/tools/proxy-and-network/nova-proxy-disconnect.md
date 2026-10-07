# `nova.proxy_disconnect`

Manually disconnects the proxy for a target scope, blocking all HTTP(S) traffic as an emergency kill switch.

---

## 1. Overview

`nova.proxy_disconnect` acts as an emergency network kill switch. It severs the proxy route and blocks all outgoing HTTP(S) requests until `nova.proxy_reconnect` succeeds, preventing IP leaks.

* **Core Architecture Guide:** [Proxy Routing & Network Engine](../../../core-features/proxy-and-network/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Target ID: sandbox ID or 'browser-tabs' for the global browser scope. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_disconnect",
  "arguments": {
    "targetId": "browser-tabs"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy disconnect for target 'browser-tabs': Proxy disconnected; browsing stays blocked until reconnect."
    }
  ],
  "structuredContent": {
    "success": true,
    "targetId": "browser-tabs",
    "status": "disconnected",
    "isDisconnected": true
  }
}
```
Calling it again while already disconnected still succeeds with `"status": "already_disconnected"`. An unknown `targetId` returns `"status": "target_unavailable"` with `isDisconnected: null`.

---

## 4. Operational Best Practices

* **Leak Prevention:** Use if proxy latency spikes or if you suspect proxy degradation to prevent background traffic from falling back to real IPs.

---

## See Also

* [`nova.proxy_reconnect`](nova-proxy-reconnect.md) - Reconnect proxy.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
