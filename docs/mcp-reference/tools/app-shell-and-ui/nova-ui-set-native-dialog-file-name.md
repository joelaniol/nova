# `nova.ui_set_native_dialog_file_name`

> **Fills the file path or name field of an active Win32 native file picker dialog.**

* **Security Tier:** Tier 2 (Native Dialog Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_set_native_dialog_file_name` types a target file path directly into the OS Open/Save file dialog input field.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `text` | `string` | Yes | — | — | File path or file name text to place into the dialog's standard file-name field. Control characters are removed and extremely long values are rejected. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_set_native_dialog_file_name",
  "arguments": {
    "fileName": "E:\\Reports\\Q4_Summary.pdf"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Filled file name in native dialog: E:\\Reports\\Q4_Summary.pdf."
    }
  ],
  "structuredContent": {
    "ok": true,
    "fileName": "E:\\Reports\\Q4_Summary.pdf",
    "fieldFound": true
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
