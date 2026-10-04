# `nova.mail_backup_start`

Launches a background job to back up an entire mail account or specific folders.

---

## 1. Overview

`nova.mail_backup_start` backs up a whole mail account, or chosen folders, as a background job and returns at once with a `jobId`. Pull-only: folders open read-only and nothing on the server changes. Output is ZIP part files (`mail-backup_<account>_<time>_partNN.zip`) that mirror the mailbox layout with one `.eml` per message, each part carrying a `manifest.json`. A part grows up to the user's configured size (default 100 GB, ZIP64) before the backup continues into the next part; there is no per-message size limit. `mode='auto'` (the default) continues after the last committed part of this account, including after a stop, crash, or Nova restart; `'full'` starts over; `'incremental'` fails with `backup_no_resume_point` when there is nothing to continue. Only one backup per account runs at a time — starting again while one is running returns the already-running job (`alreadyRunning: true`). Requires the account's `read` capability plus Nova's independent SensitiveRead and PersistentWrite policies.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
| `mode` | `string` | No | `"auto"` | `auto`, `full`, `incremental` | auto: continue after the last backup or run in full; full: start over; incremental: only continue. |
| `folders` | `array` of `string` | No | — | ≤ 200 items | Optional exact folder fullNames. Omit for every selectable personal folder the grant allows. |
| `since` | `string` | No | — | — | Optional ISO date; only messages delivered on or after it. |
| `localPath` | `string` | No | — | — | Optional absolute existing folder for the part files. Omit for Nova's default folder. |
| `unattended` | `boolean` | No | `false` | — | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_backup_start",
  "arguments": {
    "profileId": "conn-mail-01",
    "folders": [
      "INBOX"
    ],
    "mode": "full"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Backup job-mb-819a started (full) into C:\\Users\\you\\Downloads. Poll nova.mail_backup_status(jobId='job-mb-819a'); the mailbox is only read."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-mb-819a",
    "profileId": "conn-mail-01",
    "account": "Work Email",
    "mode": "full",
    "state": "running",
    "complete": false,
    "verified": false,
    "verificationProblems": [],
    "alreadyRunning": false,
    "foldersTotal": 1,
    "foldersDone": 0,
    "currentFolder": "INBOX",
    "messagesEstimated": 142,
    "messagesEstimateIsUpperBound": false,
    "messagesDone": 0,
    "messagesSkipped": 0,
    "progressRatio": 0.0,
    "etaSeconds": null,
    "bytesWritten": 0,
    "maxPartBytes": 107374182400,
    "destination": "C:\\Users\\you\\Downloads",
    "parts": [],
    "foldersRestarted": [],
    "startedUtc": "2026-10-03T12:00:00Z",
    "finishedUtc": null,
    "elapsedMs": 50,
    "suggestedPollMs": 5000,
    "serverChanged": false,
    "retryAttempt": null,
    "retryNote": null,
    "skipped": [],
    "skippedListTruncated": false,
    "reasonCode": null,
    "message": null,
    "retryable": null,
    "nextAction": null,
    "localAccess": "approved_folders_only",
    "approvedFolders": ["Downloads"],
    "grantFilter": { "restricted": false, "allowedFolders": [], "allowedSenders": [] }
  }
}
```
Output is ZIP part files with one `.eml` per message, not a database; there is no `targetFolders`/`status` pair at the top level — the fields above (shared with `nova.mail_backup_status`) are the actual shape, and most of the detail fields above zero out for a run that just started.

---

## 4. Operational Best Practices

* **Non-Blocking Execution:** Runs in the background without tying up active agent turns.
* **Monitor Progress:** Use [`nova.mail_backup_status`](nova-mail-backup-status.md) to inspect progress and downloaded message counts.
* **`mode='auto'` Survives Restarts:** the resume point is saved per account; continuing after a stop, crash, or Nova restart just needs `mode='auto'` (the default) again.
* **Incomplete Is Not Completed:** if the grant filter excludes some messages, the finished job reports `state: "incomplete"`, `complete: false`, and lists them in `skipped` — never a silent `"completed"`.

---

## 5. Related Tools

* [`nova.mail_backup_status`](nova-mail-backup-status.md)
* [`nova.mail_backup_stop`](nova-mail-backup-stop.md)
