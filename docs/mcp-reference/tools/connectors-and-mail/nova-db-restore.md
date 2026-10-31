# `nova.db_restore`

Restores a MySQL or MariaDB database from an export that `nova.db_export` made on the same server. Nova backs up the database's current state first and asks the user before every restore.

---

## 1. Overview

`nova.db_restore` is the way back after a migration, an import or a script went wrong. It plays back only Nova's own exports. It does not take a file from somewhere else.

* **Backup first.** Before anything changes, the job exports the target database's current state as a new export with `role='rollback'`. The restore goes on only if that backup finished cleanly. Its id comes back as `backupExportId`. One exception: playing back the backup of a restore that stopped partway runs without a new backup, because the database then holds that restore's half-finished state (a broken view in it can make every new backup fail). The prompt says so, and `backupExportId` stays empty.
* **Asks each time.** Every restore shows the user one prompt with the database, the export, its size and the tables it replaces. The prompt offers no "always" and no "this session". Setting the `db.restore` permission to `always` only means it is not blocked. An unattended run or a host without prompts gets `approval_required`, and nothing is touched.
* **Checked before the prompt.** Nova reads the export first. A missing, unfinished or incomplete export, an export of another database, a dump that would switch to or create another database, or a file that changed since the export are all refused before the user is asked (`reasonCode` `db_restore.*`).
* **A job on the server.** The call starts the job and waits up to `waitSeconds`. The job keeps running on the server if the connection drops. Call again with `restoreId` to read its `state`. On a server that ends every process of an SSH session when it closes (logind `KillUserProcesses=yes`), `endsWithSession` is `true` and the warning `may_die_on_logout` says to wait for the end with `waitSeconds`.
* **States that tell what happened to the data.** `complete` means everything was applied. `failed_before_apply` means the database was not changed (for example the backup failed or the login was refused). `partial` means the import stopped partway, and `outcome_unknown` means the job ended without a result. In those last two cases `mayHaveApplied` is `true` and `nextAction` names the call that restores the backup (after a way back without a backup: the same export again).
* **Its own permission.** Capability `db.restore`, separate from `db.write` and `db.export`. The database login needs the privileges the dump uses (create, drop, insert, and trigger/routine privileges where the export has them).

* **Subsystem Overview:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SSH/SFTP connector id from nova.connector_list. |
| `databaseId` | `string` | No | — | — | Database entry to restore into (connectors[].databases[].id); required with exportId. It must name the database the export was made from. |
| `exportId` | `string` | No | — | — | The finished export to play back (dbx_..., from nova.db_export or its action='list', or a backupExportId of an earlier restore). Starts a restore. |
| `restoreId` | `string` | No | — | — | Id a previous call returned (dbr_...): read that restore's state instead of starting one. Not together with exportId. |
| `waitSeconds` | `integer` | No | `30` | 0–120 | How long the call waits for the job to finish before it returns the current state; the job goes on either way. |
| `connectTimeoutSeconds` | `integer` | No | `15` | 1–60 | TCP and SSH handshake deadline in seconds. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of asking the user; a restore then never starts. Scheduled-task hosts enforce this even when omitted. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.db_restore",
  "arguments": {
    "profileId": "cn_9f2c41",
    "databaseId": "db_4a7c19e2b0d1",
    "exportId": "dbx_5c0e9a1f3b7d2e64"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "state": "complete",
    "restoreId": "dbr_8d31c0a7e94f2b16",
    "exportId": "dbx_5c0e9a1f3b7d2e64",
    "backupExportId": "dbx_a2f7e04c9b1d3e58",
    "tablesReplaced": ["customers", "orders"],
    "mayHaveApplied": true,
    "warnings": []
  }
}
```

---

## 4. Operational Best Practices

* **Export right before a risky change.** `nova.db_export` before a migration gives you an export to come back to.
* **Read `mayHaveApplied`.** After `partial` or `outcome_unknown`, restore the backup with the `nextAction` call before you try anything else.
* **Keep the backups until you are sure.** `nova.db_export(action='list')` shows them with `role='rollback'`. Deleting one asks the user again.
* **Same database only.** An export restores into the database it was made from. To copy data to another database, fetch the export with `nova.sftp_get` and import it there.

---

## 5. Related Tools

* [`nova.db_export`](nova-db-export.md) — Makes the exports this tool restores, and lists or deletes them
* [`nova.db_query`](nova-db-query.md) — Checks the restored data
* [`nova.connector_database_set`](nova-connector-database-set.md) — Adds or updates database connection profiles
* [`nova.connector_history`](nova-connector-history.md) — Shows which restores ran on a server
* [`nova.connector_list`](nova-connector-list.md) — Lists connections and configured databases
