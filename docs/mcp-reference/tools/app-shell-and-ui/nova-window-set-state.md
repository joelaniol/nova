# `nova.window_set_state`

> **Sets host application window state: minimize, maximize, restore, or bring to foreground.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Window State Control)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.window_set_state` controls the OS window display state, allowing automated agents to maximize the browser, minimize it, or focus it.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `state` | `string` | **Yes** | Target state. 'minimize' uses normal OS minimize. 'foreground' restores if needed and brings the window to front. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_window_set_state",
  "arguments": {
    "state": "maximized"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Set Nova window state to maximized."
    }
  ],
  "structuredContent": {
    "ok": true,
    "state": "maximized"
  }
}
```

---

## 4. Operational Best Practices

* **Bring to Foreground:** Use `state: "foreground"` when handing control over to human operators.
* **Maximized Workflows:** Ensure window is maximized during responsive layout testing.

---

## 5. Related Tools

* [`nova.window_get_bounds`](nova-window-get-bounds.md)
* [`nova.window_set_size`](nova-window-set-size.md)
