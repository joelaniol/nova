# `nova.scheduled_task_run_cancel`

Requests cancellation of an in-flight background task run asynchronously.

---

## 1. Overview

`nova.scheduled_task_run_cancel` sends a cancellation request for the given run. Cancellation is asynchronous and not guaranteed to be instantaneous — the response reports whether the request was delivered, not whether the run has actually stopped; poll [`nova.scheduled_task_runs`](nova-scheduled-task-runs.md) or [`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md) to confirm the run reaches a `Cancelled` state. Calling it on a run that already finished, or on an active run this engine instance cannot reach, returns `cancelled: false` with a `reason` explaining why instead of an error.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `runId` | `string` | Yes | — | — | ID of the run to cancel. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_run_cancel",
  "arguments": {
    "runId": "8f14e45fceea167a5a36dedd4bea2543"
  }
}
```

### JSON-RPC Response (cancellation delivered)
```json
{
  "content": [
    {
      "type": "text",
      "text": "Cancellation requested for run '8f14e45fceea167a5a36dedd4bea2543'. Poll to confirm the run reaches Cancelled."
    }
  ],
  "structuredContent": {
    "runId": "8f14e45fceea167a5a36dedd4bea2543",
    "taskId": "a1b2c3d4e5f6",
    "cancelled": false,
    "cancelRequested": true,
    "reason": "cancel_requested_delivered",
    "status": "Running",
    "polling": {
      "hint": "Cancellation is asynchronous. Poll to confirm the run has stopped.",
      "tool": "nova.scheduled_task_runs",
      "suggestedIntervalMs": 3000
    }
  }
}
```

### JSON-RPC Response (run already finished)
```json
{
  "content": [
    {
      "type": "text",
      "text": "Run '8f14e45fceea167a5a36dedd4bea2543' already finished with status Completed. Cannot cancel."
    }
  ],
  "structuredContent": {
    "runId": "8f14e45fceea167a5a36dedd4bea2543",
    "taskId": "a1b2c3d4e5f6",
    "cancelled": false,
    "cancelRequested": false,
    "reason": "already_finished",
    "status": "Completed",
    "polling": null
  }
}
```

---

## 4. Operational Best Practices

* **Asynchronous Drain:** Cancellation is non-blocking; verify termination by polling [`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md) or `nova.scheduled_task_runs`, not by trusting `cancelRequested: true` alone.
* **Unknown runId:** Passing a `runId` the scheduler has no record of at all is an invalid-params error, distinct from the `already_finished` / `not_owned` outcomes above.

---

## 5. Related Tools

* [`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md) — Check active runs.
* [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md) — Start a run.
