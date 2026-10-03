# `nova.mail_backup_start`

Launches a background job to back up an entire mail account or specific folders.

---

## 1. Overview

`nova.mail_backup_start` initiates a resilient, pull-only background backup job. It streams emails into a local encrypted SQLite database and returns a `jobId` for monitoring.

* **Security Tier:** Tier 2 (Background Backup)
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
