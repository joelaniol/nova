# `nova.media_transcribe_start`

Transcribes local audio or video files into text entirely on-device using local Whisper.cpp.

---

## 1. Overview

`nova.media_transcribe_start` converts spoken audio from local files into structured text. Transcription runs locally inside the sandboxed Outrider process via whisper.cpp with SIMD acceleration. No audio ever leaves the user's computer.

* **Security Tier:** Tier 2 (Local AI Speech-to-Text)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path of the audio or video file to transcribe. |
| `language` | `string` | No | — | — | Spoken language as an ISO code, e.g. 'de' or 'en'. Omit to detect it, which costs roughly 18% more time and is less reliable on short clips. |
| `model` | `string` | No | — | — | Substring of the model file name to prefer, e.g. 'small'. Omit to use the most accurate model installed. |
| `waitMs` | `integer` | No | `0` | 0–30000 | Wait up to this many milliseconds for the job to finish before returning, so a short recording needs only this one call. On timeout the jobId is returned and the job keeps running. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_start",
  "arguments": {
    "path": "downloads/captured-stream.wav",
    "model": "ggml-base",
    "language": "auto"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Started speech transcription job 'job-tx-1092' for captured-stream.wav."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-tx-1092",
    "model": "ggml-base",
    "status": "transcribing",
    "audioDurationSeconds": 24.3
  }
}
```

---

## 4. Operational Best Practices

* **Privacy Guarantees:** 100% on-device processing guarantees confidentiality for internal meetings, voicemails, and private recordings.
* **Asynchronous Processing:** Returns immediately with a `jobId`; use [`nova.media_transcribe_status`](nova-media-transcribe-status.md) to poll for transcribed text segments.

---

## 5. Related Tools

* [`nova.media_transcribe_status`](nova-media-transcribe-status.md)
* [`nova.media_transcribe_stop`](nova-media-transcribe-stop.md)
* [`nova.media_file_info`](nova-media-file-info.md)
