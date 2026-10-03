# `nova.mail_backup_status`

Reports progress, downloaded message counts, and active phase of a mail backup job.

---

## 1. Overview

`nova.mail_backup_status` monitors active and completed mail backup jobs, reporting progress percentages, folders processed, and error counters.

* **Security Tier:** Tier 1 (Read-Only)
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
      "text": "Backup job-mb-819a: 142/142 messages downloaded (completed)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-mb-819a",
    "status": "completed",
    "messagesDownloaded": 142,
    "totalMessages": 142,
    "durationSeconds": 38
  }
}
```

---

## 4. Operational Best Practices

* **Job Polling:** Poll periodically to determine completion before accessing exported backup databases.

---

## 5. Related Tools

* [`nova.mail_backup_start`](nova-mail-backup-start.md)
* [`nova.mail_backup_stop`](nova-mail-backup-stop.md)
