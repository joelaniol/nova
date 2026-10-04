# `nova.ui_get_state`

> **Inspects host application UI state: active tab, overlay visibility, responsiveness, and open dialogs.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_get_state` reports the active tab, whether the settings and downloads overlays are open, and whether a native Windows dialog currently has focus. When a native dialog is open, the settings/downloads state is reported as unknown rather than guessed, and `uiThreadResponsive` is `false` because the UI thread is blocked by the dialog.

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
      "text": "ActiveTab=tab-1 SettingsOpen=False DownloadsOpen=False"
    }
  ],
  "structuredContent": {
    "activeTargetId": "tab-1",
    "settingsOpen": false,
    "downloadsOpen": false,
    "uiThreadResponsive": true,
    "nativeDialog": { "isOpen": false }
  }
}
```
While a native dialog has focus, the response looks like:
```json
{
  "structuredContent": {
    "activeTargetId": "tab-1",
    "settingsOpen": null,
    "downloadsOpen": null,
    "uiThreadResponsive": false,
    "nativeDialog": { "isOpen": true }
  }
}
```

---

## 4. Operational Best Practices

* **Pre-flight Gate:** Call when automation commands time out unexpectedly to detect unhandled modal dialogs (`uiThreadResponsive: false`).

---

## 5. Related Tools

* [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)
* [`nova.app_info`](nova-app-info.md)
