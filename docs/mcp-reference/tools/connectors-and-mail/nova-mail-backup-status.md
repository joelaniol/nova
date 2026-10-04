# `nova.mail_backup_status`

Reports progress, downloaded message counts, and active phase of a mail backup job.

---

## 1. Overview

`nova.mail_backup_status` reports the progress of mail backups. With `jobId`: state (`planning`/`running`/`stopping`/`completed`/`stopped`/`failed`), folders/messages done, an ETA for full runs only, the ZIP parts written so far (path/bytes/sha256/messages), messages skipped by the grant filter, and on failure a reasonCode with a concrete next action. Without `jobId`: the jobs of this Nova session (optionally for one `profileId`) plus that account's last run from the saved resume point, which survives restarts. `acknowledge: true` with `profileId` clears that account's backup alarm after the user has been told what is missing.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | No | — | — | Job id returned by nova.mail_backup_start. |
| `profileId` | `string` | No | — | — | Optional mail connector id to list its jobs and last run. |
| `acknowledge` | `boolean` | No | `false` | — | With profileId: acknowledge that account's backup alarm (failed/incomplete/interrupted), which removes backupIntegrityWarning from every answer. Only after the user was told what is missing. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_backup_status",
  "arguments": {
    "jobId": "job-mb-819a"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "job-mb-819a: completed, 142 messages, 1 part(s)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-mb-819a",
    "profileId": "conn-mail-01",
    "account": "Work Email",
    "mode": "full",
    "state": "completed",
    "complete": true,
    "verified": true,
    "verificationProblems": [],
    "alreadyRunning": false,
    "foldersTotal": 1,
    "foldersDone": 1,
    "currentFolder": null,
    "messagesEstimated": 142,
    "messagesEstimateIsUpperBound": false,
    "messagesDone": 142,
    "messagesSkipped": 0,
    "progressRatio": 1.0,
    "etaSeconds": null,
    "bytesWritten": 48234112,
    "maxPartBytes": 107374182400,
    "destination": "C:\\Users\\you\\Downloads",
    "parts": [
      { "number": 1, "path": "C:\\Users\\you\\Downloads\\mail-backup_Work-Email_2026-10-03_120000_part01.zip", "bytes": 48234112, "sha256": "...", "messages": 142 }
    ],
    "foldersRestarted": [],
    "startedUtc": "2026-10-03T12:00:00Z",
    "finishedUtc": "2026-10-03T12:00:38Z",
    "elapsedMs": 38000,
    "suggestedPollMs": null,
    "serverChanged": false,
    "retryAttempt": null,
    "retryNote": null,
    "skipped": [],
    "skippedListTruncated": false,
    "reasonCode": null,
    "message": null,
    "retryable": null,
    "nextAction": null
  }
}
```
There is no `messagesDownloaded`/`totalMessages`/`durationSeconds` triple — the field names are `messagesDone`, `messagesEstimated` (an upper bound for incremental runs), and `elapsedMs`.

---

## 4. Operational Best Practices

* **Job Polling:** Use `suggestedPollMs` while a job is active; it is `null` once the job stops.
* **`complete` Is Stricter Than `state`:** a job can reach `state: "completed"` while `complete: false` when some messages were skipped by the grant filter — check both plus `skipped[]`.
* **On Failure, Read `nextAction`:** a failed job's `reasonCode`/`nextAction` name a concrete recovery step (checking the password, the connection security setting, choosing another folder, or resuming with `mode='auto'`) rather than a generic error.

---

## 5. Related Tools

* [`nova.mail_backup_start`](nova-mail-backup-start.md)
* [`nova.mail_backup_stop`](nova-mail-backup-stop.md)
