# `nova.media_status`

Inspects playback status, current timestamp, duration, and volume of in-page audio/video elements.

---

## 1. Overview

`nova.media_status` inspects HTML5 `<video>` and `<audio>` elements on the active page. It reports whether media is playing, buffered time ranges, current playback position, total duration, volume, and muted state.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_status",
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
      "text": "Primary video: playing at 42.5s / 180.0s (volume 1.0)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "hasMedia": true,
    "mediaType": "video",
    "isPlaying": true,
    "currentTimeSeconds": 42.5,
    "durationSeconds": 180,
    "volume": 1,
    "isMuted": false
  }
}
```

---

## 4. Operational Best Practices

* **Playback Confirmation:** Verify that in-page media has settled and playback has started before capturing streams with [`nova.media_capture_start`](nova-media-capture-start.md).

---

## 5. Related Tools

* [`nova.media_capture_start`](nova-media-capture-start.md)
* [`nova.media_file_info`](nova-media-file-info.md)
