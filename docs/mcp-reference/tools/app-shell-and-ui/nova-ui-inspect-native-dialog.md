# `nova.ui_inspect_native_dialog`

> **Inspects details of the currently active host-owned Win32 native dialog (title, class, control types).**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_inspect_native_dialog` reports the Windows dialog Nova currently owns (title, class, kind, whether it is in the foreground) together with what automation found on it: which actions are supported (`confirm`, `cancel`, `set_file_name`), the confirm/cancel buttons, the file-name field, and the full button list. For one of Nova's own prompts (sign-in, certificate, permission, download warning, restore tabs) it also reports the resolver tool that can answer it.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_inspect_native_dialog",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Native file dialog detected. Nova can inspect its buttons and control the standard file-name field."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "nativeDialog": {
      "isOpen": true,
      "kind": "file_picker",
      "title": "Open File",
      "className": "#32770",
      "foreground": true
    },
    "automation": {
      "dialogType": "file_picker",
      "supportsConfirm": true,
      "supportsCancel": true,
      "supportsSetFileName": true,
      "supportedActions": ["confirm", "cancel", "set_file_name"],
      "confirmButton": { "text": "Open", "defaultButton": true },
      "cancelButton": { "text": "Cancel", "defaultButton": false },
      "fileNameField": { "className": "Edit" },
      "buttons": [
        { "text": "Open", "defaultButton": true },
        { "text": "Cancel", "defaultButton": false }
      ]
    },
    "nextActions": [
      { "priority": 105, "tool": "nova.ui_inspect_native_dialog", "reason": "Inspect the detected native dialog and see which automation actions are currently available." },
      { "priority": 100, "tool": "nova.ui_dismiss_native_dialog", "reason": "Dismiss the detected native dialog before continuing browser automation." }
    ]
  }
}
```
Response fields are shortened above (each button/field also carries `controlId`, `role`, `visible`, `enabled`, `windowHandle`, and `bounds`). When no native dialog is open, `ok` is still `true`, with `status: "not_found"` and `nativeDialog: { "isOpen": false }`.

---

## 4. Operational Best Practices

* **Dialog Identification:** Check `automation.supportedActions` before deciding whether to call `nova.ui_set_native_dialog_file_name`, `nova.ui_confirm_native_dialog`, or `nova.ui_dismiss_native_dialog`.

---

## 5. Related Tools

* [`nova.ui_set_native_dialog_file_name`](nova-ui-set-native-dialog-file-name.md)
* [`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)
