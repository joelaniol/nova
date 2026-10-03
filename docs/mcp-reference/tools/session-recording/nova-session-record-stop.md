# `nova.session_record_stop`

Stops an active session recording, flushes memory channels, and generates cryptographic integrity manifests.

---

## 1. Overview

`nova.session_record_stop` cleanly terminates an ongoing session recording. It flushes in-memory streaming channels, finalizes encrypted chunk files on disk, computes SHA-256 checksums in `integrity.json`, and seals the recording for post-hoc forensic inspection.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 2 (Session Control)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID returned from session_record_start. |
| `reason` | `string` | No | — | — | Optional canonical reason code (default: agent_stop). |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_stop",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "reason": "test_complete"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Session recording 'rec-9b21f04a' stopped and finalized. Artifacts sealed with SHA-256 integrity."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "state": "finalised",
    "durationMs": 42310,
    "totalEvents": 418,
    "streams": [
      "network.jsonl",
      "console.jsonl",
      "interactions.jsonl",
      "dom-snapshots.jsonl"
    ],
    "integritySha256": "8e4b7c129f..."
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Finalization:** The temporary directory `.tmp` is atomically renamed to its permanent recording directory upon successful stop.
* **Query Ready:** Once finalized, query tools such as [`nova.session_record_query`](nova-session-record-query.md) and [`nova.session_record_interactions`](nova-session-record-interactions.md) can be safely executed against the recording.
* **Auto-Stop on Tab Close:** If the parent tab is closed before `stop` is called, Nova automatically halts recording and preserves available chunks.

---

## 5. Related Tools

* [`nova.session_record_start`](nova-session-record-start.md) — Start recording session.
* [`nova.session_record_query`](nova-session-record-query.md) — Query network entries in finalized recordings.
