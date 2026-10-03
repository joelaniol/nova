# `nova.session_record_purge`

Destructively deletes finalized session recordings older than a specified day threshold.

---

## 1. Overview

`nova.session_record_purge` deletes expired recording folders from `%LOCALAPPDATA%\NovaBrowser\Recordings`. It permanently frees disk space by removing historical chunk files, encrypted keys, and index artifacts older than the specified age in days.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 3 (Destructive Purge)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `olderThanDays` | `integer` | Yes | — | 1–3650 | Required threshold in days — recordings older than this are deleted. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_purge",
  "arguments": {
    "olderThanDays": 7,
    "_meta": {
      "intent": "Weekly automated maintenance cleanup of old recording archives"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Purged 14 recording directories older than 7 days (freed 420 MB)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "olderThanDays": 7,
    "deletedRecordingsCount": 14,
    "freedBytes": 440401920
  }
}
```

---

## 4. Operational Best Practices

* **Intent Required:** As a destructive file-deletion tool, Nova enforces mandatory `_meta.intent` declaration.
* **Preserve Active Sessions:** Only finalised or expired recordings are deleted; active running recordings are never touched.
* **Automated Housekeeping:** Recommended for scheduled weekly cron cleanup tasks.

---

## 5. Related Tools

* [`nova.session_record_export`](nova-session-record-export.md) — Export before purging if archiving is needed.
* [`nova.scheduled_task_create`](../scheduled-tasks/nova-scheduled-task-create.md) — Schedule periodic maintenance.
