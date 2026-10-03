# `nova.task_instance_complete`

Requests server evaluation and completion for an episodic task instance.

---

## 1. Overview

`nova.task_instance_complete` evaluates the task instance against its completion condition and mandatory checks. If checks fail or coverage is incomplete, Nova rejects completion (`completed: false`) with specific remediation reasons.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Completion Gate)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`clientEventId`** | `string` | Yes | `null` | Client-generated unique event ID for idempotency. |
| **`completionNote`** | `string` | No | `null` | Legacy alias for note. Prefer note in new calls. |
| **`evidenceReport`** | `array` | No | `null` | Optional evidence from verification contract execution. Each entry is the result of executing a verification step's tool; failed required fast-gate steps can block completion. |
| **`expectedInstanceRev`** | `integer` | Yes | `null` | Expected current instanceRev for CAS. |
| **`instanceId`** | `string` | Yes | `null` | The instance to complete. |
| **`note`** | `string` | No | `null` | Optional note for the completion event. Canonical field for new calls. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_complete",
  "arguments": {
    "instanceId": "inst-881a",
    "expectedInstanceRev": 4,
    "clientEventId": "evt-complete-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Task instance inst-881a successfully completed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "instanceId": "inst-881a",
    "completed": true,
    "status": "Completed",
    "verifiedChecksPassed": true
  }
}
```

---

## 4. Operational Best Practices

* **Server-Enforced Done Criteria:** Nova verifies actual evidence before marking tasks completed; do not claim completion without satisfying all mandatory checks.
* **Handle Rejections:** If `completed: false`, inspect `rejectionReason` and execute missing work units before retrying.

---

## 5. Related Tools

* [`nova.task_instance_verify`](nova-task-instance-verify.md)
* [`nova.task_instance_progress`](nova-task-instance-progress.md)
