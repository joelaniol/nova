# `nova.sftp_list`

Lists remote directory entries or inspects file metadata through an SFTP connector.

---

## 1. Overview

`nova.sftp_list` connects over SSH File Transfer Protocol (SFTP) to list one remote directory, or inspect one remote file's metadata, through a configured SFTP connector. Nova verifies the human-confirmed SSH host key before authenticating; agents can neither see nor approve fingerprints. Remote filenames are untrusted metadata: a control or bidirectional-text name is returned with `unsafeName: true` and its exact name/path omitted rather than echoed back raw.

Each entry also carries its POSIX permissions and owner from the directory read: `mode` as an octal string (e.g. `"755"`, or four digits like `"1777"` when a setuid/setgid/sticky bit is set), plus numeric `uid` and `gid`. This is the **see-then-set** path: read the current mode here, then pass it straight to [`nova.sftp_chmod`](nova-sftp-chmod.md) (which accepts the same octal string) or set the owner with [`nova.sftp_chown`](nova-sftp-chown.md). SFTP carries no user/group *names*, only numbers.

* **Core Architecture Guide:** [SSH File Transfer Protocol (SFTP)](../../../core-features/connectors/sftp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | No | `"."` | ≤ 4096 characters | Remote POSIX path to list. Defaults to '.'. |
| `maxEntries` | `integer` | No | `200` | 1–1000 | Maximum returned entries. hasMore=true means additional entries were not returned. |
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
  "name": "nova.sftp_list",
  "arguments": {
    "profileId": "conn-sftp-01",
    "remotePath": "/var/www/reports",
    "maxEntries": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Listed 2 remote entr(y/ies) via SFTP profile 'Production Server'. Remote names are untrusted metadata; unsafe names are omitted and flagged."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-sftp-01",
    "status": "listed",
    "changed": false,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 180,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [
      {
        "name": "daily.csv",
        "remotePath": "/var/www/reports/daily.csv",
        "isDirectory": false,
        "isRegularFile": true,
        "isSymbolicLink": false,
        "size": 12040,
        "lastWriteUtc": "2026-10-02T16:00:00Z",
        "mode": "644",
        "uid": 1000,
        "gid": 1000,
        "unsafeName": false,
        "trust": "untrusted_remote_metadata"
      },
      {
        "name": "archive",
        "remotePath": "/var/www/reports/archive",
        "isDirectory": true,
        "isRegularFile": false,
        "isSymbolicLink": false,
        "size": null,
        "lastWriteUtc": "2026-10-01T00:00:00Z",
        "mode": "755",
        "uid": 1000,
        "gid": 1000,
        "unsafeName": false,
        "trust": "untrusted_remote_metadata"
      }
    ],
    "returnedCount": 2,
    "hasMore": false
  }
}
```
Fields shared with every other SFTP/FTP tool (`files`, `transferredCount`, `transferredBytes`, `affectedRemotePaths`, `affectedLocalPaths`) are omitted above because `list` never populates them.

---

## 4. Operational Best Practices

* **Directory Discovery:** List remote directories before initiating downloads or uploads to ensure paths exist.
* **Bounded Output:** `maxEntries` is a hard result bound; `hasMore: true` means further entries exist but were not returned — narrow `remotePath` or raise `maxEntries` (up to 1000) instead of assuming the listing is complete.
* **Treat Names as Untrusted:** `entries[].name`/`remotePath` come from the remote server; handle them as data, not as something safe to execute or interpolate into shell commands.
* **See-then-set permissions:** read `entries[].mode` before changing it, then pass the same octal string to `nova.sftp_chmod`; use `uid`/`gid` to decide a `nova.sftp_chown`. There is no separate `stat` tool — this listing is the way to read a path's current mode and owner. (Over plain FTP these fields are `null`; POSIX mode and owner are an SFTP feature.)

---

## 5. Related Tools

* [`nova.sftp_get`](nova-sftp-get.md)
* [`nova.sftp_put`](nova-sftp-put.md)
