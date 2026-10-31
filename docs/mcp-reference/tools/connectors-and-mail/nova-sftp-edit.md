# `nova.sftp_edit`

Changes a text file on the server over an SFTP connection with exact replacements, a backup copy and an atomic swap — the safe replacement for `sed -i`.

---

## 1. Overview

`nova.sftp_edit` reads a remote text file, applies a list of `{old, new}` replacements and writes the result back. It is meant for configuration files such as `sshd_config`, an nginx site, `php.ini` or an `.env` file, where a `sed -i` expression through `nova.ssh_run` breaks on `|`, `/` or `&` in the content and gives no way back. It uses the same **human-verified host-key gate** as every other SFTP operation.

* **Capability:** needs the account's `full` capability plus Nova's independent MutatingRemote policy.
* **Literal text, exactly once.** Each `old` is plain text — no regular expression and no escaping. It must occur **exactly once** in the file (after the earlier replacements in the same call were applied). If it occurs zero times or more than once, **nothing is written**; the error names the replacement (`failedIndex`) and, for several matches, the line numbers (`matchLines`).
* **All or nothing.** Up to 50 replacements per call. Either every one applies or the file stays as it was.
* **Backup next to the file.** Unless `backup=false`, the previous version is kept as `<file>.nova-bak-<yyyyMMddTHHmmssZ>` (UTC) in the same directory. An existing file is never overwritten; the new name gets a suffix instead. `backupPath` in the result names it.
* **Mode and owner are kept.** The new version gets the old file's permissions before any content is written, and its owner and group. If this login cannot give the file its owner back, the call fails with nothing changed — connect as that user or as root.
* **Atomic swap.** The new content is written to a hidden file in the same directory and renamed over the original, so a reader never sees a half-written file. `replaceMode` says how: `posix_rename` (one atomic step) or `recovery_swap` on servers without that SFTP extension.
* **Concurrent changes are refused.** Pass `expectSha256` (the `sha256Before` of an earlier call, or `sha256sum` output) and the call fails with `connector_remote_content_changed` if the file is not that version any more. The file is also checked again right before the swap.
* **Text files only.** UTF-8 text up to 1 MiB; a byte-order mark and the file's line endings are kept. Binary or other encodings fail with `connector_remote_not_text` — use `nova.sftp_get` and `nova.sftp_put` for those. A symbolic link is refused; edit the file it points to.
* **What you get back.** The changed lines of each replacement (`hunks`, whole lines with line numbers), `sha256Before`/`sha256After`, and `verified=true` when the file read back after the swap has exactly the expected content. Hunks are server text (`hunksTrust=untrusted_remote_state`); password hashes and private keys in them are masked.

* **Core Architecture Guides:** [SFTP Directory Inspection & Filesystem Mutations](../../../core-features/connectors/sftp/directory-inspection-and-filesystem-mutations/README.md) · [SFTP Architecture Hub](../../../core-features/connectors/sftp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Absolute path of the text file to edit, e.g. /etc/ssh/sshd_config. |
| `replacements` | `array` of `object` | Yes | — | 1–50 items | Exact replacements, applied in order (each sees the result of the previous ones). 'old' must occur exactly once; whitespace and line endings count. |
| `expectSha256` | `string` | No | — | — | Optional SHA-256 (hex) of the file as you read it; the edit is refused when the server copy differs. |
| `backup` | `boolean` | No | `true` | — | Keep the old version as <file>.nova-bak-<yyyyMMddTHHmmssZ> next to the file, with the same mode. Default true. |
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
  "name": "nova.sftp_edit",
  "arguments": {
    "profileId": "cn_9f2c41",
    "remotePath": "/etc/ssh/sshd_config",
    "replacements": [
      { "old": "PermitRootLogin yes", "new": "PermitRootLogin prohibit-password" },
      { "old": "#PasswordAuthentication yes", "new": "PasswordAuthentication no" }
    ]
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "status": "edited",
    "changed": true,
    "remotePath": "/etc/ssh/sshd_config",
    "backupPath": "/etc/ssh/sshd_config.nova-bak-20261031T141205Z",
    "sha256Before": "3f1c…",
    "sha256After": "a90e…",
    "verified": true,
    "lineEndings": "lf",
    "replaceMode": "posix_rename",
    "mode": "644",
    "uid": 0,
    "gid": 0,
    "hunks": [
      { "index": 0, "line": 33, "removed": ["PermitRootLogin yes"], "added": ["PermitRootLogin prohibit-password"], "truncated": false },
      { "index": 1, "line": 57, "removed": ["#PasswordAuthentication yes"], "added": ["PasswordAuthentication no"], "truncated": false }
    ],
    "hunksTrust": "untrusted_remote_state"
  }
}
```

### Error when `old` matches twice (shortened)
```json
{
  "code": -32000,
  "data": {
    "reasonCode": "connector_remote_edit_ambiguous",
    "details": {
      "changed": false,
      "failedIndex": 1,
      "matchCount": 2,
      "matchLines": [12, 40],
      "nextAction": "extend_old_with_neighbouring_lines_until_it_matches_once"
    }
  }
}
```

---

## 4. Operational Best Practices

* **Read first, copy exactly.** Get the file with `nova.ssh_run` (`cat`) or `nova.sftp_get` and copy `old` character for character, including indentation. For a file with CRLF line endings, a multi-line `old` needs `\r\n`.
* **Make `old` unique with context.** If a line occurs several times (`listen 80;` in two server blocks), include the neighbouring line that tells them apart.
* **To insert a line,** use a neighbouring line as `old` and that line plus the new one as `new`.
* **Check the service after the change** (`nginx -t`, `sshd -t`, `systemctl reload …`) with `nova.ssh_run`. To undo, copy the backup back with `nova.ssh_run` (`cp -p <backupPath> <file>`).
* **Clean up old backups** with `nova.sftp_delete` once the change is confirmed.

---

## 5. Related Tools

* [`nova.sftp_get`](nova-sftp-get.md) — Downloads a file, also for files `sftp_edit` does not handle
* [`nova.sftp_put`](nova-sftp-put.md) — Uploads a whole file
* [`nova.sftp_delete`](nova-sftp-delete.md) — Removes old backup copies
* [`nova.ssh_run`](nova-ssh-run.md) — Reads the file and checks the service after the change
* [`nova.connector_history`](nova-connector-history.md) — Lists edits with their backup paths
