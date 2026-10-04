# `nova.ui_open_downloads`

> **Opens the download manager drawer panel in the Nova host user interface.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_open_downloads` slides out the download tray for operator inspection of active and past file transfers.

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
  "name": "nova_ui_open_downloads",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Download manager opened."
    }
  ],
  "structuredContent": {
    "ok": true
  }
}
```

---

## 4. Operational Best Practices

* **Operator Feedback:** Reveal downloads panel when handing off completed exports to the user.

---

## 5. Related Tools

* [`nova.ui_close_downloads`](nova-ui-close-downloads.md)
* [`nova.downloads_list`](../downloads/nova-downloads-list.md)
