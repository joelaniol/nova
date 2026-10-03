# `nova.scheduled_task_trigger`

Manually triggers an immediate run of a scheduled task with optional dynamic inputs.

---

## 1. Overview

`nova.scheduled_task_trigger` starts an out-of-schedule run of a task immediately. The task must be in an enabled state. Callers can supply an optional `inputs` JSON string, which is written to `shared/trigger-inputs.json` inside the task workspace for the executor to consume.

* **Security Tier:** Tier 2 (Task Trigger)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to trigger. |
| `inputs` | `string` | No | — | — | Optional JSON string with dynamic parameters for this run. Written to shared/trigger-inputs.json before the task starts. The task prompt should reference this file. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_trigger",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "inputs": "{\"overrideUrl\": \"https://store.example.com/item/202\", \"forceRefresh\": true}"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Triggered run 'run-8120c' for task task-7c81a2f0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "runId": "run-8120c",
    "status": "Starting",
    "triggeredAtUtc": "2026-10-02T20:30:00Z"
  }
}
```

---

## 4. Operational Best Practices

* **Dynamic Parameter Injection:** Pass runtime options via `inputs` so the background executor can process dynamic targets without reconfiguring the master task.
* **Follow-Up Monitoring:** Monitor stdout and execution progress via [`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md).

---

## 5. Related Tools

* [`nova.scheduled_task_run_output`](nova-scheduled-task-run-output.md) — Read live run logs.
* [`nova.scheduled_task_run_cancel`](nova-scheduled-task-run-cancel.md) — Cancel manual run.
