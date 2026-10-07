# `nova.scheduled_task_enable`

Enables a paused or circuit-broken scheduled task and resets failure counters.

---

## 1. Overview

`nova.scheduled_task_enable` resumes a task that was previously disabled or tripped by Nova's circuit breaker. Enabling a task always resets its consecutive-failure counter to 0, whether or not the circuit breaker was actually tripped; the response's `circuitBreakerReset` flag tells you whether it had been.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to enable. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_enable",
  "arguments": {
    "taskId": "a1b2c3d4e5f6"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Task 'a1b2c3d4e5f6' enabled. Circuit breaker failure count was reset to 0."
    }
  ],
  "structuredContent": {
    "taskId": "a1b2c3d4e5f6",
    "enabled": true,
    "circuitBreakerReset": true
  }
}
```

---

## 4. Operational Best Practices

* **Circuit Breaker Recovery:** When a task auto-disables after repeated failures (5 consecutive errors by default), resolve the underlying issue and call `enable` to reset the breaker.
* **Immediate Execution:** If you want the task to run right away upon enabling, follow up with [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md).

---

## 5. Related Tools

* [`nova.scheduled_task_disable`](nova-scheduled-task-disable.md) — Pause execution.
* [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md) — Execute manually.
