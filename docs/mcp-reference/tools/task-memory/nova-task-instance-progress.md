# `nova.task_instance_progress`

Commits progress deltas, completed work units, and observations to a task instance.

---

## 1. Overview

`nova.task_instance_progress` appends completed work units and observations to a task instance using compare-and-set revision concurrency.

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 2 (Progress Commit)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`clientEventId`** | `string` | Yes | `null` | Client-generated unique event ID for idempotency. Duplicate submissions are safely ignored. |
| **`discoveredUnits`** | `array` | No | `null` | New work units discovered during this progress event. |
| **`expectedInstanceRev`** | `integer` | Yes | `null` | Expected current instanceRev for CAS. Reject on mismatch. |
| **`findings`** | `array` | No | `null` | Structured findings appended to the instance event log and counted for distinct-findings completion. |
| **`instanceId`** | `string` | Yes | `null` | The instance to update. |
| **`mandatoryCheckUpdates`** | `array` | No | `null` | Updates to the mandatory-check state machine for this instance. |
| **`note`** | `string` | No | `null` | Optional free-text note for the event log. |
| **`resumeStateDelta`** | `object` | No | `null` | Delta object merged into resumeState so the task can be resumed later. |
| **`setDiscoveryState`** | `string` | No | `null` | Transition discovery state. 'unknown' = discovery has not started or was reset, 'partial' = discovery is in progress and more units may still appear, 'frozen' = discovery is intentionally closed and no further automatic unit discovery is expected. |
| **`unitUpdates`** | `array` | No | `null` | Status updates for already known units. Valid statuses are checked, excluded, blocked, or failed. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_progress",
  "arguments": {
    "instanceId": "inst-881a",
    "expectedInstanceRev": 2,
    "clientEventId": "evt-prog-02",
    "completedUnits": [
      "unit-item-101"
    ],
    "observationDelta": "Audited product 101: no link errors."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Committed progress to inst-881a (new rev: 3)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "instanceId": "inst-881a",
    "newInstanceRev": 3,
    "completedUnitsTotal": 9
  }
}
```

---

## 4. Operational Best Practices

* **Frequent Progress Commits:** Commit progress after every few work units to safeguard against agent disconnects or token budget limits.

---

## 5. Related Tools

* [`nova.task_instance_get`](nova-task-instance-get.md)
* [`nova.task_instance_complete`](nova-task-instance-complete.md)
