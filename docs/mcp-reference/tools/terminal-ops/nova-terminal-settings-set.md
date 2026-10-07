# `nova.terminal_settings_set`

Updates terminal appearance settings such as color theme, font size, and program color rules.

---

## 1. Overview

`nova.terminal_settings_set` modifies terminal presentation properties. Changes to theme and font size update open sessions immediately, while `programColors` applies to sessions opened afterwards.

* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `theme` | `string` | No | — | `nova`, `dark` | Terminal colour scheme. |
| `fontSize` | `string` | No | — | `small`, `medium`, `large`, `xlarge` | Terminal font size. |
| `programColors` | `string` | No | — | `auto`, `off` | 'auto' states no preference and lets the program decide; 'off' sets the NO_COLOR standard for every shell Nova starts. There is deliberately no 'always on' - that would mean FORCE_COLOR, which also writes escape sequences into files and pipes the user redirects to. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.terminal_settings_set",
  "arguments": {
    "theme": "nova",
    "fontSize": "medium",
    "programColors": "auto"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Terminal settings updated: theme, fontSize, programColors."
    }
  ],
  "structuredContent": {
    "ok": true,
    "changed": ["theme", "fontSize", "programColors"],
    "theme": "nova",
    "fontSize": "medium",
    "programColors": "auto",
    "previousTheme": "dark",
    "previousFontSize": "small",
    "previousProgramColors": "off",
    "colorsEnabled": true,
    "colorsReasonCode": "program_decides",
    "themeAndFontAppliedToOpenSessions": true,
    "programColorsAppliesToNewSessionsOnly": true,
    "schemaVersion": "1"
  }
}
```

If every given value already matched, `changed` comes back empty and the text reads "Terminal settings already had these values; nothing changed."

---

## 4. Operational Best Practices

* **Scope Limitation:** Deliberately does not allow agents to switch on or off agent control of the terminal dock, or change the onboarding default, keeping those decisions with the user.

---

## See Also

* [`nova.terminal_settings_get`](nova-terminal-settings-get.md) - Read terminal settings.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
