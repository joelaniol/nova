# `nova.setup_wizard_open`

> **Opens Nova's guided connection setup wizard dialog in the graphical user interface.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.setup_wizard_open` opens Nova's guided connection setup dialog so a human operator can link an AI client to this Nova instance. If another dialog already has the screen, the call reports that the dialog was not opened instead of silently doing nothing.

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
  "name": "nova_setup_wizard_open",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Connection setup dialog opened."
    }
  ],
  "structuredContent": {
    "ok": true,
    "opened": true
  }
}
```

If another dialog already owns the screen, the response instead looks like:
```json
{
  "structuredContent": {
    "ok": false,
    "opened": false,
    "reasonCode": "dialog_busy",
    "message": "Another dialog is already open; close it and retry."
  }
}
```

---

## 4. Operational Best Practices

* **Operator Guidance:** Call when a human operator needs to connect a new AI client to this Nova instance.

---

## 5. Related Tools

* [`nova.setup_status`](nova-setup-status.md)
* [`nova.ui_open_settings`](nova-ui-open-settings.md)
