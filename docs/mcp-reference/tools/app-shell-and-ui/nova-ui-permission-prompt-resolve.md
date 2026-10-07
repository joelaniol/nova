# `nova.ui_permission_prompt_resolve`

> **Defers or answers the permission dialog that Nova is showing for a site (for example location, notifications, clipboard read or advanced device access).**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

While Nova shows a site permission dialog, other tool calls are blocked. `nova.ui_permission_prompt_resolve` resolves the topmost such dialog. `defer` (the default) grants and refuses nothing: the page is told the request is undecided, the same dialog does not reappear for about five minutes, and the user still decides later. `allow` and `deny` answer for the user and are a real decision about a site capability; Nova's usual confirmation policy applies, and `_meta.intent` may be required.

Some dialogs, such as the camera and microphone prompt, can only be answered by the user; the call then returns `ok: false` with `reasonCode: "permission_prompt.user_only"`. If no permission dialog is open, the result is `ok: true` with `status: "noop"` (`permission_prompt.not_open`). A dialog that does not accept the requested decision returns `permission_prompt.decision_not_supported`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | No | — | `defer`, `allow`, `deny` | defer = postpone without deciding (default, always available); allow/deny = answer for the user. |

**`_meta.intent` is required for certain arguments.** Passing a short reason in `_meta.intent` is always safe; a rejected call names the argument that made it required.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_permission_prompt_resolve",
  "arguments": {
    "decision": "defer"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Permission question deferred. Nothing was granted or refused; the page was told the request is undecided, the same dialog will not reappear for a few minutes, and the user still decides it."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "message": "Permission question deferred. Nothing was granted or refused; the page was told the request is undecided, the same dialog will not reappear for a few minutes, and the user still decides it.",
    "decision": "defer",
    "decided": false,
    "deferMinutes": 5
  }
}
```

---

## 4. Operational Best Practices

* **Defer by default:** Use `defer` to keep working when the permission is not needed for the task; `decided: false` means nothing was answered.
* **Answer only with a reason:** Use `allow` or `deny` only when the task needs that decision, and say why in `_meta.intent`.

---

## 5. Related Tools

* [`nova.media_permission_set`](../media-and-transcription/nova-media-permission-set.md)
* [`nova.notifications_permission_set`](../notifications/nova-notifications-permission-set.md)
