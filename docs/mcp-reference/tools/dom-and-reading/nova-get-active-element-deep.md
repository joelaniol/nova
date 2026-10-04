# `nova.get_active_element_deep`

> **Traverses through nested Shadow DOM boundaries to find the truly focused interactive element.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.get_active_element_deep` pierces open Shadow DOM trees to discover the actual innermost focused element instead of just reporting the top-level host custom element.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.get_active_element_deep",
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
      "text": "{\"ok\":true,\"found\":true,\"scope\":\"top >>> app-header\",\"element\":{...},\"chain\":[...],\"warnings\":[],\"meta\":{...}}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "result": {
      "ok": true,
      "found": true,
      "scope": "top >>> app-header",
      "element": {
        "tagName": "input",
        "id": "search-field",
        "className": null,
        "role": null,
        "ariaLabel": null,
        "name": null,
        "type": "text",
        "isContentEditable": false,
        "rect": { "x": 120, "y": 64, "width": 240, "height": 32 }
      },
      "chain": [ { "tagName": "app-header", "id": null } ],
      "warnings": [],
      "meta": { "framesScanned": 0, "framesVisited": 0, "crossOriginFrames": 0, "shadowDepth": 1 }
    }
  }
}
```

`scope` is a path string (` >>> `-separated) describing where the focused element was found, not a
separate `shadowHost` field. `chain` lists every element from the top-level active element down to
the innermost one (one entry per shadow boundary crossed); `found: false` with `element: null` means
nothing in the document currently has focus.

---

## 4. Operational Best Practices

* **Shadow DOM Typing:** Verify focus before typing when web components encapsulate input fields.

---

## 5. Related Tools

* [`nova.get_element_rect`](nova-get-element-rect.md)
* [`nova.click_selector`](../browser-automation/nova-click-selector.md)
