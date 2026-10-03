# `nova.task_instance_complete`

Requests server evaluation and completion for an episodic task instance.

---

## 1. Overview

`nova.task_instance_complete` evaluates the task instance against its completion condition and mandatory checks. If checks fail or coverage is incomplete, Nova rejects completion (`completed: false`) with specific remediation reasons.

* **Security Tier:** Tier 2 (Completion Gate)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `instanceId` | `string` | Yes | — | — | The instance to complete. |
| `expectedInstanceRev` | `integer` | Yes | — | — | Expected current instanceRev for CAS. |
| `clientEventId` | `string` | Yes | — | — | Client-generated unique event ID for idempotency. |
| `note` | `string` | No | — | — | Optional note for the completion event. Canonical field for new calls. |
| `completionNote` | `string` | No | — | — | Legacy alias for note. Prefer note in new calls. |
| `evidenceReport` | `array` of `object` | No | — | — | Optional evidence from verification contract execution. Each entry is the result of executing a verification step's tool; failed required fast-gate steps can block completion. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
<!-- /generated:parameters -->

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
