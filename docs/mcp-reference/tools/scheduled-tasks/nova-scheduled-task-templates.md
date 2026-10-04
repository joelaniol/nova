# `nova.scheduled_task_templates`

Lists pre-built task templates for common automation scenarios (monitoring, reporting, maintenance).

---

## 1. Overview

`nova.scheduled_task_templates` provides ready-to-use task definitions with tuned prompts, recommended executors, default cron schedules, and parameter placeholders.

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
  "name": "nova.scheduled_task_templates",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "6 task template(s) available. Use scheduled_task_create with the template's fields to create a task from a template."
    }
  ],
  "structuredContent": {
    "templates": [
      {
        "id": "website-status",
        "displayName": "Website-Statuscheck",
        "description": "Prüft eine Website auf Erreichbarkeit und meldet Probleme.",
        "executorKind": "ClaudeCode",
        "intervalSeconds": 3600,
        "cronExpression": null,
        "timeoutSeconds": 120,
        "maxTurns": 10,
        "mcpAccess": true,
        "prompt": "Check the website for availability. Load the homepage, verify the HTTP status is 200 and content loaded successfully. Write the result as JSON to shared/status.json with fields: url, status, responseTimeMs, timestamp, ok (boolean)."
      }
    ]
  }
}
```
(Truncated — the real response lists all 6 built-in templates: `website-status`, `seo-audit`, `backup-check`, `weekly-report`, `api-health`, `data-cleanup`.)

---

## 4. Operational Best Practices

* **Accelerated Setup:** Use template configurations directly as arguments in [`nova.scheduled_task_create`](nova-scheduled-task-create.md) by substituting placeholders.
* **Best Practice Guidance:** Templates illustrate recommended executor and timeout pairings for common workloads.

---

## 5. Related Tools

* [`nova.scheduled_task_create`](nova-scheduled-task-create.md) — Instantiate task from template.
