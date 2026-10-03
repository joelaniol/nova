# `nova.session_record_export`

Decodes a finalized encrypted recording to plaintext files on disk for debugging or archival.

---

## 1. Overview

`nova.session_record_export` decrypts all JSONL event streams in a finalized recording using its DEK and writes them as human-readable plaintext files into an export directory. It generates a verified export folder containing plaintext `network.jsonl`, `console.jsonl`, `interactions.jsonl`, and integrity manifests.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 2 (Export Decryption)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`recordingId`** | `string` | Yes | `none` | Finalized recording ID. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "Recording rec-9b21f04a successfully exported to plaintext folder."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordingId": "rec-9b21f04a",
    "exportDirectory": "Recordings/rec-9b21f04a_export",
    "exportedFiles": [
      "manifest.json",
      "network.jsonl",
      "console.jsonl",
      "interactions.jsonl",
      "dom-snapshots.jsonl"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Redaction Retention:** Exported plaintext files retain all in-flight redactions (vault credentials, tokens, session cookies remain masked).
* **Bug Report Attachments:** Ideal for attaching full interaction and network logs to bug tracking tickets or QA reports.
* **Storage Housekeeping:** After exporting, ensure sensitive archives are purged when no longer required using [`nova.session_record_purge`](nova-session-record-purge.md).

---

## 5. Related Tools

* [`nova.session_record_purge`](nova-session-record-purge.md) — Delete old recordings.
* [`nova.session_record_stop`](nova-session-record-stop.md) — Finalize recording.
