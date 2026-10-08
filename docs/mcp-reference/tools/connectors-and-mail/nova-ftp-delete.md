# `nova.ftp_delete`

Deletes a remote regular file or empty directory on an FTP/FTPS server.

---

## 1. Overview

`nova.ftp_delete` deletes one remote FTP/FTPS regular file or empty directory. Requires the connector's transfer-full access and Nova's independent global MutatingRemote confirmation policy. Recursive delete is intentionally not exposed; a missing path or a non-empty directory never reports success. A plaintext profile additionally needs the user's debug/legacy option plus `allowInsecure: true`.

* **Core Architecture Guide:** [FTP & FTPS](../../../core-features/connectors/ftp-and-ftps/README.md)

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

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Deleted 1 remote path(s) via 'Web Host'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-ftp-01",
    "status": "deleted",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 85,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [],
    "transferredCount": 0,
    "transferredBytes": 0,
    "affectedRemotePaths": ["/public_html/temp.txt"],
    "affectedLocalPaths": []
  }
}
```

---

## 4. Operational Best Practices

* **Empty Directories Only:** A non-empty directory is refused rather than deleted; delete its contents first. There is no recursive delete on this tool.
* **Missing Path Is Not Success:** A path that no longer exists is reported as a failure, not a quiet `ok`.

---

## 5. Related Tools

* [`nova.ftp_list`](nova-ftp-list.md)
* [`nova.ftp_rename`](nova-ftp-rename.md)
