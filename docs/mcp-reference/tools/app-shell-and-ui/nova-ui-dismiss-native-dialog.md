# `nova.ui_dismiss_native_dialog`

> **Dismisses or cancels the currently active host-owned Win32 native dialog.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_dismiss_native_dialog` cancels the Windows dialog Nova currently owns (such as a file open/save or print dialog). If the dialog was a file picker, the response points the agent at `nova.file_upload` for the upload it was likely trying to do instead. If no native dialog was open, the call reports that instead of acting on anything.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_dismiss_native_dialog",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Native dialog dismissed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "dismissed": true,
    "attemptedActions": ["escape_key"],
    "nativeDialogBefore": { "isOpen": true },
    "nativeDialogAfter": { "isOpen": false }
  }
}
```
If dismissing fails, the response instead has `ok: false`, `status: "blocked"`, `reasonCode: "native_dialog.dismiss_failed"`, `retryable: true`, `retryAfterMs: 1500`, and a `recoveryHint`. If no native dialog was open to begin with, the call returns `ok: true` with `status: "not_found"` and `dismissed: false` — it reports nothing happened rather than erroring.

---

## 4. Operational Best Practices

* **Unblock Automation:** Use as an emergency unblocker when an unexpected file picker or print modal traps tab focus.
* **File Pickers:** If the dismissed dialog was a file picker and an upload was intended, use `nova.file_upload` instead of retrying the dialog.

---

## 5. Related Tools

* [`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)
* [`nova.ui_get_state`](nova-ui-get-state.md)
