# `nova.ui_close_settings`

> **Closes the settings drawer overlay in the Nova host user interface.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_close_settings` dismisses the application configuration panel.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_close_settings",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Settings overlay closed."
    }
  ],
  "structuredContent": {
    "ok": true
  }
}
```

---

## 4. Operational Best Practices

* **Viewport Hygiene:** Keep UI chrome clean when performing automated viewport inspections.

---

## 5. Related Tools

* [`nova.ui_open_settings`](nova-ui-open-settings.md)
