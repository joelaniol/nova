# `nova.media_capture_stop`

Stops in-tab media capture, flushes pending segments, closes files, and returns completed paths.

---

## 1. Overview

`nova.media_capture_stop` cleanly terminates an active streaming capture. It performs a final buffer drain, writes container headers (e.g. WAV RIFF headers), and returns the finalized file paths on disk.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Capture Finalization)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID of the capturing tab, or 'active' / 'activeBrowserTab'. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_capture_stop",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Stopped capture on tab-1. File saved: downloads/captured-stream.wav (380 KB)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "filePath": "downloads/captured-stream.wav",
    "totalBytes": 389120,
    "durationSeconds": 24.3
  }
}
```

---

## 4. Operational Best Practices

* **Direct Transcription Handoff:** Pass the resulting `filePath` directly to [`nova.media_transcribe_start`](nova-media-transcribe-start.md) for local speech-to-text processing.

---

## 5. Related Tools

* [`nova.media_capture_start`](nova-media-capture-start.md)
* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
