# `nova.scheduled_task_list`

Lists all scheduled tasks with execution status, next run times, last results, and cumulative costs.

---

## 1. Overview

`nova.scheduled_task_list` retrieves an inventory of all configured background tasks. It reports runtime states (`Enabled`, `Paused`, `Disabled`), next scheduled execution timestamps, consecutive failure counts, cumulative costs, and chaining configurations.

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
  "name": "nova.scheduled_task_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 2 scheduled tasks: 1 Enabled, 1 Paused."
    }
  ],
  "structuredContent": {
    "ok": true,
    "totalTasks": 2,
    "tasks": [
      {
        "taskId": "task-7c81a2f0",
        "displayName": "Competitor Price Tracker",
        "status": "Enabled",
        "schedule": "daily 09:00",
        "nextRunUtc": "2026-10-03T07:00:00Z",
        "lastRunStatus": "Success",
        "lastRunDurationMs": 14200,
        "cumulativeCostUsd": 0.12
      },
      {
        "taskId": "task-19e0b44a",
        "displayName": "Daily Standup Summary",
        "status": "Paused",
        "schedule": "daily 18:00",
        "nextRunUtc": null,
        "lastRunStatus": "Success",
        "cumulativeCostUsd": 1.45
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Circuit Breaker Inspection:** If a task shows consecutive failures, check `lastRunStatus` and query [`nova.scheduled_task_runs`](nova-scheduled-task-runs.md) for error logs.
* **Cost Tracking:** Monitor `cumulativeCostUsd` across recurring tasks to verify spend remains within expected limits.

---

## 5. Related Tools

* [`nova.scheduled_task_get`](nova-scheduled-task-get.md) — Inspect complete task definition.
* [`nova.scheduled_task_runs`](nova-scheduled-task-runs.md) — View execution history.
