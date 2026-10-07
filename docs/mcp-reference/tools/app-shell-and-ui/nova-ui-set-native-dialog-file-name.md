# `nova.ui_set_native_dialog_file_name`

> **Fills the file path or name field of an active Win32 native file picker dialog.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_set_native_dialog_file_name` places a file path or file name into the standard file-name field of an open Windows Open/Save file dialog. The response example below is an excerpt; it omits the dialog snapshots (`nativeDialogBefore`, `nativeDialogAfter`, `automation`, `fileNameField`).

If no dialog is open, the call returns `status: "not_found"` with `applied: false`. If the open dialog has no standard file-name field, it returns `ok: false`, `status: "unsupported"` and `reasonCode: "native_dialog.file_name_unsupported"`. `verification` is `matched`, `mismatch`, `unverified` or `send_failed`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `text` | `string` | Yes | — | — | File path or file name text to place into the dialog's standard file-name field. Control characters are removed and extremely long values are rejected. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_set_native_dialog_file_name",
  "arguments": {
    "text": "C:\\Temp\\report.pdf"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Native dialog file-name field updated."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "applied": true,
    "textLength": 18,
    "verification": "matched",
    "verifiedLength": 18
  }
}
```

---

## 4. Operational Best Practices

* **Follow with Confirm:** Immediately call `nova.ui_confirm_native_dialog` after setting the file path to execute the dialog action.
* **Absolute Paths:** Always supply verified, absolute paths.

---

## 5. Related Tools

* [`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)
* [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)
