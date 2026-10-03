# `nova.sftp_delete`

Deletes a remote file, empty directory, or bounded directory tree over SFTP.

---

## 1. Overview

`nova.sftp_delete` removes files or directories on an SFTP server. Supports recursive directory deletion when explicitly configured.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 3 (Destructive File Deletion)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`maxBytes`** | `integer` | No | `1073741824` | Requested total-byte ceiling for this call; cannot exceed Nova's hard limit. |
| **`maxFiles`** | `integer` | No | `500` | Requested entry ceiling for this call; cannot exceed Nova's hard limit. |
| **`profileId`** | `string` | Yes | `null` | SFTP connector id from nova.connector_list. |
| **`recursive`** | `boolean` | No | `false` | Delete a non-empty directory tree after enforcing maxFiles/maxBytes. False deletes only a file or empty directory. |
| **`remotePath`** | `string` | Yes | `null` | Remote file or directory to delete. |
| **`unattended`** | `boolean` | No | `false` | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sftp_delete",
  "arguments": {
    "profileId": "conn-sftp-01",
    "remotePath": "/var/www/incoming/old-report.csv"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted remote SFTP file /var/www/incoming/old-report.csv."
    }
  ],
  "structuredContent": {
    "ok": true,
    "deletedPath": "/var/www/incoming/old-report.csv"
  }
}
```

---

## 4. Operational Best Practices

* **High-Impact Action:** Deletions are permanent on remote hosts; double-check remote paths before calling.
* **Recursive Bounding:** When using `recursive: true`, Nova pre-flights the file count to enforce safety bounds.

---

## 5. Related Tools

* [`nova.sftp_list`](nova-sftp-list.md)
* [`nova.sftp_rename`](nova-sftp-rename.md)
