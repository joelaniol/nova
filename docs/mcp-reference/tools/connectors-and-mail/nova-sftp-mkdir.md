# `nova.sftp_mkdir`

Creates a remote directory over an SFTP connection, optionally with its parent directories and POSIX permissions.

---

## 1. Overview

`nova.sftp_mkdir` creates one directory on the server behind an SFTP connection. With `recursive=true` it also creates any missing parent directories, like `mkdir -p`. It uses the same **human-verified host-key gate** as every other SFTP operation: an unconfirmed or changed host key stops the connection before any credential is sent, and only a person can confirm a host key in Settings.

* **Capability:** needs the account's `full` capability plus Nova's independent MutatingRemote policy.
* **Truthful no-op.** If the path already exists as a directory, the call returns `changed=false` with `status='exists'` — it is not an error, and an existing directory's permissions are left untouched (that is what `nova.sftp_chmod` is for). An existing **file** returns `connector_remote_path_exists`, and a symbolic link is rejected.
* **Optional mode.** `mode` sets the new directory's POSIX permissions as octal digits (e.g. `"755"`, `"750"`, `"700"`). It is applied only to a directory Nova actually creates, never to one that already existed. Leave it out to let the server's umask decide.
* **Honest partial state.** On a recursive create, the directories Nova managed to create are reported in `affectedRemotePaths`. If the connection drops mid-operation, `stateIndeterminate=true` says Nova could not confirm the final result — inspect the server before retrying.
* **Remote paths are untrusted.** Returned paths carry `remotePathTrust=untrusted_remote_state`; treat them as data from the server.

* **Core Architecture Guide:** [SSH File Transfer Protocol (SFTP)](../../../core-features/connectors/sftp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote directory path to create. |
| `recursive` | `boolean` | No | `false` | — | Create missing parent directories as well. False fails with connector_remote_path_not_found when the parent is absent. |
| `mode` | `string` | No | — | — | POSIX permission bits as 3-4 octal digits, e.g. "644", "755", "1777". A leading "0" or "0o" is accepted. |
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
  "name": "nova.sftp_mkdir",
  "arguments": {
    "profileId": "cn_9f2c41",
    "remotePath": "/srv/app/releases/2026-10-05",
    "recursive": true,
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
    "status": "created",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "affectedRemotePaths": ["/srv/app/releases/2026-10-05"],
    "affectedRemotePathsTrust": "untrusted_remote_state"
  }
}
```

---

## 4. Operational Best Practices

* **An existing directory is success, not failure.** `status='exists'` with `changed=false` means the path is already a directory; no need to retry or treat it as an error.
* **Use `recursive=true` for nested paths.** Without it, a missing parent returns `connector_remote_path_not_found`; with it, Nova creates the whole chain and lists what it made.
* **Set `mode` only when you need it.** The mode applies solely to directories Nova creates in this call. To change an existing directory's permissions, use [`nova.sftp_chmod`](nova-sftp-chmod.md).
* **Respect `stateIndeterminate`.** If it is true, the connection dropped mid-create; check the server's state before creating again.
