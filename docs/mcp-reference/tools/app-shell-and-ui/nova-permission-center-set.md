# `nova.permission_center_set`

> **Configures global Permission Center default policies and preferred media hardware devices.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Permission Administration)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.permission_center_set` updates default handling (Allow, Prompt, Block) for browser capability requests and assigns default audio/video capture hardware.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `cameraPermissionMode` | `string` | No | Default camera permission: 'ask' (prompt user), 'allow' (auto-grant), 'deny' (auto-block). |
| `clearPreferredDevices` | `boolean` | No | If true, clears all preferred device IDs before applying explicit IDs. |
| `geolocationPermissionMode` | `string` | No | Default geolocation permission: 'ask' (prompt user), 'allow' (auto-grant navigator.geolocation for the effective origin via the proactive permission policy), 'deny' (auto-block). |
| `microphonePermissionMode` | `string` | No | Default microphone permission: 'ask' (prompt user), 'allow' (auto-grant), 'deny' (auto-block). |
| `preferredCameraDeviceId` | `string` | No | Preferred camera device ID — must come from the latest permission_center_get output of this Nova session. Empty string clears. |
| `preferredMicrophoneDeviceId` | `string` | No | Preferred microphone device ID — must come from the latest permission_center_get output of this Nova session. Empty string clears. |
| `preferredSpeakerDeviceId` | `string` | No | Preferred speaker device ID — must come from the latest permission_center_get output of this Nova session. Empty string clears. |
| `speakerPermissionMode` | `string` | No | Default speaker/audio-output permission: 'ask' (prompt user), 'allow' (auto-grant), 'deny' (auto-block). |
| `validateDeviceIds` | `boolean` | No | If true, reject unknown device IDs based on current OS media inventory plus cached Chromium enumerateDevices IDs. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_permission_center_set",
  "arguments": {
    "cameraDefault": "Allow",
    "preferredCameraId": "dev-cam-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Updated Permission Center defaults."
    }
  ],
  "structuredContent": {
    "ok": true,
    "cameraDefault": "Allow",
    "preferredCameraId": "dev-cam-01"
  }
}
```

---

## 4. Operational Best Practices

* **Test Isolation:** Avoid setting permissive defaults in shared environments; prefer per-origin rules with `nova.media_permission_set`.

---

## 5. Related Tools

* [`nova.permission_center_get`](nova-permission-center-get.md)
* [`nova.media_permission_set`](../media-and-transcription/nova-media-permission-set.md)
