# `nova.sftp_delete`

Deletes a remote file, empty directory, or bounded directory tree over SFTP.

---

## 1. Overview

`nova.sftp_delete` removes one remote file or empty directory; `recursive: true` deletes a non-empty directory tree after Nova preflights it against the `maxFiles`/`maxBytes` ceilings. Requires the connector's full capability and Nova's independent global MutatingRemote confirmation policy. A missing path is reported as a failure with `reasonCode: "connector_remote_path_not_found"` and `changed: false` — never a silent success. SSH host-key trust remains human-only in Settings.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote file or directory to delete. |
| `recursive` | `boolean` | No | `false` | — | Delete a non-empty directory tree after enforcing maxFiles/maxBytes. False deletes only a file or empty directory. |
| `maxFiles` | `integer` | No | `500` | 1–500 | Requested entry ceiling for a recursive delete; cannot exceed Nova's per-call blast-radius limit. |
| `maxBytes` | `integer` | No | `1073741824` | 1–1073741824 | Requested total-byte ceiling for a recursive delete; cannot exceed Nova's per-call blast-radius limit. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Deleted 1 remote path(s) via 'Production Server'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-sftp-01",
    "status": "deleted",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 95,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [],
    "transferredCount": 0,
    "transferredBytes": 0,
    "affectedRemotePaths": ["/var/www/incoming/old-report.csv"],
    "affectedLocalPaths": []
  }
}
```

---

## 4. Operational Best Practices

* **High-Impact Action:** Deletions are permanent on remote hosts; double-check remote paths before calling.
* **Recursive Bounding:** `recursive: true` deletes a non-empty directory tree only after Nova preflights it against `maxFiles`/`maxBytes`; a tree that exceeds either ceiling is refused before anything is deleted.
* **Missing Path Is Not Success:** A path that no longer exists returns a failure (`connector_remote_path_not_found`, `changed: false`), not a quiet `ok`.

---

## 5. Related Tools

* [`nova.sftp_list`](nova-sftp-list.md)
* [`nova.sftp_rename`](nova-sftp-rename.md)
