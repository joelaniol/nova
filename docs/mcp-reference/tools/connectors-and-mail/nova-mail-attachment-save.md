# `nova.mail_attachment_save`

Saves a specific email attachment to Downloads or the workspace directory.

---

## 1. Overview

`nova.mail_attachment_save` extracts an attachment by its numeric index (from `nova.mail_read`) and writes it to disk. Enforces boundary validation to prevent path traversal.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (File Download)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`attachmentIndex`** | `integer` | Yes | `null` | Zero-based attachmentIndex returned by nova.mail_read, 0..199. The runtime also accepts a parseable integer string. |
| **`localPath`** | `string` | No | `null` | Optional absolute Windows destination inside Downloads, the host-verified workspace, or the signed task's shared directory. An existing directory uses the sanitized remote filename; otherwise this is the final filename and its parent must already exist. Omit for Nova's context-aware default. |
| **`messageId`** | `string` | Yes | `null` | Opaque Nova message handle returned by nova.mail_list or nova.mail_search and resolved only in Nova's encrypted local locator index. |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

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
      "text": "Saved attachment invoice-1042.pdf (45 KB)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "messageId": "msg-h9a12b",
    "filename": "invoice-1042.pdf",
    "bytesWritten": 45200,
    "destinationPath": "invoices/invoice-1042.pdf"
  }
}
```

---

## 4. Operational Best Practices

* **Index Resolution:** Retrieve the attachment list and indexes using [`nova.mail_read`](nova-mail-read.md) prior to saving.
* **Path Isolation:** Local paths are confined to Downloads or the current active workspace.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_export_eml`](nova-mail-export-eml.md)
