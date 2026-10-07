# `nova.crawl_history`

Lists past crawl jobs and high-level summaries from the persistent crawler database.

---

## 1. Overview

`nova.crawl_history` queries the local SQLite `crawl.db` index for past crawl jobs. It returns lightweight summaries (status, URLs discovered, start/finish timestamps, error counts) without loading large page text blobs into memory.

* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Defaults to 'default'. |
| `ownerAgentId` | `string` | No | — | — | Optional explicit owner filter. If omitted, history is scoped to the calling agentId. Any different ownerAgentId is rejected. |
| `scopeKey` | `string` | No | — | — | Filter by persisted crawl scope. Hidden and live_tab crawls both persist origin-style keys like `https://example.com:8443`, so same-host different-port histories stay separate. Accepts only host, host:port, or origin syntax; full page URLs with path/query/fragment are invalid params. |
| `status` | `string` | No | — | `running`, `completed`, `failed`, `cancelled`, `interrupted` | Filter by crawl status. |
| `taskInstanceId` | `string` | No | — | — | Optional ETM task-instance filter. Returns only crawls bound to this taskInstanceId. |
| `limit` | `integer` | No | `20` | 1–100 | Maximum number of crawl summaries to return. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Crawl history: 2 of 2 crawls found."
    }
  ],
  "structuredContent": {
    "crawls": [
      {
        "crawlId": "crawl-4a92c81e",
        "ownerAgentId": "default",
        "crawlKind": "bfs",
        "crawlMode": "hidden",
        "startUrl": "https://docs.example.com/api",
        "scopeKey": "https://docs.example.com",
        "status": "completed",
        "maxPages": 25,
        "pagesPersisted": 25,
        "pagesSucceeded": 25,
        "pagesFailed": 0,
        "createdUtc": "2026-10-02T18:30:00Z",
        "startedUtc": "2026-10-02T18:30:01Z",
        "finishedUtc": "2026-10-02T18:35:12Z",
        "retentionClass": "best_effort"
      },
      {
        "crawlId": "crawl-10b8f33a",
        "ownerAgentId": "default",
        "crawlKind": "bfs",
        "crawlMode": "hidden",
        "startUrl": "https://docs.example.com/api",
        "scopeKey": "https://docs.example.com",
        "status": "completed",
        "maxPages": 25,
        "pagesPersisted": 22,
        "pagesSucceeded": 22,
        "pagesFailed": 0,
        "createdUtc": "2026-09-25T14:10:00Z",
        "startedUtc": "2026-09-25T14:10:01Z",
        "finishedUtc": "2026-09-25T14:14:40Z",
        "retentionClass": "best_effort"
      }
    ],
    "total": 2,
    "hasMore": false,
    "truncated": false,
    "queryInput": "https://docs.example.com",
    "matchedScopeKeys": ["https://docs.example.com"],
    "advisoryNote": "Use crawl_results(crawlId) to retrieve page-level details for your own historical crawls."
  }
}
```

There is no top-level `ok` field. Page counts are `pagesPersisted`/`pagesSucceeded`/`pagesFailed`, not `visitedPages`; timestamps are `createdUtc`/`startedUtc`/`finishedUtc`, not `startedAt`/`completedAt` (entries also carry `config`, `urlCount`, and a few other fields omitted above for brevity).

---

## 4. Operational Best Practices

* **Delta Analysis Input:** Identify the two most recent `crawlId` entries from history to feed into [`nova.crawl_diff`](nova-crawl-diff.md).
* **Resume Discovery:** Check previous crawl history before crawling an unfamiliar domain to see if an index already exists.
* **Origin Scoping:** Always provide `scopeKey` when querying large multi-domain local databases to minimize result payload size.

---

## 5. Related Tools

* [`nova.crawl_diff`](nova-crawl-diff.md) — Compare two historical crawls.
* [`nova.crawl_results`](nova-crawl-results.md) — Inspect full page results from a specific job.
