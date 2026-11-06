# `nova.db_restore`

Restores a MySQL or MariaDB database from an export that `nova.db_export` made on the same server, or imports a `.sql`/`.sql.gz` file from elsewhere on that server. Nova backs up the database's current state first and asks the user before every restore; a dry run checks a file without changing anything.

---

## 1. Overview

`nova.db_restore` is the way back after a migration, an import or a script went wrong, and the way in for a dump Nova did not write (a phpMyAdmin export, the old host's backup, a file uploaded with `nova.sftp_put`).

* **Backup first.** Before anything changes, the job exports the target database's current state as a new export with `role='rollback'`. The restore goes on only if that backup finished cleanly. Its id comes back as `backupExportId`. One exception: playing back the backup of a restore that stopped partway runs without a new backup, because the database then holds that restore's half-finished state (a broken view in it can make every new backup fail). The prompt says so, and `backupExportId` stays empty.
* **Asks each time.** Every restore shows the user one prompt with the database, the export, its size and the tables it replaces. The prompt offers no "always" and no "this session". Setting the `db.restore` permission to `always` only means it is not blocked. An unattended run or a host without prompts gets `approval_required`, and nothing is touched.
* **Checked before the prompt.** Nova reads the export first. A missing, unfinished or incomplete export, an export of another database, a dump that would switch to or create another database, or a file that changed since the export are all refused before the user is asked (`reasonCode` `db_restore.*`).
* **A job on the server.** The call starts the job and waits up to `waitSeconds`. The job keeps running on the server if the connection drops. Call again with `restoreId` to read its `state`. On a server that ends every process of an SSH session when it closes (logind `KillUserProcesses=yes`), `endsWithSession` is `true` and the warning `may_die_on_logout` says to wait for the end with `waitSeconds`.
* **States that tell what happened to the data.** `complete` means everything was applied. `failed_before_apply` means the database was not changed (for example the backup failed or the login was refused). `partial` means the import stopped partway, and `outcome_unknown` means the job ended without a result. In those last two cases `mayHaveApplied` is `true` and `nextAction` names the call that restores the backup (after a way back without a backup: the same export again).
* **Its own permission.** Capability `db.restore`, separate from `db.write` and `db.export`. The database login needs the privileges the dump uses (create, drop, alter, insert, lock tables, and view/trigger/routine privileges where the dump has them). Nova reads the login's grants before the backup and stops with `db_restore.privilege_missing`, naming what is missing, instead of letting the import fail halfway.

### Files Nova did not write (`sourcePath`)

* **Dry run first.** `sourcePath` with `dryRun=true` checks the file where it lies and changes nothing: format and gzip integrity, its sha256, and what it would create, drop or replace, compared with the target database's tables, collations and storage engines and with the database user's privileges. It needs only `db.read` and `sftp.read` and shows no restore prompt. The answer has `state='inspected'`, `refusals[]`, `warnings[]` and an `import` block (`tablesReplaced`, `tablesNew`, `objects`, `definers`, `unknownCollations`, `writeScope`, `limitations`).
* **A private copy.** A real import first copies the file into Nova's private folder on the server and checks only that copy, so a file changed afterwards cannot slip in. The copy is listed like an export with `role='imported'` (`importId` in the answer, `nova.db_export(action='delete')` removes it) and can be played back again with `exportId`.
* **Refused before the prompt.** A dump that drops the database, switches to or creates another one, writes into tables of another database, creates tables that link to other servers, holds server or account statements, or needs a privilege the database user lacks is refused. Archives Nova cannot read (zip, bz2, xz) are refused as `unsupported_format`.
* **Warned in the prompt.** Privileges that reach beyond the target database (`writeScope='wider'`) come first in the prompt and first in `warnings`; the user decides. Other warnings name collations or engines the server lacks, foreign `DEFINER` accounts and the tables the file replaces.
* **`stripDefiners=true`** drops the `DEFINER` clauses while the file is read, so views, triggers and routines of another account import without administrator rights. They then run with the rights of the entry's database user.
* **A hint, not a proof.** The check reads the file's statements, it does not run them. The database user's privileges are the real boundary, and in a foreign file every SQL error counts as `partial`.

* **Subsystem Overview:** [Database Management (MySQL & MariaDB over SSH)](../../../core-features/connectors/database/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SSH/SFTP connector id from nova.connector_list. |
| `databaseId` | `string` | No | — | — | Database entry to restore into (connectors[].databases[].id); required with exportId or sourcePath. For an export it must name the database the export was made from; a foreign file goes into the entry's defaultDatabase. |
| `exportId` | `string` | No | — | — | The finished export to play back (dbx_..., from nova.db_export or its action='list', a backupExportId of an earlier restore, or the importId of an earlier import). Starts a restore. |
| `restoreId` | `string` | No | — | — | Id a previous call returned (dbr_...): read that restore's state instead of starting one. Not together with exportId or sourcePath. |
| `sourcePath` | `string` | No | — | ≤ 400 characters | Absolute path of a .sql or .sql.gz file on the SSH server that Nova did not write, e.g. /home/u/backup.sql.gz (letters, digits, _ . / - only; no '..'; not under /proc, /sys, /dev, /run). Plain text or gzip; zip, bz2, xz are refused (unsupported_format). |
| `dryRun` | `boolean` | No | `false` | — | With sourcePath: only check the file and report what an import would do and why Nova would refuse it; nothing is copied or changed, no restore prompt (db.read + sftp.read are asked). |
| `stripDefiners` | `boolean` | No | `false` | — | For a foreign file: drop DEFINER clauses on CREATE lines while reading (like db_export portable), so views, triggers and routines of another account import without SUPER (no ERROR 1227). They then run with the rights of the entry's database user. |
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

### Dry run of a foreign file
```json
{
  "name": "nova.db_restore",
  "arguments": {
    "profileId": "cn_9f2c41",
    "databaseId": "db_4a7c19e2b0d1",
    "sourcePath": "/home/shop/backup-2026-10.sql.gz",
    "dryRun": true
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "state": "inspected",
    "executed": false,
    "databaseModified": false,
    "refusals": [],
    "warnings": ["The file sets DEFINER `olduser`@`localhost`. Without SUPER or SET_USER_ID the restore stops at the first such object (ERROR 1227); stripDefiners=true removes DEFINER on CREATE lines, ..."],
    "import": {
      "tablesReplaced": ["customers", "orders"],
      "tablesNew": ["coupons"],
      "writeScope": "database_only"
    }
  }
}
```

---

## 4. Operational Best Practices

* **Export right before a risky change.** `nova.db_export` before a migration gives you an export to come back to.
* **Read `mayHaveApplied`.** After `partial` or `outcome_unknown`, restore the backup with the `nextAction` call before you try anything else.
* **Keep the backups until you are sure.** `nova.db_export(action='list')` shows them with `role='rollback'`. Deleting one asks the user again.
* **Same database only.** An export restores into the database it was made from. To copy data to another database, pass the export's file as `sourcePath` with the other database entry.
* **Dry run before every foreign import.** `dryRun=true` shows refusals and warnings without asking the user; use `stripDefiners=true` when it names foreign `DEFINER` accounts and the database user lacks administrator rights.

---

## 5. Related Tools

* [`nova.db_export`](nova-db-export.md) — Makes the exports this tool restores, and lists or deletes them
* [`nova.db_query`](nova-db-query.md) — Checks the restored data
* [`nova.connector_database_set`](nova-connector-database-set.md) — Adds or updates database connection profiles
* [`nova.connector_history`](nova-connector-history.md) — Shows which restores ran on a server
* [`nova.connector_list`](nova-connector-list.md) — Lists connections and configured databases
