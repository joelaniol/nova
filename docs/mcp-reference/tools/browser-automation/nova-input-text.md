# `nova.input_text`

> **Sends a raw text string into the currently focused DOM element.**

* **Core Feature Guide:** [Input Dispatch](../../../core-features/browser-interaction/input-dispatch/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.input_text` inserts the given text into the currently focused element in a single step via `Input.insertText` — **not** key by key, and with no per-keystroke delay. Because it is one atomic insert, it handles unicode and emoji sequences without needing to simulate individual keystrokes for them. If the text is empty, Nova skips the dispatch entirely (`actionDispatched: false`) instead of sending a no-op insert.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `text` | `string` | Yes | — | — | Text to type. Maximum 500000 characters; use nova.type_selector for selector-focused typing. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Typed 13 chars."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "chars": 13,
    "actionDispatched": true
  }
}
```

There is no top-level `ok` field and no `charactersTyped` — the character count is reported as `chars`.

---

## 4. Operational Best Practices

* **Requires Focus:** Ensure target input is focused first (via `nova.click_selector`) or use `nova.type_selector` directly.

---

## 5. Related Tools

* [`nova.type_selector`](nova-type-selector.md)
* [`nova.input_key`](nova-input-key.md)
