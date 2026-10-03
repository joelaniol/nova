# `nova.ui_inspect_native_dialog`

> **Inspects details of the currently active host-owned Win32 native dialog (title, class, control types).**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Native Dialog Inspection)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_inspect_native_dialog` queries Win32 UI Automation to inspect native dialog windows, returning window titles, button text, and file path input fields.

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
      "text": "Active dialog: 'Open File' (Win32 #32770). Buttons: Open, Cancel."
    }
  ],
  "structuredContent": {
    "ok": true,
    "dialogFound": true,
    "title": "Open File",
    "className": "#32770",
    "hasFileNameInput": true,
    "buttons": [
      "Open",
      "Cancel"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Dialog Identification:** Check dialog class and buttons before deciding whether to call `nova.ui_set_native_dialog_file_name` or `nova.ui_dismiss_native_dialog`.

---

## 5. Related Tools

* [`nova.ui_set_native_dialog_file_name`](nova-ui-set-native-dialog-file-name.md)
* [`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)
