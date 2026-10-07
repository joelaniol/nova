# `nova.crawl_status`

Checks the live progress, active phase, and error metrics of a background crawl job.

---

## 1. Overview

`nova.crawl_status` queries the current operational status of an active or completed crawl job. It provides real-time counts of discovered, visited, failed, and remaining URLs, as well as circuit breaker status and poll hints.

* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for crawl ownership checks. Must match the agentId that started the crawl. Defaults to 'default'. |
| `crawlId` | `string` | Yes | — | — | Crawl job ID returned by crawl_start. |
| `outputDetail` | `string` | No | `"full"` | `minimal`, `summary`, `full` | Status projection. 'minimal' keeps state/counts/watermarks/phase/error/poll and compact rate control. 'summary' adds compact config and session/readiness/script counters without raw customScript. 'full' preserves complete config and diagnostics. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_status",
  "arguments": {
    "crawlId": "crawl-4a92c81e",
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
      "text": "Crawl crawl-4a92c81e: running — 12 visited, 1 queued, 0 failed"
    }
  ],
  "structuredContent": {
    "crawlId": "crawl-4a92c81e",
    "status": "running",
    "crawlKind": "bfs",
    "crawlMode": "hidden",
    "ownerAgentId": "default",
    "visited": 12,
    "queued": 1,
    "failed": 0,
    "elapsedMs": 18400,
    "resultsComplete": false,
    "pauseRequested": false,
    "challengeHold": null,
    "phase": "visiting",
    "pollAfterMs": 2000,
    "resultCount": 12,
    "latestSequence": 12,
    "lastResultAtUtc": "2026-10-02T18:34:50Z",
    "currentUrl": "https://docs.example.com/api/webhooks",
    "error": null,
    "rateControl": {
      "scope": "origin",
      "configuredParallel": 1,
      "effectiveParallel": 1,
      "pageDelayMs": 500,
      "backoffActiveOrigins": 0,
      "throttledUrls": 0
    },
    "research": null
  }
}
```

There is no top-level `ok` field, and the real field names are `visited`/`queued`/`failed`, not `visitedPages`/`queuedPages`/`consecutiveErrors`; there is no `discoveredUrls` or scalar `circuitBreakerOpen` field. Per-origin circuit-breaker state lives inside `health.domains[host].circuitBroken` (only present with `outputDetail: "full"`, where this tool also returns `health`, `config`, `robotsTxt`, `sitemap`, and more); with the default/`minimal` detail shown above, use `rateControl.backoffActiveOrigins` (count of origins currently backing off) as the lightweight signal instead.

---

## 4. Operational Best Practices

* **Respect Poll Hints:** Use the returned `pollAfterMs` value to pace status queries and avoid flooding the MCP host.
* **Circuit Breaker Awareness:** A nonzero `rateControl.backoffActiveOrigins` means at least one origin is currently backing off after errors; request `outputDetail: "full"` and inspect `health.domains[host].circuitBroken` for the per-domain detail.
* **Minimal Projections:** Prefer `outputDetail: "minimal"` when polling in high-frequency monitoring loops.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Initiate a crawl job.
* [`nova.crawl_results`](nova-crawl-results.md) — Fetch data once visited pages accumulate.
* [`nova.crawl_stop`](nova-crawl-stop.md) — Abort an active crawl.
