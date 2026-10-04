# `nova.session_record_export`

Decodes a finalized encrypted recording to plaintext files on disk for debugging or archival.

---

## 1. Overview

`nova.session_record_export` decrypts every captured event stream in a finalized recording and writes each one as a plaintext `.jsonl` file into a `decoded/` subfolder inside the recording directory, alongside a copy of `manifest.json` and a generated `_summary.txt`. The decoded content is exactly what the replay tools already read — capture-time redaction stays in place, so this does not reveal raw secrets.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID (the dir under %LOCALAPPDATA%/NovaBrowser/Recordings). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_export",
  "arguments": {
    "recordingId": "rec-9b21f04a"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Decoded recording rec-9b21f04a → .../Recordings/rec-9b21f04a/decoded\n  console.jsonl (12 lines) → .../decoded/console.jsonl\n  network.cdp.jsonl (48 lines) → .../decoded/network.cdp.jsonl\n  interactions.jsonl (6 lines) → .../decoded/interactions.jsonl"
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "outDir": "<RecordingsDir>/rec-9b21f04a/decoded",
    "summaryPath": "<RecordingsDir>/rec-9b21f04a/decoded/_summary.txt",
    "streamsWritten": [
      { "stream": "console.jsonl", "lineCount": 12, "path": "<RecordingsDir>/rec-9b21f04a/decoded/console.jsonl" },
      { "stream": "network.cdp.jsonl", "lineCount": 48, "path": "<RecordingsDir>/rec-9b21f04a/decoded/network.cdp.jsonl" },
      { "stream": "interactions.jsonl", "lineCount": 6, "path": "<RecordingsDir>/rec-9b21f04a/decoded/interactions.jsonl" }
    ],
    "skipped": []
  }
}
```

Only streams that were actually captured in this recording are written; a stream whose permission class was revoked since capture appears in `skipped` instead (`reason: "permission_revoked"`) and is not decoded.

---

## 4. Operational Best Practices

* **Redaction Retention:** Exported plaintext files retain all capture-time redactions (vault credentials, tokens, session cookies remain masked).
* **Bug Report Attachments:** Ideal for attaching full interaction and network logs to bug tracking tickets or QA reports.
* **Storage Housekeeping:** The `decoded/` folder lives inside the recording directory, so it is removed together with the recording when [`nova.session_record_purge`](nova-session-record-purge.md) deletes it.

---

## 5. Related Tools

* [`nova.session_record_purge`](nova-session-record-purge.md) — Delete old recordings.
* [`nova.session_record_stop`](nova-session-record-stop.md) — Finalize recording.
