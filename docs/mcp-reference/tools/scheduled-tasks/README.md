# Scheduled Tasks, Cron & Workspaces

Background task automation, cron expressions, file-system watches, task workspaces, and execution logs.

* **Capability Bundle(s):** `scheduled_tasks`
* **Core Architecture Guide:** [Core Features: scheduled-tasks.md](../../../core-features/scheduled-tasks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (25 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md)** | Documented | List all currently in-flight task runs across all tasks. |
| **[`nova.scheduled_task_create`](nova-scheduled-task-create.md)** | Documented | Create a new scheduled task. |
| **[`nova.scheduled_task_delete`](nova-scheduled-task-delete.md)** | Documented | Delete a scheduled task. |
| **[`nova.scheduled_task_disable`](nova-scheduled-task-disable.md)** | Documented | Disable/pause a scheduled task. |
| **[`nova.scheduled_task_enable`](nova-scheduled-task-enable.md)** | Documented | Enable a paused/disabled scheduled task. |
| **[`nova.scheduled_task_export`](nova-scheduled-task-export.md)** | Documented | Export all task definitions as a JSON array. |
| **[`nova.scheduled_task_get`](nova-scheduled-task-get.md)** | Documented | Get full details of a scheduled task: prompt, executor, schedule, chaining config, budget caps, and status. |
| **[`nova.scheduled_task_import`](nova-scheduled-task-import.md)** | Documented | Import task definitions from a JSON array (as produced by nova.scheduled_task_export). |
| **[`nova.scheduled_task_list`](nova-scheduled-task-list.md)** | Documented | List all scheduled tasks with status, next run, last result, chain targets, cumulative cost, and budget cap info. |
| **[`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md)** | Documented | Cancel a currently running task run. |
| **[`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md)** | Documented | Read stdout or stderr output of a run (tail-read, memory-safe for large logs). |
| **[`nova.scheduled_task_runs`](nova-scheduled-task-runs.md)** | Documented | Get the run history of a scheduled task (status, duration, exit code, cost, output summary). |
| **[`nova.scheduled_task_secret_list`](nova-scheduled-task-secret-list.md)** | Documented | List a bounded page of secret key names stored for a task (values are never returned). |
| **[`nova.scheduled_task_secret_set`](nova-scheduled-task-secret-set.md)** | Documented | Store an encrypted secret (API key, token) for a task using Windows DPAPI. |
| **[`nova.scheduled_task_templates`](nova-scheduled-task-templates.md)** | Documented | List available pre-built task templates. |
| **[`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md)** | Documented | Immediately trigger a manual run of a task, outside its regular schedule. |
| **[`nova.scheduled_task_update`](nova-scheduled-task-update.md)** | Documented | Update fields of an existing scheduled task. |
| **[`nova.scheduled_task_var_delete`](nova-scheduled-task-var-delete.md)** | Documented | Delete a persistent variable from a task. |
| **[`nova.scheduled_task_var_get`](nova-scheduled-task-var-get.md)** | Documented | Get a persistent variable value for a task. |
| **[`nova.scheduled_task_var_list`](nova-scheduled-task-var-list.md)** | Documented | List a bounded page of persistent variable keys and value previews for a task. |
| **[`nova.scheduled_task_var_set`](nova-scheduled-task-var-set.md)** | Documented | Set a persistent key-value variable for a task. |
| **[`nova.scheduled_task_workspace`](nova-scheduled-task-workspace.md)** | Documented | Get workspace info for a task: path, bounded shared directory summary, last run status. |
| **[`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md)** | Documented | List a bounded page of files in a task's shared/ workspace directory. |
| **[`nova.scheduled_task_workspace_read`](nova-scheduled-task-workspace-read.md)** | Documented | Read a UTF-8 text file from a task's shared/ workspace. |
| **[`nova.scheduled_task_workspace_write`](nova-scheduled-task-workspace-write.md)** | Documented | Write a file into a task's shared/ directory using atomic writes (temp-file + rename). |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
