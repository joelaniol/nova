# `nova.crawl_start`

Starts a background breadth-first search (BFS) crawl from a root URL using isolated hidden WebViews.

---

## 1. Overview

`nova.crawl_start` launches an autonomous, background crawler task that navigates a website according to breadth-first traversal rules. It runs entirely inside dedicated hidden WebView2 instances without interfering with the user's active browser tabs or visual viewport.

The crawler automatically detects DOM settlement (waiting for MutationObserver quiescence and network idle), extracts structured page metadata, follows in-scope hyperlinks, respects rate limits, and persists results into the local SQLite `crawl.db` index.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 2 (Autonomous Navigation)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`startUrl`** | `string` | Yes | `none` | Absolute HTTP/HTTPS URL to start crawling from. |
| **`maxPages`** | `integer` | No | `50` | Maximum number of pages to discover and visit before stopping. |
| **`maxDepth`** | `integer` | No | `3` | Maximum link traversal depth from the starting URL. |
| **`crawlMode`** | `string` | No | `"hidden"` | Execution mode: `"hidden"` (background worker) or `"live_tab"` (foreground). |
| **`sameDomainOnly`** | `boolean` | No | `true` | If true, restricts BFS link traversal to the starting domain. |
| **`sameScopeOnly`** | `boolean` | No | `true` | Preferred alias: restricts crawling to the exact origin and authorized subdomains. |
| **`urlPattern`** | `string` | No | `null` | Regular expression filter; only links matching this pattern will be queued. |
| **`excludePattern`** | `string` | No | `null` | Regular expression filter for URLs to skip (e.g. logout, tracking). |
| **`extractMetadata`** | `boolean` | No | `true` | Extract page title, meta description, and semantic header structure. |
| **`extractContent`** | `boolean` | No | `false` | Extract serialized text content from each visited page. |
| **`contentMode`** | `string` | No | `"text_blob"` | Content extraction format: `"text_blob"`, `"structured"`, or `"markdown"`. |
| **`contentSelector`** | `string` | No | `null` | CSS selector scoping content extraction to a container (e.g. `"main, article"`). |
| **`captureScreenshots`** | `boolean` | No | `false` | Capture screenshot artifacts for each visited page. |
| **`pageDelayMs`** | `integer` | No | `500` | Minimum delay in milliseconds between requests to avoid rate limits. |
| **`settleTimeMs`** | `integer` | No | `3000` | Maximum time to wait for JavaScript settlement and network idle. |
| **`parallel`** | `integer` | No | `1` | Number of parallel hidden WebView workers (1-3). |
| **`respectRobotsTxt`** | `boolean` | No | `true` | Parse and obey robots.txt crawl delay and exclusion directives. |
| **`useSitemap`** | `boolean` | No | `false` | Parse sitemap.xml on the canonical domain to seed the BFS queue. |
| **`targetId`** | `string` | No | `null` | Target tab ID whose session cookies and authentication should be shared. |
| **`taskInstanceId`** | `string` | No | `null` | Optional Episodic Task Memory (ETM) task instance ID to bind crawl artifacts to. |
| **`_meta`** | `object` | No | `null` | Optional call metadata and intent declaration. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_start",
  "arguments": {
    "startUrl": "https://docs.example.com/api",
    "maxPages": 25,
    "maxDepth": 2,
    "extractMetadata": true,
    "extractContent": true,
    "contentSelector": "main",
    "pageDelayMs": 750
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Background crawl job started with ID 'crawl-4a92c81e' on https://docs.example.com/api (max 25 pages, depth 2)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "crawlId": "crawl-4a92c81e",
    "status": "running",
    "startUrl": "https://docs.example.com/api",
    "scopeKey": "https://docs.example.com",
    "maxPages": 25,
    "maxDepth": 2,
    "queuedPages": 1
  }
}
```

---

## 4. Operational Best Practices

* **Polling Progress:** Use [`nova.crawl_status`](nova-crawl-status.md) to inspect crawl progression rather than making blocking wait calls.
* **Targeted Content Extraction:** Always specify `contentSelector: "main"` or `contentSelector: "article"` when enabling `extractContent: true` to avoid ingesting repetitive navigation and footer boilerplate.
* **Session Continuity:** Pass `targetId` if the target website requires an active authenticated session from an existing browser tab.

---

## 5. Related Tools

* [`nova.crawl_status`](nova-crawl-status.md) — Monitor crawl progress and page counters.
* [`nova.crawl_results`](nova-crawl-results.md) — Retrieve discovered URLs and extracted content.
* [`nova.crawl_stop`](nova-crawl-stop.md) — Cancel a running crawl job.
