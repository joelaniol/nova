# `nova.task_instance_abort`

Ends a task instance without meeting completion conditions (site offline, unsolvable error).

---

## 1. Overview

`nova.task_instance_abort` terminates an episodic task instance when the stated goal cannot be achieved. It records the failure classification and final state.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Task Abort)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`clientEventId`** | `string` | Yes | `null` | Client-generated unique event ID for idempotency. |
| **`expectedInstanceRev`** | `integer` | Yes | `null` | Expected current instanceRev for CAS. |
| **`instanceId`** | `string` | Yes | `null` | The instance to end. |
| **`outcome`** | `string` | No | `null` | aborted (default): stopped on purpose or by an external blocker. failed: attempted and did not work. |
| **`reason`** | `string` | Yes | `null` | Why the task cannot be completed. Stored on the instance event log. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_abort",
  "arguments": {
    "instanceId": "inst-881a",
    "expectedInstanceRev": 3,
    "clientEventId": "evt-abort-01",
    "reason": "Target portal in maintenance mode"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Aborted task instance inst-881a: Target portal in maintenance mode."
    }
  ],
  "structuredContent": {
    "ok": true,
    "instanceId": "inst-881a",
    "status": "Aborted",
    "reason": "Target portal in maintenance mode"
  }
}
```

---

## 4. Operational Best Practices

* **Compare-and-Set Guard:** Always pass `expectedInstanceRev` to prevent clobbering concurrent progress updates.

---

## 5. Related Tools

* [`nova.task_instance_complete`](nova-task-instance-complete.md)
* [`nova.task_instance_progress`](nova-task-instance-progress.md)
