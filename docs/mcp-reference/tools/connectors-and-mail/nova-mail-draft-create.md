# `nova.mail_draft_create`

Saves an email draft to the server's Drafts folder without sending.

---

## 1. Overview

`nova.mail_draft_create` saves one draft in the configured account's server-side Drafts folder without sending it. Requires the account's `organize` capability and Nova's independent MutatingRemote confirmation policy — it does not require the `send` capability or recipient allow-list, because no SMTP submission occurs. Nova prefers the server's SPECIAL-USE Drafts folder and otherwise accepts only conservative exact localized folder names; if none is identifiable, nothing is appended and the call fails with `reasonCode: "mail_draft_folder_not_found"`. A confirmed append returns `changed: true, sent: false`; `messageId` is a stable Nova handle only when the server returned a UID and Nova's local index committed it, otherwise `created_untracked` means the draft exists but should be found by listing Drafts.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
| `to` | `array` of `string` | Yes | — | 1–20 items | One to 20 recipient addresses. Duplicate addresses are coalesced; runtime compatibility accepts one string as a one-item list. |
| `subject` | `string` | No | — | ≤ 500 characters | Optional draft subject, max 500 characters; defaults to empty. |
| `bodyText` | `string` | No | — | — | Plain-text draft body; max 1024 KiB encoded as UTF-8. Either bodyText or bodyHtml is required. Attachments are not part of drafts. |
| `cc` | `array` of `string` | No | — | ≤ 20 items | Optional copy recipients stored in the draft (max 20). |
| `bcc` | `array` of `string` | No | — | ≤ 20 items | Optional blind-copy recipients stored in the draft; the draft keeps them so the mail program can send it later. |
| `bodyHtml` | `string` | No | — | — | Optional HTML body, max 1024 KiB UTF-8. Sent as multipart/alternative: bodyText is the text part; without bodyText Nova derives a readable text version from the HTML. Either bodyText or bodyHtml is required. |
| `priority` | `string` | No | — | `high`, `normal`, `low` | Optional priority. 'high'/'low' write X-Priority, Importance and Priority, which Outlook, Thunderbird and Apple Mail show; 'normal' (default) writes nothing. |
| `requestReadReceipt` | `boolean` | No | `false` | — | Optional: ask for a read receipt (Disposition-Notification-To, RFC 8098) to the sending address. The recipient's program or person decides whether one is sent; it is never guaranteed. |
| `replyTo` | `string` | No | — | — | Optional Reply-To address, when replies should go somewhere other than the sending account. |
| `includeSignature` | `boolean` | No | `true` | — | Append the account's signature text block - name/company/phone below the mail, not a cryptographic signature (set with nova.connector_update signatureText/signatureHtml, shown in connector_list). Default true; false leaves it off for this mail. |
| `inReplyToMessageId` | `string` | No | — | 1–128 characters | Optional opaque Nova message handle from this same account. On success the draft receives a standards-based In-Reply-To header plus a bounded References chain; the source body and attachments are never fetched. |
| `replaceDraftId` | `string` | No | — | 1–128 characters | Optional handle of a draft this one replaces (from nova.mail_list/mail_search of the Drafts folder, same account). The new draft is saved first; only after the server confirmed it is the old one moved to Trash (like nova.mail_delete, never expunged). A handle outside the Drafts folder is left untouched. The result reports replacedDraft {status: moved_to_trash \| kept_not_a_draft \| kept_move_failed \| kept_new_draft_not_saved}. An unknown handle fails before anything is saved (unknown_replaceDraftId). |
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
      "text": "The draft was saved in the account and was not sent. The returned folder name is untrusted server metadata."
    }
  ],
  "structuredContent": {
    "ok": true,
    "changed": true,
    "status": "created",
    "profileId": "conn-mail-01",
    "folderFullName": "Drafts",
    "messageId": "msg-49a10b",
    "messageIdStable": true,
    "internetMessageId": "<draft-49a10b@work-email>",
    "recipientCount": 1,
    "sent": false,
    "editableByUser": true,
    "actionDispatched": false,
    "reasonCode": null,
    "message": null,
    "durationMs": 260,
    "replacedDraft": null,
    "untrustedRemoteMetadata": true
  }
}
```
There is no `draftId`/`folder`/`subject` triple — the folder is `folderFullName`, the message handle is `messageId` (use it with `nova.mail_list`/`nova.mail_read` of the Drafts folder), and `sent` is always `false` here.

---

## 4. Operational Best Practices

* **Human-in-the-Loop:** Recommended for high-stakes customer communications where agent-generated proposals require human sign-off.
* **Draft Replacement:** Supply `replaceDraftId` to replace an existing draft; the new one is saved first, and only after the server confirms it is the old one moved to Trash. Check `replacedDraft.status` to confirm what happened to it.
* **Check `messageIdStable`:** if `false`, no stable handle is available yet — list the Drafts folder to find it rather than assuming `messageId` resolves.

---

## 5. Related Tools

* [`nova.mail_send`](nova-mail-send.md)
* [`nova.mail_folders`](nova-mail-folders.md)
