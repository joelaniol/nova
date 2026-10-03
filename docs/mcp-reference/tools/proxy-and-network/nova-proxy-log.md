# `nova.proxy_log`

Reads recent redacted proxy routing and diagnostic log entries from disk.

---

## 1. Overview

`nova.proxy_log` returns diagnostic log lines from `Logs/proxy`. All credentials, basic auth tokens, and session secrets are automatically scrubbed and redacted.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 1 (Safe Diagnostics)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`maxLines`** | `integer` | No | `50` | Maximum number of log lines to return (1 - 500). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "20 proxy log lines retrieved."
    }
  ],
  "structuredContent": {
    "lineCount": 20,
    "lines": [
      "[2026-10-02 21:00:12] SOCKS5 connection to 198.51.100.25:1080 established.",
      "[2026-10-02 21:00:15] WebRTC STUN request blocked by leak guard."
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Diagnosing Connection Drops:** Use to verify whether connection issues stem from remote server resets or local firewall rules.

---

## See Also

* [`nova.proxy_status`](nova-proxy-status.md) - View live proxy health.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
