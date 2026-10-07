# `nova.mail_attachment_save`

Saves a specific email attachment to Downloads or the workspace directory.

---

## 1. Overview

`nova.mail_attachment_save` saves exactly one attachment identified by `attachmentIndex` from a message returned by `nova.mail_read`. Requires the account's `read` capability plus Nova's independent SensitiveRead and PersistentWrite policies, since a visible local file is created. Nova fetches only the selected IMAP body part, opens the folder read-only, never overwrites an existing file (it appends " (2)" and further suffixes instead), and never opens or executes the result. An executable-like filename follows the user's host-only setting: isolate (default, appends `.isolated`), discard, or keep the original extension with a warning. Remote filenames are normalized against bidi/invisible/control and suspicious Unicode dot/slash characters before use.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `messageId` | `string` | Yes | — | — | Opaque Nova message handle returned by nova.mail_list or nova.mail_search and resolved only in Nova's encrypted local locator index. |
| `attachmentIndex` | `integer` | Yes | — | 0–199 | Zero-based attachmentIndex returned by nova.mail_read, 0..199. The runtime also accepts a parseable integer string. |
| `localPath` | `string` | No | — | — | Optional absolute Windows destination inside Downloads, the host-verified workspace, or the signed task's shared directory. An existing directory uses the sanitized remote filename; otherwise this is the final filename and its parent must already exist. Omit for Nova's context-aware default. |
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
  "name": "nova.mail_attachment_save",
  "arguments": {
    "messageId": "msg-h9a12b",
    "attachmentIndex": 0,
    "localPath": "invoices/invoice-1042.pdf"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "The selected attachment was saved as a local file. Nova did not open or execute it; remote filenames remain untrusted metadata."
    }
  ],
  "structuredContent": {
    "ok": true,
    "changed": true,
    "status": "saved",
    "profileId": "conn-mail-01",
    "messageId": "msg-h9a12b",
    "attachmentIndex": 0,
    "finalPath": "invoices/invoice-1042.pdf",
    "bytesWritten": 45200,
    "dangerous": false,
    "isolated": false,
    "discarded": false,
    "originalName": "invoice-1042.pdf",
    "savedFileName": "invoice-1042.pdf",
    "sourceNameSanitized": false,
    "source": "server",
    "warning": null,
    "reasonCode": null,
    "grantFilter": { "restricted": false, "allowedFolders": [], "allowedSenders": [] },
    "durationMs": 310,
    "opened": false,
    "executed": false,
    "untrustedRemoteMetadata": true
  }
}
```
There is no `filename`/`destinationPath` pair — the written path is `finalPath`, and the original remote name is `originalName`. An executable-like attachment instead reports `discarded: true` (nothing written) or `isolated: true` (saved as `*.isolated`), per the user's dangerous-attachment setting.

---

## 4. Operational Best Practices

* **Index Resolution:** Retrieve the attachment list and indexes using [`nova.mail_read`](nova-mail-read.md) prior to saving.
* **Path Isolation:** An explicit `localPath` must resolve inside Downloads, the host-verified workspace, or the signed task's shared directory; omit it to use Nova's context-aware default.
* **Check `dangerous`/`isolated`/`discarded`:** an executable-like file is never opened or executed, and may be renamed or dropped entirely depending on the user's setting — check these fields before assuming the saved file is usable as-is.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_export_eml`](nova-mail-export-eml.md)
