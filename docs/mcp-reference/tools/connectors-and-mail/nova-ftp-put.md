# `nova.ftp_put`

Uploads a local regular file over FTP/FTPS to a remote server.

---

## 1. Overview

`nova.ftp_put` uploads a file from the local workspace to a remote FTP/FTPS server.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (File Upload)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Existing local regular file inside Downloads or the host-verified current workspace. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote destination file (or an existing directory that receives the local filename). |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing regular-file destination. False preserves it. |
| `maxBytes` | `integer` | No | `1073741824` | 1–1073741824 | Requested byte ceiling for this single-file call; cannot exceed Nova's hard limit. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ftp_put",
  "arguments": {
    "profileId": "conn-ftp-01",
    "localPath": "dist/app.js",
    "remotePath": "/public_html/app.js",
    "overwrite": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Uploaded app.js (120 KB) over FTP."
    }
  ],
  "structuredContent": {
    "ok": true,
    "localPath": "dist/app.js",
    "remotePath": "/public_html/app.js",
    "bytesTransferred": 122880
  }
}
```

---

## 4. Operational Best Practices

* **Overwrites:** Specify `overwrite: true` when replacing existing remote assets.

---

## 5. Related Tools

* [`nova.ftp_get`](nova-ftp-get.md)
* [`nova.ftp_rename`](nova-ftp-rename.md)
