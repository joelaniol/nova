# `nova.ftp_get`

Downloads a remote regular file over FTP/FTPS into Downloads or the workspace.

---

## 1. Overview

`nova.ftp_get` transfers a single file from an FTP/FTPS server to the local workspace or Downloads folder.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (File Transfer)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |
| **`localPath`** | `string` | Yes | `null` | Local destination inside Downloads or the host-verified current workspace. |
| **`maxBytes`** | `integer` | No | `1073741824` | Requested byte ceiling for this single-file call; cannot exceed Nova's hard limit. |
| **`overwrite`** | `boolean` | No | `false` | Replace an existing local destination file. False preserves it. |
| **`profileId`** | `string` | Yes | `null` | FTP connector id from nova.connector_list. |
| **`remotePath`** | `string` | Yes | `null` | Remote regular file to download. |
| **`unattended`** | `boolean` | No | `false` | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.ftp_get",
  "arguments": {
    "profileId": "conn-ftp-01",
    "remotePath": "/public_html/assets/logo.svg",
    "localPath": "assets/logo.svg"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Downloaded logo.svg (8 KB) over FTP."
    }
  ],
  "structuredContent": {
    "ok": true,
    "remotePath": "/public_html/assets/logo.svg",
    "localPath": "assets/logo.svg",
    "bytesTransferred": 8192
  }
}
```

---

## 4. Operational Best Practices

* **Path Security:** Destination paths are validated to prevent writing outside authorized workspace bounds.

---

## 5. Related Tools

* [`nova.ftp_put`](nova-ftp-put.md)
* [`nova.ftp_list`](nova-ftp-list.md)
