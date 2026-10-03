# `nova.ftp_rename`

Renames or moves a remote file or directory on an FTP/FTPS server.

---

## 1. Overview

`nova.ftp_rename` renames or relocates a file or directory on an FTP/FTPS host.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Remote Mutation)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Existing remote source path. |
| `destinationRemotePath` | `string` | Yes | — | ≤ 4096 characters | New remote destination path. |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing regular-file destination. Directories and links are never overwritten. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ftp_rename",
  "arguments": {
    "profileId": "conn-ftp-01",
    "remotePath": "/public_html/app.old.js",
    "destinationRemotePath": "/public_html/app.bak.js"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Renamed /public_html/app.old.js to /public_html/app.bak.js."
    }
  ],
  "structuredContent": {
    "ok": true,
    "oldPath": "/public_html/app.old.js",
    "newPath": "/public_html/app.bak.js"
  }
}
```

---

## 4. Operational Best Practices

* **Atomic Deployments:** Deploy new code by uploading to a versioned directory and renaming over FTP.

---

## 5. Related Tools

* [`nova.ftp_put`](nova-ftp-put.md)
* [`nova.ftp_delete`](nova-ftp-delete.md)
