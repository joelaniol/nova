# `nova.session_record_events`

Decrypts and streams generic event logs (console, errors, lifecycle, IndexedDB) from a recording.

---

## 1. Overview

`nova.session_record_events` decrypts and reads arbitrary event streams stored inside a session recording archive. It provides direct access to captured console outputs (`console.jsonl`), unhandled runtime exceptions (`errors.jsonl`), tab lifecycle transitions (`lifecycle.jsonl`), and database transactions (`indexeddb.jsonl`).

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`recordingId`** | `string` | Yes | `none` | Finalized recording ID. |
| **`stream`** | `string` | Yes | `none` | Stream file name: `"console.jsonl"`, `"errors.jsonl"`, `"lifecycle.jsonl"`, or `"indexeddb.jsonl"`. |
| **`limit`** | `integer` | No | `200` | Maximum number of events to return. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_events",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "stream": "console.jsonl",
    "limit": 2
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 2 console log events from rec-9b21f04a."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "stream": "console.jsonl",
    "count": 2,
    "events": [
      {
        "timestampUtc": "2026-10-02T20:15:10Z",
        "level": "info",
        "message": "App initialized: version 2.4.1"
      },
      {
        "timestampUtc": "2026-10-02T20:18:22Z",
        "level": "error",
        "message": "Uncaught (in promise) Error: Payment failed with status 402"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Console Log Correlation:** Correlate console log timestamps with network events in [`nova.session_record_query`](nova-session-record-query.md) to reconstruct failure sequences.
* **Crash Forensics:** Read `errors.jsonl` first when diagnosing unexpected script exceptions or blank page render states.
* **IndexedDB Auditing:** Query `indexeddb.jsonl` to verify local cache mutations and offline sync states.

---

## 5. Related Tools

* [`nova.session_record_interactions`](nova-session-record-interactions.md) — Read user and agent interaction streams.
* [`nova.session_record_query`](nova-session-record-query.md) — Query network traffic.
