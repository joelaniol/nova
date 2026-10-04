# `nova.permission_center_get`

> **Retrieves the global default permission modes for camera, microphone, speaker, and geolocation, plus the detected hardware devices.**

* **Core Feature Guide:** [Media Intelligence](../../../core-features/media-intelligence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.permission_center_get` reports the browser-wide default permission mode (`ask`/`allow`/`deny`) for camera, microphone, speaker, and geolocation, the preferred/default/communications device ids, and the enumerated camera, microphone, and speaker devices. It does not cover notifications or per-site permission state — those are read with `nova.notifications_permissions_list` and `nova.media_permissions_list`/`nova.media_permission_get`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_permission_center_get",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Permission center loaded. devices(camera/mic/speaker)=1/1/2"
    }
  ],
  "structuredContent": {
    "permissionCenter": {
      "cameraPermissionMode": "ask",
      "microphonePermissionMode": "ask",
      "speakerPermissionMode": "ask",
      "geolocationPermissionMode": "deny",
      "preferredCameraDeviceId": null,
      "preferredMicrophoneDeviceId": null,
      "preferredSpeakerDeviceId": null,
      "defaultCameraDeviceId": "cam-1",
      "defaultMicrophoneDeviceId": "mic-1",
      "defaultSpeakerDeviceId": "spk-1",
      "communicationsMicrophoneDeviceId": "mic-1",
      "communicationsSpeakerDeviceId": "spk-1",
      "cameras": [{ "id": "cam-1", "name": "Integrated Webcam", "isDefault": true, "isDefaultCommunications": false }],
      "microphones": [{ "id": "mic-1", "name": "Microphone Array", "isDefault": true, "isDefaultCommunications": true }],
      "speakers": [
        { "id": "spk-1", "name": "Speakers", "isDefault": true, "isDefaultCommunications": true },
        { "id": "spk-2", "name": "Headphones", "isDefault": false, "isDefaultCommunications": false }
      ],
      "deviceEnumerationError": null
    }
  }
}
```

---

## 4. Operational Best Practices

* **Permission Audit:** Call before workflows requiring media capture to anticipate dialog prompts, and check `deviceEnumerationError` — a non-null value means the device lists above may be incomplete.

---

## 5. Related Tools

* [`nova.permission_center_set`](nova-permission-center-set.md)
* [`nova.media_permissions_list`](../media-and-transcription/nova-media-permissions-list.md)
