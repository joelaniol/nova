# `nova.ftp_put`

Uploads a local regular file over FTP/FTPS to a remote server.

---

## 1. Overview

`nova.ftp_put` uploads one policy-approved local regular file over FTP/FTPS. Requires the connector's transfer-full access and Nova's independent global MutatingRemote confirmation policy. Nova writes a unique remote staging file, verifies its byte count, and renames it into place; an existing destination is preserved unless `overwrite: true`. Directory recursion and remote links are intentionally rejected — this tool uploads exactly one regular file. A plaintext profile additionally needs the user's debug/legacy option plus `allowInsecure: true`.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Existing local regular file inside Downloads or the host-verified current workspace. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote destination file (or an existing directory that receives the local filename). |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing regular-file destination. False preserves it. |
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
  "name": "nova.ftp_put",
  "arguments": {
    "profileId": "conn-ftp-01",
    "localPath": "dist/app.js",
    "remotePath": "/public_html/app.js",
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
      "text": "Uploaded 1 file(s) via 'Web Host' (122880 bytes)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-ftp-01",
    "status": "uploaded",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 980,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [],
    "returnedCount": 0,
    "hasMore": false,
    "files": [
      {
        "source": "dist/app.js",
        "destination": "/public_html/app.js",
        "size": 122880,
        "lastWriteUtc": "2026-10-02T09:00:00Z",
        "sourceTrust": "host_verified_local_path",
        "destinationTrust": "untrusted_remote_state"
      }
    ],
    "transferredCount": 1,
    "transferredBytes": 122880,
    "affectedRemotePaths": ["/public_html/app.js"],
    "affectedLocalPaths": []
  }
}
```

---

## 4. Operational Best Practices

* **Overwrites:** Specify `overwrite: true` when replacing existing remote assets; otherwise an existing destination is preserved and the call fails rather than silently skipping.
* **Single File Only:** There is no `recursive` option; upload a directory by calling this tool once per file.

---

## 5. Related Tools

* [`nova.ftp_get`](nova-ftp-get.md)
* [`nova.ftp_rename`](nova-ftp-rename.md)
