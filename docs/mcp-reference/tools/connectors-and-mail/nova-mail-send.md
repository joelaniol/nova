# `nova.mail_send`

Sends an email with optional HTML body, CC/BCC, priority, and attachments via SMTP.

---

## 1. Overview

`nova.mail_send` dispatches an email through the connector's configured SMTP gateway. Outbound transmissions are audited, rate-limited, and checked against the recipient allow-list.

* **Security Tier:** Tier 2 (Outbound Email Dispatch)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
| `to` | `array` of `string` | Yes | — | ≤ 20 items | Recipient address(es), max 20 unique values. A single string is accepted and treated as one recipient. All must be allow-listed or approved interactively. |
| `subject` | `string` | No | — | ≤ 500 characters | Subject line, max 500 characters. Optional (defaults to empty). |
| `bodyText` | `string` | No | — | — | Plain-text body; max 1024 KiB encoded as UTF-8 (runtime byte limit). Either bodyText or bodyHtml is required; with both, this is the text alternative to the HTML. |
| `cc` | `array` of `string` | No | — | ≤ 20 items | Optional copy recipients (max 20; to+cc+bcc together max 50). Each passes the same allow-list/approval gate as 'to'. A single string is accepted. |
| `bcc` | `array` of `string` | No | — | ≤ 20 items | Optional blind-copy recipients: delivered, but not visible to the others (the Bcc header is never transmitted). Each passes the same allow-list/approval gate as 'to'. |
| `bodyHtml` | `string` | No | — | — | Optional HTML body, max 1024 KiB UTF-8. Sent as multipart/alternative: bodyText is the text part; without bodyText Nova derives a readable text version from the HTML. Either bodyText or bodyHtml is required. |
| `priority` | `string` | No | — | `high`, `normal`, `low` | Optional priority. 'high'/'low' write X-Priority, Importance and Priority, which Outlook, Thunderbird and Apple Mail show; 'normal' (default) writes nothing. |
| `requestReadReceipt` | `boolean` | No | `false` | — | Optional: ask for a read receipt (Disposition-Notification-To, RFC 8098) to the sending address. The recipient's program or person decides whether one is sent; it is never guaranteed. |
| `replyTo` | `string` | No | — | — | Optional Reply-To address, when replies should go somewhere other than the sending account. |
| `includeSignature` | `boolean` | No | `true` | — | Append the account's signature text block - name/company/phone below the mail, not a cryptographic signature (set with nova.connector_update signatureText/signatureHtml, shown in connector_list). Default true; false leaves it off for this mail. |
| `attachments` | `array` of `string` | No | — | ≤ 20 items | Optional local file paths to attach. Files must be inside Downloads or the host-verified current workspace project folder (else reasonCode 'local_path_not_allowed'); max 20 files and 25 MB source-file bytes total (MIME transfer encoding adds overhead). |
| `inReplyToMessageId` | `string` | No | — | 1–128 characters | Optional opaque Nova message handle from this same account. On success Nova sets standards-based In-Reply-To and bounded References headers after a read-only source-header lookup; no source body or attachment is fetched. |
| `unattended` | `boolean` | No | `false` | — | Optional fail-closed hint for a non-interactive caller: an ungranted send fails cleanly instead of prompting. Scheduled-task hosts enforce this automatically even when omitted; this caller field can never override the host's unattended state. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true for a plaintext SMTP endpoint or one whose stored debug policy allows an invalid TLS certificate, and likewise for the IMAP source lookup of a threaded reply. It works only after the user separately enabled insecure connector connections in Settings; omit/false when every endpoint used by this call is strict TLS. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_send",
  "arguments": {
    "profileId": "conn-mail-01",
    "to": [
      "client@example.com"
    ],
    "subject": "Report Update",
    "bodyText": "Here is the summary of operations."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Email sent successfully to client@example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-mail-01",
    "messageId": "smtp-out-810a",
    "recipients": [
      "client@example.com"
    ],
    "sentAtUtc": "2026-10-02T20:45:00Z"
  }
}
```

---

## 4. Operational Best Practices

* **Rate Limiting Guard:** Nova enforces built-in send rate limiting to prevent runaway autonomous email dispatching.
* **Drafting Alternative:** When unsure, create a draft via [`nova.mail_draft_create`](nova-mail-draft-create.md) for human review before sending.

---

## 5. Related Tools

* [`nova.mail_draft_create`](nova-mail-draft-create.md)
* [`nova.connector_recipient_set`](nova-connector-recipient-set.md)
