# `nova.dom_extract`

Extracts a bounded set of fixed, strongly-typed DOM properties and bounding geometry for all elements matching a CSS selector, without executing arbitrary JavaScript.

---

## 1. Overview

`nova.dom_extract` is the preferred tool for high-speed, structured element inspection. Instead of evaluating ad-hoc JavaScript snippets via `eval`—which can crash pages, trigger CSP violations, or leak side effects—`nova.dom_extract` runs a native, read-only extraction pipeline over matched DOM nodes.

* **Capability Bundle:** `dom_reading`, `element_inspection`
* **Safe Read-Only Properties:** Extracts fixed properties (`text`, `href`, `rect`, `ariaLabel`, etc.) with zero runtime script execution.
* **Shadow-DOM Piercing:** Traverses custom Web Components using ` >>> `.
* **Bounded Output:** Hard limits on items (`maxItems`) and total character count (`maxChars`) prevent LLM buffer overflows.

---

## 2. Supported Extractable Properties

The `properties` array accepts any combination of the following 16 fixed property names:

| Property | Data Type | Description |
| :--- | :--- | :--- |
| **`text`** | `string` | Trimmed visible inner text of the element. |
| **`value`** | `string` | Current form value (for `<input>`, `<textarea>`, `<select>`). |
| **`checked`** | `boolean` | Checked status for checkboxes and radio buttons. |
| **`selected`** | `boolean` | Selected state for `<option>` items. |
| **`disabled`** | `boolean` | Whether the interactive element is disabled. |
| **`href`** | `string` | Resolved absolute hyperlink destination for `<a>` tags. |
| **`src`** | `string` | Resolved URL for `<img>`, `<video>`, `<audio>`, or `<iframe>`. |
| **`title`** | `string` | The HTML `title` tooltip attribute. |
| **`ariaLabel`** | `string` | Value of `aria-label` or computed accessible name. |
| **`role`** | `string` | Explicit ARIA role (e.g. `button`, `tab`, `combobox`). |
| **`tagName`** | `string` | Uppercase tag name (e.g. `BUTTON`, `A`, `DIV`). |
| **`id`** | `string` | The element's unique `id` attribute. |
| **`className`** | `string` | Raw CSS class string. |
| **`attributes`** | `object` | Key-value dictionary of all raw element attributes. |
| **`rect`** | `object` | Physical screen geometry: `{ x, y, width, height }`. |
| **`visible`** | `boolean` | True if the element is rendered and not hidden. |

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | 1–10000 characters | Required CSS selector. Supports the ' >>> ' combinator for open Shadow DOM boundaries. |
| `properties` | `array` of `string` | Yes | — | 1–16 items | Fixed read-only fields to extract in the requested order. Unsupported names are rejected instead of evaluated as JavaScript. |
| `maxItems` | `integer` | No | `20` | 1–100 | Maximum matching elements returned in document order. Over-limit runtime fallbacks are clamped to 100 and reported through limits.maxItems. |
| `maxChars` | `integer` | No | `20000` | 1000–200000 | Maximum total characters across returned string values. Structural JSON overhead is not counted; truncation is reported truthfully. |
<!-- /generated:parameters -->

---

## 4. Example Calls

### Extract Search Result Links and Titles
```json
{
  "selector": "div.search-results a.result-link",
  "properties": ["text", "href", "rect", "visible"],
  "maxItems": 10
}
```

### Inspect Form Inputs and Current Values
```json
{
  "selector": "form#checkout-form input, form#checkout-form select",
  "properties": ["id", "tagName", "value", "checked", "disabled", "ariaLabel"],
  "maxItems": 25
}
```

### Extract Web Component Interactive Nodes via Shadow DOM
```json
{
  "selector": "nav-bar-wc >>> button.nav-action",
  "properties": ["text", "role", "ariaLabel", "rect"],
  "maxItems": 15
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "selector": "div.search-results a.result-link",
  "matchCount": 3,
  "items": [
    {
      "text": "Getting Started with Nova Workspace",
      "href": "https://example.com/docs/getting-started",
      "visible": true,
      "rect": { "x": 120, "y": 240, "width": 540, "height": 32 }
    },
    {
      "text": "Architectural Overview & Security Bounds",
      "href": "https://example.com/docs/architecture",
      "visible": true,
      "rect": { "x": 120, "y": 290, "width": 540, "height": 32 }
    },
    {
      "text": "MCP Tool Reference & Protocol Details",
      "href": "https://example.com/docs/mcp-reference",
      "visible": true,
      "rect": { "x": 120, "y": 340, "width": 540, "height": 32 }
    }
  ],
  "limits": {
    "maxItems": 20,
    "truncated": false
  }
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Unsupported property: '...'` | An invalid or arbitrary JavaScript property name was passed. | Select only from the 16 supported properties listed above. |
| `Selector matched nothing: ...` | Selector didn't match any nodes in the document. | Verify selector spelling or check if element is inside an iframe. |
| `maxChars limit reached` | Extracted attribute or text volume exceeded `maxChars`. | Increase `maxChars` or narrow the `properties` list. |

---

## 7. Related Tools & Documentation

* [`nova.read_text_structured`](nova-read-text-structured.md) — Extract text grouped by page landmarks.
* [`nova.extract_table`](nova-extract-table.md) — Extract tabular data into headers and rows.
* [`nova.search_text`](nova-search-text.md) — Search for visible text and obtain matching selectors.
