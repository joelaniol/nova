# `nova.memory_stats`

Reports memory engine metrics, commit rates, verification health, and outbox queues.

---

## 1. Overview

`nova.memory_stats` reads health and performance metrics from Nova's cognitive memory subsystem: candidate intake, verification rates, curation quality, and outbox sync status.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `windowHours` | `integer` | No | `24` | — | Lookback window in hours for windowed metrics (1-720). Default 24. |
| `topComponents` | `integer` | No | `8` | — | Top LCJ components to include (1-20). Default 8. |
| `maxSkipReasons` | `integer` | No | `8` | — | Skip reason buckets to include (1-20). Default 8. |
| `topRoutes` | `integer` | No | `8` | — | Top scroll_smart routes to include (1-20). Default 8. |
| `topHosts` | `integer` | No | `8` | — | Top scroll_smart hosts to include (1-20). Default 8. |
| `topSelectors` | `integer` | No | `8` | — | Top scroll_smart selector candidates to include (1-20). Default 8. |
| `componentFilter` | `string` | No | — | — | Optional LCJ component filter. When set, LCJ candidate/curation aggregates are scoped to this component only (e.g. 'evm'). |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.memory_stats",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Memory health: 98% verification rate, 0 outbox pending."
    }
  ],
  "structuredContent": {
    "ok": true,
    "totalMemories": 148,
    "candidatesPending": 3,
    "verificationRate": 0.98,
    "outboxPending": 0
  }
}
```

---

## 4. Operational Best Practices

* **System Diagnostics:** Inspect during long benchmark runs to verify that memory curation is running properly.

---

## 5. Related Tools

* [`nova.memory_recall`](nova-memory-recall.md)
* [`nova.memory_add_candidate`](nova-memory-add-candidate.md)
