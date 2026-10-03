# `nova.sftp_put`

Uploads a local file or directory tree over SFTP to a remote destination.

---

## 1. Overview

`nova.sftp_put` transfers files from the local workspace or Downloads directory to a remote SFTP host with atomic temporary write semantics.

* **Security Tier:** Tier 2 (File Upload)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Existing local source path inside Downloads or the host-verified current workspace. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote destination file or directory root. |
| `recursive` | `boolean` | No | `false` | — | Required for a directory source; transfers its bounded tree using one SFTP connection. |
| `overwrite` | `boolean` | No | `false` | — | Replace existing remote destination files. False preserves them and returns connector_remote_path_exists. |
| `maxFiles` | `integer` | No | `500` | 1–500 | Requested entry ceiling for this call; cannot exceed Nova's hard limit. |
| `maxBytes` | `integer` | No | `1073741824` | 1–1073741824 | Requested total-byte ceiling for this call; cannot exceed Nova's hard limit. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
<!-- /generated:parameters -->

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
