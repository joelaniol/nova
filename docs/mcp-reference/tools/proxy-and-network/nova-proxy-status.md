# `nova.proxy_status`

Queries real-time connectivity status, latency, and external IP for a proxy profile.

---

## 1. Overview

`nova.proxy_status` reads the latest known health of a proxy profile or the active global proxy — the result of the last background check or `nova.proxy_test` call — without itself sending a new probe. It reports a visual state (`Healthy`, `Slow`, `Degraded`, `Failed`, `Disconnected`, or `Unknown` with no data yet), latency, and external IP.

* **Core Architecture Guide:** [Proxy Routing & Network Engine](../../../core-features/proxy-and-network/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | No | — | — | Proxy profile ID. Omit to query the active global default proxy. |
| `targetId` | `string` | No | — | — | Target ID (sandbox ID or 'browser-tabs') to get status for a specific tab scope. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_status",
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
      "text": "Proxy 'US East SOCKS5' (socks5://198.51.100.25:1080) — Healthy, latency: 85 ms, IP: 198.51.100.25"
    }
  ],
  "structuredContent": {
    "active": true,
    "profileId": "proxy-2",
    "name": "US East SOCKS5",
    "endpoint": "socks5://198.51.100.25:1080",
    "isUsable": true,
    "hasPassword": true,
    "state": "Healthy",
    "isDisconnected": false,
    "hasProbeResult": true,
    "lastProbeOk": true,
    "lastLatencyMs": 85,
    "averageLatencyMs": 85,
    "remoteIp": "198.51.100.25",
    "connectedSinceUtc": "2026-10-04T10:00:00.0000000Z",
    "lastCheckedUtc": "2026-10-04T12:05:30.0000000Z",
    "message": null
  }
}
```
If no profile matches (and no live status applies), the result is just `{"content": [{"type": "text", "text": "No active proxy configured."}], "structuredContent": {"active": false, "state": "none"}}`.

---

## 4. Operational Best Practices

* **IP Verification:** Check `remoteIp` to ensure the outbound connection is correctly routed before accessing geo-restricted targets. It only has a value once a probe has run — call `nova.proxy_test` first if `hasProbeResult` is `false`.

---

## See Also

* [`nova.proxy_test`](nova-proxy-test.md) - Run deep diagnostic probe.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
