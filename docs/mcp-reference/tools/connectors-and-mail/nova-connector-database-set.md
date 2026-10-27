# `nova.connector_database_set`

Adds or changes a MySQL/MariaDB database on an SSH/SFTP connection, so `nova.db_query` can reach it.

---

## 1. Overview

A database entry names a database user and, optionally, the database and where it runs as seen from the SSH server. Without `databaseId` a new entry is created (`label` and `username` are required); with it, only the passed fields change and an empty string clears an optional one.

* **No password argument.** The user sets the password in Settings > Connectors > SFTP > Databases…, or the agent passes `passwordFromVault` with the id of a vault entry; the user confirms that copy and the agent never sees the password.
* **Where the database runs.** By default the client's local socket on the SSH server. Pass `host`/`port` for a database in a container or on another machine, or `socket` for a non-default socket path.
* **Entries are listed** in `nova.connector_list` under `connectors[].databases[]`, with `hasPassword`, the detected engine, the server version and the last privilege check.

* **Subsystem Overview:** [Secure Shell (SSH)](../../../core-features/connectors/ssh/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SSH/SFTP connector id from nova.connector_list. |
| `databaseId` | `string` | No | — | — | Existing entry to change; omit to create a new one. |
| `label` | `string` | No | — | ≤ 80 characters | How the user recognizes the database, e.g. 'Shop'. |
| `username` | `string` | No | — | ≤ 80 characters | Database user (letters, digits, _ . @ % + -). A user that may only read is the safest choice. |
| `passwordFromVault` | `string` | No | — | — | Id of a Nova vault entry (nova.vault_list) whose password becomes this database's password. The user confirms the copy; 'always' binds that entry to this server and database user. |
| `defaultDatabase` | `string` | No | — | ≤ 64 characters | Database (schema) selected for queries, e.g. 'shop'. Letters, digits, _ -. |
| `host` | `string` | No | — | ≤ 253 characters | Database host as seen from the SSH server (e.g. 127.0.0.1 or a container name). Omit to use the client's default socket. Not together with socket. |
| `port` | `integer` | No | — | 0–65535 | Database port with host (default 3306). 0 clears it. |
| `socket` | `string` | No | — | ≤ 201 characters | Absolute path of the server's database socket, e.g. /run/mysqld/mysqld.sock. Not together with host. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_database_set",
  "arguments": {
    "profileId": "cn_9f2c41",
    "label": "Shop",
    "username": "shop_readonly",
    "defaultDatabase": "shop"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "status": "created",
    "database": {
      "id": "db_4a7c19e2b0d1",
      "label": "Shop",
      "username": "shop_readonly",
      "defaultDatabase": "shop",
      "hasPassword": false
    },
    "next": "No password yet: the user sets it in Settings > Connectors > SFTP > Databases…, or pass passwordFromVault. Then run nova.db_query."
  }
}
```

---

## 4. Operational Best Practices

* **Prefer a read-only database user.** It is the boundary that holds even when a query slips past every other check.
* **Ask the user for the password step**, or use `passwordFromVault` when the vault already holds the database login.
