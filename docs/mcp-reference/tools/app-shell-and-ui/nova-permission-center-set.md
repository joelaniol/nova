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
<!-- /generated:parameters -->

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
