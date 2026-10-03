# `nova.scheduled_task_active_runs`

Lists all currently executing task runs across all background tasks.

---

## 1. Overview

`nova.scheduled_task_active_runs` queries the scheduler for all tasks currently executing. It reports process IDs, elapsed execution time, memory usage, and assigned worker slots.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_active_runs",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "1 task run currently active."
    }
  ],
  "structuredContent": {
    "ok": true,
    "activeCount": 1,
    "activeRuns": [
      {
        "runId": "run-8120c",
        "taskId": "task-7c81a2f0",
        "displayName": "Competitor Price Tracker",
        "elapsedSeconds": 45,
        "pid": 14204
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Detect Hung Processes:** Identify runs that have exceeded standard execution times and cancel them using [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md).
* **System Load Verification:** Verify worker concurrency before manually triggering heavy multi-turn tasks.

---

## 5. Related Tools

* [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) — Terminate an active run.
* [`nova.scheduled_task_list`](nova-scheduled-task-list.md) — View all task definitions.
