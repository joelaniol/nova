# `nova.proxy_log`

Reads recent redacted proxy routing and diagnostic log entries from disk.

---

## 1. Overview

`nova.proxy_log` returns diagnostic log lines from `Logs/proxy`. Credentials embedded in a logged URL (`user:pass@host`) are redacted to `***@host` before the line is ever written to disk.

* **Core Architecture Guide:** [Proxy Routing & Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `maxLines` | `integer` | No | `100` | 1–500 | Maximum lines to return (1–500). Default: 100. |

Capability bundle: `proxy_management` (load it with `nova.tools_bundle(bundle='proxy_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.proxy_log",
  "arguments": {
    "maxLines": 20
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 browser web-proxy log line(s) from Logs/proxy."
    }
  ],
  "structuredContent": {
    "lines": [
      "2026-10-02 21:00:12.345 +02:00 INFO Proxy manually disconnected. Target=browser-tabs Profile=proxy-2",
      "2026-10-02 21:00:15.012 +02:00 INFO MCP probe OK for 'US East SOCKS5' (socks5://198.51.100.25:1080): Proxy test OK. External IP: 198.51.100.25. [78 ms]"
    ],
    "count": 2
  }
}
```
Response is shortened to 2 lines for this example; a real call returns up to `maxLines`.

---

## 4. Operational Best Practices

* **Diagnosing Connection Drops:** Use to verify whether connection issues stem from remote server resets or local firewall rules.

---

## See Also

* [`nova.proxy_status`](nova-proxy-status.md) - View live proxy health.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
