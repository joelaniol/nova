# `nova.scheduled_task_disable`

Pauses execution of a scheduled task without modifying its configuration or history.

---

## 1. Overview

`nova.scheduled_task_disable` pauses a scheduled task, cancelling future timer triggers and preventing scheduled runs from executing. Configuration, run history, secrets, and workspace files remain completely preserved.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (Task Control)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to disable. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_disable",
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
      "text": "Disabled scheduled task task-7c81a2f0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "status": "Disabled",
    "nextRunUtc": null
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
