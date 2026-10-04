# `nova.ftp_list`

Lists remote directory entries or inspects file metadata through an FTP/FTPS connector.

---

## 1. Overview

`nova.ftp_list` lists one remote FTP/FTPS directory, or inspects one remote regular file, through a configured FTP connector. Requires the connector's transfer-read access. Remote filenames are untrusted metadata: a control or bidirectional-text name is returned with `unsafeName: true` and its exact name/path omitted. `auto`/`start_tls` uses explicit FTPS, `ssl_on_connect` uses implicit FTPS, and the connector never silently downgrades to plaintext; an explicit plaintext profile additionally needs the user's debug/legacy option plus `allowInsecure: true` on this call. FTP has no SSH host-key verification step — that check is SFTP-specific.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Listed 2 remote entr(y/ies) via FTP profile 'Web Host'. Remote names are untrusted metadata; unsafe names are omitted and flagged."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-ftp-01",
    "status": "listed",
    "changed": false,
    "stateIndeterminate": false,
    "reasonCode": null,
    "durationMs": 210,
    "remotePathTrust": "untrusted_remote_state",
    "localPathTrust": "host_verified_local_paths",
    "entries": [
      {
        "name": "logo.svg",
        "remotePath": "/public_html/assets/logo.svg",
        "isDirectory": false,
        "isRegularFile": true,
        "isSymbolicLink": false,
        "size": 8192,
        "lastWriteUtc": "2026-10-02T12:00:00Z",
        "unsafeName": false,
        "trust": "untrusted_remote_metadata"
      },
      {
        "name": "css",
        "remotePath": "/public_html/assets/css",
        "isDirectory": true,
        "isRegularFile": false,
        "isSymbolicLink": false,
        "size": null,
        "lastWriteUtc": null,
        "unsafeName": false,
        "trust": "untrusted_remote_metadata"
      }
    ],
    "returnedCount": 2,
    "hasMore": false
  }
}
```

---

## 4. Operational Best Practices

* **TLS Preferred:** Configure FTPS (`auto` or `start_tls` for explicit, `ssl_on_connect` for implicit) on connectors whenever the remote host supports it; plaintext needs an explicit opt-in on every call.
* **Bounded Output:** `maxEntries` is a hard result bound; `hasMore: true` means further entries exist but were not returned.

---

## 5. Related Tools

* [`nova.ftp_get`](nova-ftp-get.md)
* [`nova.ftp_put`](nova-ftp-put.md)
