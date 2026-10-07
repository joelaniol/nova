# `nova.media_activity_status`

Returns an O(1) instant snapshot of currently active camera, microphone, and screen-sharing streams.

---

## 1. Overview

`nova.media_activity_status` performs a zero-overhead check of active media streams across all browser tabs. It returns the number of origins with at least one live track, the total live track count, and the list of those origins — as an aggregate, not broken down by camera/microphone/screen-share.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_activity_status",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "0 origin(s), 0 live track(s)."
    }
  ],
  "structuredContent": {
    "activeOriginCount": 0,
    "activeTrackCount": 0,
    "origins": [],
    "isAnyActive": false
  }
}
```

---

## 4. Operational Best Practices

* **Privacy Pre-Check:** Query before navigating away from sensitive domains to ensure background tabs are not recording audio or video. Use `isAnyActive` for a quick yes/no check and `origins` to see which sites are involved.

---

## 5. Related Tools

* [`nova.media_stop_all`](nova-media-stop-all.md)
* [`nova.media_activity_audit`](nova-media-activity-audit.md)
