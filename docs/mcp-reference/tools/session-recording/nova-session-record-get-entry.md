# `nova.session_record_get_entry`

Retrieves the complete event timeline, headers, and decoded payload for a single CDP request ID.

---

## 1. Overview

`nova.session_record_get_entry` performs a deep lookup for a specific `requestId` identified via `nova.session_record_query`. It reconstructs the entire network lifecycle: request headers, response headers, redirect chains, timing breakdowns (DNS, TLS, TTFB), and optional base64 payload bytes.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID. |
| `requestId` | `string` | Yes | — | — | CDP requestId from a prior session_record_query result. |
| `includeBody` | `boolean` | No | `false` | — | Include the inline base64-encoded body bytes. |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_get_entry",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "requestId": "req-44810a",
    "includeBody": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded full network entry req-44810a: POST https://example.com/api/v1/checkout/pay (402 Payment Required)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "requestId": "req-44810a",
    "url": "https://example.com/api/v1/checkout/pay",
    "method": "POST",
    "status": 402,
    "requestHeaders": {
      "Content-Type": "application/json",
      "Authorization": "[REDACTED_BEARER]"
    },
    "responseHeaders": {
      "Content-Type": "application/json; charset=utf-8",
      "Date": "Fri, 02 Oct 2026 20:18:22 GMT"
    },
    "bodyText": "{\"error\":\"card_declined\",\"code\":\"insufficient_funds\"}",
    "timings": {
      "dnsMs": 12,
      "tlsMs": 45,
      "ttfbMs": 180,
      "downloadMs": 5
    }
  }
}
```

---

## 4. Operational Best Practices

* **Decoded Text Convenience:** If the response is UTF-8 text or JSON, Nova provides `bodyText` directly alongside raw base64 data.
* **Masked Secrets:** Authorization headers and cookie values remain safely masked according to Nova's redaction policies.
* **Timing Diagnostics:** Use `timings` to determine whether a slow API call was caused by network latency or backend processing delays.

---

## 5. Related Tools

* [`nova.session_record_query`](nova-session-record-query.md) — Search network events to obtain request IDs.
* [`nova.network_replay`](../proxy-and-network/nova-network-replay.md) — Replay request with modifications.
