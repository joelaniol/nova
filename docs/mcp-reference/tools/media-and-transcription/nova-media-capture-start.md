# `nova.media_capture_start`

Starts streaming capture of live audio/video playing in a tab (WebAudio, MSE, dynamic blobs).

---

## 1. Overview

`nova.media_capture_start` intercepts and records audio or video playing inside a tab that cannot be downloaded via standard URL fetching (e.g. MSE streams, WebAudio graphs, encrypted media). It captures audio chunks directly and writes them to local disk files.

* **Security Tier:** Tier 2 (Media Stream Capture)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID of the tab playing the media from nova.tabs, or 'active' / 'activeBrowserTab'. |
| `saveDir` | `string` | No | — | — | Absolute directory to write the track files into. Requires 'Allow local files'. Omit to use a MediaCaptures folder inside Nova's Exports folder. |
| `fileName` | `string` | No | — | ≤ 80 characters | Base name for the output files; a track suffix and the container extension are appended. Omit for a timestamped name. |
| `maxBytes` | `integer` | No | — | ≥ 1 | Stop collecting after this many bytes (default 2 GB, ceiling 16 GB). Reaching it does not interrupt playback — the capture simply stops growing and reports limitHit. |
| `reload` | `boolean` | No | `false` | — | Reload the tab after installing the recorder, so a player that already started is captured from the beginning. Restarts playback and can destroy an in-memory session, which is why it is off by default. |
| `source` | `string` | No | `"both"` | `both`, `mse`, `webaudio` | Which playback paths to record. Default both, so you need not know how the page plays its media: mse covers HLS/DASH streaming, webaudio covers decodeAudioData (messenger voice messages). Narrow it only to avoid installing a recorder you know is useless. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_capture_start",
  "arguments": {
    "targetId": "tab-1",
    "source": "audio",
    "fileName": "captured-stream.wav",
    "maxBytes": 10485760
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Started audio capture on tab-1 -> captured-stream.wav."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "captureId": "cap-audio-01",
    "outputFile": "downloads/captured-stream.wav",
    "status": "recording"
  }
}
```

---

## 4. Operational Best Practices

* **MSE & WebAudio Capture:** Ideal for voice messages, web radio, or streaming audio that lacks a static direct download URL.
* **Max Bytes Bound:** Always specify `maxBytes` to prevent unbounded disk usage during long streaming sessions.

---

## 5. Related Tools

* [`nova.media_capture_status`](nova-media-capture-status.md)
* [`nova.media_capture_stop`](nova-media-capture-stop.md)
* [`nova.media_status`](nova-media-status.md)
