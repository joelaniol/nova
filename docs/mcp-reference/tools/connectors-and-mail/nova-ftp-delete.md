# `nova.ftp_delete`

Deletes a remote regular file or empty directory on an FTP/FTPS server.

---

## 1. Overview

`nova.ftp_delete` removes a file or empty folder on an FTP/FTPS host. Destructive operations require transfer full access capability.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 3 (Destructive Deletion)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |
| **`profileId`** | `string` | Yes | `null` | FTP connector id from nova.connector_list. |
| **`remotePath`** | `string` | Yes | `null` | Remote regular file or empty directory to delete. |
| **`unattended`** | `boolean` | No | `false` | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ftp_delete",
  "arguments": {
    "profileId": "conn-ftp-01",
    "remotePath": "/public_html/temp.txt"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted remote FTP file /public_html/temp.txt."
    }
  ],
  "structuredContent": {
    "ok": true,
    "deletedPath": "/public_html/temp.txt"
  }
}
```

---

## 4. Operational Best Practices

* **Empty Directories:** FTP protocols require directories to be empty before deletion; delete child files first.

---

## 5. Related Tools

* [`nova.ftp_list`](nova-ftp-list.md)
* [`nova.ftp_rename`](nova-ftp-rename.md)
