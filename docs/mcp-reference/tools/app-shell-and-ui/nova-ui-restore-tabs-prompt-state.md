# `nova.ui_restore_tabs_prompt_state`

> **Inspects whether a startup tab restoration prompt is active and previews saved session tabs.**

* **Security Tier:** Tier 1 (Read-Only Recovery State)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_restore_tabs_prompt_state` checks if Nova booted in a crashed state with tabs awaiting user restoration decisions.

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
  "name": "nova_ui_restore_tabs_prompt_state",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Tab restore prompt active: 4 tabs available for restore."
    }
  ],
  "structuredContent": {
    "ok": true,
    "isPromptActive": true,
    "tabs": [
      {
        "title": "Dashboard",
        "url": "https://app.example.com"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Startup Check:** Run during initialization to handle unexpected crash recoveries cleanly.

---

## 5. Related Tools

* [`nova.ui_restore_tabs_prompt_resolve`](nova-ui-restore-tabs-prompt-resolve.md)
