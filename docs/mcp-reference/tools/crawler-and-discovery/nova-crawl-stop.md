# `nova.crawl_stop`

Requests cancellation of an active crawl job, safely draining in-flight workers.

---

## 1. Overview

`nova.crawl_stop` signals the crawl orchestrator to stop scheduling new URLs and gracefully drain active hidden WebView workers. Visited page records and extracted metadata accumulated prior to cancellation remain fully preserved in `crawl.db`.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 2 (Crawl Lifecycle Control)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`crawlId`** | `string` | Yes | `none` | Crawl job ID returned by `nova.crawl_start`. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.crawl_stop",
  "arguments": {
    "crawlId": "crawl-4a92c81e"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cancellation requested for crawl-4a92c81e. Workers are draining."
    }
  ],
  "structuredContent": {
    "ok": true,
    "crawlId": "crawl-4a92c81e",
    "status": "cancelling",
    "visitedPages": 14,
    "remainingQueued": 0
  }
}
```

---

## 4. Operational Best Practices

* **Graceful Drain:** In-flight page fetches will complete before the job transitions from `cancelling` to `stopped`.
* **Preserved Data:** Stopping a crawl does not discard already extracted data; use [`nova.crawl_results`](nova-crawl-results.md) to inspect pages retrieved before stopping.
* **Agent Ownership:** Cancellation must be requested by the same agent ID that initiated the crawl.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Start a crawl job.
* [`nova.crawl_status`](nova-crawl-status.md) — Verify final stopped status.
