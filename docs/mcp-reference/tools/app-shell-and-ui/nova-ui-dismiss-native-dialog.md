# `nova.ui_dismiss_native_dialog`

> **Dismisses or cancels the currently active host-owned Win32 native dialog.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Native Dialog Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_dismiss_native_dialog` safely dismisses blocking modal dialogs (Escape/Cancel) to restore automation flow.

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
      "text": "Dismissed native host dialog."
    }
  ],
  "structuredContent": {
    "ok": true,
    "dismissed": true
  }
}
```

---

## 4. Operational Best Practices

* **Unblock Automation:** Use as an emergency unblocker when an unexpected file picker or print modal traps tab focus.

---

## 5. Related Tools

* [`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)
* [`nova.ui_get_state`](nova-ui-get-state.md)
