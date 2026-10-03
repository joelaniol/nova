# `nova.scheduled_task_workspace_read`

Reads a UTF-8 text file from a task’s shared workspace folder.

---

## 1. Overview

`nova.scheduled_task_workspace_read` reads text content from a file inside the task's `shared/` directory. It returns the complete file string, encoding information, and byte size.

* **Security Tier:** Tier 1 (Read-Only)
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
      "text": "Read price.json (128 bytes)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "relativePath": "price.json",
    "byteCount": 128,
    "encoding": "utf-8",
    "content": "{\n  \"sku\": \"101\",\n  \"price\": 49.99,\n  \"currency\": \"USD\",\n  \"timestamp\": \"2026-10-02T20:30:12Z\"\n}"
  }
}
```

---

## 4. Operational Best Practices

* **Safe Path Resolution:** Only files inside the task's `shared/` directory can be accessed; attempts to access parent directories fail closed.
* **JSON Parsing:** When reading JSON artifacts, parse `structuredContent.content` in your agent workflow to make automated decisions.

---

## 5. Related Tools

* [`nova.scheduled_task_workspace_write`](nova-scheduled-task-workspace-write.md) — Write workspace files.
* [`nova.scheduled_task_workspace_list`](nova-scheduled-task-workspace-list.md) — List available files.
