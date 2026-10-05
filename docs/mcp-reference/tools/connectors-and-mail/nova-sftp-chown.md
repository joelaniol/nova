# `nova.sftp_chown`

Changes the owner and/or group of a remote file or directory over an SFTP connection.

---

## 1. Overview

`nova.sftp_chown` sets the numeric owner (uid) and/or group (gid) of one existing file or directory on the server behind an SFTP connection. It uses the same **human-verified host-key gate** as every other SFTP operation: an unconfirmed or changed host key stops the connection before any credential is sent, and only a person can confirm a host key in Settings.

* **Capability:** needs the account's `full` capability plus Nova's independent MutatingRemote policy.
* **Numeric ids only.** SFTP does not resolve names, so `uid`/`gid` are numbers (e.g. `33` for `www-data` on Debian). Pass `uid`, `gid`, or both — at least one. The id you leave out keeps its current value. To find the numbers, read them with `nova.ssh_run` (`stat -c '%u %g' path` or `id -u www-data`).
* **Symbolic links are refused.** An SFTP `SETSTAT` follows the final path component, so a `chown` on a link would change the link's **target**. Nova rejects a symbolic-link leaf rather than touch an unintended file.
* **Usually root-only.** Most servers only let root change ownership; a non-root connection will get a permission error (reported truthfully, nothing changed).
* **Truthful not-found / indeterminate.** A missing path returns `connector_remote_path_not_found` with `changed=false`. If the connection drops around the change, `stateIndeterminate=true` says Nova could not confirm it — inspect the server before retrying.
* **Remote paths are untrusted.** Returned paths carry `remotePathTrust=untrusted_remote_state`; treat them as data from the server.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote file or directory whose owner/group changes. |
| `uid` | `integer` | No | — | ≥ 0 | Numeric owner id (uid). Pass uid, gid, or both. Omitting it keeps the current owner. |
| `gid` | `integer` | No | — | ≥ 0 | Numeric group id (gid). Pass uid, gid, or both. Omitting it keeps the current group. |
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
  "name": "nova.sftp_chown",
  "arguments": {
    "profileId": "cn_9f2c41",
    "remotePath": "/srv/app/storage",
    "uid": 33,
    "gid": 33
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "schemaVersion": "1",
    "ok": true,
    "status": "owner_changed",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "affectedRemotePaths": ["/srv/app/storage"],
    "affectedRemotePathsTrust": "untrusted_remote_state"
  }
}
```

---

## 4. Operational Best Practices

* **Look up the numbers first.** There is no name resolution over SFTP; get the uid/gid with `nova.ssh_run` (`id -u <name>`, `stat -c '%u %g' <path>`) before you set them.
* **Set only what you mean to.** Passing just `uid` keeps the current group, and vice versa — the omitted id is preserved, not zeroed.
* **Expect permission errors off root.** Changing ownership usually needs root; a non-privileged connection fails truthfully without changing anything.
* **Links are intentionally rejected.** To change a link target's owner, pass the target's real path, not the link.
