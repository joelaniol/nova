# `nova.media_file_info`

Inspects media container metadata, duration, channels, and codecs from a local file without ffmpeg.

---

## 1. Overview

`nova.media_file_info` reads audio and video container headers directly in C#. It extracts duration, bitrate, sample rate, audio channels, and video dimensions without spawning external CLI tools.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only File Probe)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`path`** | `string` | Yes | `null` | Absolute path of the media file to inspect. |

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
      "text": "Probe recording.wav: audio/wav, duration 14.2s, 16000Hz mono."
    }
  ],
  "structuredContent": {
    "ok": true,
    "format": "wav",
    "durationSeconds": 14.2,
    "sampleRate": 16000,
    "channels": 1,
    "sizeBytes": 454400
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Transcription Validation:** Verify sample rates and audio durations before passing files to [`nova.media_transcribe_start`](nova-media-transcribe-start.md).
* **Zero External Dependencies:** Built-in container parsers handle WAV, MP3, AAC, and OGG formats.

---

## 5. Related Tools

* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
