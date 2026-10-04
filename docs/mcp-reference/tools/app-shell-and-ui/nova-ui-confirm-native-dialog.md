# `nova.ui_confirm_native_dialog`

> **Triggers the primary affirmative action on the currently active host-owned Win32 native dialog.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_confirm_native_dialog` presses the confirm button (e.g. "Open" or "Save") on the Windows dialog Nova currently owns (such as a file open/save dialog), falling back to sending Enter if no confirm button is found through UI Automation. If no such dialog is open, the call reports that instead of acting on anything.

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
  "name": "nova_ui_confirm_native_dialog",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Native dialog confirm action dispatched and the dialog closed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "confirmed": true,
    "dialogStillOpen": false,
    "attemptedActions": ["foreground", "button_click"],
    "nativeDialogBefore": { "isOpen": true },
    "nativeDialogAfter": { "isOpen": false },
    "clickedButton": { "name": "Open" }
  }
}
```
`nativeDialogBefore`/`nativeDialogAfter` carry the same dialog snapshot shape as `nova.ui_inspect_native_dialog` (shown shortened above). If the click or the Enter-key fallback could not be dispatched, `ok` is `false`, `status` is `"apply_failed"`, and `reasonCode` is `"native_dialog.confirm_failed"`. If no native dialog was open to begin with, the call still returns `ok: true` with `status: "not_found"` and `confirmed: false` — it reports nothing happened rather than erroring.

---

## 4. Operational Best Practices

* **Pre-check State:** Call `nova.ui_inspect_native_dialog` first to confirm a dialog is actually open and see which button it will press.

---

## 5. Related Tools

* [`nova.ui_dismiss_native_dialog`](nova-ui-dismiss-native-dialog.md)
* [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)
