# `nova.task_promotion_candidates`

Lists guidance log entries and override patterns that are candidates for profile promotion.

---

## 1. Overview

`nova.task_promotion_candidates` surfaces frequently observed workarounds and high-confidence guidance entries that are ready for permanent promotion.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | The profile ID to check for promotion candidates. |
| `threshold` | `integer` | No | `3` | 1–100 | Minimum occurrence count to qualify as candidate. Default: 3. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "{\"profileId\":\"tp-checkout-01\",\"threshold\":3,\"guidanceCandidates\":[...],\"guidanceCandidateCount\":1, ...}"
    }
  ],
  "structuredContent": {
    "profileId": "tp-checkout-01",
    "threshold": 3,
    "guidanceCandidates": [
      {
        "guidanceLogId": "log-guid-401",
        "guidanceKind": "workflow",
        "payload": { "text": "Modal requires clicking backdrop to dismiss." },
        "sourceKind": "agent",
        "occurrenceCount": 4,
        "status": "pending",
        "createdAtUtc": "2026-09-18T09:00:00Z"
      }
    ],
    "guidanceCandidateCount": 1,
    "overrideCandidates": [],
    "overrideCandidateCount": 0
  }
}
```

There is no separate summary sentence: `content[0].text` is the same structured data serialized as plain JSON text. There is no `candidates` or `confidence` field — guidance candidates are listed under `guidanceCandidates` (by `occurrenceCount >= threshold`), and recurring override patterns are listed separately under `overrideCandidates`.

---

## 4. Operational Best Practices

* **Self-Improvement Loop:** Query promotion candidates periodically to elevate discovered solutions into permanent guidance.

---

## 5. Related Tools

* [`nova.task_promote_guidance`](nova-task-promote-guidance.md)
* [`nova.task_guidance_logs`](nova-task-guidance-logs.md)
