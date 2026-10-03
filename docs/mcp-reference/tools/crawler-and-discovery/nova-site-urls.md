# `nova.site_urls`

Queries the persistent Site-URL-Index for known endpoints, utility scores, and route candidates.

---

## 1. Overview

`nova.site_urls` queries the persistent cross-crawl URL index maintained in `crawl.db`. As Nova crawls websites, navigates pages, and executes tasks, it indexes discovered endpoints along with utility scores, observed HTTP statuses, and content freshness. Agents use this index to locate routes instantly without crawling from scratch.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scopeKey`** | `string` | No | `null` | Canonical site scope (e.g. `"https://docs.example.com"`). |
| **`domain`** | `string` | No | `null` | Domain name or host to search (e.g. `"docs.example.com"`). |
| **`origin`** | `string` | No | `null` | Exact origin filter. |
| **`pathPrefix`** | `string` | No | `null` | Path prefix filter (e.g. `"/api/v2"`). |
| **`limit`** | `integer` | No | `50` | Maximum number of URLs to return, sorted by utility score. |
| **`includeDead`** | `boolean` | No | `false` | Include URLs confirmed dead (404/410). |
| **`includeStale`** | `boolean` | No | `false` | Include stale URLs not observed in recent crawls. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.site_urls",
  "arguments": {
    "domain": "docs.example.com",
    "pathPrefix": "/api",
    "limit": 3
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 3 indexed URLs for docs.example.com matching path prefix /api."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scopeKey": "https://docs.example.com",
    "totalMatches": 28,
    "urls": [
      {
        "url": "https://docs.example.com/api",
        "title": "API Overview",
        "httpStatus": 200,
        "utilityScore": 0.98,
        "lastSeenAt": "2026-10-02T18:35:12Z"
      },
      {
        "url": "https://docs.example.com/api/auth",
        "title": "Authentication & Tokens",
        "httpStatus": 200,
        "utilityScore": 0.94,
        "lastSeenAt": "2026-10-02T18:35:12Z"
      },
      {
        "url": "https://docs.example.com/api/pricing",
        "title": "API Pricing & Tiers",
        "httpStatus": 200,
        "utilityScore": 0.88,
        "lastSeenAt": "2026-10-02T18:35:12Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Index-First Retrieval:** Before starting an expensive crawl, query `nova.site_urls` to see if the required route is already known in the index.
* **Utility Sorting:** Results are sorted by `utilityScore` descending, ranking high-traffic landing pages and API hubs higher than peripheral leaf nodes.
* **Path Prefix Filtering:** Use `pathPrefix` to narrow candidates to specific application sub-trees (e.g. `"/settings"`, `"/dashboard"`).

---

## 5. Related Tools

* [`nova.site_urls_report`](nova-site-urls-report.md) — Update the index with live observations.
* [`nova.crawl_start`](nova-crawl-start.md) — Re-crawl to refresh the index.
