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

## 4. Related Tools

* [`nova.db_query`](nova-db-query.md) — Queries databases over SSH without password exposure
* [`nova.connector_database_set`](nova-connector-database-set.md) — Adds or updates database connection profiles
* [`nova.connector_list`](nova-connector-list.md) — Lists connections and database entries
