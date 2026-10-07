# `nova.scheduled_task_active_runs`

Lists all currently executing task runs across all background tasks.

---

## 1. Overview

`nova.scheduled_task_active_runs` queries the scheduler for all task runs currently executing, returning each run's run ID and the ID of the task it belongs to. If the scheduler engine is not running, it reports zero active runs and `engineRunning: false` rather than an error.

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
      "text": "1 active run(s). Use nova.scheduled_task_run_cancel(runId='<runId>') to stop a run."
    }
  ],
  "structuredContent": {
    "activeRuns": [
      {
        "runId": "8f14e45fceea167a5a36dedd4bea2543",
        "taskId": "a1b2c3d4e5f6"
      }
    ],
    "engineRunning": true
  }
}
```

---

## 4. Operational Best Practices

* **Find a Stuck Run's ID:** Use this tool to get the `runId` of a task that appears stuck, then pass it to [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) to stop it.
* **Engine Health Check:** `engineRunning: false` means the scheduler engine itself is not running (so no task will fire until it is), not just that there are no active runs.

---

## 5. Related Tools

* [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) — Terminate an active run.
* [`nova.scheduled_task_list`](nova-scheduled-task-list.md) — View all task definitions.
