# `nova.scheduled_task_var_list`

Lists persistent variable keys and value previews configured for a task.

---

## 1. Overview

`nova.scheduled_task_var_list` returns a paginated list of all persistent state variables stored for a task, with value previews or full values.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`taskId`** | `string` | Yes | `none` | The task ID. |
| **`includeValues`** | `boolean` | No | `false` | Include full values in response (`false` returns previews only). |
| **`limit`** | `integer` | No | `100` | Maximum variables to return (1-200). |
| **`offset`** | `integer` | No | `0` | Pagination offset. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_var_list",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "includeValues": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded 1 variable for task-7c81a2f0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "variables": [
      {
        "key": "last_scraped_id",
        "value": "10482"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Overview Inspection:** Use `includeValues: false` when scanning tasks with large state dictionaries to save context window tokens.

---

## 5. Related Tools

* [`nova.scheduled_task_var_get`](nova-scheduled-task-var-get.md) — Read single variable.
* [`nova.scheduled_task_var_set`](nova-scheduled-task-var-set.md) — Update variable.
