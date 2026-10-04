# `nova.session_record_purge`

Destructively deletes finalized session recordings older than a specified day threshold.

---

## 1. Overview

`nova.session_record_purge` deletes expired recording folders from `%LOCALAPPDATA%\NovaBrowser\Recordings`. It permanently frees disk space by removing historical chunk files, encrypted keys, and index artifacts older than the specified age in days.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `olderThanDays` | `integer` | Yes | — | 1–3650 | Required threshold in days — recordings older than this are deleted. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
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
      "text": "Recording purge: purged 14, retained 6, skipped 0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "completed",
    "reasonCode": null,
    "olderThanDays": 7,
    "cutoffUtc": "2026-09-25T20:00:00Z",
    "scannedCount": 20,
    "retainedCount": 6,
    "purgedCount": 14,
    "purgedIds": ["rec-7a1b2c3d", "rec-8e9f0a1b"],
    "skippedCount": 0,
    "skipped": []
  }
}
```

The response does not report freed disk space — only counts of scanned/retained/purged/skipped recording directories. A directory is purged by its creation timestamp against the `olderThanDays` cutoff; `skipped` lists any directory that could not be deleted (e.g. a path-guard failure), with `ok: false` and `status: "partial_failure"`/`"failed"` when that happens.

---

## 4. Operational Best Practices

* **Intent Required:** As a destructive file-deletion tool, Nova enforces mandatory `_meta.intent` declaration.
* **TTL Protects Active Sessions:** Since a running recording's hard TTL cap is 60 minutes, no directory can still be "active" once it is a day or more old — the minimum `olderThanDays` value — so a purge call never has to choose between an active and a finalized recording.
* **Automated Housekeeping:** Recommended for scheduled weekly cron cleanup tasks.

---

## 5. Related Tools

* [`nova.session_record_export`](nova-session-record-export.md) — Export before purging if archiving is needed.
* [`nova.scheduled_task_create`](../scheduled-tasks/nova-scheduled-task-create.md) — Schedule periodic maintenance.
