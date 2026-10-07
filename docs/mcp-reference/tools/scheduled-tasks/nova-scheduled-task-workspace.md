# `nova.scheduled_task_workspace`

Returns the task's workspace paths, a page of its shared files, and the status of its last run.

---

## 1. Overview

`nova.scheduled_task_workspace` inspects the folder dedicated to a task. Each task is bound to a terminal workspace (by default a dedicated one Nova creates), and its files live under that workspace's `nova-tasks/<taskId>/` subtree with a `shared/` folder for agent-visible output. The tool returns the workspace and shared-folder paths, up to 25 files from `shared/` (paginated), and the status of the task's last run.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Workspace for task 'task-7c81a2f0': C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Workspaces\\<workspaceId>\\nova-tasks\\task-7c81a2f0"
    }
  ],
  "structuredContent": {
    "taskId": "task-7c81a2f0",
    "workspaceId": "<workspaceId>",
    "path": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Workspaces\\<workspaceId>\\nova-tasks\\task-7c81a2f0",
    "sharedPath": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Workspaces\\<workspaceId>\\nova-tasks\\task-7c81a2f0\\shared",
    "exists": true,
    "lastRunId": "run-8120c",
    "lastRunStatus": "Completed",
    "sharedFiles": [
      { "name": "price.json", "isDirectory": false, "size": 128, "lastWriteUtc": "2026-10-02T20:30:12Z" }
    ],
    "sharedFilesTruncated": false,
    "sharedFilesNextOffset": null
  }
}
```

---

## 4. Operational Best Practices

* **Workspace Health:** `sharedFiles` returns up to 25 entries from `shared/`; a `sharedFilesTruncated: true` means the folder holds more — follow up with `nova.scheduled_task_workspace_list` (which pages through all entries) to see the rest.
* **File Discovery:** Follow up with [`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md) to inspect file names and sizes individually.

---

## 5. Related Tools

* [`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md) — List files in workspace.
* [`nova.scheduled_task_workspace_read`](nova-scheduled-task-workspace-read.md) — Read file content.
