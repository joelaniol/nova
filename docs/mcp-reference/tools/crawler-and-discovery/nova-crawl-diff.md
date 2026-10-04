# `nova.crawl_diff`

Compares two completed crawls of the same site to detect added, removed, or modified pages.

---

## 1. Overview

`nova.crawl_diff` computes the delta between two completed crawl runs of a website. By hashing content and comparing URL inventories, it identifies new pages, deleted or broken routes (404s), and content revisions between crawl runs.

* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Defaults to 'default'. Must own both crawls. |
| `oldCrawlId` | `string` | Yes | — | — | Crawl ID of the baseline (older) crawl to compare from. |
| `newCrawlId` | `string` | Yes | — | — | Crawl ID of the newer crawl to compare against the baseline. |
| `includeUnchanged` | `boolean` | No | `false` | — | If true, include unchanged pages in the response. Default false to save tokens. |
| `limit` | `integer` | No | `50` | 1–200 | Maximum number of diff entries to return. Unchanged/hashMissing counts are always reported regardless of limit. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Delta: 2 changed, 3 added, 0 removed, 20 unchanged (25 pages compared)."
    }
  ],
  "structuredContent": {
    "oldCrawlId": "crawl-10b8f33a",
    "newCrawlId": "crawl-4a92c81e",
    "oldScopeKey": "https://docs.example.com",
    "newScopeKey": "https://docs.example.com",
    "oldCreatedUtc": "2026-09-25T14:10:00Z",
    "newCreatedUtc": "2026-10-02T18:30:00Z",
    "pages": [
      {
        "changeType": "added",
        "url": "https://docs.example.com/api/v2/webhooks",
        "oldTitle": null,
        "newTitle": "Webhooks v2 — Example Docs",
        "oldHash": null,
        "newHash": "f49c02d1",
        "oldHttpStatus": null,
        "newHttpStatus": 200,
        "oldConfidence": null,
        "newConfidence": 0.95
      },
      {
        "changeType": "changed",
        "url": "https://docs.example.com/api/auth",
        "oldTitle": "Authentication — Example Docs",
        "newTitle": "Authentication — Example Docs",
        "oldHash": "a38b1f89",
        "newHash": "f49c02d1",
        "oldHttpStatus": 200,
        "newHttpStatus": 200,
        "oldConfidence": 0.9,
        "newConfidence": 0.92
      }
    ],
    "truncated": false,
    "summary": {
      "changed": 2,
      "added": 3,
      "removed": 0,
      "unchanged": 20,
      "unchangedIncluded": 0,
      "hashMissing": 0,
      "total": 25
    },
    "warnings": null,
    "advisoryNote": "Use crawl_verify(urls=[...]) to re-crawl changed/added URLs for fresh content."
  }
}
```

There is no top-level `ok` field. The per-page array is `pages`, not `changes`; a page's status is `changeType` ("added"/"removed"/"changed"/"unchanged"), not `status`, and content hashes are `oldHash`/`newHash`, not `contentHashOld`/`contentHashNew`. The summary key for modified-content pages is `changed`, not `modified`. Both crawls must already be `completed` and scoped to the same site, or the call is rejected as invalid params.

---

## 4. Operational Best Practices

* **Website Change Detection:** Run scheduled crawls weekly and execute `nova.crawl_diff` to detect documentation updates or silent API schema changes.
* **Token Conservation:** Leave `includeUnchanged: false` to focus exclusively on changed routes.
* **Pre-Flight History Check:** Use [`nova.crawl_history`](nova-crawl-history.md) to locate valid `crawlId` pairs before invoking diff.

---

## 5. Related Tools

* [`nova.crawl_history`](nova-crawl-history.md) — Find completed crawl IDs.
* [`nova.site_urls`](nova-site-urls.md) — Persistent accumulated site URL index.
