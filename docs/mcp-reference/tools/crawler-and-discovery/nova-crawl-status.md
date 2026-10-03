# `nova.crawl_status`

Checks the live progress, active phase, and error metrics of a background crawl job.

---

## 1. Overview

`nova.crawl_status` queries the current operational status of an active or completed crawl job. It provides real-time counts of discovered, visited, failed, and remaining URLs, as well as circuit breaker status and poll hints.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`crawlId`** | `string` | Yes | `none` | Crawl job ID returned by `nova.crawl_start`. |
| **`outputDetail`** | `string` | No | `"full"` | Projection detail: `"minimal"` (counts, status, phase) or `"full"` (includes rate limits, error breakdowns). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "Crawl job crawl-4a92c81e is running: 12/25 pages visited (1 queued, 0 errors)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "crawlId": "crawl-4a92c81e",
    "status": "running",
    "phase": "visiting",
    "visitedPages": 12,
    "queuedPages": 1,
    "discoveredUrls": 38,
    "consecutiveErrors": 0,
    "circuitBreakerOpen": false,
    "pollHintMs": 2000
  }
}
```

---

## 4. Operational Best Practices

* **Respect Poll Hints:** Use the returned `pollHintMs` value to pace status queries and avoid flooding the MCP host.
* **Circuit Breaker Awareness:** If `circuitBreakerOpen: true`, the target server has returned consecutive rate-limit (429) or forbidden (403) responses, and the crawl has been halted to prevent IP blocks.
* **Minimal Projections:** Prefer `outputDetail: "minimal"` when polling in high-frequency monitoring loops.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Initiate a crawl job.
* [`nova.crawl_results`](nova-crawl-results.md) — Fetch data once visited pages accumulate.
* [`nova.crawl_stop`](nova-crawl-stop.md) — Abort an active crawl.
