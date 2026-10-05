# `nova.sftp_symlink`

Creates a symbolic link on the server over an SFTP connection.

---

## 1. Overview

`nova.sftp_symlink` creates a symbolic link on the server behind an SFTP connection — the classic `ln -s <target> <link>`. It uses the same **human-verified host-key gate** as every other SFTP operation: an unconfirmed or changed host key stops the connection before any credential is sent, and only a person can confirm a host key in Settings.

* **Capability:** needs the account's `full` capability plus Nova's independent MutatingRemote policy.
* **Two paths, clear roles.** `remotePath` is the **new link** to create; `targetPath` is **what it points to** and must be an **absolute path**. A classic use is a release switch: point `/srv/app/current` at `/srv/app/releases/2026-10-05`.
* **Target must be absolute.** `targetPath` has to start with `/`. A relative target is rejected: the SSH client resolves it against the connection's home directory (not the link's directory), which would silently create a link to the wrong place. An absolute target is stored as written and may point at something that does not exist yet (a dangling link is allowed).
* **Never overwrites.** If anything already exists at `remotePath`, the call fails with `connector_remote_path_exists` and changes nothing — remove the old path first (e.g. with `nova.sftp_delete`) or choose another link path.
* **Indeterminate honesty.** If the connection drops around the create, `stateIndeterminate=true` says Nova could not confirm whether the link was created — inspect the server before retrying.
* **Remote paths are untrusted.** Returned paths carry `remotePathTrust=untrusted_remote_state`; treat them as data from the server.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | The new symbolic link to create. Must not already exist. |
| `targetPath` | `string` | Yes | — | ≤ 4096 characters | What the link points to. Must be an absolute path (starting with '/'); may point at something that does not exist yet. Relative targets are rejected (they resolve against the connection home, not the link's directory). |
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
  "name": "nova.sftp_symlink",
  "arguments": {
    "profileId": "cn_9f2c41",
    "remotePath": "/srv/app/current",
    "targetPath": "/srv/app/releases/2026-10-05"
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "schemaVersion": "1",
    "ok": true,
    "status": "symlink_created",
    "changed": true,
    "stateIndeterminate": false,
    "reasonCode": null,
    "affectedRemotePaths": ["/srv/app/current"],
    "affectedRemotePathsTrust": "untrusted_remote_state"
  }
}
```

---

## 4. Operational Best Practices

* **Remember the order:** `remotePath` is the link you create, `targetPath` is where it points. Swapping them makes a link with the wrong name.
* **Use an absolute target.** Relative targets are rejected because the client resolves them against the connection home, not the link's directory — pass the full path like `/srv/app/releases/2026-10-05`.
* **Replacing a link is two steps.** Nova never overwrites; delete the existing link with `nova.sftp_delete` first, then create the new one. (An atomic swap is not available over plain SFTP.)
* **Respect `stateIndeterminate`.** If it is true, the connection dropped around the create; check the server before trying again.
