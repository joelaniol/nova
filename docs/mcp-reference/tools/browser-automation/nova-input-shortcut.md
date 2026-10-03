# `nova.input_shortcut`

> **Dispatches a multi-key keyboard shortcut (e.g. Ctrl+A, Control+C, Shift+Enter) to the active element.**

* **Security Tier:** Tier 2 (Keyboard Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_shortcut` fires keydown and keyup events in strict modifier order, allowing agents to execute common productivity combinations.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `combo` | `string` | Yes | — | — | Keyboard shortcut string, e.g. 'Ctrl+L', 'Ctrl+Shift+K', 'Alt+Left', 'Ctrl++' or 'Ctrl+Plus'. Modifier names: Ctrl, Shift, Alt, Meta. Exactly one non-modifier key is required. Key aliases include Plus/Equal, Minus, and Digit0-Digit9. Case-insensitive. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_shortcut",
  "arguments": {
    "targetId": "tab-1",
    "shortcut": "Control+A"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Dispatched shortcut Control+A."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "shortcut": "Control+A"
  }
}
```

---

## 4. Operational Best Practices

* **Select All & Replace:** Pair `Control+A` with `nova.input_key` (`Backspace`) for clean input clearing.
* **Rich Text Formatting:** Trigger bold/italic shortcuts in WYSIWYG editors (`Control+B`).

---

## 5. Related Tools

* [`nova.input_key`](nova-input-key.md)
* [`nova.type_selector`](nova-type-selector.md)
