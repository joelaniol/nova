# `nova.task_instance_progress`

Commits progress deltas, completed work units, and observations to a task instance.

---

## 1. Overview

`nova.task_instance_progress` appends completed work units and observations to a task instance using compare-and-set revision concurrency.

* **Security Tier:** Tier 2 (Progress Commit)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `instanceId` | `string` | Yes | — | — | The instance to update. |
| `expectedInstanceRev` | `integer` | Yes | — | — | Expected current instanceRev for CAS. Reject on mismatch. |
| `clientEventId` | `string` | Yes | — | — | Client-generated unique event ID for idempotency. Duplicate submissions are safely ignored. |
| `discoveredUnits` | `array` of `object` | No | — | — | New work units discovered during this progress event. |
| `unitUpdates` | `array` of `object` | No | — | — | Status updates for already known units. Valid statuses are checked, excluded, blocked, or failed. |
| `findings` | `array` of `object` | No | — | — | Structured findings appended to the instance event log and counted for distinct-findings completion. |
| `mandatoryCheckUpdates` | `array` of `object` | No | — | — | Updates to the mandatory-check state machine for this instance. |
| `resumeStateDelta` | `object` | No | — | — | Delta object merged into resumeState so the task can be resumed later. |
| `resumeStateDelta.cursor` | `string` | No | — | — | Optional opaque pagination or resume cursor. |
| `resumeStateDelta.lastProcessedUrl` | `string` | No | — | — | Optional last URL or page reference processed before the task paused. |
| `resumeStateDelta.lastAction` | `string` | No | — | — | Optional last significant action taken before resume. |
| `resumeStateDelta.checkpoint` | `string` | No | — | — | Optional named checkpoint label for operator-facing resumes. |
| `setDiscoveryState` | `string` | No | — | `unknown`, `partial`, `frozen` | Transition discovery state. 'unknown' = discovery has not started or was reset, 'partial' = discovery is in progress and more units may still appear, 'frozen' = discovery is intentionally closed and no further automatic unit discovery is expected. |
| `note` | `string` | No | — | — | Optional free-text note for the event log. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
<!-- /generated:parameters -->

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
