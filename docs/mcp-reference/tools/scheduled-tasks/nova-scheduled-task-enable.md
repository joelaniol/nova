# `nova.scheduled_task_enable`

Enables a paused or circuit-broken scheduled task and resets failure counters.

---

## 1. Overview

`nova.scheduled_task_enable` resumes automatic scheduling for a task that was previously disabled or tripped by Nova's circuit breaker. It resets the consecutive failure count and schedules the next run based on the task's cron or interval expression.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (Task Control)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID to enable. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_enable",
  "arguments": {
    "taskId": "task-7c81a2f0"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Enabled scheduled task task-7c81a2f0. Circuit breaker reset. Next run: 2026-10-03 09:00 Europe/Berlin."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "status": "Enabled",
    "consecutiveFailures": 0,
    "nextRunUtc": "2026-10-03T07:00:00Z"
  }
}
```

---

## 4. Operational Best Practices

* **Circuit Breaker Recovery:** When a task auto-disables after repeated failures (e.g. 5 consecutive errors), resolve the underlying issue and call `enable` to reset the breaker.
* **Immediate Execution:** If you want the task to run right away upon enabling, follow up with [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md).

---

## 5. Related Tools

* [`nova.scheduled_task_disable`](nova-scheduled-task-disable.md) — Pause execution.
* [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md) — Execute manually.
