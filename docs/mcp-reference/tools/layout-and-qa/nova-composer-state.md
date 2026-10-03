# `nova.composer_state`

> **Inspects visual state, selection range, and placeholder text of rich text composers.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Inspection)
* **Core Feature Guide:** [Visual Evidence & Layout QA](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.composer_state` inspects complex contenteditable editors (Draft.js, Slate, ProseMirror, Lexical) to determine cursor position, character length, and active formatting tags.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `frameId` | `string` | No | Optional same-origin frame ID from nova.perceive(deep=true).structuredContent.frames[]. |
| `selector` | `string` | No | Optional CSS selector for the composer input. Omit to let Nova resolve the composer (cache, then heuristics). |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_composer_state",
  "arguments": {
    "targetId": "tab-1",
    "selector": ".ProseMirror"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Composer state: 240 chars, cursor at end, placeholder hidden."
    }
  ],
  "structuredContent": {
    "ok": true,
    "selector": ".ProseMirror",
    "textLength": 240,
    "hasFocus": true,
    "activeTags": [
      "strong"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Rich Text Writing:** Check composer state before and after typing in modern collaborative editors.

---

## 5. Related Tools

* [`nova.type_selector`](../browser-automation/nova-type-selector.md)
* [`nova.measure_elements`](nova-measure-elements.md)
