# `nova.task_instance_verify`

Retrieves the verification contract steps, assertions, and checks required for task completion.

---

## 1. Overview

`nova.task_instance_verify` returns the exact verification checks required by the instance's task profile (mandatory assertions, screenshot proofs, URL coverage minimums).

* **Capability Bundle:** `task_memory`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/etm-and-task-memory.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`instanceId`** | `string` | Yes | `null` | The instance to verify. |

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
  "content": [
    {
      "type": "text",
      "text": "Loaded verification contract for inst-881a: 2 mandatory checks."
    }
  ],
  "structuredContent": {
    "ok": true,
    "instanceId": "inst-881a",
    "mandatoryChecks": [
      {
        "checkId": "chk-order-conf",
        "assertion": "confirmation-banner is visible"
      },
      {
        "checkId": "chk-tuc-100",
        "assertion": "100% URL coverage"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Contract Adherence:** Review mandatory checks at task start so you collect necessary evidence during execution.

---

## 5. Related Tools

* [`nova.task_instance_complete`](nova-task-instance-complete.md)
* [`nova.task_profile_get`](nova-task-profile-get.md)
