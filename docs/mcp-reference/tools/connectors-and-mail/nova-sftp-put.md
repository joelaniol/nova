# `nova.sftp_put`

Uploads a local file or directory tree over SFTP to a remote destination.

---

## 1. Overview

`nova.sftp_put` uploads one local file, or a bounded directory tree with `recursive: true`, from Downloads or Nova's host-verified current workspace. Each file uploads to a unique remote temporary name and is renamed into place only after it is verified complete; the local file's modification time is preserved on the remote copy. The local source is checked against Nova's path policy (including a local tree walk for `recursive: true`) before any approval prompt or SSH login, so a request that could never run is never shown to the user. Requires the connector's full capability and is also subject to Nova's independent global MutatingRemote confirmation policy. SSH host-key trust remains human-only in Settings.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Uploaded 1 file(s) via 'Production Server' (4096 bytes)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-sftp-01",
    "status": "uploaded",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 310,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [
      {
        "source": "reports/summary.json",
        "destination": "/var/www/incoming/summary.json",
        "size": 4096,
        "lastWriteUtc": "2026-10-02T09:00:00Z",
        "sourceTrust": "host_verified_local_path",
        "destinationTrust": "untrusted_remote_state"
      }
    ],
    "transferredCount": 1,
    "transferredBytes": 4096,
    "affectedRemotePaths": ["/var/www/incoming/summary.json"],
    "affectedLocalPaths": []
  }
}
```

---

## 4. Operational Best Practices

* **Workspace Confinement:** Local source files must reside within the host-verified current workspace or Downloads directory; this is checked before any prompt is shown.
* **Overwrite Safety:** An existing remote regular-file destination is refused with `reasonCode: "connector_remote_path_exists"` unless `overwrite: true` is set.
* **Verification:** Verify uploaded files by calling [`nova.sftp_list`](nova-sftp-list.md) afterwards.

---

## 5. Related Tools

* [`nova.sftp_get`](nova-sftp-get.md)
* [`nova.sftp_rename`](nova-sftp-rename.md)
