# `nova.scheduled_task_var_get`

Retrieves the current value of a persistent state variable for a task.

---

## 1. Overview

`nova.scheduled_task_var_get` reads a persistent state variable stored for a task. It returns the exact string value, or `null` if the key does not exist.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID. |
| **`key`** | `string` | Yes | `none` | Variable name to retrieve. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
    "ok": true,
    "taskId": "task-7c81a2f0",
    "key": "last_scraped_id",
    "value": "10482"
  }
}
```

---

## 4. Operational Best Practices

* **State Resumption:** Read variables at the beginning of a task run to resume execution from the previous stopping point.
* **Missing Key Handling:** Check for `value: null` to initialize state on the first execution run.

---

## 5. Related Tools

* [`nova.scheduled_task_var_set`](nova-scheduled-task-var-set.md) — Set variable value.
* [`nova.scheduled_task_var_delete`](nova-scheduled-task-var-delete.md) — Delete variable.
