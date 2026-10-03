# `nova.sftp_get`

Downloads a remote file or directory tree over SFTP into Downloads or the workspace.

---

## 1. Overview

`nova.sftp_get` securely transfers files from a remote SFTP server to the local system. Supports single file downloads or bounded recursive directory tree fetching.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (File Transfer)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Local destination path inside Downloads or the host-verified current workspace. For a remote directory, this is the destination root. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote file or directory path to download. |
| `recursive` | `boolean` | No | `false` | — | Required for a directory source; transfers its bounded tree using one SFTP connection. |
| `overwrite` | `boolean` | No | `false` | — | Replace existing local destination files. False preserves them and returns connector_local_path_exists. |
| `maxFiles` | `integer` | No | `500` | 1–500 | Requested entry ceiling for this call; cannot exceed Nova's hard limit. |
| `maxBytes` | `integer` | No | `1073741824` | 1–1073741824 | Requested total-byte ceiling for this call; cannot exceed Nova's hard limit. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sftp_get",
  "arguments": {
    "profileId": "conn-sftp-01",
    "remotePath": "/var/www/reports/daily.csv",
    "localPath": "downloads/daily.csv"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Downloaded daily.csv (12 KB)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "remotePath": "/var/www/reports/daily.csv",
    "localPath": "downloads/daily.csv",
    "bytesTransferred": 12040
  }
}
```

---

## 4. Operational Best Practices

* **Bounded Transfers:** Use `maxBytes` and `maxFiles` when enabling `recursive: true` to prevent accidental multi-gigabyte downloads.
* **Overwrite Safety:** Fails if destination file exists unless `overwrite: true` is explicitly provided.

---

## 5. Related Tools

* [`nova.sftp_put`](nova-sftp-put.md)
* [`nova.sftp_list`](nova-sftp-list.md)
