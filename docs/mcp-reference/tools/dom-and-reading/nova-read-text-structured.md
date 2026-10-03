# `nova.read_text_structured`

Extracts visible page text organized by semantic HTML landmark regions (`header`, `nav`, `main`, `aside`, `footer`, and `modals`), eliminating monolithic text dumps and saving LLM context tokens.

---

## 1. Overview

`nova.read_text_structured` is designed for agents that need to inspect page contents, verify textual messages, or conduct quality-assurance audits without downloading raw HTML or unformatted string blobs. Instead of flat dumps, Nova groups text by semantic landmarks, allowing agents to focus directly on `main` content or inspect `modals` specifically.

* **Landmark-Scoped Extraction:** Automatically categorizes text into `header`, `nav`, `main`, `aside`, `footer`, and open `modals`.
* **Subtree Scoping (`selector`):** Target a specific container or shadow root (` >>> `) rather than reading the entire page.
* **Token Efficiency:** Drops scripts, stylesheets, hidden DOM nodes, and decorative whitespace.

---

## 2. Key Capabilities & Features

### A. Landmark Partitioning
When invoked without a selector, Nova parses the document according to WAI-ARIA and HTML5 landmark rules:
* `header`: Site banners, top-level headings, user account summaries.
* `nav`: Primary and secondary navigation links, breadcrumbs.
* `main`: Core document content, article body, search results.
* `aside`: Sidebars, related links, secondary metadata.
* `footer`: Copyright information, legal links, language switchers.
* `modals`: Active dialog overlays, consent banners, and drawer panels.

### B. Scoped Subtree Reading (`selector`)
When auditing a specific component (e.g. a product card or conversation feed):
* Pass `selector: "div.checkout-summary"` to limit extraction to that subtree.
* If landmarks exist inside the subtree, they are retained; otherwise, text is returned under a single `"scope"` region.
* Pierces open Shadow DOM using the ` >>> ` combinator (e.g. `chat-widget >>> .message-history`).

### C. Character Limits per Region (`maxCharsPerRegion`)
Enforces predictable payload bounds (default `10,000` characters per region). Long regions are safely truncated with truncation indicators, preventing unexpected token exhaustion in the LLM context.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | — | ≤ 10000 characters | Optional CSS selector scoping the scan to the first matched element's subtree. Supports the ' >>> ' shadow DOM combinator. Landmarks and modals inside that subtree are reported; a subtree without landmarks comes back as a single 'scope' region. Errors if it matches nothing instead of falling back to the whole page. Omit to scan the entire document. |
| `maxCharsPerRegion` | `integer` | No | `10000` | 100–200000 | Maximum characters per region. Regions exceeding this limit are truncated. |

Capability bundles: `browser_automation`, `page_read_debug`.
<!-- /generated:parameters -->

---

## 4. Example Calls

### Read Structured Page Landmarks
```json
{
  "maxCharsPerRegion": 5000
}
```

### Inspect Only the Main Content Container
```json
{
  "selector": "main#primary-content",
  "maxCharsPerRegion": 20000
}
```

### Read Text Inside a Web Component / Shadow DOM
```json
{
  "selector": "user-feedback-modal >>> .dialog-body",
  "maxCharsPerRegion": 3000
}
```

---

## 5. Return Value Structure

```json
{
  "targetId": "tab-101",
  "url": "https://example.com/products/wireless-headphones",
  "regions": {
    "header": "Nova Store | Free Worldwide Shipping on orders over $50",
    "nav": "Products > Audio > Noise-Cancelling Headphones",
    "main": "Nova Elite Wireless Headphones\nPrice: $299.00\nIn Stock (14 remaining)\nHigh-fidelity active noise cancellation with 40-hour battery life...",
    "aside": "Customer Reviews (4.8 / 5.0 stars from 1,240 ratings)\nRelated accessories...",
    "footer": "© 2026 Nova Workspace Inc. All rights reserved. Privacy Policy | Terms of Service",
    "modals": []
  },
  "totalChars": 2840,
  "truncated": false
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Selector matched nothing: ...` | Provided `selector` does not exist on the current page. | Verify the selector or omit `selector` to scan the full page. |
| `Region truncated: main` | Main content exceeded `maxCharsPerRegion`. | Increase `maxCharsPerRegion` or use a more specific child selector. |
| `Empty text returned` | The target element contains only canvas, images, or SVG nodes without text. | Use [`nova.perceive`](nova-perceive.md) or [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md). |

---

## 7. Related Tools & Documentation

* [`nova.dom_extract`](nova-dom-extract.md) — Extract specific typed attributes and bounding boxes.
* [`nova.extract_table`](nova-extract-table.md) — Parse tabular data into structured JSON rows.
* [`nova.search_text`](nova-search-text.md) — Find specific text strings and obtain their selectors.
