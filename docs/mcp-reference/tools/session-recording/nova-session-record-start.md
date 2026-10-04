# `nova.session_record_start`

Initiates encrypted background recording of CDP network, DOM mutations, console logs, and user interactions on a tab.

---

## 1. Overview

`nova.session_record_start` attaches Nova's asynchronous recording pipeline to an active browser tab. It streams CDP network events, console messages, JavaScript runtime errors, DOM mutations, IndexedDB operations, and user/agent inputs into local encrypted JSONL chunks.

All sensitive data (passwords, auth tokens, session cookies, DPAPI vault secrets) is automatically redacted at ingestion time prior to disk serialization. Recordings are protected with an ephemeral AES-GCM Data Encryption Key (DEK).

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `tabId` | `string` | Yes | — | — | Browser tab ID from nova.tabs. The tab must be bound to a WebView. |
| `ttlMs` | `integer` | No | — | 5000–3600000 | Recording TTL in milliseconds. Defaults to SessionRecordingDefaultTtlMs (5 min). Hard cap 60 min. |
| `permissionClasses` | `array` of `string` | No | — | — | Permission classes to grant for this recording. Defaults to ['metadata', 'interactions_mcp', 'dom_snapshots']. Available classes: metadata, network_timing_detail, headers_sensitive, request_bodies, response_bodies, storage_values, performance_marks, worker_messages, interactions_mcp, interactions_native, dom_snapshots, websocket_payloads, indexeddb_values [secret-bearing], dom_mutations, streaming_bodies [Wave R4 conditional], fetch_interception [reserved non-grantable — returns permission_request_denied_reserved_active_mode]. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_start",
  "arguments": {
    "tabId": "tab-1",
    "ttlMs": 600000,
    "permissionClasses": [
      "metadata",
      "interactions_mcp",
      "dom_snapshots",
      "dom_mutations"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Recording started — recordingId: rec-9b21f04a\n  tab=tab-1  ttl=600000ms  classes=[metadata, interactions_mcp, dom_snapshots, dom_mutations]"
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "tabId": "tab-1",
    "ttlMs": 600000,
    "state": "running",
    "permissionClasses": [
      "metadata",
      "interactions_mcp",
      "dom_snapshots",
      "dom_mutations"
    ],
    "captureWaves": ["R1", "R2", "R3"]
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Flight Tab Attachment:** Ensure the tab is fully initialized and not in an unattached detached state before starting.
* **Permission Class Minimization:** Only request `request_bodies`/`response_bodies` when inspecting raw HTTP payloads to reduce disk footprint and avoid payload buffer overhead.
* **Lifecycle Pairing:** Always call [`nova.session_record_stop`](nova-session-record-stop.md) when testing or workflow completes to finalize artifacts cleanly.

---

## 5. Related Tools

* [`nova.session_record_stop`](nova-session-record-stop.md) — Finalize and seal the recording.
* [`nova.session_record_status`](nova-session-record-status.md) — Check live recording health and remaining TTL.
