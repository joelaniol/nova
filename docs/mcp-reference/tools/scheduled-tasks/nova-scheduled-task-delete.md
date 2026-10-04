# `nova.scheduled_task_delete`

Permanently deletes a scheduled task, its configuration, and associated run history.

---

## 1. Overview

`nova.scheduled_task_delete` removes a scheduled task and its metadata from the database and wakes the scheduler so no further runs fire. If the task currently has an active run (in the scheduler or still recorded as active in the database), the call is refused with a policy error instead of deleting the task — cancel the run first and wait for it to reach a terminal state.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to delete. |
| `cleanupWorkspace` | `boolean` | No | `false` | — | If true, also delete the task's workspace directory. Default: false. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_delete",
  "arguments": {
    "taskId": "9f3e7d2c08b1",
    "_meta": {
      "intent": "Deprecating legacy daily standup summary task"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Task 'Daily Standup Summary' (9f3e7d2c08b1) deleted."
    }
  ],
  "structuredContent": {
    "taskId": "9f3e7d2c08b1",
    "displayName": "Daily Standup Summary",
    "deleted": true,
    "workspaceRemoved": false
  }
}
```

### Error Response (active run blocks the delete)
```json
{
  "content": [
    {
      "type": "text",
      "text": "Tool blocked by policy: task '9f3e7d2c08b1' has active run(s). Cancel and wait for terminal run state before deleting."
    }
  ],
  "isError": true,
  "structuredContent": {
    "ok": false,
    "errorCode": -32035,
    "message": "Tool blocked by policy: task '9f3e7d2c08b1' has active run(s). Cancel and wait for terminal run state before deleting.",
    "reasonCode": "scheduled_task.active_runs_exist"
  }
}
```

---

## 4. Operational Best Practices

* **Export First:** Call [`nova.scheduled_task_export`](nova-scheduled-task-export.md) before batch deletions if you may need to restore configurations later.
* **Active Run Guard:** Deleting a task with an active run does not force-kill it — the call fails with error `-32035` (`scheduled_task.active_runs_exist`) instead. Cancel the run with [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) and confirm it has stopped before retrying the delete.

---

## 5. Related Tools

* [`nova.scheduled_task_disable`](nova-scheduled-task-disable.md) — Non-destructive pausing alternative.
* [`nova.scheduled_task_export`](nova-scheduled-task-export.md) — Backup task definitions.
