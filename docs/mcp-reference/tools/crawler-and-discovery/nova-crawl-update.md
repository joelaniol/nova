# `nova.crawl_update`

Dynamically modifies parameters (rate limits, filters, depth, pauses) of an active crawl mid-flight.

---

## 1. Overview

`nova.crawl_update` adjusts the operational behavior of a running or paused crawl job without cancelling or restarting it. It allows agents to throttle rate limits, pause execution, change depth boundaries, or update regex patterns on the fly.

* **Core Architecture Guide:** [Autonomous Crawler & URL Discovery](../../../core-features/crawler-and-discovery/crawler/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for crawl ownership checks. Must match the agentId that started the crawl. Defaults to 'default'. |
| `crawlId` | `string` | Yes | — | — | Crawl job ID returned by crawl_start. |
| `maxPages` | `integer` | No | — | 1–500 | New maximum page count. Out-of-range values are rejected. The new limit applies before the next dequeue; a paused crawl that already visited at least this many pages completes immediately. |
| `maxDepth` | `integer` | No | — | 0–10 | New BFS depth limit. Out-of-range values are rejected. Already-queued items are revalidated against the new limit before they start, but completed pages are not revisited. |
| `pageDelayMs` | `integer` | No | — | 200–5000 | New global minimum spacing in milliseconds between starts on the same origin. Out-of-range values are rejected. The updated value applies before the next not-yet-started URL. |
| `settleTimeMs` | `integer` | No | — | 500–15000 | New maximum JS settlement wait time per page in milliseconds. Out-of-range values are rejected. The updated value applies on the next page load. |
| `parallel` | `integer` | No | — | 1–3 | New maximum hidden-WebView worker count for not-yet-started URLs. Workers above a lowered limit retire after their current page; raising the limit starts additional workers lazily. live_tab remains fixed at 1. |
| `burstSize` | `integer` | No | — | 1–50 | New maximum number of page starts per origin in one burst. Applies before the next not-yet-started URL. |
| `burstDelayMs` | `integer` | No | — | 0–60000 | New minimum pause in milliseconds between bursts on the same origin. 0 disables an extra burst pause while pageDelayMs still applies. |
| `urlPattern` | `string` | No | — | — | New regex filter for URLs to follow. Replaces the original urlPattern. Pass an empty string to clear the filter. Already-queued items are rechecked against the new filter before they start. |
| `excludePattern` | `string` | No | — | — | New regex filter for URLs to exclude. Replaces the original excludePattern. Pass an empty string to clear the filter. Already-queued items are rechecked against the new filter before they start. |
| `paused` | `boolean` | No | — | — | true to request a pause after the current page fully drains; the job remains running until it reaches the pause gate. false resumes a paused crawl. |
| `maxConsecutiveErrors` | `integer` | No | — | 1–50 | Update circuit breaker threshold. After this many consecutive failures on a domain, remaining URLs are skipped. |
| `backoffStrategy` | `string` | No | — | `none`, `linear`, `exponential` | Update adaptive delay strategy. |
| `maxBackoffMs` | `integer` | No | — | 1000–60000 | Update maximum adaptive delay cap in ms. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Crawl crawl-4a92c81e updated: pageDelayMs=1500, maxPages=40. Status: running, visited: 12/40."
    }
  ],
  "structuredContent": {
    "crawlId": "crawl-4a92c81e",
    "status": "running",
    "updated": ["pageDelayMs=1500", "maxPages=40"],
    "effectiveConfig": {
      "maxDepth": 2,
      "maxPages": 40,
      "pageDelayMs": 1500
    },
    "visited": 12,
    "queued": 1,
    "pauseRequested": false,
    "phase": "visiting",
    "parallel": { "configured": 1, "effectiveParallel": 1, "activeWorkers": 1 },
    "pollAfterMs": 2000,
    "retentionMode": "best_effort",
    "terminalRetentionMinutes": 30,
    "maxRetainedTerminalCrawls": 12,
    "retentionUntilUtc": null,
    "currentUrl": "https://docs.example.com/api/webhooks"
  }
}
```

There is no top-level `ok` field. Updated values are not individually echoed as top-level fields — `updated` lists each applied change as a `"name=value"` string, and the full post-update configuration (including unchanged fields) lives under `effectiveConfig` (shown abbreviated above). Calling with no recognized field to change (e.g. an empty arguments object) is rejected as invalid params instead of a no-op success.

---

## 4. Operational Best Practices

* **Dynamic Throttling:** If the target server exhibits elevated latency or returns warning headers, increase `pageDelayMs` to reduce server pressure immediately.
* **Selective Scope Expansion:** Increase `maxPages` or `maxDepth` dynamically if initial crawl results indicate high-value sub-paths.
* **Pause for Manual Inspection:** Use `paused: true` to halt scheduling while reviewing intermediate findings in [`nova.crawl_results`](nova-crawl-results.md); the applied pause state is reflected in `pauseRequested`, not in a `paused` field.

---

## 5. Related Tools

* [`nova.crawl_status`](nova-crawl-status.md) — Monitor crawl progress after updates.
* [`nova.crawl_start`](nova-crawl-start.md) — Initial crawl launcher.
