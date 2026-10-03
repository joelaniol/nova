# `nova.scheduled_task_workspace`

Returns directory metadata, file count, and last run status for a task’s isolated workspace.

---

## 1. Overview

`nova.scheduled_task_workspace` inspects the filesystem container dedicated to a task (`%LOCALAPPDATA%\ScheduledTasks\<taskId>\`). It summarizes total files in the `shared/` folder, storage consumed, and the status of the last completed run.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_workspace",
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
      "text": "Workspace for task-7c81a2f0: 2 shared files (4 KB), last run: Success."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "workspacePath": "ScheduledTasks/task-7c81a2f0",
    "sharedFileCount": 2,
    "sharedBytesTotal": 4096,
    "lastRunStatus": "Success"
  }
}
```

---

## 4. Operational Best Practices

* **Workspace Health:** Check `sharedBytesTotal` to ensure task runs are not accumulating uncompressed logs or excessive output artifacts.
* **File Discovery:** Follow up with [`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md) to inspect file names.

---

## 5. Related Tools

* [`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md) — List files in workspace.
* [`nova.scheduled_task_workspace_read`](nova-scheduled-task-workspace-read.md) — Read file content.
