# `nova.permission_center_set`

> **Sets the global Permission Center defaults for camera, microphone, speaker and location, and the preferred media devices.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.permission_center_set` changes the default handling (`ask`, `allow`, `deny`) that applies when a site requests the camera, microphone, speaker output or location, and sets the preferred camera, microphone and speaker. Only the parameters you pass change. Device ids must come from the latest `nova.permission_center_get` result of the same Nova session; unknown ids are rejected while `validateDeviceIds` is true. Switching camera or microphone to `deny` stops active captures first.

The result contains the full Permission Center state after the change, in the same shape as `nova.permission_center_get`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `cameraPermissionMode` | `string` | No | — | `ask`, `allow`, `deny` | Default camera permission: 'ask' (prompt user), 'allow' (auto-grant), 'deny' (auto-block). |
| `microphonePermissionMode` | `string` | No | — | `ask`, `allow`, `deny` | Default microphone permission: 'ask' (prompt user), 'allow' (auto-grant), 'deny' (auto-block). |
| `speakerPermissionMode` | `string` | No | — | `ask`, `allow`, `deny` | Default speaker/audio-output permission: 'ask' (prompt user), 'allow' (auto-grant), 'deny' (auto-block). |
| `geolocationPermissionMode` | `string` | No | — | `ask`, `allow`, `deny` | Default geolocation permission: 'ask' (prompt user), 'allow' (auto-grant navigator.geolocation for the effective origin via the proactive permission policy), 'deny' (auto-block). |
| `preferredCameraDeviceId` | `string` | No | — | — | Preferred camera device ID — must come from the latest permission_center_get output of this Nova session. Empty string clears. |
| `preferredMicrophoneDeviceId` | `string` | No | — | — | Preferred microphone device ID — must come from the latest permission_center_get output of this Nova session. Empty string clears. |
| `preferredSpeakerDeviceId` | `string` | No | — | — | Preferred speaker device ID — must come from the latest permission_center_get output of this Nova session. Empty string clears. |
| `clearPreferredDevices` | `boolean` | No | `false` | — | If true, clears all preferred device IDs before applying explicit IDs. |
| `validateDeviceIds` | `boolean` | No | `true` | — | If true, reject unknown device IDs based on current OS media inventory plus cached Chromium enumerateDevices IDs. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_permission_center_set",
  "arguments": {
    "cameraPermissionMode": "ask",
    "geolocationPermissionMode": "deny"
  }
}
```

### JSON-RPC Response
Abridged; `permissionCenter` also lists the preferred and default device ids and the detected `cameras`, `microphones` and `speakers`.

```json
{
  "content": [
    {
      "type": "text",
      "text": "Permission center updated: camera=ask, microphone=ask, speaker=ask, geolocation=deny"
    }
  ],
  "structuredContent": {
    "success": true,
    "permissionCenter": {
      "cameraPermissionMode": "ask",
      "microphonePermissionMode": "ask",
      "speakerPermissionMode": "ask",
      "geolocationPermissionMode": "deny",
      "preferredCameraDeviceId": null,
      "preferredMicrophoneDeviceId": null,
      "preferredSpeakerDeviceId": null
    }
  }
}
```

---

## 4. Operational Best Practices

* **Test Isolation:** Avoid permissive global defaults in shared environments; prefer per-origin rules with `nova.media_permission_set`.
* **Fresh device ids:** Call `nova.permission_center_get` in the same session before setting a preferred device.

---

## 5. Related Tools

* [`nova.permission_center_get`](nova-permission-center-get.md)
* [`nova.media_permission_set`](../media-and-transcription/nova-media-permission-set.md)
