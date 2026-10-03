# `nova.ui_confirm_native_dialog`

> **Triggers the primary affirmative action on the currently active host-owned Win32 native dialog.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Native Dialog Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_confirm_native_dialog` sends affirmative input (Enter/OK) to an active OS dialog, such as a file save confirmation or print prompt.

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
      "text": "Confirmed native host dialog."
    }
  ],
  "structuredContent": {
    "ok": true,
    "confirmed": true
  }
}
```

---

## 4. Operational Best Practices

* **Pre-check State:** Always call `nova.ui_get_state` or `nova.ui_inspect_native_dialog` first to ensure the target dialog is active and focused.

---

## 5. Related Tools

* [`nova.ui_dismiss_native_dialog`](nova-ui-dismiss-native-dialog.md)
* [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)
