# `nova.session_record_events`

Decrypts and streams generic event logs (console, errors, lifecycle, IndexedDB) from a recording.

---

## 1. Overview

`nova.session_record_events` decrypts and reads arbitrary event streams stored inside a session recording archive. It provides direct access to captured console outputs (`console.jsonl`), unhandled runtime exceptions (`errors.jsonl`), tab lifecycle transitions (`lifecycle.jsonl`), and IndexedDB operation metadata (`indexeddb-ops.jsonl`), among the other streams listed in the `stream` enum below. `console.jsonl`/`errors.jsonl` entries wrap the raw CDP `Runtime.consoleAPICalled`/`Runtime.exceptionThrown` event under a `parameters` object, not a flattened level/message shape.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID. |
| `stream` | `string` | Yes | — | `console.jsonl`, `errors.jsonl`, `lifecycle.jsonl`, `network.cdp.jsonl`, `indexeddb-ops.jsonl`, `security-violations.jsonl`, `performance.jsonl`, `workers.jsonl`, `interactions.jsonl`, `dom-snapshots.jsonl`, `websocket-payloads.jsonl`, `indexeddb-values.jsonl`, `dom-mutations.jsonl` | Stream file name (e.g. 'console.jsonl'). The three V2 sidecars may report available=false when this recording did not capture them. |
| `limit` | `integer` | No | `200` | 1–5000 | Max events returned. |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Recording rec-9b21f04a: stream console.jsonl returned 2 event(s)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "stream": "console.jsonl",
    "available": true,
    "count": 2,
    "events": [
      {
        "ts": "2026-10-02T20:15:10Z",
        "method": "Runtime.consoleAPICalled",
        "parameters": {
          "type": "info",
          "args": [
            { "type": "string", "value": "App initialized: version 2.4.1" }
          ]
        }
      },
      {
        "ts": "2026-10-02T20:18:22Z",
        "method": "Runtime.consoleAPICalled",
        "parameters": {
          "type": "error",
          "args": [
            { "type": "string", "value": "Uncaught (in promise) Error: Payment failed with status 402" }
          ]
        }
      }
    ]
  }
}
```

Each entry is a thin wrapper (`ts`, `method`, `parameters`) around the raw CDP event; the log level and message text live inside `parameters` (`parameters.type` for the console level, `parameters.args[]` for the logged values; `errors.jsonl` nests the failure under `parameters.exceptionDetails` instead).

If `stream` names a recognised V2 sidecar (`websocket-payloads.jsonl`, `indexeddb-values.jsonl`, `dom-mutations.jsonl`) that this recording never captured, the result still has `ok: true` but with `available: false`, `count: 0`, an empty `events` array, and a `reasonCode: "stream_not_captured"` plus an explanatory `note` — distinguishing "never captured" from "captured but empty".

---

## 4. Operational Best Practices

* **Console Log Correlation:** Correlate console log timestamps with network events in [`nova.session_record_query`](nova-session-record-query.md) to reconstruct failure sequences.
* **Crash Forensics:** Read `errors.jsonl` first when diagnosing unexpected script exceptions or blank page render states.
* **IndexedDB Auditing:** Query `indexeddb-ops.jsonl` for operation/key-hash metadata (database/store names, operation type, hashed key) — it does not include the stored values unless the `indexeddb_values` permission class was granted, in which case `indexeddb-values.jsonl` carries the actual values.

---

## 5. Related Tools

* [`nova.session_record_interactions`](nova-session-record-interactions.md) — Read user and agent interaction streams.
* [`nova.session_record_query`](nova-session-record-query.md) — Query network traffic.
