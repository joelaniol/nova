# `nova.discovery_reset_scope`

Destructively clears all persisted crawl history, results, and URL indexes for a site scope.

---

## 1. Overview

`nova.discovery_reset_scope` purges all stored crawler and surface-exploration artifacts for a domain or canonical origin from `crawl.db`. This includes crawl job histories, extracted page/block records, Site-URL-Index rows, and Surface Explorer state/trigger/transition/artifact rows. It is used when a website undergoes a complete redesign or during clean testing. The reset is refused (`status: "blocked"`) instead of applied while any crawl or exploration run for that scope is still active.

* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Defaults to 'default'. |
| `domain` | `string` | No | — | — | Legacy primary scope query. Accepts a domain, host:port, or origin (for example 'www.example.com', 'www.example.com:8443', or 'https://www.example.com'). Paths, queries, and fragments are invalid. |
| `scopeKey` | `string` | No | — | — | Preferred alias when reusing a persisted crawler scope from crawl_history. Accepts the same host/host:port/origin syntax as domain and must match domain/origin if multiple aliases are provided. |
| `origin` | `string` | No | — | — | Explicit origin-style alias for the reset scope (for example 'https://www.example.com:8443'). Must match domain/scopeKey if multiple aliases are provided. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.discovery_reset_scope",
  "arguments": {
    "domain": "docs.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Discovery reset completed for https://docs.example.com: removed 4 crawl jobs, 120 site URLs, and 0 exploration runs."
    }
  ],
  "structuredContent": {
    "status": "ok",
    "reasonCode": null,
    "queryInput": "docs.example.com",
    "origin": "https://docs.example.com",
    "matchedScopeKeys": ["https://docs.example.com"],
    "matchedOrigins": ["https://docs.example.com"],
    "activeCrawlCount": 0,
    "activeExplorationRunCount": 0,
    "deleted": {
      "crawlJobs": 4,
      "crawlPages": 85,
      "crawlPageBlocks": 310,
      "siteUrls": 120,
      "siteLinks": 240,
      "explorationRuns": 0,
      "surfaceStates": 0,
      "surfaceTriggers": 0,
      "surfaceTransitions": 0,
      "explorationArtifacts": 0,
      "artifactFiles": 0,
      "runtimeCrawlEntries": 0
    }
  }
}
```

There is no top-level `ok` field and no `scopeKey`/`deletedCrawls`/`deletedPageRecords`/`deletedIndexEntries` — the real fields are `status` ("ok" or "blocked"), `origin`, and a `deleted` object with one count per table. If any crawl or exploration run for the scope is still active, the call returns `status: "blocked"` with `reasonCode: "discovery_reset.active_jobs"` and deletes nothing — stop those jobs first.

---

## 4. Operational Best Practices

* **Use with Caution:** This operation is irreversible; historical diff baselines for this scope will be lost.
* **Pre-Redesign Clean Slates:** Recommended after major web application releases or site architecture overhauls to avoid stale route pollution.
* **Domain Scoping:** Only purges data matching the exact scopeKey or domain; other sites in `crawl.db` remain untouched.
* **Active-Job Guard:** If the response comes back with `status: "blocked"`, stop the active crawls/exploration runs reported in `activeCrawlCount`/`activeExplorationRunCount` and retry.

---

## 5. Related Tools

* [`nova.crawl_history`](nova-crawl-history.md) — Inspect history before resetting.
* [`nova.site_urls`](nova-site-urls.md) — Query index state.
