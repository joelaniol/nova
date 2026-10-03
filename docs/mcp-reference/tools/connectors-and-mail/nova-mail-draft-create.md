# `nova.mail_draft_create`

Saves an email draft to the server's Drafts folder without sending.

---

## 1. Overview

`nova.mail_draft_create` composes an email message and appends it to the IMAP server's canonical Drafts folder. Human operators can review, edit, and send the draft in their desktop email client.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Draft Creation)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`bcc`** | `array` | No | `null` | Optional blind-copy recipients stored in the draft; the draft keeps them so the mail program can send it later. |
| **`bodyHtml`** | `string` | No | `null` | Optional HTML body, max 1024 KiB UTF-8. Sent as multipart/alternative: bodyText is the text part; without bodyText Nova derives a readable text version from the HTML. Either bodyText or bodyHtml is required. |
| **`bodyText`** | `string` | No | `null` | Plain-text draft body; max 1024 KiB encoded as UTF-8. Either bodyText or bodyHtml is required. Attachments are not part of drafts. |
| **`cc`** | `array` | No | `null` | Optional copy recipients stored in the draft (max 20). |
| **`inReplyToMessageId`** | `string` | No | `null` | Optional opaque Nova message handle from this same account. On success the draft receives a standards-based In-Reply-To header plus a bounded References chain; the source body and attachments are never fetched. |
| **`includeSignature`** | `boolean` | No | `true` | Append the account's signature text block - name/company/phone below the mail, not a cryptographic signature (set with nova.connector_update signatureText/signatureHtml, shown in connector_list). Default true; false leaves it off for this mail. |
| **`priority`** | `string` | No | `null` | Optional priority. 'high'/'low' write X-Priority, Importance and Priority, which Outlook, Thunderbird and Apple Mail show; 'normal' (default) writes nothing. |
| **`profileId`** | `string` | Yes | `null` | Mail connector id (from nova.connector_list). |
| **`replaceDraftId`** | `string` | No | `null` | Optional handle of a draft this one replaces (from nova.mail_list/mail_search of the Drafts folder, same account). The new draft is saved first; only after the server confirmed it is the old one moved to Trash (like nova.mail_delete, never expunged). A handle outside the Drafts folder is left untouched. The result reports replacedDraft {status: moved_to_trash | kept_not_a_draft | kept_move_failed | kept_new_draft_not_saved}. An unknown handle fails before anything is saved (unknown_replaceDraftId). |
| **`replyTo`** | `string` | No | `null` | Optional Reply-To address, when replies should go somewhere other than the sending account. |
| **`requestReadReceipt`** | `boolean` | No | `false` | Optional: ask for a read receipt (Disposition-Notification-To, RFC 8098) to the sending address. The recipient's program or person decides whether one is sent; it is never guaranteed. |
| **`subject`** | `string` | No | `null` | Optional draft subject, max 500 characters; defaults to empty. |
| **`to`** | `array` | Yes | `null` | One to 20 recipient addresses. Duplicate addresses are coalesced; runtime compatibility accepts one string as a one-item list. |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_draft_create",
  "arguments": {
    "profileId": "conn-mail-01",
    "to": [
      "client@example.com"
    ],
    "subject": "Proposal Draft",
    "bodyText": "Draft proposal content."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Draft saved to server Drafts folder (draft-49a10b)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "draftId": "draft-49a10b",
    "folder": "Drafts",
    "subject": "Proposal Draft"
  }
}
```

---

## 4. Operational Best Practices

* **Human-in-the-Loop:** Recommended for high-stakes customer communications where agent-generated proposals require human sign-off.
* **Draft Replacement:** Supply `replaceDraftId` to update an existing draft in-place without creating duplicates.

---

## 5. Related Tools

* [`nova.mail_send`](nova-mail-send.md)
* [`nova.mail_folders`](nova-mail-folders.md)
