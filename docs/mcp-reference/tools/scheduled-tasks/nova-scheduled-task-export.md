# `nova.scheduled_task_export`

Exports all scheduled task definitions as a structured array (excluding secrets and history).

---

## 1. Overview

`nova.scheduled_task_export` reads every task definition and returns it both as a structured array (`tasks`) in `structuredContent` and as a pretty-printed JSON copy embedded in the text response, ready to save to a file. It captures prompts, schedules, executor configuration, budget caps, and chaining rules, while always omitting run history; a redacted-but-present `argsTemplate` placeholder marks that a value existed without revealing it, and DPAPI-encrypted secrets (stored separately from the task definition) are never included.

To re-import an export, the array must be serialized back to a JSON string for the `tasksJson` parameter of [`nova.scheduled_task_import`](nova-scheduled-task-import.md) — the two tools use different shapes (array vs. string) for the same data.

* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.scheduled_task_export",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Exported 1 task definition(s). Save this JSON to a file for backup or import on another instance.\n\n[ ... pretty-printed JSON, same shape as structuredContent.tasks ... ]"
    }
  ],
  "structuredContent": {
    "taskCount": 1,
    "tasks": [
      {
        "displayName": "Competitor Price Tracker",
        "prompt": "Check https://store.example.com/item/101 and write the current price to shared/price.json",
        "executorKind": "ClaudeCode",
        "autonomyMode": "Safe",
        "command": null,
        "argsTemplate": null,
        "workingDirectory": null,
        "intervalSeconds": 3600,
        "cronExpression": "daily 09:00",
        "timeZoneId": "Europe/Berlin",
        "oneShot": false,
        "mcpAccess": true,
        "timeoutSeconds": 180,
        "maxTurns": 50,
        "maxBudgetUsd": null,
        "maxConsecutiveFailures": 5,
        "concurrencyPolicy": "Skip",
        "extraSystemPrompt": null,
        "catchUpMissed": true,
        "triggerNextTaskId": null,
        "triggerOnStatus": null,
        "triggerConditionKey": null,
        "totalBudgetCapUsd": null,
        "watchPath": null
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Version Control Integration:** Commit exported task configurations into Git repositories to manage scheduled automations as code.
* **Disaster Recovery:** Store JSON exports before major migrations or system updates.

---

## 5. Related Tools

* [`nova.scheduled_task_import`](nova-scheduled-task-import.md) — Restore exported tasks.
* [`nova.scheduled_task_list`](nova-scheduled-task-list.md) — List active tasks.
