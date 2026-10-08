# `nova.sftp_rename`

Renames or moves a remote file or directory over SFTP.

---

## 1. Overview

`nova.sftp_rename` renames or moves one remote path. Requires the connector's full capability and Nova's independent global MutatingRemote confirmation policy. An existing destination is preserved unless `overwrite: true`; overwriting a regular file goes through a bounded sibling-recovery stage, and an interrupted stage reports `stateIndeterminate: true` with the paths to inspect rather than claiming success. A missing source or a protected existing destination returns a truthful reasonCode and `changed: false`. SSH host-key trust remains human-only in Settings.

* **Core Architecture Guide:** [SSH File Transfer Protocol (SFTP)](../../../core-features/connectors/sftp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Existing source path. |
| `destinationRemotePath` | `string` | Yes | — | ≤ 4096 characters | New remote destination path. |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing regular-file destination through a bounded sibling recovery stage. An interrupted stage returns stateIndeterminate and paths to inspect. False preserves the destination. |
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
  "name": "nova.sftp_rename",
  "arguments": {
    "profileId": "conn-sftp-01",
    "remotePath": "/var/www/incoming/summary.json",
    "destinationRemotePath": "/var/www/processed/summary.json"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Renamed the remote path via 'Production Server'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-sftp-01",
    "status": "renamed",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 60,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [],
    "transferredCount": 0,
    "transferredBytes": 0,
    "affectedRemotePaths": [
      "/var/www/incoming/summary.json",
      "/var/www/processed/summary.json"
    ],
    "affectedLocalPaths": []
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Staging:** Upload to a staging file name with [`nova.sftp_put`](nova-sftp-put.md) and rename to the target name to ensure downstream services see complete files.
* **Interrupted Overwrite:** If `overwrite: true` is interrupted mid-stage, the result sets `stateIndeterminate: true` and names the paths to inspect instead of claiming either outcome.

---

## 5. Related Tools

* [`nova.sftp_put`](nova-sftp-put.md)
* [`nova.sftp_delete`](nova-sftp-delete.md)
