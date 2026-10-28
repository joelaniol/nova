# `nova.db_export`

Exports (backs up) a MySQL or MariaDB database that the user set up on an SSH/SFTP connection as an SQL dump file on the server - with the stored database login, without the agent ever seeing its password.

---

## 1. Overview

`nova.db_export` is the backup counterpart of `nova.db_query`. Running `mysqldump` through `nova.ssh_run` would need the database password in a command line, or root on the server; this tool runs the server's own dump client with the login stored in Nova and hands it the password itself.

* **A job on the server.** The call starts the dump and waits up to `waitSeconds`. The dump keeps running on the server if the connection drops. Call again with `exportId` to read its `state`: `running`, `finalizing`, `done`, `failed` or `lost` (the process is gone, nothing was published).
* **Private file, checked before it appears.** The file lands in `~/.nova-db-exports/<exportId>/` on the server, readable only by the SSH user. Nova publishes it only after the dump client and the writer ended without error, the gzip archive tests clean and the dump's last line reads `-- Dump completed`. `complete=true` sums that up.
* **Ready for phpMyAdmin.** No `CREATE DATABASE` or `USE`, so the import lands in the database selected in phpMyAdmin (or given to the `mysql` client). `format='sql.gz'` (default) or `format='sql'`.
* **Portable by default.** `portable=true` removes `DEFINER` clauses from views, triggers and routines and MariaDB's sandbox line, so the file imports for a user without the SUPER privilege, as on shared hosting, and on older servers. Row data is never changed.
* **Honest about what is missing.** `objectsOmitted` lists routines and events when they were not requested, and triggers when the database user lacks the TRIGGER privilege (the dump client then leaves them out without any error). `consistency` says whether all tables shared one snapshot (`innodb_snapshot`) or not (`mixed_engines`). `warnings` names collations another server may not know.
* **Its own permission.** Capability `db.export`, separate from `db.read`: the file is a full copy of the data.

* **Subsystem Overview:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SSH/SFTP connector id from nova.connector_list. |
| `databaseId` | `string` | No | — | — | Database entry id from nova.connector_list (connectors[].databases[].id); required to start. The entry must name its database (defaultDatabase). |
| `exportId` | `string` | No | — | — | Id a previous call returned (dbx_...): read that export's state instead of starting a new one. |
| `format` | `string` | No | `"sql.gz"` | `sql.gz`, `sql` | sql.gz (gzip, much smaller) or sql (plain text). phpMyAdmin imports both. |
| `portable` | `boolean` | No | `true` | — | Drop DEFINER clauses and MariaDB's sandbox line so the dump imports on another server and for a user without SUPER. false keeps the dump exactly as the client wrote it. |
| `includeRoutines` | `boolean` | No | `false` | — | Also dump stored procedures and functions (needs further privileges; listed in objectsOmitted when off). |
| `includeEvents` | `boolean` | No | `false` | — | Also dump scheduled events (needs the EVENT privilege; listed in objectsOmitted when off). |
| `waitSeconds` | `integer` | No | `30` | 0–120 | How long the call waits for the job to finish before it returns state='running'; the job goes on either way. |
| `connectTimeoutSeconds` | `integer` | No | `15` | 1–60 | TCP and SSH handshake deadline in seconds. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of asking the user; scheduled-task hosts enforce this even when omitted. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.db_export",
  "arguments": {
    "profileId": "cn_9f2c41",
    "databaseId": "db_4a7c19e2b0d1",
    "format": "sql.gz"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "state": "done",
    "exportId": "dbx_5c0e9a1f3b7d2e64",
    "remotePath": "/home/deploy/.nova-db-exports/dbx_5c0e9a1f3b7d2e64/shop-20261027T090000Z-5c0e9a1f3b7d2e64.sql.gz",
    "bytes": 184213,
    "sha256": "…",
    "complete": true,
    "consistency": "innodb_snapshot",
    "objectsOmitted": ["routines", "events"],
    "warnings": [],
    "nextAction": "nova.sftp_get(remotePath, verifySha256=true)"
  }
}
```

---

## 4. Operational Best Practices

* **Fetch with a checksum.** `nova.sftp_get(remotePath, verifySha256=true)` compares the copy with the server's file.
* **Read `complete` and `warnings` before calling it a backup.** A dump without triggers or with a collation the target server lacks still imports partly or stops halfway.
* **Grant TRIGGER for complete exports.** A read-only user with `SELECT, SHOW VIEW, TRIGGER` is enough for tables, views and triggers.
* **Large databases.** The dump holds one long read transaction; run it outside peak hours and keep polling with `exportId` instead of starting again.
* **Old exports stay on the server.** Remove them with `nova.sftp_delete` when they are no longer needed.

---

## 5. Related Tools

* [`nova.db_query`](nova-db-query.md) — Queries databases over SSH without password exposure
* [`nova.connector_database_set`](nova-connector-database-set.md) — Adds or updates database connection profiles
* [`nova.connector_database_delete`](nova-connector-database-delete.md) — Removes database profiles and stored credentials
* [`nova.sftp_get`](nova-sftp-get.md) — Downloads the exported SQL dump with checksum verification
* [`nova.sftp_delete`](nova-sftp-delete.md) — Removes old dump files from the server
* [`nova.connector_list`](nova-connector-list.md) — Lists connections and configured databases
* [`nova.vault_list`](../vault-and-security/nova-vault-list.md) — Lists Vault credentials available for database logins
