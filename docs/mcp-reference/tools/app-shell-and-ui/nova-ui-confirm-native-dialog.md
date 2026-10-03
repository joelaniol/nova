# `nova.ui_confirm_native_dialog`

> **Triggers the primary affirmative action on the currently active host-owned Win32 native dialog.**

* **Security Tier:** Tier 2 (Native Dialog Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_confirm_native_dialog` sends affirmative input (Enter/OK) to an active OS dialog, such as a file save confirmation or print prompt.

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
