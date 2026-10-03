# `nova.crawl_update`

Dynamically modifies parameters (rate limits, filters, depth, pauses) of an active crawl mid-flight.

---

## 1. Overview

`nova.crawl_update` adjusts the operational behavior of a running or paused crawl job without cancelling or restarting it. It allows agents to throttle rate limits, pause execution, change depth boundaries, or update regex patterns on the fly.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 2 (Crawl Control)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`crawlId`** | `string` | Yes | `none` | Crawl job ID returned by `nova.crawl_start`. |
| **`paused`** | `boolean` | No | `null` | Set to `true` to pause scheduling after current pages complete, or `false` to resume. |
| **`pageDelayMs`** | `integer` | No | `null` | Update per-origin minimum delay between page requests in ms. |
| **`maxPages`** | `integer` | No | `null` | Adjust the maximum page cap (applies to future dequeues). |
| **`maxDepth`** | `integer` | No | `null` | Adjust BFS depth limit; queued items exceeding the new depth are pruned. |
| **`parallel`** | `integer` | No | `null` | Adjust number of concurrent hidden WebView workers (1-3). |
| **`urlPattern`** | `string` | No | `null` | Update URL follow regex filter. Pass empty string `""` to clear. |
| **`excludePattern`** | `string` | No | `null` | Update URL exclusion regex filter. Pass empty string `""` to clear. |
| **`settleTimeMs`** | `integer` | No | `null` | Update maximum JS settlement wait time per page. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_update",
  "arguments": {
    "crawlId": "crawl-4a92c81e",
    "pageDelayMs": 1500,
    "maxPages": 40
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Crawl job crawl-4a92c81e updated: pageDelayMs=1500, maxPages=40."
    }
  ],
  "structuredContent": {
    "ok": true,
    "crawlId": "crawl-4a92c81e",
    "pageDelayMs": 1500,
    "maxPages": 40,
    "paused": false
  }
}
```

---

## 4. Operational Best Practices

* **Dynamic Throttling:** If the target server exhibits elevated latency or returns warning headers, increase `pageDelayMs` to reduce server pressure immediately.
* **Selective Scope Expansion:** Increase `maxPages` or `maxDepth` dynamically if initial crawl results indicate high-value sub-paths.
* **Pause for Manual Inspection:** Use `paused: true` to halt scheduling while reviewing intermediate findings in [`nova.crawl_results`](nova-crawl-results.md).

---

## 5. Related Tools

* [`nova.crawl_status`](nova-crawl-status.md) — Monitor crawl progress after updates.
* [`nova.crawl_start`](nova-crawl-start.md) — Initial crawl launcher.
