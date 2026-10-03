# `nova.crawl_links`

Instantly extracts and classifies all hyperlinks from an existing active browser tab.

---

## 1. Overview

`nova.crawl_links` performs fast, synchronous hyperlink extraction from an open tab without launching a background crawl job. It categorizes links by relation, external vs internal domain status, and navigation intent, while optionally penetrating Shadow DOM roots and iframes.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`sameDomainOnly`** | `boolean` | No | `false` | If true, only returns links matching the current tab's host. |
| **`sameScopeOnly`** | `boolean` | No | `false` | Preferred alias: restricts returned links to the current origin. |
| **`includeText`** | `boolean` | No | `true` | Include the visible anchor text for each link. |
| **`deep`** | `boolean` | No | `false` | If true, penetrates Shadow DOM trees and same-origin iframes. |
| **`urlPattern`** | `string` | No | `null` | JavaScript-compatible regex pattern to filter returned URLs. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_links",
  "arguments": {
    "sameDomainOnly": true,
    "includeText": true,
    "urlPattern": ".*\\/docs\\/.*"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Extracted 12 same-domain doc links from active tab."
    }
  ],
  "structuredContent": {
    "ok": true,
    "count": 12,
    "pageUrl": "https://example.com/welcome",
    "links": [
      {
        "url": "https://example.com/docs/getting-started",
        "text": "Getting Started Guide",
        "rel": "",
        "isExternal": false,
        "isNavigation": true
      },
      {
        "url": "https://example.com/docs/api-reference",
        "text": "Full API Reference",
        "rel": "",
        "isExternal": false,
        "isNavigation": true
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Zero-Cost Exploration:** Use `nova.crawl_links` when you only need to explore the immediate next steps on the current page without background worker overhead.
* **Shadow DOM Extraction:** Pass `deep: true` if the target application uses Web Components or custom elements for navigation menus.
* **Prefilter with RegEx:** Use `urlPattern` to discard anchor fragments (`#section`), media links, or unwanted paths before receiving the payload.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Comprehensive multi-page background crawler.
* [`nova.dom_extract`](../dom-and-reading/nova-dom-extract.md) — Custom selector attribute extraction.
