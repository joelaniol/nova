# `nova.crawl_diff`

Compares two completed crawls of the same site to detect added, removed, or modified pages.

---

## 1. Overview

`nova.crawl_diff` computes the delta between two completed crawl runs of a website. By hashing content and comparing URL inventories, it identifies new pages, deleted or broken routes (404s), and content revisions between crawl runs.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`oldCrawlId`** | `string` | Yes | `none` | Crawl ID of the baseline (older) crawl job. |
| **`newCrawlId`** | `string` | Yes | `none` | Crawl ID of the newer crawl job to compare against baseline. |
| **`includeUnchanged`** | `boolean` | No | `false` | When true, includes unchanged pages in the result list. |
| **`limit`** | `integer` | No | `50` | Maximum number of diff entries to return. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_diff",
  "arguments": {
    "oldCrawlId": "crawl-10b8f33a",
    "newCrawlId": "crawl-4a92c81e"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Diff computed: 3 added pages, 0 removed pages, 2 modified pages (20 unchanged)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "oldCrawlId": "crawl-10b8f33a",
    "newCrawlId": "crawl-4a92c81e",
    "summary": {
      "added": 3,
      "removed": 0,
      "modified": 2,
      "unchanged": 20
    },
    "changes": [
      {
        "url": "https://docs.example.com/api/v2/webhooks",
        "status": "added",
        "httpStatus": 200,
        "title": "Webhooks v2 — Example Docs"
      },
      {
        "url": "https://docs.example.com/api/auth",
        "status": "modified",
        "title": "Authentication — Example Docs",
        "contentHashOld": "a38b1f89",
        "contentHashNew": "f49c02d1"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Website Change Detection:** Run scheduled crawls weekly and execute `nova.crawl_diff` to detect documentation updates or silent API schema changes.
* **Token Conservation:** Leave `includeUnchanged: false` to focus exclusively on changed routes.
* **Pre-Flight History Check:** Use [`nova.crawl_history`](nova-crawl-history.md) to locate valid `crawlId` pairs before invoking diff.

---

## 5. Related Tools

* [`nova.crawl_history`](nova-crawl-history.md) — Find completed crawl IDs.
* [`nova.site_urls`](nova-site-urls.md) — Persistent accumulated site URL index.
