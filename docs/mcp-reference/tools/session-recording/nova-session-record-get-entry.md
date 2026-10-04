# `nova.session_record_get_entry`

Retrieves the complete event timeline, headers, and decoded payload for a single CDP request ID.

---

## 1. Overview

`nova.session_record_get_entry` performs a deep lookup for a specific `requestId` identified via `nova.session_record_query`. It returns every raw CDP Network event line recorded for that request ID (request/response/redirect events as captured), plus the separately tracked response-body metadata (policy, MIME type, size, SHA-256) and, when requested, the inline base64 body bytes.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "Recording rec-9b21f04a: entry req-44810a returned 2 event(s)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "requestId": "req-44810a",
    "events": [
      {
        "method": "Network.requestWillBeSent",
        "parameters": {
          "requestId": "req-44810a",
          "request": {
            "url": "https://example.com/api/v1/checkout/pay",
            "method": "POST"
          }
        }
      },
      {
        "method": "Network.responseReceived",
        "parameters": {
          "requestId": "req-44810a",
          "response": {
            "status": 402,
            "mimeType": "application/json"
          }
        }
      }
    ],
    "body": {
      "policy": "Captured",
      "mimeType": "application/json",
      "sizeBytes": 58,
      "sha256": "8e4b7c129f...",
      "inlineBase64": "eyJlcnJvciI6ImNhcmRfZGVjbGluZWQiLCJjb2RlIjoiaW5zdWZmaWNpZW50X2Z1bmRzIn0="
    }
  }
}
```

`events` holds the raw matching CDP Network lines as captured (field shapes follow the CDP Network domain); there is no separate flattened `requestHeaders`/`responseHeaders`/`timings` projection — read those values out of the relevant CDP event's `parameters`.

---

## 4. Operational Best Practices

* **Body Metadata:** `body.inlineBase64` is only populated when `includeBody: true` was passed and a response body was actually captured (`body.policy` reflects whether/how it was stored).
* **Masked Secrets:** Authorization headers and cookie values remain safely masked according to Nova's redaction policies before they reach the CDP event lines.
* **Raw Event Inspection:** Use the `method` field on each entry in `events` (e.g. `Network.requestWillBeSent`, `Network.responseReceived`) to find the specific lifecycle stage you need.

---

## 5. Related Tools

* [`nova.session_record_query`](nova-session-record-query.md) — Search network events to obtain request IDs.
* [`nova.network_replay`](../proxy-and-network/nova-network-replay.md) — Replay request with modifications.
