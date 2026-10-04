# `nova.scheduled_task_var_list`

Lists persistent variable keys and value previews configured for a task.

---

## 1. Overview

`nova.scheduled_task_var_list` returns a paginated list of all persistent state variables stored for a task, with value previews or full values.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID. |
| `limit` | `integer` | No | `100` | 1–200 | Maximum variables to return (1-200). Default: 100. |
| `offset` | `integer` | No | `0` | ≥ 0 | Number of variables to skip before returning this page. Default: 0. |
| `includeValues` | `boolean` | No | `false` | — | Include full values for the returned page. Default: false; use var_get for a single full value. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "last_scraped_id = 10482"
    }
  ],
  "structuredContent": {
    "taskId": "task-7c81a2f0",
    "totalCount": 1,
    "returnedCount": 1,
    "limit": 100,
    "offset": 0,
    "truncated": false,
    "nextOffset": null,
    "includeValues": true,
    "variables": [
      {
        "key": "last_scraped_id",
        "valueLength": 5,
        "valuePreview": "10482",
        "valueTruncated": false,
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
