# `nova.media_status`

Inspects the first `<video>` or `<audio>` element on a page: playback state, position, and why it may have stopped.

---

## 1. Overview

`nova.media_status` reads the first `<video>` or `<audio>` element found on the page (`document.querySelector('video') || document.querySelector('audio')`). It reports play/pause/ended/seeking state, current time and duration, volume, muted state, playback rate, the element's `readyState`/`networkState`, and any `error` the element carries. It also carries page-visibility/focus state and — when Nova's in-page diagnostics script is present — a classified pause reason and a short recent-events trail, which together explain things like "paused because the tab lost focus" rather than just reporting paused. It also has light YouTube-specific detection (`isAd`, `adSkippable`) when a `#movie_player` element is present. There is no distinction between "video" vs "audio" media type in the response, and no buffered time ranges.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "{\"found\":true,\"playing\":true,\"paused\":false,\"ended\":false,\"seeking\":false,\"currentTime\":42.5,\"duration\":180,\"volume\":1,\"muted\":false,\"playbackRate\":1,\"isAd\":null,\"adSkippable\":false,\"readyState\":4,\"networkState\":1,\"error\":null,\"src\":\"https://example.com/video.mp4\",\"title\":\"Example\",\"page\":{\"hidden\":false,\"visibilityState\":\"visible\",\"hasFocus\":true},\"diag\":null}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "media": {
      "found": true,
      "playing": true,
      "paused": false,
      "ended": false,
      "seeking": false,
      "currentTime": 42.5,
      "duration": 180,
      "volume": 1,
      "muted": false,
      "playbackRate": 1,
      "isAd": null,
      "adSkippable": false,
      "readyState": 4,
      "networkState": 1,
      "error": null,
      "src": "https://example.com/video.mp4",
      "title": "Example",
      "page": { "hidden": false, "visibilityState": "visible", "hasFocus": true },
      "diag": null
    }
  }
}
```

When no `<video>` or `<audio>` element exists on the page, `media` is `{ "found": false }`. `diag` is only non-null when Nova's page-side media diagnostics script has run; it then adds `pauseReason` and a short trail of recent focus/visibility/play events.

---

## 4. Operational Best Practices

* **Playback Confirmation:** Verify that in-page media has settled and playback has started (`media.playing`) before capturing streams with [`nova.media_capture_start`](nova-media-capture-start.md).
* **Diagnose Stalled Playback:** When `media.playing` is false, check `media.diag.pauseReason` and `media.page` (hidden/visibilityState/hasFocus) before assuming the page is broken — many sites pause on tab-hide or focus loss.

---

## 5. Related Tools

* [`nova.media_capture_start`](nova-media-capture-start.md)
* [`nova.media_file_info`](nova-media-file-info.md)
