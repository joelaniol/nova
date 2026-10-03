# `nova.task_guidance_logs`

Lists guidance log entries filtered by profile, domain, or guidance kind.

---

## 1. Overview

`nova.task_guidance_logs` queries the guidance observation history to review proposed playbooks, learning traces, and execution anomalies.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`guidanceKind`** | `string` | No | `null` | Filter by kind: style, terminology, scope_rule, workflow, quality, match_telemetry, custom. |
| **`instanceId`** | `string` | No | `null` | Filter by instance ID. |
| **`limit`** | `integer` | No | `50` | Max entries to return. Default: 50. |
| **`profileId`** | `string` | No | `null` | Filter by profile ID. When set, also returns profileLearningStats (instance counts, completionPercent as 0..100, terminalFailureCount, weighted avg match score, accepted/total match telemetry, top overrides). Legacy aliases like completionRate and abortedCount remain for compatibility. |
| **`status`** | `string` | No | `null` | Filter by status: logged, proposed, accepted, rejected, promoted. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_guidance_logs",
  "arguments": {
    "taskProfileId": "tp-checkout-01",
    "limit": 5
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 1 guidance log entry for tp-checkout-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "total": 1,
    "logs": [
      {
        "guidanceLogId": "log-guid-401",
        "guidanceKind": "workaround",
        "text": "Modal requires clicking backdrop..."
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Audit Opportunities:** Inspect logs before promoting hints to master profiles.

---

## 5. Related Tools

* [`nova.task_guidance_log_add`](nova-task-guidance-log-add.md)
* [`nova.task_promotion_candidates`](nova-task-promotion-candidates.md)
