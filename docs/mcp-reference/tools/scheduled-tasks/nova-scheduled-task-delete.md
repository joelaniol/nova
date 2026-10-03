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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID to delete. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. High-impact requires `_meta.intent`. |

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
