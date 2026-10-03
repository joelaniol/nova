# `nova.search_text`

Searches the page for visible text occurrences and returns matching DOM elements with actionable CSS selectors, bounding geometry, and Shadow-DOM traversal chains.

---

## 1. Overview

When an agent knows the visible label of an element (such as a button text "Add to Cart", a menu item "Settings", or a heading "Billing History") but does not know its selector, running a full `perceive` or `read_dom` call is unnecessarily token-heavy. `nova.search_text` provides targeted, low-cost text queries that return precise, ready-to-use CSS selectors.

* **Capability Bundle:** `dom_reading`, `element_inspection`
* **Targeted Selector Discovery:** Returns actionable selectors for immediate use in [`nova.click_selector`](../browser-automation/nova-click-selector.md) or [`nova.type_selector`](../browser-automation/nova-type-selector.md).
* **Deep Shadow-DOM Traversal (`deep: true`):** Returns multi-level ` >>> ` piercing chains when matching text resides inside Web Components.
* **Match Modes:** Supports `contains`, `exact`, `starts_with`, and `regex`.
* **Selector Quality Classification:** Classifies generated selectors by stability (`id`, `testid`, `attribute`, `class`, `anchored`, or `positional`).

---

## 2. Key Capabilities & Features

### A. Match Modes (`match`)
* `contains` *(default)*: Substring search (case-insensitive by default).
* `exact`: Matches exact trimmed element text, avoiding container ancestors.
* `starts_with`: Matches strings starting with the query.
* `regex`: Executes regular expression patterns for dynamic patterns (e.g. order numbers `ORD-[0-9]{5}`).

### B. Tag Filtering (`tag`)
Narrow search results to interactive elements or specific semantic nodes:
```json
{
  "text": "Sign In",
  "tag": "button"
}
```

### C. Selector Quality Scoring (`selectorKind`)
Nova analyzes each matched node and produces the most stable, human-readable selector possible:
* `testid`: Uses data attributes (`[data-testid="..."]`). Highly resilient to design changes.
* `id`: Matches unique element ID (`#login-btn`).
* `attribute` / `class`: Specific unique attributes or semantic class names.
* `anchored`: Short relative path from a reliable ancestor.
* `positional`: Nth-child/nth-of-type chains (flagged as volatile; should not be cached long-term).

### D. Shadow-DOM Support (`deep: true`)
If the matching text lives inside an open shadow root or same-origin iframe:
* When `deep: true` is passed, Nova constructs the full combinator string:
  ```css
  settings-dialog >>> profile-section >>> button.save-changes
  ```
  This selector can be passed directly into [`nova.click_selector`](../browser-automation/nova-click-selector.md).

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `text` | `string` | Yes | — | — | Visible text to search for. |
| `tag` | `string` | No | — | — | Filter by HTML tag name (e.g. 'button', 'a', 'h1'). |
| `match` | `string` | No | `"contains"` | `contains`, `exact`, `starts_with`, `regex` | Match mode for text comparison. |
| `maxResults` | `integer` | No | `100` | 1–2000 | Maximum number of matching elements to return. |
| `caseSensitive` | `boolean` | No | `false` | — | If true, text matching is case-sensitive. |
| `visibleOnly` | `boolean` | No | `true` | — | Only return elements that are visible on the page. |
| `deep` | `boolean` | No | `false` | — | If true, searches in same-origin iframes and open shadow roots in addition to the top document. Returns full >>> selector chains for shadow-contained elements. |
<!-- /generated:parameters -->

---

## 4. Example Calls

### Find a Submit Button by Exact Label
```json
{
  "text": "Complete Purchase",
  "match": "exact",
  "tag": "button"
}
```

### Search Inside Web Components and Shadow DOM
```json
{
  "text": "Export as CSV",
  "deep": true,
  "visibleOnly": true
}
```

### Match Order Numbers with Regex
```json
{
  "text": "INV-2026-[0-9]+",
  "match": "regex",
  "tag": "span"
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "query": "Complete Purchase",
  "totalMatches": 1,
  "matches": [
    {
      "index": 0,
      "text": "Complete Purchase",
      "tagName": "BUTTON",
      "selector": "button#btn-checkout-submit",
      "selectorKind": "id",
      "visible": true,
      "rect": {
        "x": 680,
        "y": 520,
        "width": 210,
        "height": 48
      }
    }
  ]
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `0 matches found` | Text is split across child nodes, hidden, or inside a shadow root without `deep: true`. | Set `deep: true`, use `match: "contains"`, or check with [`nova.read_text_structured`](nova-read-text-structured.md). |
| `Ancestor container returned` | `match: "contains"` matched a large wrapper `<div>` containing the text. | Use `match: "exact"` or pass `tag: "button"` / `tag: "a"`. |
| `Invalid regex syntax` | A malformed regular expression pattern was provided in `text`. | Verify regex escaping before sending. |

---

## 7. Related Tools & Documentation

* [`nova.click_selector`](../browser-automation/nova-click-selector.md) — Click the selector returned by `search_text`.
* [`nova.read_text_structured`](nova-read-text-structured.md) — Read full textual content grouped by landmarks.
* [`nova.dom_extract`](nova-dom-extract.md) — Extract structured attributes from known selectors.
