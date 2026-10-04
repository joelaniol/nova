# `nova.dom_extract`

Extracts a bounded set of fixed, strongly-typed DOM properties and bounding geometry for all elements matching a CSS selector, without executing arbitrary JavaScript.

---

## 1. Overview

`nova.dom_extract` is the preferred tool for high-speed, structured element inspection. Instead of evaluating ad-hoc JavaScript snippets via `eval`—which can crash pages, trigger CSP violations, or leak side effects—`nova.dom_extract` runs a native, read-only extraction pipeline over matched DOM nodes.

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

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
  "properties": ["text", "href", "rect", "visible"],
  "ok": true,
  "status": "ok",
  "reasonCode": null,
  "matchedCount": 3,
  "returnedCount": 3,
  "hasMore": false,
  "truncated": false,
  "sourceValueChars": 118,
  "returnedValueChars": 118,
  "limits": { "maxItems": 20, "maxChars": 20000 },
  "result": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "matchedCount": 3,
    "returnedCount": 3,
    "hasMore": false,
    "truncated": false,
    "sourceValueChars": 118,
    "returnedValueChars": 118,
    "matches": [
      {
        "index": 0,
        "values": {
          "text": "Getting Started with Nova Workspace",
          "href": "https://example.com/docs/getting-started",
          "rect": { "x": 120, "y": 240, "width": 540, "height": 32 },
          "visible": true
        }
      }
    ]
  }
}
```

The requested properties come back per match under `values`, in the order given in `properties`;
`result` duplicates the same counters the top level already reports (the top level is a convenience
projection of `result`).

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Invalid params: unsupported DOM property '...'. Allowed: ...` | An invalid or arbitrary JavaScript property name was passed. | Select only from the 16 supported properties listed above. |
| `Invalid params: selector is not valid CSS.` | The selector string could not be parsed as CSS (or Shadow-DOM chain). | Fix the selector syntax. |
| `No DOM element matched selector '...'.` | The selector is valid CSS but matched nothing in the document. | Verify selector spelling or check if the element is inside an iframe. |

Exceeding `maxChars` or `maxItems` is not an error: the call still returns `ok: true` with
`status: "truncated"`, `reasonCode: "dom.output_truncated"`, and `truncated: true` so the caller can
decide whether to raise the limit.

---

## 7. Related Tools & Documentation

* [`nova.read_text_structured`](nova-read-text-structured.md) — Extract text grouped by page landmarks.
* [`nova.extract_table`](nova-extract-table.md) — Extract tabular data into headers and rows.
* [`nova.search_text`](nova-search-text.md) — Search for visible text and obtain matching selectors.
