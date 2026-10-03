# `nova.scheduled_task_create`

Creates a new scheduled task running on cron expressions, intervals, or filesystem change events.

---

## 1. Overview

`nova.scheduled_task_create` registers an automated background task with Nova's scheduling engine. Tasks execute unattended according to cron patterns, fixed intervals, or folder change watches.

Supported executors include `ClaudeCode`, `CodexCli`, `Shell` (PowerShell 7), `CustomCommand`, and `HttpWebhook`. Tasks run in dedicated sandboxed workspaces with isolated SQLite state, atomic file sharing, and encrypted DPAPI secret storage.

* **Capability Bundle:** `scheduled_tasks`
* **Security Tier:** Tier 2 (Background Automation)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`displayName`** | `string` | Yes | `none` | Human-readable name for the task. |
| **`prompt`** | `string` | Yes | `none` | Task instruction prompt or shell script to execute. |
| **`executorKind`** | `string` | No | `"ClaudeCode"` | Executor engine: `"ClaudeCode"`, `"CodexCli"`, `"Shell"`, `"CustomCommand"`, or `"HttpWebhook"`. |
| **`cronExpression`** | `string` | No | `null` | Schedule expression (e.g. `"daily 08:00"`, `"every 2 hours"`, or standard 5-part cron `"0 8 * * *"`). |
| **`intervalSeconds`** | `integer` | No | `null` | Interval in seconds between runs (minimum 60s). Optional if cronExpression is provided. |
| **`timeZoneId`** | `string` | No | `"UTC"` | IANA or Windows timezone (e.g. `"Europe/Berlin"`, `"America/New_York"`). |
| **`watchPath`** | `string` | No | `null` | Directory path to monitor; file changes trigger an immediate run (2s debounce). |
| **`mcpAccess`** | `boolean` | No | `false` | Grants the task execution process MCP access to Nova tools. |
| **`timeoutSeconds`** | `integer` | No | `300` | Maximum run duration in seconds before termination (default 5 min). |
| **`oneShot`** | `boolean` | No | `false` | If true, auto-disables after first successful completion. |
| **`catchUpMissed`** | `boolean` | No | `true` | Catch up on missed executions if the machine was asleep or Nova was closed. |
| **`concurrencyPolicy`** | `string` | No | `"Skip"` | Overlap policy: `"Skip"` (skip if prior run is still active) or `"Replace"`. |
| **`maxTurns`** | `integer` | No | `50` | Maximum agent conversation turns for AI executors. |
| **`maxBudgetUsd`** | `number` | No | `null` | Maximum cost budget per run in USD. |
| **`totalBudgetCapUsd`** | `number` | No | `null` | Cumulative cost cap in USD across all runs before auto-disabling. |
| **`triggerNextTaskId`** | `string` | No | `null` | Target task ID to trigger upon completion (chaining). |
| **`triggerConditionKey`** | `string` | No | `null` | JSON key in structured_result that must evaluate to truthy to fire chain. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_create",
  "arguments": {
    "displayName": "Competitor Price Tracker",
    "prompt": "Check https://store.example.com/item/101 and write the current price to shared/price.json",
    "cronExpression": "daily 09:00",
    "timeZoneId": "Europe/Berlin",
    "executorKind": "ClaudeCode",
    "mcpAccess": true,
    "timeoutSeconds": 180
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Created scheduled task 'task-7c81a2f0' (Competitor Price Tracker). Next run: 2026-10-03 09:00 Europe/Berlin."
    }
  ],
  "structuredContent": {
    "ok": true,
    "taskId": "task-7c81a2f0",
    "displayName": "Competitor Price Tracker",
    "schedule": "daily 09:00 (Europe/Berlin)",
    "nextRunUtc": "2026-10-03T07:00:00Z",
    "executor": "ClaudeCode",
    "mcpAccess": true,
    "status": "Enabled"
  }
}
```

---

## 4. Operational Best Practices

* **MCP Tool Access:** Enable `mcpAccess: true` if the task instruction requires browser navigation, DOM extraction, or screenshots.
* **Timezone Accuracy:** Always declare `timeZoneId` when setting human-centric schedules (e.g. daily business hours) to handle daylight saving time correctly.
* **Budget Guardrails:** Set `maxBudgetUsd` and `totalBudgetCapUsd` on recurring tasks to prevent accidental cost overruns.

---

## 5. Related Tools

* [`nova.scheduled_task_list`](nova-scheduled-task-list.md) — List active tasks.
* [`nova.scheduled_task_trigger`](nova-scheduled-task-trigger.md) — Trigger manual execution.
* [`nova.scheduled_task_secret_set`](nova-scheduled-task-secret-set.md) — Inject encrypted API tokens.
