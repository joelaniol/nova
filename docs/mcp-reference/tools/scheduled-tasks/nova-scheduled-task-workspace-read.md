# `nova.scheduled_task_workspace_read`

Reads a UTF-8 text file from a task’s shared workspace folder.

---

## 1. Overview

`nova.scheduled_task_workspace_read` reads text content from a file inside the task's `shared/` directory. It returns the complete file string, encoding information, and byte size.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `relativePath` | `string` | Yes | — | — | Path relative to the shared/ directory (e.g. 'latest-report.json', 'result.json'). Only files inside shared/ are accessible. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_workspace_read",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "relativePath": "price.json"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\n  \"sku\": \"101\",\n  \"price\": 49.99,\n  \"currency\": \"USD\",\n  \"timestamp\": \"2026-10-02T20:30:12Z\"\n}"
    }
  ],
  "structuredContent": {
    "taskId": "task-7c81a2f0",
    "relativePath": "price.json",
    "content": "{\n  \"sku\": \"101\",\n  \"price\": 49.99,\n  \"currency\": \"USD\",\n  \"timestamp\": \"2026-10-02T20:30:12Z\"\n}",
    "encoding": "utf-8",
    "bytesRead": 128,
    "size": 128,
    "lastWriteUtc": "2026-10-02T20:30:12Z"
  }
}
```

---

## 4. Operational Best Practices

* **Safe Path Resolution:** Only files inside the task's `shared/` directory can be accessed; attempts to access parent directories fail closed.
* **Size Limit:** Files larger than 1 MB are rejected; read them in pieces via your own logic or shrink the output written to `shared/`.
* **JSON Parsing:** When reading JSON artifacts, parse `structuredContent.content` in your agent workflow to make automated decisions.

---

## 5. Related Tools

* [`nova.scheduled_task_workspace_write`](nova-scheduled-task-workspace-write.md) — Write workspace files.
* [`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md) — List available files.
