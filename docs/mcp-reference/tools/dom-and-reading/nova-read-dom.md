# `nova.read_dom`

Reads a sanitized snapshot of the document's outer HTML from a tab, bounded by a configurable character cap and mirrored in structured content.

---

## 1. Overview

`nova.read_dom` returns the raw serialized HTML of the current document. It is intended for scenarios where an agent needs full structural context, unusual attribute inspection, or when automated parsers require the raw markup hierarchy.

* **Dual Output:** Returns HTML in both the standard response text and `structuredContent.domHtml`.
* **Bounded Output (`maxChars`):** Prevents blowing agent context windows on megabyte-sized HTML dumps.
* **Token Preservation Warning:** For targeted extraction, agents should prefer [`nova.dom_extract`](nova-dom-extract.md) or [`nova.read_text_structured`](nova-read-text-structured.md) to save up to 90% of tokens.

---

## 2. Key Capabilities & Features

### A. Serialized Outer HTML
Returns the live DOM state (including dynamically inserted JavaScript nodes and client-rendered elements), rather than the static source code originally fetched from the network.

### B. Mirroring in `structuredContent.domHtml`
For client runtimes that support structured tool responses (such as Claude Code or Antigravity with `--mirror-structured-content`), the complete HTML string is mirrored in `structuredContent.domHtml`, preserving formatting without escaping issues.

### C. Character Bounds (`maxChars`)
By default, extraction is capped at `30,000` characters. If the page exceeds this limit, Nova cleanly truncates the markup and sets the `truncated: true` flag in the response metadata.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `maxChars` | `integer` | No | `30000` | 1000–5000000 | Maximum characters to return. Larger values = more detail but more tokens. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Standard DOM Read
```json
{
  "maxChars": 25000
}
```

### Deep Inspection with Extended Character Budget
```json
{
  "targetId": "tab-103",
  "maxChars": 100000
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-103",
  "url": "https://example.com/checkout",
  "title": "Secure Checkout - Nova Store",
  "totalChars": 24890,
  "truncated": false,
  "structuredContent": {
    "domHtml": "<!DOCTYPE html><html lang=\"en\"><head><title>Secure Checkout</title>...</head><body><div id=\"app\">...</div></body></html>"
  }
}
```

---

## 6. Token Economics & Best Practices

> [!TIP]
> **Use the Right Tool for the Job:**
> Raw DOM dumps consume massive token budgets.
> * If you need specific element attributes or coordinates: use [`nova.dom_extract`](nova-dom-extract.md).
> * If you need readable page text: use [`nova.read_text_structured`](nova-read-text-structured.md).
> * If you need table data: use [`nova.extract_table`](nova-extract-table.md).
> * If you need to find an element with specific text: use [`nova.search_text`](nova-search-text.md).
> Only use `nova.read_dom` when comprehensive, unparsed markup is strictly required.

---

## 7. Related Tools & Documentation

* [`nova.dom_extract`](nova-dom-extract.md) — Extract specific element properties without raw HTML.
* [`nova.read_text_structured`](nova-read-text-structured.md) — Read visible text grouped by landmark regions.
* [`nova.perceive`](nova-perceive.md) — Comprehensive visual and structural page inspection.
