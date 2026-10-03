# `nova.input_text`

> **Sends a raw text string into the currently focused DOM element.**

* **Security Tier:** Tier 2 (Keyboard Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_text` emits keyboard character events directly to the focused input field, handling unicode text and emoji sequences.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `text` | `string` | Yes | — | — | Text to type. Maximum 500000 characters; use nova.type_selector for selector-focused typing. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_input_text",
  "arguments": {
    "targetId": "tab-1",
    "text": "Hello, World!"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Typed 13 characters into focused element."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "charactersTyped": 13
  }
}
```

---

## 4. Operational Best Practices

* **Requires Focus:** Ensure target input is focused first (via `nova.click_selector`) or use `nova.type_selector` directly.

---

## 5. Related Tools

* [`nova.type_selector`](nova-type-selector.md)
* [`nova.input_key`](nova-input-key.md)
