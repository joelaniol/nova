# `nova.setup_wizard_open`

> **Opens Nova's guided connection setup wizard dialog in the graphical user interface.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (UI Dialog Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.setup_wizard_open` launches the visual setup dialog to assist human operators in linking external AI developer tools to the Nova browser instance.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.
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
      "text": "Guided connection setup wizard opened."
    }
  ],
  "structuredContent": {
    "ok": true,
    "isOpen": true
  }
}
```

---

## 4. Operational Best Practices

* **Operator Guidance:** Call when onboarding a new workstation or configuring secondary AI tools.

---

## 5. Related Tools

* [`nova.setup_status`](nova-setup-status.md)
* [`nova.ui_open_settings`](nova-ui-open-settings.md)
