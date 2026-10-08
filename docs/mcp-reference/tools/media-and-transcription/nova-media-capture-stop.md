# `nova.media_capture_stop`

Stops in-tab media capture, flushes pending segments, closes the per-track files, and returns their paths.

---

## 1. Overview

`nova.media_capture_stop` cleanly terminates an active streaming capture started by [`nova.media_capture_start`](nova-media-capture-start.md). It flushes and closes one file per SourceBuffer track (video and audio are not muxed together) and returns each track's file path and byte count. A stream with separate audio/video tracks needs a tool like ffmpeg afterwards to combine them.

* **Core Architecture Guide:** [Media Capture](../../../core-features/media-intelligence/media-capture/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID of the capturing tab, or 'active' / 'activeBrowserTab'. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Captured 1 track(s), 389120 bytes in 24300 ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "stopped": true,
    "targetId": "tab-1",
    "reasonCode": null,
    "saveDir": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Exports\\MediaCaptures",
    "elapsedMs": 24300,
    "bytesWritten": 389120,
    "limitHit": false,
    "droppedBytes": 0,
    "recorderLost": false,
    "trackCount": 1,
    "tracks": [
      { "recorder": "mse", "index": 0, "mime": "audio/webm; codecs=\"opus\"", "filePath": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Exports\\MediaCaptures\\capture-20261003-120000-mse0.webm", "bytesWritten": 389120 }
    ],
    "muxHint": null
  }
}
```

A stop with nothing running returns `{ "ok": false, "stopped": false, "targetId": "tab-1", "reasonCode": "not_capturing" }`. A stop where the recorder was armed but never saw data returns `{ "ok": false, "stopped": true, "reasonCode": "no_media_captured", ... }` — this is also what a DRM-protected stream looks like, since the decrypted bytes never reach the page.

---

## 4. Operational Best Practices

* **Direct Transcription Handoff:** Pass a resulting track's `filePath` to [`nova.media_transcribe_start`](nova-media-transcribe-start.md) for local speech-to-text processing.
* **Combine Separate Tracks:** When `tracks` has more than one entry, `muxHint` names the ffmpeg command to combine them into a single container.

---

## 5. Related Tools

* [`nova.media_capture_start`](nova-media-capture-start.md)
* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
