# `nova.task_instance_abort`

Ends a task instance without meeting completion conditions (site offline, unsolvable error).

---

## 1. Overview

`nova.task_instance_abort` terminates an episodic task instance when the stated goal cannot be achieved. It records the failure classification and final state.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `instanceId` | `string` | Yes | — | — | The instance to end. |
| `expectedInstanceRev` | `integer` | Yes | — | — | Expected current instanceRev for CAS. |
| `clientEventId` | `string` | Yes | — | — | Client-generated unique event ID for idempotency. |
| `reason` | `string` | Yes | — | — | Why the task cannot be completed. Stored on the instance event log. |
| `outcome` | `string` | No | — | `aborted`, `failed` | aborted (default): stopped on purpose or by an external blocker. failed: attempted and did not work. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "{\"ok\":true,\"status\":\"aborted\",\"previousStatus\":\"active\",\"instanceId\":\"inst-881a\",\"instanceRev\":4,\"evidenceScopeReleased\":false}"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "aborted",
    "previousStatus": "active",
    "instanceId": "inst-881a",
    "instanceRev": 4,
    "evidenceScopeReleased": false
  }
}
```

`status` echoes back the resolved `outcome` (`aborted` or `failed`). `evidenceScopeReleased` is `true` only when the instance had an open evidence scope that this call closed. On a revision conflict the call does not raise an error; it returns `ok: false` with `reasonCode: "rev_conflict"` and the `currentInstanceRev` to retry against.

---

## 4. Operational Best Practices

* **Compare-and-Set Guard:** Always pass `expectedInstanceRev` to prevent clobbering concurrent progress updates.

---

## 5. Related Tools

* [`nova.task_instance_complete`](nova-task-instance-complete.md)
* [`nova.task_instance_progress`](nova-task-instance-progress.md)
