# `nova.terminal_settings_set`

Updates terminal appearance settings such as color theme, font size, and program color rules.

---

## 1. Overview

`nova.terminal_settings_set` modifies terminal presentation properties. Changes to theme and font size update open sessions immediately, while `programColors` applies to sessions opened afterwards.

* **Capability Bundle:** `terminal_ops`
* **Security Tier:** Tier 2 (Configuration)
* **Architecture Guide:** [Terminal Workspaces & ConPTY Integration](../../../core-features/terminal-workspaces.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`theme`** | `string` | No | `unchanged` | Terminal theme: `"nova"` or `"dark"`. |
| **`fontSize`** | `string` | No | `unchanged` | Font size: `"small"`, `"medium"`, `"large"`, or `"xlarge"`. |
| **`programColors`** | `string` | No | `unchanged` | Color preference: `"auto"` (program decides) or `"off"` (enforces `NO_COLOR`). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "Terminal settings updated."
    }
  ],
  "structuredContent": {
    "ok": true,
    "theme": "nova",
    "fontSize": "medium",
    "programColors": "auto"
  }
}
```

---

## 4. Operational Best Practices

* **Scope Limitation:** Deliberately does not allow agents to alter `TerminalAgentCanControlDock` or onboarding defaults, maintaining secure least-privilege boundaries.

---

## See Also

* [`nova.terminal_settings_get`](nova-terminal-settings-get.md) - Read terminal settings.
* [Headless Terminal Workspaces Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
