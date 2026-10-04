# `nova.scheduled_task_disable`

Pauses execution of a scheduled task without modifying its configuration or history.

---

## 1. Overview

`nova.scheduled_task_disable` pauses a scheduled task, cancelling future timer triggers and preventing scheduled runs from executing. Configuration, run history, secrets, and workspace files remain completely preserved.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to disable. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_disable",
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
      "text": "Task 'a1b2c3d4e5f6' disabled."
    }
  ],
  "structuredContent": {
    "taskId": "a1b2c3d4e5f6",
    "enabled": false,
    "circuitBreakerReset": false
  }
}
```

---

## 4. Operational Best Practices

* **Maintenance Windows:** Disable tasks during target system maintenance or deployment windows to avoid false alarm alerts and failed run records.
* **In-Flight Runs:** Disabling a task does not abort a currently executing run; use [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) to cancel active runs.

---

## 5. Related Tools

* [`nova.scheduled_task_enable`](nova-scheduled-task-enable.md) — Resume execution.
* [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) — Abort active run.
