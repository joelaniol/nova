# `nova.permission_center_get`

> **Retrieves global Permission Center default policies and detected hardware media devices.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Permissions)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.permission_center_get` reports default browser-wide rules for camera, microphone, geolocation, and notifications, plus connected physical audio/video devices.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |

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
      "text": "Global policies: Camera=Prompt, Mic=Prompt, Geolocation=Deny."
    }
  ],
  "structuredContent": {
    "ok": true,
    "defaults": {
      "camera": "Prompt",
      "microphone": "Prompt",
      "geolocation": "Deny",
      "notifications": "Prompt"
    },
    "devicesCount": 3
  }
}
```

---

## 4. Operational Best Practices

* **Permission Audit:** Call before workflows requiring media capture to anticipate dialog prompts.

---

## 5. Related Tools

* [`nova.permission_center_set`](nova-permission-center-set.md)
* [`nova.media_permissions_list`](../media-and-transcription/nova-media-permissions-list.md)
