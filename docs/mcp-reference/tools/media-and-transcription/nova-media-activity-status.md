# `nova.media_activity_status`

Returns an O(1) instant snapshot of currently active camera, microphone, and screen-sharing streams.

---

## 1. Overview

`nova.media_activity_status` performs a zero-overhead check of active media streams across all browser tabs. It returns origin lists and stream counts for camera, microphone, and desktop screen-sharing.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
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
      "text": "No media streams currently active."
    }
  ],
  "structuredContent": {
    "ok": true,
    "activeStreamsCount": 0,
    "origins": []
  }
}
```

---

## 4. Operational Best Practices

* **Privacy Pre-Check:** Query before navigating away from sensitive domains to ensure background tabs are not recording audio or video.

---

## 5. Related Tools

* [`nova.media_stop_all`](nova-media-stop-all.md)
* [`nova.media_activity_audit`](nova-media-activity-audit.md)
