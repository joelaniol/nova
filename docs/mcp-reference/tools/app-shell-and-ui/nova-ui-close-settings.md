# `nova.ui_close_settings`

> **Closes the settings drawer overlay in the Nova host user interface.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (UI Window Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_close_settings` dismisses the application configuration panel.

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
    "ok": true,
    "isOpen": false
  }
}
```

---

## 4. Operational Best Practices

* **Viewport Hygiene:** Keep UI chrome clean when performing automated viewport inspections.

---

## 5. Related Tools

* [`nova.ui_open_settings`](nova-ui-open-settings.md)
