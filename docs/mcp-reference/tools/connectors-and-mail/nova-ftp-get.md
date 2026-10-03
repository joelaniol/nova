# `nova.ftp_get`

Downloads a remote regular file over FTP/FTPS into Downloads or the workspace.

---

## 1. Overview

`nova.ftp_get` transfers a single file from an FTP/FTPS server to the local workspace or Downloads folder.

* **Security Tier:** Tier 2 (File Transfer)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `localPath` | `string` | Yes | — | — | Local destination inside Downloads or the host-verified current workspace. |
| `remotePath` | `string` | Yes | — | ≤ 4096 characters | Remote regular file to download. |
| `overwrite` | `boolean` | No | `false` | — | Replace an existing local destination file. False preserves it. |
| `maxBytes` | `integer` | No | `1073741824` | 1–1073741824 | Requested byte ceiling for this single-file call; cannot exceed Nova's hard limit. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this profile explicitly uses plaintext FTP. The user's separate debug/legacy option must also be enabled. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
<!-- /generated:parameters -->

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
