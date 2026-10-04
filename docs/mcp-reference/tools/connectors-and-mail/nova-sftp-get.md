# `nova.sftp_get`

Downloads a remote file or directory tree over SFTP into Downloads or the workspace.

---

## 1. Overview

`nova.sftp_get` downloads one remote file, or a bounded directory tree with `recursive: true`, into Downloads or Nova's host-verified current workspace. Each file is staged under a temporary local name and committed only after its byte count matches what the server reported; the remote file's modification time is preserved on the local copy. The local destination is checked against Nova's path policy before any approval prompt or connection is opened, so a request that could never be written is never shown to the user. Nova verifies the human-confirmed SSH host key before authenticating; agents can neither see nor approve fingerprints.

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

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Downloaded 1 file(s) via 'Production Server' (12040 bytes)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-sftp-01",
    "status": "downloaded",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 540,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [
      {
        "source": "/var/www/reports/daily.csv",
        "destination": "downloads/daily.csv",
        "size": 12040,
        "lastWriteUtc": "2026-10-02T16:00:00Z",
        "sourceTrust": "untrusted_remote_state",
        "destinationTrust": "host_verified_local_path"
      }
    ],
    "transferredCount": 1,
    "transferredBytes": 12040,
    "affectedRemotePaths": [],
    "affectedLocalPaths": ["downloads/daily.csv"]
  }
}
```
A destination that already exists and was not overwritten is refused with `reasonCode: "connector_local_path_exists"` rather than silently skipped.

---

## 4. Operational Best Practices

* **Bounded Transfers:** `maxBytes`/`maxFiles` cap this single call; Nova's hard ceiling is 500 files and 1 GiB regardless of what is requested. Use `recursive: true` only for a directory source.
* **Overwrite Safety:** A destination that already exists is refused unless `overwrite: true` is set; nothing is downloaded over it silently.
* **Local Path Is Pre-Checked:** `localPath` must resolve inside Downloads or the host-verified current workspace; a path outside those roots is refused before any prompt, with `reasonCode: "local_path_not_allowed"`.

---

## 5. Related Tools

* [`nova.sftp_put`](nova-sftp-put.md)
* [`nova.sftp_list`](nova-sftp-list.md)
