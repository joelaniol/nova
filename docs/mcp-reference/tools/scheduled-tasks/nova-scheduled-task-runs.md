# `nova.scheduled_task_runs`

Retrieves the run execution history (status, duration, exit code, cost) of a scheduled task.

---

## 1. Overview

`nova.scheduled_task_runs` queries the historical executions of a task, most recent first. It reports each run's trigger kind (`Scheduled`, `Manual`, `CatchUp`, `FileWatch`), status (`Completed`, `Failed`, `Timeout`, `MaxTurns`, `MaxBudget`, `Cancelled`, `Missed`, `SkippedOverlap`, and other terminal states), duration, exit code, cost in USD, turn count, and an output summary, plus whether a structured result is available.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `limit` | `integer` | No | `10` | 1–100 | Maximum number of runs to return (1-100). Default: 10. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_runs",
  "arguments": {
    "taskId": "a1b2c3d4e5f6",
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
      "text": "2 run(s) for task 'a1b2c3d4e5f6'. Use nova.scheduled_task_run_output(runId='<runId>') to read stdout/stderr of a specific run."
    }
  ],
  "structuredContent": {
    "taskId": "a1b2c3d4e5f6",
    "runs": [
      {
        "runId": "8f14e45fceea167a5a36dedd4bea2543",
        "triggerKind": "Scheduled",
        "status": "Completed",
        "startedAtUtc": "2026-10-02T20:30:00Z",
        "finishedAtUtc": "2026-10-02T20:30:12Z",
        "durationMs": 12400,
        "exitCode": 0,
        "outputSummary": "Price scraped successfully: $49.99",
        "totalCostUsd": 0.04,
        "turnCount": 3,
        "hasStructuredResult": false
      },
      {
        "runId": "b2d4f6a8c1e39074523618900abcdef",
        "triggerKind": "Scheduled",
        "status": "Completed",
        "startedAtUtc": "2026-10-02T07:00:00Z",
        "finishedAtUtc": "2026-10-02T07:00:11Z",
        "durationMs": 11800,
        "exitCode": 0,
        "outputSummary": "Price scraped successfully: $54.99",
        "totalCostUsd": 0.04,
        "turnCount": 3,
        "hasStructuredResult": false
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Failure Diagnosis:** Identify runs with `exitCode != 0` and pass their `runId` to [`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md) with `stream: "stderr"`.
* **Cost Auditing:** Review `totalCostUsd` per run to optimize prompt lengths and agent efficiency.

---

## 5. Related Tools

* [`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md) — Read full logs.
* [`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md) — View currently running jobs.
