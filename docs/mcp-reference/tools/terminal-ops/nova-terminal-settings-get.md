# `nova.terminal_settings_get`

Reads terminal appearance settings and reports why ANSI colour output is enabled or disabled.

---

## 1. Overview

`nova.terminal_settings_get` retrieves terminal UI styling (theme, font size, color preference) and diagnoses the exact reason behind color availability (`colorsReasonCode`).

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 1 (Safe)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_settings_get",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Terminal settings: theme=nova, fontSize=medium, programColors=auto (colours available: program decides)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "theme": "nova",
    "fontSize": "medium",
    "programColors": "auto",
    "colorsEnabled": true,
    "colorsReasonCode": "program_decides"
  }
}
```

---

## 4. Operational Best Practices

* **Color Diagnostics:** If CLI commands output plain monochrome text, check `colorsReasonCode`. Values include `"off_by_terminal_setting"`, `"off_by_user_environment"` (`NO_COLOR`), and `"program_decides"`.

---

## See Also

* [`nova.terminal_settings_set`](nova-terminal-settings-set.md) - Configure appearance settings.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
