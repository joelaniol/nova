# `nova.connector_database_delete`

Removes a database entry from an SSH/SFTP connection together with its stored password.

---

## 1. Overview

Nova forgets the entry and deletes the password it stored for it. The database on the server is not touched. Deleting the whole connection removes all of its database entries the same way.

* **Not found is reported.** A `databaseId` that does not exist on that connection answers `status='not_found'`, never a silent success.

* **Subsystem Overview:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SSH/SFTP connector id from nova.connector_list. |
| `databaseId` | `string` | Yes | — | — | Database entry id from nova.connector_list. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_database_delete",
  "arguments": {
    "profileId": "cn_9f2c41",
    "databaseId": "db_4a7c19e2b0d1"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "status": "deleted",
    "profileId": "cn_9f2c41",
    "databaseId": "db_4a7c19e2b0d1"
  }
}
```

---

## 4. Operational Best Practices

* **Local Profile Deletion Only:** Deleting a database entry via this tool removes the encrypted credentials and connection parameters from Nova's vault. It has zero destructive effect on the physical database, schemas, or tables hosted on the remote server.
* **Pre-Flight ID Lookup:** Always query [`nova.connector_list`](nova-connector-list.md) beforehand to retrieve the canonical `databaseId` and `profileId`. Deleting an unrecognized database identifier returns `status: "not_found"`.
* **Cascade on Connector Removal:** If an entire server connection profile is being decommissioned via [`nova.connector_delete`](nova-connector-delete.md), all associated database entries attached to that connector are purged automatically without requiring individual deletion calls.

---

## 5. Related Tools

* [`nova.db_query`](nova-db-query.md) — Queries databases over SSH without password exposure.
* [`nova.db_export`](nova-db-export.md) — Exports a database as an SQL dump on the server without exposing the password.
* [`nova.connector_database_set`](nova-connector-database-set.md) — Adds or updates database connection profiles.
* [`nova.connector_list`](nova-connector-list.md) — Lists connections and database entries.
