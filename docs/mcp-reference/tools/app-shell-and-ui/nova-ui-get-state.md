# `nova.ui_get_state`

> **Inspects host application UI state: active tab, overlay visibility, responsiveness, and open dialogs.**

* **Security Tier:** Tier 1 (Read-Only UI State)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_get_state` provides a consolidated view of Nova's visual state. Crucial for detecting whether a native file picker or modal dialog is currently trapping input.

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
  "name": "nova_ui_get_state",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "UI State: Active tab tab-1. Native dialog open: False. Overlays: None."
    }
  ],
  "structuredContent": {
    "ok": true,
    "activeTabId": "tab-1",
    "hasNativeDialog": false,
    "isResponsive": true,
    "openOverlays": []
  }
}
```

---

## 4. Operational Best Practices

* **Pre-flight Gate:** Call when automation commands time out unexpectedly to detect unhandled modal dialogs.

---

## 5. Related Tools

* [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)
* [`nova.app_info`](nova-app-info.md)
