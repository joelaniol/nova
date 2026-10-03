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

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |
| **`localPath`** | `string` | Yes | `null` | Existing local regular file inside Downloads or the host-verified current workspace. |
| **`maxBytes`** | `integer` | No | `1073741824` | Requested byte ceiling for this single-file call; cannot exceed Nova's hard limit. |
| **`overwrite`** | `boolean` | No | `false` | Replace an existing regular-file destination. False preserves it. |
| **`profileId`** | `string` | Yes | `null` | FTP connector id from nova.connector_list. |
| **`remotePath`** | `string` | Yes | `null` | Remote destination file (or an existing directory that receives the local filename). |
| **`unattended`** | `boolean` | No | `false` | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

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
