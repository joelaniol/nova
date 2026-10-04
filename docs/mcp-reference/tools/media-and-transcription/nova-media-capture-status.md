# `nova.media_capture_status`

Reports progress, elapsed time, and bytes written for an active in-tab media capture.

---

## 1. Overview

`nova.media_capture_status` monitors an ongoing streaming capture started by [`nova.media_capture_start`](nova-media-capture-start.md), reporting elapsed time, total bytes written, how many tracks are open, and whether the byte cap was hit or the page's recorder was lost (e.g. after a navigation).

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID of the capturing tab, or 'active' / 'activeBrowserTab'. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_capture_status",
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
      "text": "Capturing 1 track(s), 245760 bytes written after 15200 ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "capturing": true,
    "targetId": "tab-1",
    "saveDir": "C:\\Users\\<user>\\AppData\\Local\\NovaBrowser\\Exports\\MediaCaptures",
    "elapsedMs": 15200,
    "bytesWritten": 245760,
    "trackCount": 1,
    "maxBytes": 2147483648,
    "limitHit": false,
    "droppedBytes": 0,
    "recorderLost": false,
    "tracks": [
      { "recorder": "mse", "index": 0, "mime": "video/webm; codecs=\"vp9\"", "filePath": "C:\\Users\\<user>\\AppData\\Local\\NovaBrowser\\Exports\\MediaCaptures\\capture-20261003-120000-mse0.webm", "bytesWritten": 245760 }
    ]
  }
}
```

When no capture is running on `targetId`, the response is `{ "ok": false, "capturing": false, "targetId": "tab-1", "reasonCode": "not_capturing" }`.

---

## 4. Operational Best Practices

* **Paced Polling:** Poll periodically to verify that audio chunks are actively arriving from the page.

---

## 5. Related Tools

* [`nova.media_capture_start`](nova-media-capture-start.md)
* [`nova.media_capture_stop`](nova-media-capture-stop.md)
