# `nova.scheduled_task_create`

Creates a new scheduled task running on cron expressions, intervals, or filesystem change events.

---

## 1. Overview

`nova.scheduled_task_create` registers an automated background task with Nova's scheduling engine. Tasks execute unattended according to cron patterns, fixed intervals, or folder change watches.

Supported executors include `ClaudeCode`, `CodexCli`, `Shell` (PowerShell 7), `CustomCommand`, and `HttpWebhook`. Each task binds to a dedicated terminal workspace (or an existing one, if `workspaceId` is given) with a shared `shared/` folder for files that persist between runs; task secrets are stored separately, encrypted with Windows DPAPI for the current user. Nova keeps task definitions and run history in one shared SQLite database, not an isolated database per task.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `displayName` | `string` | Yes | — | — | Human-readable task name. |
| `prompt` | `string` | Yes | — | — | ClaudeCode/CustomCommand: the instruction/prompt. Shell executor: the PowerShell SCRIPT body (run via -File; exit code drives status, and the script may write JSON to $env:NOVA_TASK_RESULT_PATH for structured chaining). |
| `intervalSeconds` | `integer` | No | — | ≥ 60 | Run interval in seconds. Minimum 60. Optional when cronExpression is set (defaults to 3600 as fallback). Required for interval-based tasks. |
| `cronExpression` | `string` | No | — | — | Optional schedule expression (overrides intervalSeconds). Patterns: 'daily HH:MM', 'weekdays HH:MM', 'weekly mon/tue/wed/thu/fri/sat/sun HH:MM', 'hourly :MM', 'every Nh', 'every Nm'. |
| `timeZoneId` | `string` | No | — | — | Optional IANA or Windows timezone for cron patterns (e.g. 'Europe/Berlin' or 'W. Europe Standard Time'). Default: UTC. Invalid identifiers are rejected. |
| `executorKind` | `string` | No | `"ClaudeCode"` | `ClaudeCode`, `CodexCli`, `CustomCommand`, `HttpWebhook`, `Shell` | Executor type. Default: 'ClaudeCode'. 'CodexCli' runs the prompt through the user's Codex CLI (codex exec, requires Codex installed / on PATH). 'Shell' runs the prompt as a PowerShell script (requires the Shell task executor enabled in Settings). |
| `autonomyMode` | `string` | No | `"Safe"` | `Safe`, `Unsafe` | Permission mode for ClaudeCode/CodexCli executors (Safe = sandboxed, no approval prompts; Unsafe = full access, requires ScheduledTaskUnsafeModeEnabled). Default: 'Safe'. |
| `command` | `string` | No | — | — | For CustomCommand executor: the executable to run. |
| `argsTemplate` | `string` | No | — | — | For CustomCommand: argument template with {PROMPT}, {TASK_ID}, {RUN_ID}, {TASK_WORKSPACE}, {TASK_WORKSPACE_SHARED}, {TASK_WORKSPACE_RUN}, and {SECRET:keyname} placeholders. Secrets are DPAPI-encrypted and resolved at execution time. |
| `workingDirectory` | `string` | No | — | — | For CustomCommand: working directory for the process. |
| `timeoutSeconds` | `integer` | No | `300` | — | Max run duration before timeout kill. Default: 300. |
| `maxTurns` | `integer` | No | `50` | — | Max conversation turns for ClaudeCode. Default: 50. |
| `maxBudgetUsd` | `number` | No | — | — | Optional: max cost budget per run in USD. |
| `mcpAccess` | `boolean` | No | `false` | — | Whether the task gets MCP access to Nova tools. Default: false. |
| `extraSystemPrompt` | `string` | No | — | — | Optional: additional system prompt prepended to the task prompt. |
| `oneShot` | `boolean` | No | `false` | — | If true, task auto-disables after first successful run. Default: false. |
| `catchUpMissed` | `boolean` | No | `true` | — | If true, a run missed while Nova was down/asleep is caught up once at next start (within a 24h window). Default: true. |
| `triggerNextTaskId` | `string` | No | — | — | Optional: task ID to trigger when this task completes. Creates a run chain (max depth 5). |
| `triggerOnStatus` | `string` | No | `"Completed"` | `Completed`, `Any` | When to trigger next task: 'Completed' (default) or 'Any'. |
| `triggerConditionKey` | `string` | No | — | — | Optional: JSON key in structured_result that must be truthy for the chain to fire. E.g. 'alert' fires only if result contains {"alert": true}. Null = status-only check. |
| `concurrencyPolicy` | `string` | No | `"Skip"` | `Skip`, `Replace` | Behavior when a new run overlaps an active one. Default: 'Skip'. |
| `totalBudgetCapUsd` | `number` | No | — | — | Optional: cumulative cost cap in USD across all runs. Task auto-disables when exceeded. 0 or null = no cap. |
| `watchPath` | `string` | No | — | — | Optional: filesystem directory to watch. Changes trigger a run (2s debounce). Null = time-based only. |
| `taskProfileId` | `string` | No | — | — | Optional: ETM task profile ID. If set, a TaskMemory instance is auto-created on each run start. |
| `workspaceId` | `string` | No | — | — | Optional: bind this task to an existing terminal workspace (its id). The task's run artifacts live under that workspace so it can be opened in the terminal dock. Omit to auto-create a dedicated workspace for this task. |
| `workspaceDisplayName` | `string` | No | — | — | Optional: display name for the auto-created dedicated workspace (only used when workspaceId is omitted). Defaults to the task's displayName. |
| `installOnboarding` | `boolean` | No | `true` | — | Optional: whether the auto-created workspace and its task run workspace install Nova onboarding files (CLAUDE.md, AGENTS.md, .nova). Only used when workspaceId is omitted. Default: true. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Created task 'Competitor Price Tracker' (a1b2c3d4e5f6). Next scheduled run at 2026-10-03T07:00:00+00:00. Use nova.scheduled_task_trigger(taskId='a1b2c3d4e5f6') to run immediately, or nova.scheduled_task_runs(taskId='a1b2c3d4e5f6') to check run history."
    }
  ],
  "structuredContent": {
    "taskId": "a1b2c3d4e5f6",
    "workspaceId": "a1b2c3d4e5f6",
    "workspaceIsTaskOwned": true,
    "nextFireAtUtc": "2026-10-03T07:00:00Z",
    "nextActions": [
      { "tool": "nova.scheduled_task_trigger", "args": { "taskId": "a1b2c3d4e5f6" }, "hint": "Run the task immediately" },
      { "tool": "nova.scheduled_task_runs", "args": { "taskId": "a1b2c3d4e5f6" }, "hint": "Check run history and status" },
      { "tool": "nova.scheduled_task_get", "args": { "taskId": "a1b2c3d4e5f6" }, "hint": "Get full task details including cumulative cost" }
    ]
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
