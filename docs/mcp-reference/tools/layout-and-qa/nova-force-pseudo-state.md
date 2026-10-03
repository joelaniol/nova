# `nova.force_pseudo_state`

> **Forces CSS pseudo-class states (:hover, :focus, :active, :visited) on an element.**

* **Security Tier:** Tier 2 (CSS Emulation)
* **Core Feature Guide:** [Visual Evidence & Layout QA](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.force_pseudo_state` overrides CDP DOM styles to lock an element in a pseudo-state, making it easy to inspect hover menus and focus rings.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector for the element whose state should be held. |
| `states` | `array` of `string` | No | — | — | Pseudo-classes to force. Omit or pass an empty array to clear the element's forced state and return it to normal. An unsupported name is rejected rather than ignored, because a silently ignored state looks like a page that does not style it. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
<!-- /generated:parameters -->

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
