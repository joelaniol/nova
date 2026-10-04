# `nova.media_device_preferences_list`

Lists stored per-site preferred device IDs (camera, microphone, speaker).

---

## 1. Overview

`nova.media_device_preferences_list` inspects stored audio/video hardware device mappings configured for specific websites.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `origin` | `string` | No | — | — | Optional filter — only return preferences for this origin. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_device_preferences_list",
  "arguments": {
    "origin": "https://meet.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 stored device preference(s)."
    }
  ],
  "structuredContent": {
    "preferences": [
      {
        "origin": "https://meet.example.com",
        "cameraDeviceId": "cam-hd-01",
        "microphoneDeviceId": "mic-usb-01",
        "speakerDeviceId": null,
        "updatedUtc": "2026-10-02T19:00:00Z"
      }
    ],
    "count": 1,
    "originFilter": "https://meet.example.com",
    "note": "Status (missing/available/stale) requires correlating storedDeviceId with current hardware - out of scope for this read tool. Use the Settings UI device list or media_activity_status for current devices."
  }
}
```

---

## 4. Operational Best Practices

* **Hardware Drift Diagnostics:** This tool returns the raw stored device IDs only — it does not itself detect whether a device is missing, available, or reassigned. Correlate the returned IDs against current hardware (e.g. the Settings device list) to spot drift.

---

## 5. Related Tools

* [`nova.media_permissions_list`](nova-media-permissions-list.md)
