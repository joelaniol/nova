# `nova.task_promotion_candidates`

Lists guidance log entries and override patterns that are candidates for profile promotion.

---

## 1. Overview

`nova.task_promotion_candidates` surfaces frequently observed workarounds and high-confidence guidance entries that are ready for permanent promotion.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`profileId`** | `string` | Yes | `null` | The profile ID to check for promotion candidates. |
| **`threshold`** | `integer` | No | `3` | Minimum occurrence count to qualify as candidate. Default: 3. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_promotion_candidates",
  "arguments": {
    "profileId": "tp-checkout-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 guidance promotion candidate for tp-checkout-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "tp-checkout-01",
    "candidates": [
      {
        "guidanceLogId": "log-guid-401",
        "text": "Modal requires clicking backdrop...",
        "confidence": 0.92
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Self-Improvement Loop:** Query promotion candidates periodically to elevate discovered solutions into permanent guidance.

---

## 5. Related Tools

* [`nova.task_promote_guidance`](nova-task-promote-guidance.md)
* [`nova.task_guidance_logs`](nova-task-guidance-logs.md)
