# `nova.ui_open_settings`

> **Opens the settings drawer overlay in the Nova host user interface.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (UI Window Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_open_settings` presents the browser settings panel for configuring sandboxes, identity presets, and network proxies.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `section` | `string` | No | Optional top-level settings section to open directly. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_open_settings",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Settings overlay opened."
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

* **Visual Settings:** Guide human operators directly to configuration panels during onboarding.

---

## 5. Related Tools

* [`nova.ui_close_settings`](nova-ui-close-settings.md)
