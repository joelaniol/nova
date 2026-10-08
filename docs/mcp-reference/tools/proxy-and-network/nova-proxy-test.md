# `nova.proxy_test`

Executes an active network diagnostic probe through a proxy profile to verify connectivity and external IP.

---

## 1. Overview

`nova.proxy_test` sends a single HTTP GET request through the specified proxy to a probe URL (an external IP-echo service by default) and reports whether it succeeded, the total elapsed time, and the external IP seen by that probe. Invalid or unsupported credentials surface indirectly, as a failed probe with the connection error.

* **Core Architecture Guide:** [Proxy Routing](../../../core-features/network/proxy/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | ID of the proxy profile to test. |
| `probeUrl` | `string` | No | — | — | Custom probe URL. Default: 'https://api.ipify.org/?format=json'. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_test",
  "arguments": {
    "profileId": "proxy-2"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Proxy 'US East SOCKS5' is healthy. External IP: 198.51.100.25, latency: 78 ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "proxy-2",
    "name": "US East SOCKS5",
    "endpoint": "socks5://198.51.100.25:1080",
    "message": "Proxy test OK. External IP: 198.51.100.25.",
    "externalIp": "198.51.100.25",
    "statusCode": 200,
    "elapsedMs": 78
  }
}
```
On failure `ok` is `false`, `externalIp`/`statusCode` are `null`, and `message` names the failure (for example an unreachable proxy or unsupported SOCKS credentials).

---

## 4. Operational Best Practices

* **Test Before Switch:** Always run `nova.proxy_test` before switching live sandboxes to ensure credentials and connectivity are functional.

---

## See Also

* [`nova.proxy_switch`](nova-proxy-switch.md) - Switch active proxy.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
