# `nova.network_replay`

Targeted HTTP request repeater for replaying, editing, and comparing network payloads out-of-band.

---

## 1. Overview

`nova.network_replay` provides an out-of-band HTTP repeater (similar to Burp Repeater) executed via an independent .NET HTTP client. Agents can freeze a captured request (`prepare`), mutate headers or body parameters, dispatch it once (`send`), and compare the outcome against a baseline (`compareTo`).

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 3 (High-Impact)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`action`** | `string` | No | `"prepare"` | Replay action: `"prepare"`, `"send"`, `"get"`, or `"discard"`. |
| **`url`** | `string` | Conditional | `none` | Destination HTTP(S) URL. |
| **`method`** | `string` | No | `"GET"` | HTTP method (`GET`, `POST`, `PUT`, `DELETE`, etc.). |
| **`headers`** | `object` | No | `{}` | Explicit HTTP headers map. |
| **`body`** | `string` | No | `null` | Payload body text. |
| **`replayId`** | `string` | Conditional | `none` | Draft or replay ID returned by `prepare`. |
| **`compareTo`** | `string` | No | `null` | Baseline replay ID for differential response analysis. |
| **`timeoutMs`** | `integer` | No | `30000` | Request timeout in ms. |
| **`_meta`** | `object` | No | `null` | Audit intent metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.network_replay",
  "arguments": {
    "action": "send",
    "replayId": "rep-4f8a19bc",
    "_meta": {
      "intent": "Repeat GraphQL query with modified pagination variable"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Replay rep-4f8a19bc sent: 200 OK (340 bytes in 120ms)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "replayId": "rep-4f8a19bc",
    "status": 200,
    "statusText": "OK",
    "durationMs": 120,
    "responseHeaders": {
      "content-type": "application/json; charset=utf-8"
    },
    "bodyBase64": "eyJyZXN1bHRzIjogW119"
  }
}
```

---

## 4. Operational Best Practices

* **Two-Phase Execution:** Always call `prepare` first to freeze the request payload, verify headers, then dispatch with `send`.
* **Isolated Cookie Jar:** `nova.network_replay` operates outside the browser tab's cookie jar. Only cookies explicitly passed in `headers` are transmitted.
* **Idempotent Retries:** Re-sending an already executed `replayId` returns the cached outcome rather than sending duplicate requests.

---

## See Also

* [`nova.network_intercept_add`](nova-network-intercept-add.md) - Intercept in-page requests.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
