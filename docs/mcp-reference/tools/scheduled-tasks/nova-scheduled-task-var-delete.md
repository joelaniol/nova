# `nova.scheduled_task_var_delete`

Deletes a persistent state variable from a task.

---

## 1. Overview

`nova.scheduled_task_var_delete` removes a key-value variable from a task's persistent SQLite storage.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (State Deletion)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `key` | `string` | Yes | — | — | Variable name to delete. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_var_delete",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "key": "last_scraped_id"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted variable 'last_scraped_id' from task task-7c81a2f0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "key": "last_scraped_id",
    "status": "Deleted"
  }
}
```

---

## 4. Operational Best Practices

* **State Reset:** Delete tracking variables to force a full re-crawl or full initial sync on the next run.

---

## 5. Related Tools

* [`nova.scheduled_task_var_set`](nova-scheduled-task-var-set.md) — Set variable.
* [`nova.scheduled_task_var_list`](nova-scheduled-task-var-list.md) — List variables.
