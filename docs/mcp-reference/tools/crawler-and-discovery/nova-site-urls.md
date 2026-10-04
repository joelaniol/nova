# `nova.site_urls`

Queries the persistent Site-URL-Index for known endpoints, utility scores, and route candidates.

---

## 1. Overview

`nova.site_urls` queries the persistent cross-crawl URL index maintained in `crawl.db`. As Nova crawls websites, navigates pages, and executes tasks, it indexes discovered endpoints along with utility scores, observed HTTP statuses, and content freshness. Agents use this index to locate routes instantly without crawling from scratch.

* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Defaults to 'default'. |
| `domain` | `string` | No | — | — | Legacy primary scope query. Accepts a domain, host:port, or origin (for example 'www.example.com', 'www.example.com:8443', or 'https://www.example.com'). Paths, queries, and fragments are invalid. The runtime resolves matching Site-URL-Index scope origins, merges legacy host-only buckets, and returns the matched canonical origin(s). |
| `scopeKey` | `string` | No | — | — | Preferred alias when reusing a persisted crawler scope from crawl_history. Accepts the same host/host:port/origin syntax as domain and must match domain/origin if multiple aliases are provided. |
| `origin` | `string` | No | — | — | Explicit origin-style alias for the Site-URL-Index query (for example 'https://www.example.com:8443'). Must match domain/scopeKey if multiple aliases are provided. |
| `pathPrefix` | `string` | No | — | — | Optional path prefix filter (e.g. '/channels'). Only returns URLs whose logical_route_path starts with this prefix. |
| `includeStale` | `boolean` | No | `false` | — | If true, include URLs marked as stale (not seen in recent crawls but not confirmed dead). |
| `includeDead` | `boolean` | No | `false` | — | If true, include URLs confirmed dead (404/410). Useful for debugging or verifying removals. |
| `limit` | `integer` | No | `50` | 1–200 | Maximum number of URLs to return. Sorted by utility_score descending. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "28 known URLs for https://docs.example.com (26 active, 2 stale, 0 dead)."
    }
  ],
  "structuredContent": {
    "origin": "https://docs.example.com",
    "matchedOrigins": ["https://docs.example.com"],
    "queryInput": "docs.example.com",
    "authoritative": false,
    "advisory": "Historical route candidates from prior crawls. Verify before relying.",
    "freshness": {
      "oldestEntry": "2026-09-25T14:10:00Z",
      "newestEntry": "2026-10-02T18:35:12Z",
      "indexSize": 28,
      "activeCount": 26,
      "staleCount": 2,
      "deadCount": 0
    },
    "recommendedStartUrls": [
      {
        "url": "https://docs.example.com/api",
        "title": "API Overview",
        "lifecycleState": "active",
        "accessState": "ok",
        "confidence": 0.95,
        "utilityScore": 0.98,
        "seenInCrawls": 3,
        "lastSeenUtc": "2026-10-02T18:35:12Z"
      }
    ],
    "otherCandidates": [
      {
        "url": "https://docs.example.com/api/auth",
        "title": "Authentication & Tokens",
        "lifecycleState": "active",
        "accessState": "ok",
        "confidence": 0.9,
        "utilityScore": 0.94,
        "seenInCrawls": 3,
        "lastSeenUtc": "2026-10-02T18:35:12Z"
      },
      {
        "url": "https://docs.example.com/api/pricing",
        "title": "API Pricing & Tiers",
        "lifecycleState": "active",
        "accessState": "ok",
        "confidence": 0.85,
        "utilityScore": 0.88,
        "seenInCrawls": 2,
        "lastSeenUtc": "2026-10-02T18:35:12Z"
      }
    ]
  }
}
```

There is no top-level `ok`, `scopeKey`, `totalMatches`, or flat `urls[]` array. The origin field is `origin`; the total/active/stale/dead counts live under `freshness`; matched entries are split into `recommendedStartUrls` and `otherCandidates` (not a single ranked `urls` list); there is no `httpStatus` field (the closest signals are `lastResult`/`accessState`), and the timestamp is `lastSeenUtc`, not `lastSeenAt`. The response also includes a `navigationGraph`/`graphEdgeCount` projection of links between indexed URLs, omitted above for brevity.

---

## 4. Operational Best Practices

* **Index-First Retrieval:** Before starting an expensive crawl, query `nova.site_urls` to see if the required route is already known in the index.
* **Utility Sorting:** Entries carry a `utilityScore`; `recommendedStartUrls` are Nova's pre-filtered high-value picks, with the rest in `otherCandidates`.
* **Path Prefix Filtering:** Use `pathPrefix` to narrow candidates to specific application sub-trees (e.g. `"/settings"`, `"/dashboard"`).

---

## 5. Related Tools

* [`nova.site_urls_report`](nova-site-urls-report.md) — Update the index with live observations.
* [`nova.crawl_start`](nova-crawl-start.md) — Re-crawl to refresh the index.
