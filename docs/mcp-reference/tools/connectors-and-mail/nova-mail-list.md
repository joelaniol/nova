# `nova.mail_list`

Lists bounded message metadata (headers, dates, senders) from an exact IMAP folder.

---

## 1. Overview

`nova.mail_list` returns lightweight message summaries from an IMAP folder without altering server read flags. It supports pagination cursors, sorting, and header previews.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`folder`** | `string` | Yes | `null` | Exact folder fullName returned by nova.mail_folders (for example INBOX). |
| **`limit`** | `integer` | No | `50` | Maximum messages returned, 1..200. The runtime also accepts a parseable integer string. |
| **`olderCursor`** | `string` | No | `null` | Optional opaque olderCursor from a previous page of the same profile/folder/query: returns the next older messages, newest first. Not combinable with sinceCursor; an older page returns no nextCursor (keep the first page's for new mail). |
| **`profileId`** | `string` | Yes | `null` | Mail connector id (from nova.connector_list). |
| **`query`** | `any` | No | `null` | Optional IMAP filters combined with AND. Runtime compatibility also accepts one string as the full-text filter. IMAP date search is calendar-day granular. Accepts: object, string. |
| **`sinceCursor`** | `string` | No | `null` | Optional opaque nextCursor from the same profile/folder/query. Returns only messages with later UIDs; do not edit or reuse it for a different query. |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

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
      "text": "Retrieved 2 message headers from INBOX."
    }
  ],
  "structuredContent": {
    "ok": true,
    "folder": "INBOX",
    "messages": [
      {
        "messageId": "msg-h9a12b",
        "subject": "Invoice #1042",
        "from": "billing@vendor.com",
        "dateUtc": "2026-10-02T14:10:00Z",
        "isSeen": false
      },
      {
        "messageId": "msg-k8c34f",
        "subject": "Team Sync",
        "from": "lead@company.com",
        "dateUtc": "2026-10-02T13:00:00Z",
        "isSeen": true
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Paging with Cursors:** Use `olderCursor` or `sinceCursor` to paginate through thousands of emails without loading the entire mailbox.
* **Opaque Message IDs:** Nova generates stable, opaque `messageId` handles for subsequent reading or moving.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_folders`](nova-mail-folders.md)
