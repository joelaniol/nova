# `nova.force_pseudo_state`

> **Forces CSS pseudo-class states (:hover, :focus, :active, :visited) on an element.**

* **Core Feature Guide:** [Visual Evidence & Layout QA](../../../core-features/research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.force_pseudo_state` holds an element in one or more CSS pseudo-classes (`active`, `hover`, `focus`, `focus-visible`, `focus-within`, `visited`, `target`), making it easy to inspect hover styles and focus rings. The state is only painted: no mouse or focus events fire, so menus and tooltips opened by JavaScript stay closed. Pass `states: []` (or omit `states`) to clear the forced state.

The state stays on that DOM node until cleared or until a navigation replaces the document; a re-render that replaces the element drops it. If no element matches, the call returns `ok: false`, `status: "not_found"` and `reasonCode: "pseudo_state.selector_not_found"`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector for the element whose state should be held. |
| `states` | `array` of `string` | No | — | — | Pseudo-classes to force. Omit or pass an empty array to clear the element's forced state and return it to normal. An unsupported name is rejected rather than ignored, because a silently ignored state looks like a page that does not style it. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
    "states": [
      "hover"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Forcing :hover on .nav-item-dropdown. Painted only - no events were fired."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "stage": "action",
    "targetId": "tab-1",
    "selector": ".nav-item-dropdown",
    "found": true,
    "forcedStates": [
      "hover"
    ],
    "cleared": false,
    "note": "A forced state only paints. No mouseenter/mouseover fires, so JavaScript-driven menus and tooltips stay closed - use nova.input_move for those. It is bound to this DOM node, so a re-render that replaces the element drops it and you set it again. Otherwise it persists until cleared (states: []) or a navigation replaces the document.",
    "toolName": "nova.force_pseudo_state"
  }
}
```

---

## 4. Operational Best Practices

* **CSS-only Menus:** Forcing `hover` opens dropdowns that are pure CSS; for menus opened by JavaScript, move the pointer with `nova.input_move` instead.
* **Clean Up:** Clear the forced state with `states: []` before taking screenshots that should show the natural page.

---

## 5. Related Tools

* [`nova.get_computed_style`](nova-get-computed-style.md)
* [`nova.measure_elements`](nova-measure-elements.md)
