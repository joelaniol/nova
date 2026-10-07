# `nova.ftp_rename`

Renames or moves a remote file or directory on an FTP/FTPS server.

---

## 1. Overview

`nova.ftp_rename` renames or moves one remote FTP/FTPS file or directory. Requires the connector's transfer-full access and Nova's independent global MutatingRemote confirmation policy. A missing source or a protected existing destination returns a truthful reasonCode; `overwrite: true` is limited to regular files — directories and links are never overwritten. A plaintext profile additionally needs the user's debug/legacy option plus `allowInsecure: true`.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Existing remote source path. |
| `destinationRemotePath` | `string` | Yes | — | ≤ 4096 characters | New remote destination path. |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing regular-file destination. Directories and links are never overwritten. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ftp_rename",
  "arguments": {
    "profileId": "conn-ftp-01",
    "remotePath": "/public_html/app.old.js",
    "destinationRemotePath": "/public_html/app.bak.js"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Renamed the remote path via 'Web Host'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-ftp-01",
    "status": "renamed",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 70,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [],
    "transferredCount": 0,
    "transferredBytes": 0,
    "affectedRemotePaths": [
      "/public_html/app.old.js",
      "/public_html/app.bak.js"
    ],
    "affectedLocalPaths": []
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Deployments:** Deploy new code by uploading to a staging name with [`nova.ftp_put`](nova-ftp-put.md) and renaming it into place.
* **Overwrite Is File-Only:** `overwrite: true` replaces an existing regular-file destination only; an existing directory or link destination is never overwritten.

---

## 5. Related Tools

* [`nova.ftp_put`](nova-ftp-put.md)
* [`nova.ftp_delete`](nova-ftp-delete.md)
