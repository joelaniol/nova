# `nova.terminal_settings_get`

Reads terminal appearance settings and reports why ANSI colour output is enabled or disabled.

---

## 1. Overview

`nova.terminal_settings_get` retrieves terminal UI styling (theme, font size, color preference) and diagnoses the exact reason behind color availability (`colorsReasonCode`).

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
    "colorsReasonCode": "program_decides",
    "autoInstallOnboarding": true,
    "agentCanControlDock": true,
    "themeValues": ["nova", "dark"],
    "fontSizeValues": ["small", "medium", "large", "xlarge"],
    "programColorsValues": ["auto", "off"],
    "schemaVersion": "1"
  }
}
```

---

## 4. Operational Best Practices

* **Color Diagnostics:** If CLI commands output plain monochrome text, check `colorsReasonCode`. Values include `"off_by_terminal_setting"`, `"off_by_user_environment"` (`NO_COLOR`), and `"program_decides"`.
* **Discover Allowed Values:** `themeValues`, `fontSizeValues`, and `programColorsValues` list every value `nova.terminal_settings_set` accepts for the matching field, so an agent does not need to guess or hard-code them.

---

## See Also

* [`nova.terminal_settings_set`](nova-terminal-settings-set.md) - Configure appearance settings.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
