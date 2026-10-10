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

### D. Conversation Snapshot (`mode="conversation"`)
Read a chat, message log or comment surface as messages in DOM order. When the page does not
declare usable message boundaries, provide `messageSelector` and optional relative text,
author and timestamp selectors. Unknown roles/authors remain unknown. This reads the rendered
window only: `coverage.historyComplete` is `null`, and the result does not establish send
delivery or reply completion. It never scrolls or sends. Overlapping/nested message boundaries
return an explicit ambiguous outcome; use non-overlapping message elements instead.

`maxMessages` and `maxChars` limit output; `maxCharsPerRegion` also limits each message text.
Existing landmark calls keep their default behavior. In conversation mode, `selector` must
identify exactly one scope; failed selection never falls back to unrelated page text.

Text uses the browser's `innerText` layout projection, rather than pixel visibility: transparent
descendants can still contribute text. `maxChars` bounds variable text and metadata values;
JSON structure adds overhead. If lists within a message create overlapping boundaries, supply
a more precise `messageSelector`.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | — | ≤ 10000 characters | Optional CSS subtree scope with ' >>> ' open-shadow traversal. Landmark mode reads the first match, including landmark/body fallback behavior. Conversation mode requires exactly one matched scope and returns an ambiguous outcome otherwise. No match is an error; neither mode broadens to unrelated page content. Omit for the document. |
| `maxCharsPerRegion` | `integer` | No | `10000` | 100–200000 | Maximum characters per landmark region, or per message text in conversation mode. Over-limit text is truncated. |
| `mode` | `string` | No | `"landmarks"` | `landmarks`, `conversation` | Output projection. Omit for the existing landmark contract; conversation reads rendered messages only with unknown total-history coverage. |
| `messageSelector` | `string` | No | — | ≤ 10000 characters | Conversation only: message boundaries inside selector scope, including the root if it matches. Supports ' >>> ' open-shadow traversal. Omit to use declared semantics; ambiguous/nested boundaries return an explicit uncertain outcome, never unrelated page text. |
| `textSelector` | `string` | No | — | ≤ 10000 characters | Conversation only: one visible text element relative to each message, including the message itself. Supports ' >>> '. Missing/ambiguous text is skipped and disclosed; no fallback to the entire message when supplied. |
| `authorSelector` | `string` | No | — | ≤ 10000 characters | Conversation only: one visible author-label element relative to each message, with optional ' >>> '. Omit or no unique match means unknown author. Labels never determine assistant/user roles. |
| `timestampSelector` | `string` | No | — | ≤ 10000 characters | Conversation only: one visible timestamp element relative to each message, with optional ' >>> '. Default time[datetime]. Returns only a declared datetime value; no inferred timestamp. |
| `roleAttribute` | `string` | No | `"data-message-author-role"` | ≤ 64 characters | Conversation only: attribute on a message declaring its role. Known machine values user/assistant/system/developer/tool normalize; others stay unknown with bounded raw evidence. Does not change auto-detection boundaries. |
| `maxMessages` | `integer` | No | `50` | 1–200 | Conversation only: maximum returned messages, in DOM order. More rendered candidates are disclosed; this is not a total-history count. |
| `maxChars` | `integer` | No | `50000` | 1000–200000 | Conversation only: total returned message text/role-value/author/timestamp character budget, excluding fixed JSON structure. Message text also respects maxCharsPerRegion. |

Capability bundles: `browser_automation`, `page_read_debug`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Read Structured Page Landmarks
```json
{
  "maxCharsPerRegion": 5000
}
```

### Read a Conversation with Explicit Message Boundaries
```json
{
  "mode": "conversation",
  "selector": "#conversation",
  "messageSelector": ".message",
  "textSelector": ".message-body",
  "authorSelector": ".author",
  "maxMessages": 50,
  "maxChars": 50000
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
  "selector": null,
  "ok": true,
  "result": {
    "ok": true,
    "scoped": false,
    "regions": [
      {
        "region": "header",
        "label": null,
        "selector": "header",
        "text": "Nova Store | Free Worldwide Shipping on orders over $50",
        "chars": 57
      },
      {
        "region": "main",
        "label": null,
        "selector": "main",
        "text": "Nova Elite Wireless Headphones\nPrice: $299.00\nIn Stock (14 remaining)...",
        "chars": 2140
      }
    ],
    "modals": []
  }
}
```

`regions` is an array of `{region, label, selector, text, chars}` objects, not an object keyed by
region name, and there is no top-level `totalChars`/`truncated` or `url` field: a region that
exceeds `maxCharsPerRegion` simply has `" [truncated]"` appended to its own `text`. `modals` is an
array of the same shape (`selector`, `label`, `text`, `chars`) for any open dialog/overlay found.
`scoped` is `true` only when `selector` matched and narrowed the scan.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Invalid params: selector is not valid CSS.` | The provided `selector` could not be parsed. | Fix the selector syntax. |
| `No DOM element matched selector '...'.` | `selector` is valid CSS but matched nothing. | Verify the selector or omit it to scan the full page. |

A region whose text exceeds `maxCharsPerRegion` is not an error — its `text` is silently truncated
with a trailing `" [truncated]"` marker. A subtree with only canvas/image/SVG content is also not an
error: it comes back as a region (or the `scope`/`body` fallback) with an empty `text` and
`chars: 0`; use [`nova.perceive`](nova-perceive.md) or
[`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md) for visual-only content.

---

## 7. Related Tools & Documentation

* [`nova.dom_extract`](nova-dom-extract.md) — Extract specific typed attributes and bounding boxes.
* [`nova.extract_table`](nova-extract-table.md) — Parse tabular data into structured JSON rows.
* [`nova.search_text`](nova-search-text.md) — Find specific text strings and obtain their selectors.
