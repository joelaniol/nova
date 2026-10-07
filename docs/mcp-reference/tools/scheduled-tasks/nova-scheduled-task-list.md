# `nova.scheduled_task_list`

Lists all scheduled tasks with enabled state, next run time, last result, and cumulative cost.

---

## 1. Overview

`nova.scheduled_task_list` retrieves an inventory of all configured background tasks. Each entry reports whether the task is enabled, its next scheduled fire time, the last run's status, the consecutive-failure count against the circuit-breaker threshold (and whether it has tripped), total run count, cumulative cost, budget cap, and any chained follow-up task. There is no separate "Paused" state — a task is either `enabled: true` or `enabled: false`.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "2 scheduled task(s)."
    }
  ],
  "structuredContent": {
    "tasks": [
      {
        "taskId": "a1b2c3d4e5f6",
        "displayName": "Competitor Price Tracker",
        "executorKind": "ClaudeCode",
        "enabled": true,
        "nextFireAtUtc": "2026-10-03T07:00:00Z",
        "lastRunStatus": "Completed",
        "lastRunFinishedAtUtc": "2026-10-02T07:00:12Z",
        "consecutiveFailureCount": 0,
        "maxConsecutiveFailures": 5,
        "circuitBreakerTripped": false,
        "totalRunCount": 14,
        "cumulativeCostUsd": 0.56,
        "totalBudgetCapUsd": null,
        "triggerNextTaskId": null,
        "triggerNextTaskDisplayName": null
      },
      {
        "taskId": "9f3e7d2c08b1",
        "displayName": "Daily Standup Summary",
        "executorKind": "ClaudeCode",
        "enabled": false,
        "nextFireAtUtc": null,
        "lastRunStatus": "Completed",
        "lastRunFinishedAtUtc": "2026-09-30T18:00:05Z",
        "consecutiveFailureCount": 0,
        "maxConsecutiveFailures": 5,
        "circuitBreakerTripped": false,
        "totalRunCount": 30,
        "cumulativeCostUsd": 1.45,
        "totalBudgetCapUsd": null,
        "triggerNextTaskId": null,
        "triggerNextTaskDisplayName": null
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Circuit Breaker Inspection:** If `circuitBreakerTripped` is true, query [`nova.scheduled_task_runs`](nova-scheduled-task-runs.md) for the failing run's error output.
* **Cost Tracking:** Monitor `cumulativeCostUsd` across recurring tasks to verify spend remains within expected limits.

---

## 5. Related Tools

* [`nova.scheduled_task_get`](nova-scheduled-task-get.md) — Inspect complete task definition.
* [`nova.scheduled_task_runs`](nova-scheduled-task-runs.md) — View execution history.
