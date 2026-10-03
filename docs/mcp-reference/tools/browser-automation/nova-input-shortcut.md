# `nova.input_shortcut`

> **Dispatches a multi-key keyboard shortcut (e.g. Ctrl+A, Control+C, Shift+Enter) to the active element.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Keyboard Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_shortcut` fires keydown and keyup events in strict modifier order, allowing agents to execute common productivity combinations.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `combo` | `string` | **Yes** | Keyboard shortcut string, e.g. 'Ctrl+L', 'Ctrl+Shift+K', 'Alt+Left', 'Ctrl++' or 'Ctrl+Plus'. Modifier names: Ctrl, Shift, Alt, Meta. Exactly one non-modifier key is required. Key aliases include Plus/Equal, Minus, and Digit0-Digit9. Case-insensitive. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

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
