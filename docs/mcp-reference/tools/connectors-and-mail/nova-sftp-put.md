# `nova.sftp_put`

Uploads a local file or directory tree over SFTP to a remote destination.

---

## 1. Overview

`nova.sftp_put` transfers files from the local workspace or Downloads directory to a remote SFTP host with atomic temporary write semantics.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (File Upload)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`localPath`** | `string` | Yes | `null` | Existing local source path inside Downloads or the host-verified current workspace. |
| **`maxBytes`** | `integer` | No | `1073741824` | Requested total-byte ceiling for this call; cannot exceed Nova's hard limit. |
| **`maxFiles`** | `integer` | No | `500` | Requested entry ceiling for this call; cannot exceed Nova's hard limit. |
| **`overwrite`** | `boolean` | No | `false` | Replace existing remote destination files. False preserves them and returns connector_remote_path_exists. |
| **`profileId`** | `string` | Yes | `null` | SFTP connector id from nova.connector_list. |
| **`recursive`** | `boolean` | No | `false` | Required for a directory source; transfers its bounded tree using one SFTP connection. |
| **`remotePath`** | `string` | Yes | `null` | Remote destination file or directory root. |
| **`unattended`** | `boolean` | No | `false` | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sftp_put",
  "arguments": {
    "profileId": "conn-sftp-01",
    "localPath": "reports/summary.json",
    "remotePath": "/var/www/incoming/summary.json",
    "overwrite": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Uploaded summary.json (4 KB) over SFTP."
    }
  ],
  "structuredContent": {
    "ok": true,
    "localPath": "reports/summary.json",
    "remotePath": "/var/www/incoming/summary.json",
    "bytesTransferred": 4096
  }
}
```

---

## 4. Operational Best Practices

* **Workspace Confinement:** Local source files must reside within the host-verified current workspace or Downloads directory.
* **Verification:** Verify uploaded files by calling [`nova.sftp_list`](nova-sftp-list.md) afterwards.

---

## 5. Related Tools

* [`nova.sftp_get`](nova-sftp-get.md)
* [`nova.sftp_rename`](nova-sftp-rename.md)
