# `nova.crawl_diff`

Compares two completed crawls of the same site to detect added, removed, or modified pages.

---

## 1. Overview

`nova.crawl_diff` computes the delta between two completed crawl runs of a website. By hashing content and comparing URL inventories, it identifies new pages, deleted or broken routes (404s), and content revisions between crawl runs.

* **Security Tier:** Tier 1 (Read-Only)
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
