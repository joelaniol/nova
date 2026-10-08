# `nova.media_file_info`

Identifies a local media file's container and duration from its header, without decoding it.

---

## 1. Overview

`nova.media_file_info` identifies a file's container from its leading bytes (not its file name) and reads its stated duration where the container provides one, without spawning external tools such as ffprobe. It does not extract bitrate, sample rate, channel count, or video dimensions. It also reports whether the container is one [`nova.media_transcribe_start`](nova-media-transcribe-start.md) accepts.

* **Core Architecture Guide:** [Speech Transcription](../../../core-features/media-intelligence/transcription/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path of the media file to inspect. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_file_info",
  "arguments": {
    "path": "downloads/recording.wav"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "wav, 454,400 bytes, 14.200 s (read from the file). Transcription accepts this container."
    }
  ],
  "structuredContent": {
    "ok": true,
    "path": "downloads/recording.wav",
    "sizeBytes": 454400,
    "container": "wav",
    "durationSeconds": 14.2,
    "durationMeasured": true,
    "transcriptionSupported": true,
    "reasonCode": null,
    "message": null
  }
}
```

Recognized containers are `wav`, `ogg`, `mp4` (also covers M4A/MOV), `mp3`, and `matroska` (also covers WebM); anything else comes back as `container: "unknown"` with `durationSeconds: null`. `durationMeasured: false` marks a duration derived from file size rather than read from the header (e.g. a variable-bitrate MP3 without a Xing/VBRI tag).

---

## 4. Operational Best Practices

* **Pre-Transcription Validation:** Check `transcriptionSupported` and `durationSeconds` before passing a file to [`nova.media_transcribe_start`](nova-media-transcribe-start.md).
* **Zero External Dependencies:** Built-in container parsers handle WAV, Ogg, MP4/M4A/MOV, MP3, and Matroska/WebM without spawning ffprobe or any other external tool.

---

## 5. Related Tools

* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
