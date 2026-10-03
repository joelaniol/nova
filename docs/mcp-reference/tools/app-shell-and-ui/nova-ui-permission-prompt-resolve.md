# `nova.ui_permission_prompt_resolve`

> **Resolves an active web permission prompt modal (camera, microphone, geolocation, notifications).**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Permission Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_permission_prompt_resolve` programmatically answers an in-page permission prompt, choosing allow, deny, or dismiss.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Metadata. Provide _meta.intent when using decision='allow' or 'deny' - answering a permission request is high-impact. Not needed for 'defer'. |
| `decision` | `string` | No | defer = postpone without deciding (default, always available); allow/deny = answer for the user. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_permission_prompt_resolve",
  "arguments": {
    "action": "grant"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Granted pending permission request."
    }
  ],
  "structuredContent": {
    "ok": true,
    "action": "grant",
    "resolved": true
  }
}
```

---

## 4. Operational Best Practices

* **Automation Flow:** Answer permission prompts immediately to prevent script execution hangs on WebRTC pages.

---

## 5. Related Tools

* [`nova.media_permission_set`](../media-and-transcription/nova-media-permission-set.md)
* [`nova.notifications_permission_set`](../notifications/nova-notifications-permission-set.md)
