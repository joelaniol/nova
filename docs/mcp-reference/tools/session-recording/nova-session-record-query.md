# `nova.session_record_query`

Queries the complete CDP network stream of a finalized recording with rich filters (URL regex, status, headers).

---

## 1. Overview

`nova.session_record_query` inspects the decrypted network timeline of a finalized recording. Unlike page-level observers, this tool reads the complete CDP Network domain stream, capturing every asset, API call, redirect chain, and background fetch, including requests from web workers and cross-origin iframes.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID (the dir under %LOCALAPPDATA%/NovaBrowser/Recordings). |
| `urlMatch` | `string` | No | — | — | Regex applied case-insensitively to entry URL. Invalid regex disables the filter. |
| `method` | `string` | No | — | — | Exact HTTP method match (GET/POST/...). |
| `mimeType` | `string` | No | — | — | MIME-type prefix match (e.g. 'application/json' matches 'application/json; charset=utf-8'). |
| `statusGte` | `integer` | No | — | 0–999 | Filter status >= value. |
| `statusLte` | `integer` | No | — | 0–999 | Filter status <= value. |
| `sinceMs` | `integer` | No | — | — | Filter timestamp >= Unix-ms (ISO-8601 string also accepted). |
| `untilMs` | `integer` | No | — | — | Filter timestamp <= Unix-ms (ISO-8601 string also accepted). |
| `hasBody` | `boolean` | No | — | — | Filter entries with/without captured body. |
| `vaultMatched` | `boolean` | No | — | — | Filter entries where the redaction pipeline matched a vault fingerprint in the body. |
| `limit` | `integer` | No | `50` | 1–1000 | Max entries returned (totalMatchCount reports the full match count). |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_query",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "urlMatch": ".*\\/api\\/v1\\/checkout.*",
    "statusGte": 400
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 matching network entry with status >= 400 in rec-9b21f04a."
    }
  ],
  "structuredContent": {
    "ok": true,
    "totalMatchCount": 1,
    "entries": [
      {
        "requestId": "req-44810a",
        "url": "https://example.com/api/v1/checkout/pay",
        "method": "POST",
        "status": 402,
        "mimeType": "application/json",
        "durationMs": 340,
        "hasBody": true,
        "timestampUtc": "2026-10-02T20:18:22Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Pinpoint API Errors:** Use `statusGte: 400` to instantly locate broken endpoints, authentication failures, and rate limit responses without manual inspection.
* **Follow-Up Detail Inspection:** Pass the discovered `requestId` to [`nova.session_record_get_entry`](nova-session-record-get-entry.md) to inspect complete request/response headers and body payloads.
* **Vault Verification:** Check `vaultMatched: true` to verify that autofilled credentials were sent correctly and masked from raw logs.

---

## 5. Related Tools

* [`nova.session_record_get_entry`](nova-session-record-get-entry.md) — Inspect single request details.
* [`nova.session_record_stop`](nova-session-record-stop.md) — Finalize recording before querying.
