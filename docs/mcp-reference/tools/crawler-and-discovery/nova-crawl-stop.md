# `nova.crawl_stop`

Requests cancellation of an active crawl job, safely draining in-flight workers.

---

## 1. Overview

`nova.crawl_stop` signals the crawl orchestrator to stop scheduling new URLs and gracefully drain active hidden WebView workers. Visited page records and extracted metadata accumulated prior to cancellation remain fully preserved in `crawl.db`.

* **Core Architecture Guide:** [Autonomous Crawler & URL Discovery](../../../core-features/crawler-and-discovery/crawler/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for crawl ownership checks. Must match the agentId that started the crawl. Defaults to 'default'. |
| `crawlId` | `string` | Yes | — | — | Crawl job ID returned by crawl_start. |

Capability bundle: `crawler_ops` (load it with `nova.tools_bundle(bundle='crawler_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Crawl crawl-4a92c81e cancelling. 14 pages visited so far."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "cancelling",
    "visited": 14,
    "currentUrl": "https://docs.example.com/api/webhooks",
    "phase": "cancelling",
    "pauseRequested": false,
    "finalPageMayStillComplete": true,
    "resultsPending": true,
    "pollAfterMs": 1000,
    "retentionMode": "best_effort",
    "terminalRetentionMinutes": 30,
    "maxRetainedTerminalCrawls": 12,
    "retentionUntilUtc": null,
    "pollUntilStatus": "cancelled",
    "reason": "cancelling"
  }
}
```

The response does not echo `crawlId` (it is only in the `content` text block, not `structuredContent`). There is also no `remainingQueued` field — poll [`nova.crawl_status`](nova-crawl-status.md) and watch `status` reach a terminal value instead.

---

## 4. Operational Best Practices

* **Graceful Drain:** In-flight page fetches will complete before the job transitions from `cancelling` to a terminal status (`cancelled`/`completed`); `finalPageMayStillComplete`/`resultsPending` tell you whether that is still in progress.
* **Preserved Data:** Stopping a crawl does not discard already extracted data; use [`nova.crawl_results`](nova-crawl-results.md) to inspect pages retrieved before stopping.
* **Agent Ownership:** Cancellation must be requested by the same agent ID that initiated the crawl.

---

## 5. Related Tools

* [`nova.crawl_start`](nova-crawl-start.md) — Start a crawl job.
* [`nova.crawl_status`](nova-crawl-status.md) — Verify final stopped status.
