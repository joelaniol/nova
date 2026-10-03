# `nova.read_text`

> **Extracts clean visible plain text from the document or a specified selector container.**

* **Security Tier:** Tier 1 (Read-Only Extraction)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.read_text` strips HTML tags and returns formatted plain text representing visible content on the page, with whitespace preserved.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | — | — | Optional CSS selector to scope text extraction. Omit to read entire document body. Supports ' >>> ' shadow DOM combinator. |
| `maxChars` | `integer` | No | `30000` | 1000–5000000 | Maximum characters to return. Defaults shrink automatically under context pressure unless explicitly provided. |
| `offset` | `integer` | No | — | 0–5000000 | Start reading at this character position. Unverified - use continuationToken when the page may have changed. Mutually exclusive with continuationToken. |
| `continuationToken` | `string` | No | — | ≤ 512 characters | Token from a previous response's continuation block. Carries the next position plus a fingerprint of that document; a changed page is rejected with reasonCode='read.source_changed' instead of returning text from elsewhere. Mutually exclusive with offset. |

Capability bundles: `browser_automation`, `page_read_debug`.
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_read_text",
  "arguments": {
    "targetId": "tab-1",
    "selector": "article.main-content"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Extracted 1,450 characters of article text."
    }
  ],
  "structuredContent": {
    "ok": true,
    "selector": "article.main-content",
    "text": "Quantum computing advances in 2026..."
  }
}
```

---

## 4. Operational Best Practices

* **Fast Summarization:** Extract body text directly without parsing heavy DOM trees.

---

## 5. Related Tools

* [`nova.read_text_structured`](nova-read-text-structured.md)
* [`nova.search_text`](nova-search-text.md)
