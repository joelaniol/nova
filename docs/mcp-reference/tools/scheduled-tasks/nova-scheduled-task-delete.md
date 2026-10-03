# `nova.scheduled_task_delete`

Permanently deletes a scheduled task, its configuration, and associated run history.

---

## 1. Overview

`nova.scheduled_task_delete` removes a scheduled task from the database. It cancels any in-flight runs, cancels scheduled timer events, and cleans up the task's metadata.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 3 (Destructive Task Deletion)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to delete. |
| `cleanupWorkspace` | `boolean` | No | `false` | — | If true, also delete the task's workspace directory. Default: false. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_delete",
  "arguments": {
    "taskId": "task-19e0b44a",
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
      "text": "Deleted scheduled task task-19e0b44a."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-19e0b44a",
    "status": "Deleted"
  }
}
```

---

## 4. Operational Best Practices

* **Export First:** Call [`nova.scheduled_task_export`](nova-scheduled-task-export.md) before batch deletions if you may need to restore configurations later.
* **Active Run Termination:** Deleting a task with an active running process immediately cancels the executor process.

---

## 5. Related Tools

* [`nova.scheduled_task_disable`](nova-scheduled-task-disable.md) — Non-destructive pausing alternative.
* [`nova.scheduled_task_export`](nova-scheduled-task-export.md) — Backup task definitions.
