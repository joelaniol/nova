# `nova.mail_export_eml`

Exports raw RFC 822 EML files preserving complete MIME headers and original parts.

---

## 1. Overview

`nova.mail_export_eml` exports original messages — every header, every MIME part, exactly as the server stores them — from handles returned by `nova.mail_list`/`nova.mail_search`. One message becomes a `.eml` file; several (or `format: 'zip'`) become one ZIP with one `.eml` per message plus a `manifest.json` (messageId, folder, internetMessageId, subject, from, receivedUtc, and the SHA-256 of each `.eml`). Pull-only: folders open read-only and nothing on the server changes. Requires the account's `read` capability plus Nova's SensitiveRead and PersistentWrite policies. Each handle reports its own status (`exported`/`not_found`/`unknown_handle`/`filtered`/`transfer_limit_exceeded`). An existing file is never overwritten: `onExists='rename'` (default) saves under a numbered name, `onExists='fail'` stops instead.

* **Core Architecture Guide:** [Mail: IMAP & SMTP](../../../core-features/connectors/mail/README.md)

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Exported 1 of 1 message(s) to archives/invoice-1042.eml. The mailbox was only read; nothing changed on the server."
    }
  ],
  "structuredContent": {
    "ok": true,
    "changed": true,
    "status": "exported",
    "profileId": "conn-mail-01",
    "format": "eml",
    "finalPath": "archives/invoice-1042.eml",
    "bytesWritten": 18432,
    "sha256": "a1b2c3...",
    "source": "server",
    "exportedCount": 1,
    "requestedCount": 1,
    "items": [
      { "messageId": "msg-h9a12b", "status": "exported", "entryName": "invoice-1042.eml" }
    ],
    "nameConflict": null,
    "localAccess": "approved_folders_only",
    "approvedFolders": ["Downloads"],
    "serverChanged": false,
    "grantFilter": { "restricted": false, "allowedFolders": [], "allowedSenders": [] },
    "durationMs": 240,
    "untrustedRemoteMetadata": true
  }
}
```
There is no bare `files` array — the single written path is `finalPath`, and per-message detail (including any `not_found`/`filtered` handles in a batch) is in `items[]`.

---

## 4. Operational Best Practices

* **Compliance Forensics:** Preserves DKIM signatures, Received headers, and MIME structures exactly as stored on the IMAP server — this is a byte-for-byte export, not a reformatted copy.
* **Batch Exports:** Pass `messageIds` (up to 200 handles from one account) instead of looping single calls; `format: 'auto'` packs more than one message into a ZIP automatically.
* **Name Conflicts Never Overwrite:** an existing file at the target name is left untouched; check `nameConflict` to see what name was actually used, or set `onExists: 'fail'` to stop instead.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_backup_start`](nova-mail-backup-start.md)
