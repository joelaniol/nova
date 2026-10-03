# `nova.mail_backup_start`

Launches a background job to back up an entire mail account or specific folders.

---

## 1. Overview

`nova.mail_backup_start` initiates a resilient, pull-only background backup job. It streams emails into a local encrypted SQLite database and returns a `jobId` for monitoring.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Background Backup)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`folders`** | `array` | No | `null` | Optional exact folder fullNames. Omit for every selectable personal folder the grant allows. |
| **`localPath`** | `string` | No | `null` | Optional absolute existing folder for the part files. Omit for Nova's default folder. |
| **`mode`** | `string` | No | `"auto"` | auto: continue after the last backup or run in full; full: start over; incremental: only continue. |
| **`profileId`** | `string` | Yes | `null` | Mail connector id (from nova.connector_list). |
| **`since`** | `string` | No | `null` | Optional ISO date; only messages delivered on or after it. |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

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
      "text": "Started background mail backup job 'job-mb-819a'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "job-mb-819a",
    "profileId": "conn-mail-01",
    "status": "running",
    "targetFolders": [
      "INBOX"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Non-Blocking Execution:** Runs in the background without tying up active agent turns.
* **Monitor Progress:** Use [`nova.mail_backup_status`](nova-mail-backup-status.md) to inspect progress and downloaded message counts.

---

## 5. Related Tools

* [`nova.mail_backup_status`](nova-mail-backup-status.md)
* [`nova.mail_backup_stop`](nova-mail-backup-stop.md)
