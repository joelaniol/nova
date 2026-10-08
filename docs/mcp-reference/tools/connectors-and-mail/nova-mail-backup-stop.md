# `nova.mail_backup_stop`

Gracefully stops an in-flight mail backup job, committing all downloaded messages.

---

## 1. Overview

`nova.mail_backup_stop` stops a running mail backup. The open ZIP part is finished and committed, so nothing already downloaded is lost; a later `nova.mail_backup_start` with `mode='auto'` continues after it. The call returns the job status with `state: "stopping"` until the worker has actually closed the part.

* **Core Architecture Guide:** [Mail: IMAP & SMTP](../../../core-features/connectors/mail/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | Job id returned by nova.mail_backup_start. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_backup_stop",
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
      "text": "Stop requested for job-mb-819a: the open part is finished and kept; continue later with mode='auto'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-mb-819a",
    "profileId": "conn-mail-01",
    "account": "Work Email",
    "mode": "full",
    "state": "stopping",
    "complete": false,
    "messagesDone": 80,
    "messagesSkipped": 0,
    "parts": [
      { "number": 1, "path": "C:\\Users\\you\\Downloads\\mail-backup_Work-Email_2026-10-03_120000_part01.zip", "bytes": 27000000, "sha256": "...", "messages": 80 }
    ],
    "destination": "C:\\Users\\you\\Downloads"
  }
}
```
The field is `state`, not `status`, and this call returns the full job status object shared with `nova.mail_backup_status` (abbreviated above) rather than a bare `{jobId, status}` pair. Poll `nova.mail_backup_status` to see `state` move from `"stopping"` to `"stopped"`.

---

## 4. Operational Best Practices

* **Safe Resumption:** Subsequent backup runs will resume incrementally from the committed watermark using `mode='auto'`.
* **Poll for Confirmation:** `state: "stopping"` means the worker is still closing the current part; call `nova.mail_backup_status` afterward to confirm `"stopped"`.

---

## 5. Related Tools

* [`nova.mail_backup_start`](nova-mail-backup-start.md)
* [`nova.mail_backup_status`](nova-mail-backup-status.md)
