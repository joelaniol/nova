# `nova.media_device_preferences_list`

Lists stored per-site preferred device IDs (camera, microphone, speaker).

---

## 1. Overview

`nova.media_device_preferences_list` inspects stored audio/video hardware device mappings configured for specific websites.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`origin`** | `string` | No | `null` | Optional filter — only return preferences for this origin. |

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
      "text": "Loaded device preferences for https://meet.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "origin": "https://meet.example.com",
    "preferences": {
      "preferredMicrophoneId": "mic-usb-01",
      "preferredCameraId": "cam-hd-01"
    }
  }
}
```

---

## 4. Operational Best Practices

* **Hardware Drift Diagnostics:** Identify when a preferred USB headset or webcam was unplugged or reassigned a new OS device GUID.

---

## 5. Related Tools

* [`nova.media_permissions_list`](nova-media-permissions-list.md)
