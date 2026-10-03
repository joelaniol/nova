# `nova.scheduled_task_workspace_write`

Atomically writes a UTF-8 text file into a task’s shared workspace folder (temp-file + rename).

---

## 1. Overview

`nova.scheduled_task_workspace_write` writes UTF-8 text content into a file located in a task's `shared/` folder. To prevent partial or corrupt reads by concurrent runs, Nova writes to a temporary file first and performs an atomic rename.

* **Security Tier:** Tier 2 (Workspace Write)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `relativePath` | `string` | Yes | — | — | Path relative to the shared/ directory (e.g. 'config.json'). |
| `content` | `string` | Yes | — | — | File content to write (UTF-8 text). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
<!-- /generated:parameters -->

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
