# `nova.ui_permission_prompt_resolve`

> **Resolves an active web permission prompt modal (camera, microphone, geolocation, notifications).**

* **Security Tier:** Tier 2 (Permission Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_permission_prompt_resolve` programmatically answers an in-page permission prompt, choosing allow, deny, or dismiss.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | No | — | `defer`, `allow`, `deny` | defer = postpone without deciding (default, always available); allow/deny = answer for the user. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

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
