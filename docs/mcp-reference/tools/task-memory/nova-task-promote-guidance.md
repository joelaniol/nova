# `nova.task_promote_guidance`

Explicitly promotes a guidance log entry into a profile’s stable guidance.

---

## 1. Overview

`nova.task_promote_guidance` promotes an observed workaround or tip from `task_guidance_logs` into the permanent `stableGuidance` of a task profile.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Guidance Promotion)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`guidanceLogId`** | `string` | Yes | `null` | The guidance log entry to promote. |
| **`profileId`** | `string` | Yes | `null` | The profile to promote the guidance into. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_promote_guidance",
  "arguments": {
    "guidanceLogId": "log-guid-401",
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
      "text": "Promoted guidance log-guid-401 into profile tp-checkout-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "tp-checkout-01",
    "guidanceLogId": "log-guid-401",
    "status": "Promoted"
  }
}
```

---

## 4. Operational Best Practices

* **Reviewed Learning:** Promotes validated hints into permanent memory for all future subagents.

---

## 5. Related Tools

* [`nova.task_promotion_candidates`](nova-task-promotion-candidates.md)
* [`nova.task_guidance_logs`](nova-task-guidance-logs.md)
