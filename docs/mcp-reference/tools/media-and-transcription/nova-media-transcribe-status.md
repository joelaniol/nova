# `nova.media_transcribe_status`

Reports progress, elapsed percentage, and recognized text segments of an active transcription.

---

## 1. Overview

`nova.media_transcribe_status` inspects a running or completed transcription job. It provides completion percentages, processed audio seconds, and full recognized text segments with timestamps.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only Status)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | Job ID returned by nova.media_transcribe_start. |
| `includeText` | `boolean` | No | `false` | — | Include the segments and the full text in the response. Off by default because a long transcript crowds out everything else; the file at transcriptPath holds the same content. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_status",
  "arguments": {
    "jobId": "job-tx-1092",
    "includeText": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Transcription completed (24.3s audio processed)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-tx-1092",
    "status": "completed",
    "progressPercent": 100,
    "text": "Hello, this is a test recording confirming that speech to text works completely offline."
  }
}
```

---

## 4. Operational Best Practices

* **Incremental Polling:** Set `includeText: false` while polling to save tokens until `status: "completed"`, then request `includeText: true` to receive the final transcript.

---

## 5. Related Tools

* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
* [`nova.media_transcribe_stop`](nova-media-transcribe-stop.md)
