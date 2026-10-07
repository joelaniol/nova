# `nova.scheduled_task_update`

Updates fields (prompt, schedule, budget, timeouts, chaining) of an existing scheduled task.

---

## 1. Overview

`nova.scheduled_task_update` modifies the configuration of a scheduled task. Only provided fields are updated; omitted fields retain their existing values. Updating the schedule recalculates the next execution timestamp immediately.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to update. |
| `displayName` | `string` | No | — | — | New display name. |
| `prompt` | `string` | No | — | — | New prompt text. |
| `intervalSeconds` | `integer` | No | — | ≥ 60 | New run interval in seconds. Minimum 60. |
| `timeoutSeconds` | `integer` | No | — | — | New timeout in seconds. |
| `maxTurns` | `integer` | No | — | — | New max turns. |
| `maxBudgetUsd` | `number` | No | — | — | New max budget per run in USD. |
| `mcpAccess` | `boolean` | No | — | — | Enable/disable MCP access. |
| `extraSystemPrompt` | `string` | No | — | — | New extra system prompt. |
| `catchUpMissed` | `boolean` | No | — | — | Enable/disable catch-up for missed runs. |
| `cronExpression` | `string` | No | — | — | New schedule expression (e.g. 'daily 08:00'). Set empty string to clear. |
| `timeZoneId` | `string` | No | — | — | New IANA or Windows timezone for cron patterns. Set empty to clear to UTC; invalid identifiers are rejected. |
| `executorKind` | `string` | No | — | `ClaudeCode`, `CodexCli`, `CustomCommand`, `HttpWebhook`, `Shell` | Change executor type. 'CodexCli' runs the prompt through the user's Codex CLI (codex exec). 'Shell' runs the prompt as a PowerShell script (requires the Shell task executor enabled in Settings). |
| `autonomyMode` | `string` | No | — | `Safe`, `Unsafe` | Change permission mode. |
| `command` | `string` | No | — | — | New command/URL for CustomCommand or HttpWebhook. |
| `argsTemplate` | `string` | No | — | — | New argument template. |
| `workingDirectory` | `string` | No | — | — | New working directory. |
| `oneShot` | `boolean` | No | — | — | Toggle one-shot mode. |
| `triggerNextTaskId` | `string` | No | — | — | Task ID to trigger on completion. Empty string to clear. |
| `triggerOnStatus` | `string` | No | — | `Completed`, `Any` | When to trigger: 'Completed' or 'Any'. |
| `triggerConditionKey` | `string` | No | — | — | JSON key in structured_result for conditional chaining. Empty string to clear. |
| `concurrencyPolicy` | `string` | No | — | `Skip`, `Replace` | Overlap behavior: 'Skip' or 'Replace'. |
| `totalBudgetCapUsd` | `number` | No | — | — | Cumulative cost cap (USD). 0 to clear. |
| `watchPath` | `string` | No | — | — | Filesystem watch path. Empty string to clear. |
| `taskProfileId` | `string` | No | — | — | ETM task profile ID. Empty string to clear. |
| `workspaceId` | `string` | No | — | — | Re-bind the task to a different existing terminal workspace (its id). Future run artifacts will live under the new workspace; existing artifacts stay where they are. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_update",
  "arguments": {
    "taskId": "task-7c81a2f0",
    "timeoutSeconds": 240,
    "cronExpression": "daily 10:00"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Task 'task-7c81a2f0' updated. Use nova.scheduled_task_get(taskId='task-7c81a2f0') to verify changes."
    }
  ],
  "structuredContent": {
    "taskId": "task-7c81a2f0",
    "updated": true,
    "nextActions": [
      { "tool": "nova.scheduled_task_get", "args": { "taskId": "task-7c81a2f0" }, "hint": "Verify updated task details" },
      { "tool": "nova.scheduled_task_trigger", "args": { "taskId": "task-7c81a2f0" }, "hint": "Test the updated task immediately" }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Schedule Recalculation:** Changing `cronExpression`, `intervalSeconds`, or `timeZoneId` instantly updates the scheduler without requiring a restart.
* **Clearing Fields:** Supply an empty string `""` to remove optional fields like `triggerNextTaskId` or `watchPath`.

---

## 5. Related Tools

* [`nova.scheduled_task_get`](nova-scheduled-task-get.md) — View updated definition.
* [`nova.scheduled_task_disable`](nova-scheduled-task-disable.md) — Pause task without deleting.
