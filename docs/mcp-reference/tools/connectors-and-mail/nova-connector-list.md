# `nova.connector_list`

Lists configured E-Mail accounts and remote file transfer server connections.

---

## 1. Overview

`nova.connector_list` retrieves all active connector profiles available to the current workspace or global session. It reports connection IDs, types, host endpoints, usernames, and granted capability permissions without disclosing secrets.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`type`** | `string` | No | `null` | Optional: only list connectors of this type. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_list",
  "arguments": {
    "type": "mail"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 configured mail connector for the current workspace."
    }
  ],
  "structuredContent": {
    "ok": true,
    "connectors": [
      {
        "id": "conn-mail-01",
        "displayName": "Work Email",
        "type": "mail",
        "host": "imap.example.com",
        "username": "agent@example.com",
        "grants": {
          "read": "allow",
          "send": "ask"
        }
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Workspace Resolution:** Passwords and credentials are resolved strictly against the calling workspace context.
* **Filtered Scanning:** Use `type: "mail"`, `type: "sftp"`, or `type: "ftp"` to narrow results when managing specific automation tasks.

---

## 5. Related Tools

* [`nova.connector_create`](nova-connector-create.md)
* [`nova.connector_update`](nova-connector-update.md)
