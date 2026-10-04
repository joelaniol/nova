# `nova.sftp_get`

Downloads a remote file or directory tree of any size over SFTP into Downloads or the workspace, as a resumable background job.

---

## 1. Overview

`nova.sftp_get` downloads one remote file, or a whole directory tree with `recursive: true`, into Downloads or Nova's host-verified current workspace. There is no size or file-count limit: the transfer runs as a background job. The call waits up to `wait` seconds (default 60); a job that is not finished by then is reported with `state: "running"` and a `jobId`, and keeps running - follow it with [`nova.sftp_transfer_status`](nova-sftp-transfer-status.md), stop it with [`nova.sftp_transfer_stop`](nova-sftp-transfer-stop.md).

Before any byte is written, the whole remote tree is listed and checked: a symbolic link, a special file, or a name Windows cannot store stops the job with nothing written. Each file is written to a part file next to its target and committed only after its size matches and the remote file is unchanged; the remote modification time is kept. A dropped connection is reconnected up to five times and continues at the part's offset. Repeating the identical call attaches to a running job or resumes an unfinished one - a part is only continued after Nova has proven that it is a prefix of the current remote file. The local destination is checked against Nova's path policy before any approval prompt or connection. Nova verifies the human-confirmed SSH host key on every connection; agents can neither see nor approve fingerprints.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Local destination path inside Downloads or the host-verified current workspace. For a remote directory, this is the destination root. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote file or directory path to download. |
| `recursive` | `boolean` | No | `false` | — | Required for a directory source; transfers its whole tree. |
| `overwrite` | `boolean` | No | `false` | — | Replace existing local destination files. False preserves them and the job fails with destination_changed before any byte is transferred. |
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
  "name": "nova.sftp_get",
  "arguments": {
    "profileId": "conn-sftp-01",
    "remotePath": "/backups/db-full.tar",
    "localPath": "C:\\Users\\you\\Downloads\\db-full.tar",
    "wait": 60
  }
}
```

### JSON-RPC Response (still running after `wait`)
```json
{
  "content": [
    {
      "type": "text",
      "text": "Download tr_4f1c2a9b7d3e5f60718293a4 is running in the background (21474836480 of 322122547200 bytes). Poll nova.sftp_transfer_status(jobId='tr_4f1c2a9b7d3e5f60718293a4')."
    }
  ],
  "structuredContent": {
    "ok": true,
    "jobId": "tr_4f1c2a9b7d3e5f60718293a4",
    "attempt": 1,
    "operation": "sftp_get",
    "profileId": "conn-sftp-01",
    "state": "transferring",
    "terminal": false,
    "running": true,
    "alreadyRunning": false,
    "resumed": false,
    "resumable": true,
    "progress": {
      "phase": "transferring",
      "bytesCompleted": 21474836480,
      "bytesTotal": 322122547200,
      "filesCompleted": 0,
      "filesTotal": 1,
      "currentFile": "",
      "currentFileBytes": 21474836480,
      "currentFileTotal": 322122547200,
      "rateBytesPerSecond": 357913941,
      "etaSeconds": 840
    },
    "verification": { "requested": "size", "performed": "size", "result": null },
    "error": null,
    "remotePath": "/backups/db-full.tar",
    "remotePathTrust": "untrusted_remote_state",
    "localPath": "C:\\Users\\you\\Downloads\\db-full.tar",
    "localPathTrust": "host_verified_local_path",
    "createdUtc": "2026-10-04T08:10:00.0000000+00:00",
    "updatedUtc": "2026-10-04T08:11:00.0000000+00:00",
    "suggestedPollMs": 5000,
    "nextAction": "poll_sftp_transfer_status"
  }
}
```
When the job finishes within `wait`, the same fields come back with `state: "completed"`, `terminal: true` and `verification.result: "passed"`.

---

## 4. Operational Best Practices

* **Repeat, do not restart:** after `interrupted` or `stopped`, send the identical call again - it resumes the same job (`resumed: true`, `attempt` + 1). Changing any argument makes it a different transfer.
* **Overwrite Safety:** an existing local target is refused before any byte moves (`error.code: "destination_changed"`) unless `overwrite: true` is set.
* **Free space is checked first:** a download that cannot fit on the target drive (with a reserve) stops with `target_full` before it starts.
* **Local Path Is Pre-Checked:** `localPath` must resolve inside Downloads or the host-verified current workspace; a path outside those roots is refused before any prompt, with `reasonCode: "local_path_not_allowed"`.

---

## 5. Related Tools

* [`nova.sftp_transfer_status`](nova-sftp-transfer-status.md)
* [`nova.sftp_transfer_stop`](nova-sftp-transfer-stop.md)
* [`nova.sftp_put`](nova-sftp-put.md)
* [`nova.sftp_list`](nova-sftp-list.md)
