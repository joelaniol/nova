# `nova.force_pseudo_state`

> **Forces CSS pseudo-class states (:hover, :focus, :active, :visited) on an element.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 2 (CSS Emulation)
* **Core Feature Guide:** [Visual Evidence & Layout QA](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.force_pseudo_state` overrides CDP DOM styles to lock an element in a pseudo-state, making it easy to inspect hover menus and focus rings.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `selector` | `string` | **Yes** | CSS selector for the element whose state should be held. |
| `states` | `array` | No | Pseudo-classes to force. Omit or pass an empty array to clear the element's forced state and return it to normal. An unsupported name is rejected rather than ignored, because a silently ignored state looks like a page that does not style it. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_force_pseudo_state",
  "arguments": {
    "targetId": "tab-1",
    "selector": ".nav-item-dropdown",
    "state": "hover"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Forced :hover state on .nav-item-dropdown."
    }
  ],
  "structuredContent": {
    "ok": true,
    "selector": ".nav-item-dropdown",
    "state": "hover"
  }
}
```

---

## 4. Operational Best Practices

* **Dropdown Inspection:** Lock dropdown hover states to safely extract menu options without cursor jitter.

---

## 5. Related Tools

* [`nova.get_computed_style`](nova-get-computed-style.md)
* [`nova.measure_elements`](nova-measure-elements.md)
