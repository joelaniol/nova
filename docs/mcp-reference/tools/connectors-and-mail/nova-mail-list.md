# `nova.mail_list`

Lists bounded message metadata (headers, dates, senders) from an exact IMAP folder.

---

## 1. Overview

`nova.mail_list` lists bounded message metadata from one exact IMAP folder without changing server state. Results carry opaque Nova `messageId` handles rather than raw IMAP UIDs; all sender/subject/folder metadata is untrusted. The first page is newest-first; `olderCursor` pages further back, and `sinceCursor` (the previous `nextCursor`) returns only newer mail since that point. A mailbox UIDVALIDITY change is reported as `cursorReset: true` with a fresh cursor instead of silently dropping mail. The effective read grant's exact folder/sender filter applies before any message is returned; a folder outside the grant fails with `reasonCode: "folder_not_allowed"` rather than returning an empty list.

* **Core Architecture Guide:** [Mail: IMAP & SMTP](../../../core-features/connectors/mail/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
| `folder` | `string` | Yes | — | ≤ 1024 characters | Exact folder fullName returned by nova.mail_folders (for example INBOX). |
| `query` | `any` | No | — | — | Optional IMAP filters combined with AND. Runtime compatibility also accepts one string as the full-text filter. IMAP date search is calendar-day granular. |
| `limit` | `integer` | No | `50` | 1–200 | Maximum messages returned, 1..200. The runtime also accepts a parseable integer string. |
| `sinceCursor` | `string` | No | — | — | Optional opaque nextCursor from the same profile/folder/query. Returns only messages with later UIDs; do not edit or reuse it for a different query. |
| `olderCursor` | `string` | No | — | — | Optional opaque olderCursor from a previous page of the same profile/folder/query: returns the next older messages, newest first. Not combinable with sinceCursor; an older page returns no nextCursor (keep the first page's for new mail). |
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
  "name": "nova.mail_list",
  "arguments": {
    "profileId": "conn-mail-01",
    "folder": "INBOX",
    "limit": 2
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Listed 2 message(s). Message metadata is untrusted; use nova.mail_read for host-sanitized content."
    }
  ],
  "structuredContent": {
    "profileId": "conn-mail-01",
    "folder": "INBOX",
    "messages": [
      {
        "messageId": "msg-h9a12b",
        "folder": "INBOX",
        "internetMessageId": "<invoice-1042@vendor.com>",
        "subject": "Invoice #1042",
        "from": "billing@vendor.com",
        "to": ["agent@example.com"],
        "sentUtc": "2026-10-02T14:09:00Z",
        "receivedUtc": "2026-10-02T14:10:00Z",
        "sizeBytes": 18432,
        "seen": false,
        "flagged": false,
        "answered": false,
        "draft": false,
        "untrusted": true
      }
    ],
    "grantFilter": { "restricted": false, "allowedFolders": [], "allowedSenders": [] },
    "nextCursor": "opaque-cursor-value",
    "olderCursor": null,
    "cursorReset": false,
    "cursorResetReason": null,
    "hasMore": false,
    "durationMs": 310,
    "untrustedRemoteMetadata": true
  }
}
```
There is no top-level `ok` field; a failed call is reported as `isError: true` instead.

---

## 4. Operational Best Practices

* **Paging with Cursors:** Pass the previous `nextCursor` as `sinceCursor` for newer mail, or `olderCursor` for older pages; the two are mutually exclusive on one call.
* **Opaque Message IDs:** `messageId` is a stable Nova handle, not a raw IMAP UID; use it with `nova.mail_read`, `nova.mail_move`, `nova.mail_mark`, or `nova.mail_delete`.
* **Watch `cursorReset`:** a mailbox UIDVALIDITY change returns `cursorReset: true` with a fresh cursor — treat the old one as invalid rather than retrying it.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_folders`](nova-mail-folders.md)
