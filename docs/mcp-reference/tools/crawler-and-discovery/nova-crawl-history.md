# `nova.crawl_history`

Lists past crawl jobs and high-level summaries from the persistent crawler database.

---

## 1. Overview

`nova.crawl_history` queries the local SQLite `crawl.db` index for past crawl jobs. It returns lightweight summaries (status, URLs discovered, start/finish timestamps, error counts) without loading large page text blobs into memory.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`scopeKey`** | `string` | No | `null` | Filter history by canonical origin scope (e.g. `"https://docs.example.com"`). |
| **`status`** | `string` | No | `null` | Filter by crawl status (`"completed"`, `"failed"`, `"stopped"`, `"running"`). |
| **`limit`** | `integer` | No | `20` | Maximum number of crawl summaries to return (max 100). |
| **`taskInstanceId`** | `string` | No | `null` | Filter by linked ETM task instance ID. |
| **`ownerAgentId`** | `string` | No | `null` | Filter by initiating agent ID. Defaults to calling agent. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_history",
  "arguments": {
    "scopeKey": "https://docs.example.com",
    "limit": 5
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 2 past crawl jobs for scope 'https://docs.example.com'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "total": 2,
    "crawls": [
      {
        "crawlId": "crawl-4a92c81e",
        "startUrl": "https://docs.example.com/api",
        "status": "completed",
        "visitedPages": 25,
        "startedAt": "2026-10-02T18:30:00Z",
        "completedAt": "2026-10-02T18:35:12Z"
      },
      {
        "crawlId": "crawl-10b8f33a",
        "startUrl": "https://docs.example.com/api",
        "status": "completed",
        "visitedPages": 22,
        "startedAt": "2026-09-25T14:10:00Z",
        "completedAt": "2026-09-25T14:14:40Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Delta Analysis Input:** Identify the two most recent `crawlId` entries from history to feed into [`nova.crawl_diff`](nova-crawl-diff.md).
* **Resume Discovery:** Check previous crawl history before crawling an unfamiliar domain to see if an index already exists.
* **Origin Scoping:** Always provide `scopeKey` when querying large multi-domain local databases to minimize result payload size.

---

## 5. Related Tools

* [`nova.crawl_diff`](nova-crawl-diff.md) — Compare two historical crawls.
* [`nova.crawl_results`](nova-crawl-results.md) — Inspect full page results from a specific job.
