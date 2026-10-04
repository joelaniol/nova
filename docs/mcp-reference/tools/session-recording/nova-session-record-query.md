# `nova.session_record_query`

Queries the complete CDP network stream of a finalized recording with rich filters (URL regex, status, headers).

---

## 1. Overview

`nova.session_record_query` inspects the decrypted network timeline of a finalized recording. It reads the CDP Network domain stream captured for the recorded tab's root frame — every asset, API call, and redirect on that frame. Cross-origin iframes (OOPIFs) are a known capture gap: Nova attaches to the root target only, so requests from cross-origin subframes are not captured.

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

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "Recording rec-9b21f04a: query returned 1 of 1 matching request row(s)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "totalMatchCount": 1,
    "entries": [
      {
        "requestId": "req-44810a",
        "timestamp": "2026-10-02T20:18:22Z",
        "method": "POST",
        "url": "https://example.com/api/v1/checkout/pay",
        "status": 402,
        "mimeType": "application/json",
        "sizeBytes": 128,
        "hasBody": true,
        "bodyPolicy": "Captured",
        "vaultFingerprintMatched": false,
        "errorText": null
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Pinpoint API Errors:** Use `statusGte: 400` to instantly locate broken endpoints, authentication failures, and rate limit responses without manual inspection.
* **Follow-Up Detail Inspection:** Pass the discovered `requestId` to [`nova.session_record_get_entry`](nova-session-record-get-entry.md) to inspect the raw network event lines and captured body metadata.
* **Vault Verification:** Check `vaultFingerprintMatched: true` on an entry (or pass `vaultMatched: true` as a filter) to verify that autofilled credentials were sent and recognized by the redaction pipeline.

---

## 5. Related Tools

* [`nova.session_record_get_entry`](nova-session-record-get-entry.md) — Inspect single request details.
* [`nova.session_record_stop`](nova-session-record-stop.md) — Finalize recording before querying.
