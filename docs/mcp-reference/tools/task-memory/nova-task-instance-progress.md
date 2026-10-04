# `nova.task_instance_progress`

Commits progress deltas, completed work units, and observations to a task instance.

---

## 1. Overview

`nova.task_instance_progress` records one progress event for a task instance: newly discovered work units (`discoveredUnits`), status changes of known units (`unitUpdates`: `checked`, `excluded`, `blocked`, `failed`), findings, mandatory-check updates, a resume-state delta and an optional discovery-state transition. Writes use compare-and-set on `expectedInstanceRev`: on a mismatch nothing is written and the result is `applied: false, reason: "rev_conflict"` with the current revision. `clientEventId` makes the call idempotent; a repeated event returns `duplicate: true`. Instances in a terminal status (`completed`, `aborted`, `failed`) are not changed (`reason: "terminal_status"`).

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_progress",
  "arguments": {
    "instanceId": "c81f2a6e0d4b4f9a9e3c7b1d5a2f8e60",
    "expectedInstanceRev": 2,
    "clientEventId": "evt-prog-02",
    "unitUpdates": [
      { "unitKey": "https://shop.example.com/products/101", "status": "checked" }
    ],
    "setDiscoveryState": "frozen",
    "note": "Audited product 101: no link errors."
  }
}
```

### JSON-RPC Response

The text block carries the same object as `structuredContent`, serialized as JSON.

```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"applied\":true,\"instanceRev\":3,\"progress\":{\"totalUnits\":10,\"checkedUnits\":10,\"remainingUnits\":0,\"blockedUnits\":0,\"failedUnits\":0,\"discovered\":10,\"checked\":10,\"remaining\":0,\"blocked\":0,\"failed\":0,\"percentComplete\":100},\"completionAllowed\":true,\"hint\":\"Completion policy satisfied. You may call task_instance_complete.\"}"
    }
  ],
  "structuredContent": {
    "applied": true,
    "instanceRev": 3,
    "progress": {
      "totalUnits": 10,
      "checkedUnits": 10,
      "remainingUnits": 0,
      "blockedUnits": 0,
      "failedUnits": 0,
      "discovered": 10,
      "checked": 10,
      "remaining": 0,
      "blocked": 0,
      "failed": 0,
      "percentComplete": 100
    },
    "completionAllowed": true,
    "hint": "Completion policy satisfied. You may call task_instance_complete."
  }
}
```

When the completion policy is not yet met, `completionAllowed` is `false` and `hint` says what is still missing.

---

## 4. Operational Best Practices

* **Frequent progress commits:** Commit progress after every few work units so a disconnect or a lost session does not lose finished work.
* **Use the returned revision:** Pass the returned `instanceRev` as `expectedInstanceRev` in the next call; on `rev_conflict` re-read the instance with `nova.task_instance_get` before retrying.

---

## 5. Related Tools

* [`nova.task_instance_get`](nova-task-instance-get.md)
* [`nova.task_instance_complete`](nova-task-instance-complete.md)
