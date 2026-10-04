# `nova.input_shortcut`

> **Dispatches a multi-key keyboard shortcut (e.g. Ctrl+A, Control+C, Shift+Enter) to the active element.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_shortcut` sends one key down and one key up event for a combination such as `Ctrl+A`, with the modifiers held, allowing agents to execute common productivity combinations. Modifier names are `Ctrl`, `Shift`, `Alt` and `Meta`; exactly one non-modifier key is required. The response example below is an excerpt; Nova adds page and contract fields such as `pageUrl`, `pageTitle` and `stage`. `modifiers` is a bit mask (Alt=1, Ctrl=2, Meta=4, Shift=8).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `combo` | `string` | Yes | — | — | Keyboard shortcut string, e.g. 'Ctrl+L', 'Ctrl+Shift+K', 'Alt+Left', 'Ctrl++' or 'Ctrl+Plus'. Modifier names: Ctrl, Shift, Alt, Meta. Exactly one non-modifier key is required. Key aliases include Plus/Equal, Minus, and Digit0-Digit9. Case-insensitive. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_shortcut",
  "arguments": {
    "targetId": "tab-1",
    "combo": "Ctrl+A"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Shortcut sent: Ctrl+A"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "combo": "Ctrl+A",
    "key": "a",
    "code": "KeyA",
    "windowsVirtualKeyCode": 65,
    "modifiers": 2,
    "ctrl": true,
    "alt": false,
    "shift": false,
    "meta": false,
    "actionDispatched": true
  }
}
```

---

## 4. Operational Best Practices

* **Select All & Replace:** Pair `Ctrl+A` with `nova.input_key` (`Backspace`) for clean input clearing.
* **Rich Text Formatting:** Trigger bold/italic shortcuts in WYSIWYG editors (`Ctrl+B`).

---

## 5. Related Tools

* [`nova.input_key`](nova-input-key.md)
* [`nova.type_selector`](nova-type-selector.md)
