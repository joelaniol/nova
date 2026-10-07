# `nova.sftp_chmod`

Changes the POSIX permissions of a remote file or directory over an SFTP connection.

---

## 1. Overview

`nova.sftp_chmod` sets the permission bits of one existing file or directory on the server behind an SFTP connection. It uses the same **human-verified host-key gate** as every other SFTP operation: an unconfirmed or changed host key stops the connection before any credential is sent, and only a person can confirm a host key in Settings.

* **Capability:** needs the account's `full` capability plus Nova's independent MutatingRemote policy.
* **Octal mode.** `mode` is required and given as octal digits, e.g. `"644"`, `"755"`, `"1777"` (a leading `"0"` or `"0o"` is accepted). The digits are read as an octal permission, so `"755"` means `rwxr-xr-x`.
* **Symbolic links are refused.** An SFTP `SETSTAT` follows the final path component on the server, so a `chmod` on a link would change the link's **target**. Nova rejects a symbolic-link leaf outright rather than touch an unintended file.
* **Truthful not-found.** A missing path returns `connector_remote_path_not_found` with `changed=false`, never a false success. A path that is neither a regular file nor a directory is rejected.
* **Honest indeterminate state.** If the connection drops around the `SETSTAT`, `stateIndeterminate=true` says Nova could not confirm whether the mode changed — inspect the server before retrying.
* **Remote paths are untrusted.** Returned paths carry `remotePathTrust=untrusted_remote_state`; treat them as data from the server.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote file or directory whose permissions change. |
| `mode` | `string` | Yes | — | — | POSIX permission bits as 3-4 octal digits, e.g. "644", "755", "1777". A leading "0" or "0o" is accepted. |
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
  "name": "nova.sftp_chmod",
  "arguments": {
    "profileId": "cn_9f2c41",
    "remotePath": "/srv/app/deploy.sh",
    "mode": "750"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "schemaVersion": "1",
    "ok": true,
    "status": "permissions_changed",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "affectedRemotePaths": ["/srv/app/deploy.sh"],
    "affectedRemotePathsTrust": "untrusted_remote_state"
  }
}
```

---

## 4. Operational Best Practices

* **Pass the mode as octal digits.** `"755"` is `rwxr-xr-x`, `"644"` is `rw-r--r--`, `"700"` is `rwx------`. Nova reads the digits as octal, not as a decimal number.
* **chmod does not create.** The path must already exist; a missing path returns `connector_remote_path_not_found`. Use [`nova.sftp_mkdir`](nova-sftp-mkdir.md) to create a directory (optionally with its mode) first.
* **Links are intentionally rejected.** If you need to change a link target's mode, pass the target's real path, not the link.
* **Respect `stateIndeterminate`.** If it is true, the connection dropped around the change; verify the file's mode on the server before setting it again.
