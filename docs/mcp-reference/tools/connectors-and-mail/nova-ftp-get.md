# `nova.ftp_get`

Downloads a remote regular file over FTP/FTPS into Downloads or the workspace.

---

## 1. Overview

`nova.ftp_get` downloads one remote regular file over FTP/FTPS into Downloads or Nova's host-verified current workspace. Requires the connector's transfer-read access plus Nova's persistent-write policy. The file is staged through an already-validated local handle and committed only after its exact byte count is received; an existing destination is preserved unless `overwrite: true`. Remote links and directory recursion are intentionally rejected — this tool transfers exactly one regular file. A plaintext profile additionally needs the user's debug/legacy option plus `allowInsecure: true`.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Local destination inside Downloads or the host-verified current workspace. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote regular file to download. |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing local destination file. False preserves it. |
| `maxBytes` | `integer` | No | — | ≥ 1 | Optional budget in bytes: the job refuses to start (caller_limit_exceeded) when the file is larger. Omit for no limit. |
| `wait` | `integer` | No | `60` | 0–540 | Seconds the call waits for the job before returning state='running' with its jobId. 0 returns at once. The job continues after the wait either way. |
| `resumeJobId` | `string` | No | — | — | Optional: continue exactly this unfinished job. Without it, repeating the identical call resumes the newest unfinished job of the same transfer. |
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
  "name": "nova.ftp_get",
  "arguments": {
    "profileId": "conn-ftp-01",
    "remotePath": "/public_html/assets/logo.svg",
    "localPath": "assets/logo.svg"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Downloaded 1 file(s) via 'Web Host' (8192 bytes)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-ftp-01",
    "status": "downloaded",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 430,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [
      {
        "source": "/public_html/assets/logo.svg",
        "destination": "assets/logo.svg",
        "size": 8192,
        "lastWriteUtc": "2026-10-02T12:00:00Z",
        "sourceTrust": "untrusted_remote_state",
        "destinationTrust": "host_verified_local_path"
      }
    ],
    "transferredCount": 1,
    "transferredBytes": 8192,
    "affectedRemotePaths": [],
    "affectedLocalPaths": ["assets/logo.svg"]
  }
}
```

---

## 4. Operational Best Practices

* **Path Security:** `localPath` is checked against Downloads/workspace roots before any prompt or connection; a path outside those roots is refused with `reasonCode: "local_path_not_allowed"`.
* **Overwrite Safety:** An existing local destination is preserved unless `overwrite: true` is set.
* **Single File Only:** There is no `recursive` option here; a remote directory or link is rejected rather than followed.

---

## 5. Related Tools

* [`nova.ftp_put`](nova-ftp-put.md)
* [`nova.ftp_list`](nova-ftp-list.md)
