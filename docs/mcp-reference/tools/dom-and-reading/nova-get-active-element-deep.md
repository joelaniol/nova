# `nova.get_active_element_deep`

> **Traverses through nested Shadow DOM boundaries to find the truly focused interactive element.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Inspection)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_active_element_deep` pierces open Shadow DOM trees to discover the actual innermost focused element instead of just reporting the top-level host custom element.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_get_active_element_deep",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deep focused element: input#search-field inside <app-header> shadow root."
    }
  ],
  "structuredContent": {
    "ok": true,
    "tagName": "INPUT",
    "id": "search-field",
    "shadowHost": "app-header"
  }
}
```

---

## 4. Operational Best Practices

* **Shadow DOM Typing:** Verify focus before typing when web components encapsulate input fields.

---

## 5. Related Tools

* [`nova.get_element_rect`](nova-get-element-rect.md)
* [`nova.click_selector`](../browser-automation/nova-click-selector.md)
