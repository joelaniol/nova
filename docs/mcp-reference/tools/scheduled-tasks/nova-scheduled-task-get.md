# `nova.scheduled_task_get`

Retrieves full details of a scheduled task including prompt, schedule, chaining, and budget settings.

---

## 1. Overview

`nova.scheduled_task_get` returns the complete configuration and runtime state for a specific background task: the prompt text, executor settings, timezone, retry/budget configuration, the on-disk workspace path, and any chaining to a follow-up task. The response has no `ok` field; an unknown `taskId` throws an invalid-params error instead. `argsTemplate` is reported as the literal string `"[REDACTED]"` (not omitted) when a value is stored, since it may embed secret placeholders.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `taskId` | `string` | Yes | — | — | The task ID to retrieve. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_get",
  "arguments": {
    "taskId": "a1b2c3d4e5f6"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Task 'Competitor Price Tracker' (a1b2c3d4e5f6)."
    }
  ],
  "structuredContent": {
    "taskId": "a1b2c3d4e5f6",
    "displayName": "Competitor Price Tracker",
    "prompt": "Check https://store.example.com/item/101 and write the current price to shared/price.json",
    "executorKind": "ClaudeCode",
    "enabled": true,
    "cronExpression": "daily 09:00",
    "timeZoneId": "Europe/Berlin",
    "timeoutSeconds": 180,
    "mcpAccess": true,
    "workspacePath": "%LOCALAPPDATA%\\NovaBrowser\\Workspaces\\a1b2c3d4e5f6\\nova-tasks\\a1b2c3d4e5f6",
    "concurrencyPolicy": "Skip",
    "nextFireAtUtc": "2026-10-03T07:00:00Z",
    "cumulativeCostUsd": 0.12
  }
}
```

Trimmed for brevity — the full response also includes `autonomyMode`, `command`, `argsTemplate`, `workingDirectory`, `intervalSeconds`, `oneShot`, `modelOverride`, `maxTurns`, `maxBudgetUsd`, `maxConsecutiveFailures`, `extraSystemPrompt`, `catchUpMissed`, `triggerNextTaskId`, `triggerOnStatus`, `triggerConditionKey`, `totalBudgetCapUsd`, `watchPath`, `taskProfileId`, `lastSuccessfulRunAtUtc`, `workspaceId`, `workspaceIsTaskOwned`, `consecutiveFailureCount`, `totalRunCount`, `cumulativeInputTokens`, `cumulativeOutputTokens`, `createdAtUtc`, and `updatedAtUtc`.

---

## 4. Operational Best Practices

* **Pre-Update Verification:** Call `get` before [`nova.scheduled_task_update`](nova-scheduled-task-update.md) to inspect current configurations.
* **Workspace Location:** Use `workspacePath` to determine where persistent shared files and run logs reside.

---

## 5. Related Tools

* [`nova.scheduled_task_update`](nova-scheduled-task-update.md) — Update task configuration.
* [`nova.scheduled_task_workspace`](nova-scheduled-task-workspace.md) — Inspect task workspace.
