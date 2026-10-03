# `nova.sftp_list`

Lists remote directory entries or inspects file metadata through an SFTP connector.

---

## 1. Overview

`nova.sftp_list` connects over SSH File Transfer Protocol (SFTP) to list files, directories, symlinks, file sizes, and modification timestamps.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | SFTP connector id from nova.connector_list. |
| `remotePath` | `string` | No | `"."` | ≤ 4096 characters | Remote POSIX path to list. Defaults to '.'. |
| `maxEntries` | `integer` | No | `200` | 1–1000 | Maximum returned entries. hasMore=true means additional entries were not returned. |
| `unattended` | `boolean` | No | `false` | — | Fail closed instead of opening account/policy prompts. Scheduled-task hosts enforce unattended mode even when omitted; this flag can only reduce authority. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sftp_list",
  "arguments": {
    "profileId": "conn-sftp-01",
    "remotePath": "/var/www/reports",
    "maxEntries": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 2 entries in /var/www/reports."
    }
  ],
  "structuredContent": {
    "ok": true,
    "remotePath": "/var/www/reports",
    "entries": [
      {
        "name": "daily.csv",
        "sizeBytes": 12040,
        "isDirectory": false,
        "modifiedUtc": "2026-10-02T16:00:00Z"
      },
      {
        "name": "archive",
        "isDirectory": true,
        "modifiedUtc": "2026-10-01T00:00:00Z"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Directory Discovery:** List remote directories before initiating downloads or uploads to ensure paths exist.
* **Bounded Output:** Default `maxEntries` prevents hanging on huge directories with tens of thousands of files.

---

## 5. Related Tools

* [`nova.sftp_get`](nova-sftp-get.md)
* [`nova.sftp_put`](nova-sftp-put.md)
