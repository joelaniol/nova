# `nova.proxy_reconnect`

Reconnects a disconnected proxy and verifies connectivity before unblocking network traffic.

---

## 1. Overview

`nova.proxy_reconnect` runs an immediate health probe against the proxy; traffic is only unblocked if the probe succeeds, guaranteeing that no unencrypted or non-proxied data leaks.

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
  "name": "nova.proxy_reconnect",
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
      "text": "Proxy reconnect for target 'browser-tabs': Proxy reconnected; the health probe succeeded and browsing is unblocked."
    }
  ],
  "structuredContent": {
    "success": true,
    "targetId": "browser-tabs",
    "status": "reconnected",
    "isDisconnected": false,
    "probeRan": true,
    "probeOk": true
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
