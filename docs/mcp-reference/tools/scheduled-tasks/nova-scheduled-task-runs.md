# `nova.scheduled_task_runs`

Retrieves the run execution history (status, duration, exit code, cost) of a scheduled task.

---

## 1. Overview

`nova.scheduled_task_runs` queries the historical executions of a task. It provides status (`Completed`, `Failed`, `TimedOut`, `Cancelled`), execution duration, exit codes, consumed tokens, cost in USD, and structured output summaries.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `limit` | `integer` | No | `10` | 1–100 | Maximum number of runs to return (1-100). Default: 10. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_runs",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "limit": 2
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 2 run records for task task-7c81a2f0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "runs": [
      {
        "runId": "run-8120c",
        "status": "Completed",
        "exitCode": 0,
        "durationMs": 12400,
        "startedAtUtc": "2026-10-02T20:30:00Z",
        "costUsd": 0.04,
        "outputSummary": "Price scraped successfully: $49.99"
      },
      {
        "runId": "run-7019a",
        "status": "Completed",
        "exitCode": 0,
        "durationMs": 11800,
        "startedAtUtc": "2026-10-02T07:00:00Z",
        "costUsd": 0.04,
        "outputSummary": "Price scraped successfully: $54.99"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Failure Diagnosis:** Identify runs with `exitCode != 0` and pass their `runId` to [`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md) with `stream: "stderr"`.
* **Cost Auditing:** Review `costUsd` per run to optimize prompt lengths and agent efficiency.

---

## 5. Related Tools

* [`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md) — Read full logs.
* [`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md) — View currently running jobs.
