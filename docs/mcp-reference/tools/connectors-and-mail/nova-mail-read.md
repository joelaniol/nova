# `nova.mail_read`

Reads the parsed body (text, HTML, markdown) and attachment inventory of a specific email.

---

## 1. Overview

`nova.mail_read` fetches the complete MIME message for an opaque `messageId`. It provides clean text extraction, sanitized HTML or markdown, sender headers, and metadata for attached files.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`bodyMode`** | `string` | No | `"full"` | metadata = envelope/flags/attachments only; preview = short sanitized text; full = bounded sanitized text. Raw HTML is never returned. |
| **`messageId`** | `string` | Yes | `null` | Opaque Nova message handle returned by mail_list/mail_search. It resolves through Nova's host-side locator instead of exposing raw folder-bound IMAP UIDs. |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_read",
  "arguments": {
    "messageId": "msg-h9a12b",
    "bodyMode": "text"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded message msg-h9a12b: Invoice #1042 from billing@vendor.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "messageId": "msg-h9a12b",
    "subject": "Invoice #1042",
    "from": "billing@vendor.com",
    "bodyText": "Please find attached invoice #1042 for September.",
    "attachments": [
      {
        "index": 0,
        "filename": "invoice-1042.pdf",
        "sizeBytes": 45200,
        "mimeType": "application/pdf"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Attachment Saving:** Use [`nova.mail_attachment_save`](nova-mail-attachment-save.md) with `attachmentIndex` to download specific files to disk.
* **Body Mode Selection:** Default `bodyMode: "text"` minimizes token usage; use `"markdown"` or `"html"` only when markup structure is critical.

---

## 5. Related Tools

* [`nova.mail_attachment_save`](nova-mail-attachment-save.md)
* [`nova.mail_mark`](nova-mail-mark.md)
* [`nova.mail_export_eml`](nova-mail-export-eml.md)
