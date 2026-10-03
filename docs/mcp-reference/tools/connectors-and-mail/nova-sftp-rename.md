# `nova.sftp_rename`

Renames or moves a remote file or directory over SFTP.

---

## 1. Overview

`nova.sftp_rename` performs an atomic remote rename or move operation on an SFTP host. Requires full transfer capability.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Remote File Mutation)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Existing source path. |
| `destinationRemotePath` | `string` | Yes | — | ≤ 4096 characters | New remote destination path. |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing regular-file destination through a bounded sibling recovery stage. An interrupted stage returns stateIndeterminate and paths to inspect. False preserves the destination. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sftp_rename",
  "arguments": {
    "profileId": "conn-sftp-01",
    "remotePath": "/var/www/incoming/summary.json",
    "destinationRemotePath": "/var/www/processed/summary.json"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Renamed /var/www/incoming/summary.json to /var/www/processed/summary.json."
    }
  ],
  "structuredContent": {
    "ok": true,
    "oldPath": "/var/www/incoming/summary.json",
    "newPath": "/var/www/processed/summary.json"
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Staging:** Upload to a staging file name and rename to the target name to ensure downstream services see complete files.

---

## 5. Related Tools

* [`nova.sftp_put`](nova-sftp-put.md)
* [`nova.sftp_delete`](nova-sftp-delete.md)
