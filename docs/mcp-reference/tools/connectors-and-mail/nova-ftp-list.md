# `nova.ftp_list`

Lists remote directory entries or inspects file metadata through an FTP/FTPS connector.

---

## 1. Overview

`nova.ftp_list` connects over FTP/FTPS to list directory contents, file sizes, and timestamps.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | FTP connector id from nova.connector_list. |
| `remotePath` | `string` | No | `"."` | ≤ 4096 characters | Remote FTP path to list. Defaults to '.'. |
| `maxEntries` | `integer` | No | `200` | 1–1000 | Maximum returned entries. hasMore=true means additional entries were not returned. |
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
  "name": "nova.ftp_list",
  "arguments": {
    "profileId": "conn-ftp-01",
    "remotePath": "/public_html/assets"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 2 entries in /public_html/assets."
    }
  ],
  "structuredContent": {
    "ok": true,
    "remotePath": "/public_html/assets",
    "entries": [
      {
        "name": "logo.svg",
        "sizeBytes": 8192,
        "isDirectory": false
      },
      {
        "name": "css",
        "isDirectory": true
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **TLS Preferred:** Configure FTPS (explicit TLS) on connectors whenever supported by the remote host.

---

## 5. Related Tools

* [`nova.ftp_get`](nova-ftp-get.md)
* [`nova.ftp_put`](nova-ftp-put.md)
