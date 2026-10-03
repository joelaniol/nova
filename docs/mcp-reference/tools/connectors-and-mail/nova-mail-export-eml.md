# `nova.mail_export_eml`

Exports raw RFC 822 EML files preserving complete MIME headers and original parts.

---

## 1. Overview

`nova.mail_export_eml` downloads original, bit-for-bit email messages directly from the server. It exports raw `.eml` files suitable for compliance archiving, forensic review, or import into external mail clients.

* **Security Tier:** Tier 1 (Read/Export)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `messageId` | `string` | No | — | — | One opaque Nova message handle. Pass this or messageIds, not both. |
| `messageIds` | `array` of `string` | No | — | 1–200 items | 1..200 opaque handles from one account; duplicates are coalesced. |
| `format` | `string` | No | `"auto"` | `auto`, `eml`, `zip` | auto: one message -> .eml, several -> .zip. eml requires exactly one message; zip also packs a single message. |
| `localPath` | `string` | No | — | — | Optional absolute existing folder, or a final filename whose folder exists. Omit for Nova's default folder. Outside the approved folders only while local file access is enabled. |
| `onExists` | `string` | No | `"rename"` | `rename`, `fail` | When the target name exists: rename saves under a numbered name and reports nameConflict; fail stops without writing. Nothing is ever overwritten. |
| `unattended` | `boolean` | No | `false` | — | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_export_eml",
  "arguments": {
    "messageIds": [
      "msg-h9a12b"
    ],
    "localPath": "archives/invoice-1042.eml"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Exported 1 EML file."
    }
  ],
  "structuredContent": {
    "ok": true,
    "exportedCount": 1,
    "files": [
      "archives/invoice-1042.eml"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Compliance Forensics:** Preserves DKIM signatures, Received headers, and MIME structures exactly as stored on the IMAP server.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_backup_start`](nova-mail-backup-start.md)
