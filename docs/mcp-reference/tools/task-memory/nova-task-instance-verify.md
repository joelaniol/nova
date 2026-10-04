# `nova.task_instance_verify`

Retrieves the completion-gate state and, if the task profile defines one, the verification contract steps required for task completion.

---

## 1. Overview

`nova.task_instance_verify` returns the instance's current completion-gate state (`completionVerification`: whether completion is currently allowed, pending mandatory checks, remaining units) and, when the task profile defines a tool-based verification contract (`hasContract: true`), the contract's steps so the agent can execute them and submit evidence via `task_instance_complete`. Most task profiles have no such contract; in that case the response reports `hasContract: false` and still returns `completionVerification`.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `instanceId` | `string` | Yes | — | — | The instance to verify. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.task_instance_verify",
  "arguments": {
    "instanceId": "inst-881a"
  }
}
```

### JSON-RPC Response
```json
{
  "structuredContent": {
    "hasContract": true,
    "instanceId": "inst-881a",
    "stepCount": 1,
    "requiredCount": 1,
    "steps": [
      {
        "stepId": "chk-order-conf",
        "tool": "nova.read_text",
        "args": { "selector": ".confirmation-banner" },
        "description": "Order confirmation banner is visible",
        "gate": "fast",
        "required": true,
        "assertionType": "has_results"
      }
    ],
    "completionVerification": {
      "completionAllowed": false,
      "reasonCode": "pending_mandatory_checks",
      "message": "1 mandatory check(s) pending.",
      "isError": false,
      "status": "active",
      "discoveryState": "discovering",
      "currentState": {
        "totalUnits": 10,
        "checkedUnits": 8,
        "remainingUnits": 2,
        "blockedUnits": 0,
        "failedUnits": 0,
        "urlUnitsRemaining": 2,
        "pendingMandatoryChecks": ["chk-order-conf"]
      }
    },
    "instructions": "Execute each tool with the given args, then submit results via task_instance_complete with evidenceReport array. Each entry: { stepId, state ('passed'|'failed'|'inconclusive'|'skipped'), toolResult (tool response), detail (optional explanation) }. Failed required fast-gate steps can block completion."
  }
}
```

The response also includes a `taskAwareness` object (trimmed here); `content[0].text` is a JSON dump of this same data. `assertionType` is one of `empty_result`, `has_results`, `field_match`, `field_equals`; `gate` is one of `fast`, `deep`, `restricted`. When the profile defines no verification contract, the response is `{ hasContract: false, instanceId, reason: "no_contract", completionVerification, taskAwareness }` instead.

---

## 4. Operational Best Practices

* **Contract Adherence:** Review mandatory checks at task start so you collect necessary evidence during execution.

---

## 5. Related Tools

* [`nova.task_instance_complete`](nova-task-instance-complete.md)
* [`nova.task_profile_get`](nova-task-profile-get.md)
