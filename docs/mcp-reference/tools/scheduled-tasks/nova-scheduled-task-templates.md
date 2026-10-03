# `nova.scheduled_task_templates`

Lists pre-built task templates for common automation scenarios (monitoring, scraping, backups).

---

## 1. Overview

`nova.scheduled_task_templates` provides ready-to-use task definitions with tuned prompts, recommended executors, default cron schedules, and parameter placeholders.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Scheduled Tasks & Background Automation Engine](../../../core-features/scheduled-tasks.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `scheduled_tasks` (load it with `nova.tools_bundle(bundle='scheduled_tasks')`).
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
      "text": "Loaded 4 pre-built task templates."
    }
  ],
  "structuredContent": {
    "ok": true,
    "templates": [
      {
        "templateId": "web_monitor",
        "displayName": "Website Content Monitor",
        "defaultSchedule": "every 1 hour",
        "suggestedExecutor": "ClaudeCode",
        "promptTemplate": "Check {URL} for changes in {SELECTOR} and notify if content changed."
      },
      {
        "templateId": "daily_email_digest",
        "displayName": "Daily Email Digest",
        "defaultSchedule": "daily 08:30",
        "suggestedExecutor": "ClaudeCode",
        "promptTemplate": "Summarize unread emails from the last 24h using mail tools."
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Accelerated Setup:** Use template configurations directly as arguments in [`nova.scheduled_task_create`](nova-scheduled-task-create.md) by substituting placeholders.
* **Best Practice Guidance:** Templates illustrate recommended executor and timeout pairings for common workloads.

---

## 5. Related Tools

* [`nova.scheduled_task_create`](nova-scheduled-task-create.md) — Instantiate task from template.
