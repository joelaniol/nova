# `nova.sftp_put`

Uploads a local file or directory tree of any size over SFTP, as a resumable background job.

---

## 1. Overview

`nova.sftp_put` uploads one local file, or a whole directory tree with `recursive: true`, from Downloads or Nova's host-verified current workspace. It needs the account's full capability and Nova's independent MutatingRemote policy. There is no size or file-count limit: the transfer runs as a background job; the call waits up to `wait` seconds (default 60) and otherwise returns `state: "running"` with a `jobId` - follow it with [`nova.sftp_transfer_status`](nova-sftp-transfer-status.md).

The local tree is checked before the approval prompt (no links or junctions, only names a server can take safely). Each file is written to a remote part next to its target at an explicit offset - never in append mode - and renamed into place only after the server holds exactly its size; the local modification time is set on the remote file. A local file that is replaced or changed during the upload is not committed. A dropped connection is reconnected up to five times; repeating the identical call resumes after a prefix check of the remote part. Existing targets are preserved unless `overwrite: true` is set.

* **Core Architecture Guide:** [SSH File Transfer Protocol (SFTP)](../../../core-features/connectors/sftp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Existing local source path inside Downloads or the host-verified current workspace. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote destination file or directory root. |
| `recursive` | `boolean` | No | `false` | — | Required for a directory source; transfers its whole tree. |
| `overwrite` | `boolean` | No | `false` | — | Replace existing remote destination files. False preserves them and the job fails with destination_changed before any byte is transferred. |
| `maxFiles` | `integer` | No | — | ≥ 1 | Optional budget: the job refuses to start (caller_limit_exceeded) when the checked plan has more files. Omit for no limit. |
| `maxBytes` | `integer` | No | — | ≥ 1 | Optional budget in bytes: the job refuses to start (caller_limit_exceeded) when the checked plan is larger. Omit for no limit. |
| `wait` | `integer` | No | `60` | 0–540 | Seconds the call waits for the job before returning state='running' with its jobId. 0 returns at once. The job continues after the wait either way. |
| `resumeJobId` | `string` | No | — | — | Optional: continue exactly this unfinished job. Without it, repeating the identical call resumes the newest unfinished job of the same transfer. |
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
    "localPath": "C:\\Users\\you\\Downloads\\site",
    "remotePath": "/var/www/site",
    "recursive": true,
    "wait": 0
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Upload tr_0b9e8d7c6a5f4e3d2c1b0a99 is running in the background (0 of 48211990 bytes). Poll nova.sftp_transfer_status(jobId='tr_0b9e8d7c6a5f4e3d2c1b0a99')."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "tr_0b9e8d7c6a5f4e3d2c1b0a99",
    "attempt": 1,
    "operation": "sftp_put",
    "profileId": "conn-sftp-01",
    "state": "scanning",
    "terminal": false,
    "running": true,
    "alreadyRunning": false,
    "resumed": false,
    "resumable": true,
    "progress": { "phase": "scanning", "bytesCompleted": 0, "bytesTotal": 48211990, "filesCompleted": 0, "filesTotal": 214 },
    "verification": { "requested": "size", "performed": "size", "result": null },
    "error": null,
    "suggestedPollMs": 5000,
    "nextAction": "poll_sftp_transfer_status"
  }
}
```

---

## 4. Operational Best Practices

* **Repeat, do not restart:** after `interrupted` or `stopped`, send the identical call again to resume the same job.
* **Do not touch the source while it uploads:** a local file that changes is not committed (`source_changed`); its remote part stays for the next attempt.
* **Overwrite Safety:** an existing remote target is refused before any byte moves (`destination_changed`) unless `overwrite: true` is set; with it, the old file is moved aside and removed only after the new one is in place.
* **Server space:** a write the server refuses (often quota or a full disk) stops the job with `remote_storage_limit`; the part stays resumable.

---

## 5. Related Tools

* [`nova.sftp_transfer_status`](nova-sftp-transfer-status.md)
* [`nova.sftp_transfer_stop`](nova-sftp-transfer-stop.md)
* [`nova.sftp_get`](nova-sftp-get.md)
* [`nova.sftp_list`](nova-sftp-list.md)
