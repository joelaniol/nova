# `nova.scheduled_task_workspace_write`

Atomically writes a UTF-8 text file into a task’s shared workspace folder (temp-file + rename).

---

## 1. Overview

`nova.scheduled_task_workspace_write` writes UTF-8 text content into a file located in a task's `shared/` folder. To prevent partial or corrupt reads by concurrent runs, Nova writes to a temporary file first and performs an atomic rename.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (Workspace Write)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID. |
| **`relativePath`** | `string` | Yes | `none` | Path relative to `shared/` (e.g. `"config.json"`, `"inputs/params.json"`). |
| **`content`** | `string` | Yes | `none` | UTF-8 text content to write (max 1 MB). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_workspace_write",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "relativePath": "config.json",
    "content": "{\"alertThreshold\": 50.00, \"notifySlack\": true}"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Atomically wrote config.json (48 bytes) into task-7c81a2f0 workspace."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "relativePath": "config.json",
    "bytesWritten": 48
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Guarantees:** Ensures background tasks never observe partially written files if triggered during a write operation.
* **1 MB Size Limit:** Enforces a 1 MB size limit to ensure efficient IPC and prevent workspace disk saturation.
* **Subdirectory Auto-Creation:** If `relativePath` references a subfolder (e.g. `reports/weekly/summary.txt`), parent directories are created automatically.

---

## 5. Related Tools

* [`nova.scheduled_task_workspace_read`](nova-scheduled-task-workspace-read.md) — Read workspace files.
* [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md) — Trigger run after writing inputs.
