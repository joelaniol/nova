# `nova.ui_dismiss_native_dialog`

> **Dismisses or cancels the currently active host-owned Win32 native dialog.**

* **Security Tier:** Tier 2 (Native Dialog Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_dismiss_native_dialog` safely dismisses blocking modal dialogs (Escape/Cancel) to restore automation flow.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
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
