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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for crawl ownership checks. Must match the agentId that started the crawl. Defaults to 'default'. |
| `crawlId` | `string` | Yes | — | — | Crawl job ID returned by crawl_start. |
| `offset` | `integer` | No | `0` | ≥ 0 | Pagination start index. Ignored when summary=true. |
| `limit` | `integer` | No | `20` | 1–50 | Maximum number of page results to return. Ignored when summary=true. |
| `filter` | `string` | No | — | — | Optional regex to filter results by URL. Applied before sorting and pagination. |
| `sortBy` | `string` | No | `"sequence"` | `sequence`, `confidence`, `depth`, `loadTime` | Sort field. 'sequence' = BFS crawl order, 'confidence' = page confidence score, 'depth' = BFS depth level, 'loadTime' = page load time in ms. |
| `sortOrder` | `string` | No | `"asc"` | `asc`, `desc` | Sort direction. Use 'desc' with sortBy='confidence' to get highest-confidence pages first. |
| `sinceSequence` | `integer` | No | — | ≥ 0 | Optional stable incremental cursor. When set, only page results with `sequence > sinceSequence` are returned. Requires offset=0 and is intended for running crawls with the default sequence/asc ordering. |
| `screenshotDetail` | `string` | No | `"meta"` | `off`, `meta`, `full` | Controls screenshot payload detail in `pages[].screenshot`. Default `meta` keeps status, dimensions, and capture metadata without base64 image data. 'off': omit screenshot object entirely. 'full': include complete base64 payload when available. |
| `outputDetail` | `string` | No | `"full"` | `minimal`, `summary`, `full` | Per-page field projection. 'minimal' keeps sequence/url/settled/session/readiness/auth/custom results/errors only and omits links, hreflang, metadata lists, content blocks, and screenshots. 'summary' adds compact title/confidence/load/framework/count fields without large collections. 'full' preserves the complete page payload. |
| `maxTextChars` | `integer` | No | `10000` | 1000–200000 | Maximum textContent/customScriptResult/readOnlyPopover serialized characters per page. Defaults shrink automatically under context pressure unless explicitly provided; truncation flags remain explicit. |
| `minConfidence` | `number` | No | — | 0–1 | Minimum confidence threshold. Pages below this value are excluded. Applied before sorting and pagination. |
| `summary` | `boolean` | No | `false` | — | When true, return aggregated statistics instead of full page results. Includes totalPages, avgConfidence, avgLoadTimeMs, totalLinks, frameworks breakdown, depth distribution, duplicate content detection, hydration drift count, and screenshot coverage stats. Significantly cheaper in tokens than reading all pages. |
<!-- /generated:parameters -->

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
