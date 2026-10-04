# `nova.scheduled_task_var_get`

Retrieves the current value of a persistent state variable for a task.

---

## 1. Overview

`nova.scheduled_task_var_get` reads a persistent state variable stored for a task. It returns the exact string value, or `null` if the key does not exist.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `key` | `string` | Yes | — | — | Variable name. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_var_get",
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
      "text": "last_scraped_id = 10482"
    }
  ],
  "structuredContent": {
    "taskId": "task-7c81a2f0",
    "key": "last_scraped_id",
    "found": true,
    "value": "10482"
  }
}
```

---

## 4. Operational Best Practices

* **State Resumption:** Read variables at the beginning of a task run to resume execution from the previous stopping point.
* **Missing Key Handling:** Check `found: false` (`value` is `null` in that case) to initialize state on the first execution run.

---

## 5. Related Tools

* [`nova.scheduled_task_var_set`](nova-scheduled-task-var-set.md) — Set variable value.
* [`nova.scheduled_task_var_delete`](nova-scheduled-task-var-delete.md) — Delete variable.
