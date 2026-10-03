# Scheduled Tasks, Cron & Workspaces

Background task automation, cron expressions, file-system watches, task workspaces, and execution logs.

* **Core Architecture Guide:** [Core Features: scheduled-tasks.md](../../../core-features/scheduled-tasks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (25 Tools)

Capability bundles of these tools: `scheduled_tasks`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.scheduled_task_active_runs`](nova-scheduled-task-active-runs.md)** | Lists all currently executing task runs across all background tasks. |
| **[`nova.scheduled_task_create`](nova-scheduled-task-create.md)** | Creates a new scheduled task running on cron expressions, intervals, or filesystem change events. |
| **[`nova.scheduled_task_delete`](nova-scheduled-task-delete.md)** | Permanently deletes a scheduled task, its configuration, and associated run history. |
| **[`nova.scheduled_task_disable`](nova-scheduled-task-disable.md)** | Pauses execution of a scheduled task without modifying its configuration or history. |
| **[`nova.scheduled_task_enable`](nova-scheduled-task-enable.md)** | Enables a paused or circuit-broken scheduled task and resets failure counters. |
| **[`nova.scheduled_task_export`](nova-scheduled-task-export.md)** | Exports all scheduled task definitions as a portable JSON array (excluding secrets and history). |
| **[`nova.scheduled_task_get`](nova-scheduled-task-get.md)** | Retrieves full details of a scheduled task including prompt, schedule, chaining, and budget settings. |
| **[`nova.scheduled_task_import`](nova-scheduled-task-import.md)** | Imports scheduled task definitions from a JSON array, creating fresh task IDs and isolated workspaces. |
| **[`nova.scheduled_task_list`](nova-scheduled-task-list.md)** | Lists all scheduled tasks with execution status, next run times, last results, and cumulative costs. |
| **[`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md)** | Cancels an in-flight background task run asynchronously. |
| **[`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md)** | Memory-safe tail reader for stdout and stderr log streams of a specific task run. |
| **[`nova.scheduled_task_runs`](nova-scheduled-task-runs.md)** | Retrieves the run execution history (status, duration, exit code, cost) of a scheduled task. |
| **[`nova.scheduled_task_secret_list`](nova-scheduled-task-secret-list.md)** | Lists registered secret key names for a task without exposing plaintext secret values. |
| **[`nova.scheduled_task_secret_set`](nova-scheduled-task-secret-set.md)** | Stores an encrypted secret (API key, auth token) for a task using Windows DPAPI encryption. |
| **[`nova.scheduled_task_templates`](nova-scheduled-task-templates.md)** | Lists pre-built task templates for common automation scenarios (monitoring, scraping, backups). |
| **[`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md)** | Manually triggers an immediate run of a scheduled task with optional dynamic inputs. |
| **[`nova.scheduled_task_update`](nova-scheduled-task-update.md)** | Updates fields (prompt, schedule, budget, timeouts, chaining) of an existing scheduled task. |
| **[`nova.scheduled_task_var_delete`](nova-scheduled-task-var-delete.md)** | Deletes a persistent state variable from a task. |
| **[`nova.scheduled_task_var_get`](nova-scheduled-task-var-get.md)** | Retrieves the current value of a persistent state variable for a task. |
| **[`nova.scheduled_task_var_list`](nova-scheduled-task-var-list.md)** | Lists persistent variable keys and value previews configured for a task. |
| **[`nova.scheduled_task_var_set`](nova-scheduled-task-var-set.md)** | Sets a persistent key-value state variable for a task that survives across runs. |
| **[`nova.scheduled_task_workspace`](nova-scheduled-task-workspace.md)** | Returns directory metadata, file count, and last run status for a task’s isolated workspace. |
| **[`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md)** | Lists files and subdirectories located within a task’s shared workspace folder. |
| **[`nova.scheduled_task_workspace_read`](nova-scheduled-task-workspace-read.md)** | Reads a UTF-8 text file from a task’s shared workspace folder. |
| **[`nova.scheduled_task_workspace_write`](nova-scheduled-task-workspace-write.md)** | Atomically writes a UTF-8 text file into a task’s shared workspace folder (temp-file + rename). |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
