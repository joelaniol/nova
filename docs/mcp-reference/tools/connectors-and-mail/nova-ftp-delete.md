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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote regular file or empty directory to delete. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

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
