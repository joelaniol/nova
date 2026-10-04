# `nova.ui_open_settings`

> **Opens the settings drawer overlay in the Nova host user interface.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_open_settings` presents the browser settings panel for configuring sandboxes, identity presets, and network proxies.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `section` | `string` | No | — | `general`, `appearance_performance`, `privacy_security`, `site_permissions`, `passwords`, `sandboxes`, `proxies`, `connectors`, `tools`, `ai_agents`, `developer`, `bookmarks`, `about` | Optional top-level settings section to open directly. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_open_settings",
  "arguments": {
    "section": "proxies"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Settings overlay opened at section 'proxies'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "section": "proxies"
  }
}
```
Without `section`, the response is `{ "ok": true }` and no `section` field is returned.

---

## 4. Operational Best Practices

* **Visual Settings:** Guide human operators directly to configuration panels during onboarding.

---

## 5. Related Tools

* [`nova.ui_close_settings`](nova-ui-close-settings.md)
