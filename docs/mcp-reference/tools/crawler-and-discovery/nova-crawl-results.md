# `nova.crawl_results`

Retrieves paginated page details, extracted text, metadata, and screenshots from a crawl job.

---

## 1. Overview

`nova.crawl_results` reads discovered pages and extracted content from the persistent SQLite `crawl.db` index. It supports server-side pagination, URL filtering, incremental cursors via `sinceSequence`, and aggregated statistical summaries.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`crawlId`** | `string` | Yes | `none` | Crawl job ID returned by `nova.crawl_start`. |
| **`summary`** | `boolean` | No | `false` | When true, returns aggregated site statistics instead of individual page rows. |
| **`limit`** | `integer` | No | `20` | Maximum number of page results to return per page (max 100). |
| **`offset`** | `integer` | No | `0` | Pagination offset index. |
| **`sinceSequence`** | `integer` | No | `null` | Incremental cursor: returns only results with `sequence > sinceSequence`. |
| **`filter`** | `string` | No | `null` | Regex filter to match URLs before sorting and pagination. |
| **`sortBy`** | `string` | No | `"sequence"` | Sort column: `"sequence"` (crawl order), `"confidence"`, or `"depth"`. |
| **`sortOrder`** | `string` | No | `"asc"` | Sort order: `"asc"` or `"desc"`. |
| **`maxTextChars`** | `integer` | No | `10000` | Maximum characters of extracted text per page result. |
| **`outputDetail`** | `string` | No | `"full"` | Field projection: `"minimal"` or `"full"`. |
| **`screenshotDetail`** | `string` | No | `"meta"` | Screenshot projection: `"meta"` (dimensions/status) or `"inline"` (base64). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_results",
  "arguments": {
    "crawlId": "crawl-4a92c81e",
    "limit": 2,
    "offset": 0,
    "outputDetail": "minimal"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Retrieved 2 page results for crawl-4a92c81e (total visited: 12)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "crawlId": "crawl-4a92c81e",
    "totalResults": 12,
    "offset": 0,
    "limit": 2,
    "pages": [
      {
        "sequence": 1,
        "url": "https://docs.example.com/api",
        "httpStatus": 200,
        "depth": 0,
        "title": "API Overview — Example Docs",
        "linksDiscovered": 14,
        "contentLength": 4210
      },
      {
        "sequence": 2,
        "url": "https://docs.example.com/api/auth",
        "httpStatus": 200,
        "depth": 1,
        "title": "Authentication & Tokens — Example Docs",
        "linksDiscovered": 8,
        "contentLength": 3120
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Incremental Polling:** Use `sinceSequence` with the highest sequence number received to incrementally stream new pages as the crawl progresses.
* **Summary First:** Call with `summary: true` first to determine total pages and crawl health before requesting large result pages.
* **Token Conservation:** Keep `outputDetail: "minimal"` unless full extracted markdown text is required for immediate prompt analysis.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Launch a crawl.
* [`nova.crawl_diff`](nova-crawl-diff.md) — Compare results across two crawl runs.
