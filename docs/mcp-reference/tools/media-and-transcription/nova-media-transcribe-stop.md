# `nova.media_transcribe_stop`

Stops an in-flight transcription job and returns recognized text segments up to the cancellation point.

---

## 1. Overview

`nova.media_transcribe_stop` cancels an active transcription job. Unlike hard aborts, it preserves and returns all text segments processed up to the stop timestamp.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Job Control)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`jobId`** | `string` | Yes | `null` | Job ID returned by nova.media_transcribe_start. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_stop",
  "arguments": {
    "jobId": "job-tx-1092"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Stopped transcription job-tx-1092. Partial transcript preserved."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-tx-1092",
    "status": "stopped",
    "partialText": "Hello, this is a test recording..."
  }
}
```

---

## 4. Operational Best Practices

* **Partial Text Preservation:** Useful when a long recording is taking too long and partial early results are sufficient.

---

## 5. Related Tools

* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
* [`nova.media_transcribe_status`](nova-media-transcribe-status.md)
