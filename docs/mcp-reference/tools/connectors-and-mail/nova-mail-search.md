# `nova.mail_search`

Searches mail metadata across the IMAP server and local encrypted search archives.

---

## 1. Overview

`nova.mail_search` executes server-side IMAP search queries and searches local encrypted message caches, returning matching `messageId` handles sorted by date.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`folder`** | `string` | No | `null` | Optional exact folder fullName. Omit to search selectable personal folders (bounded to 200 folders). |
| **`limit`** | `integer` | No | `50` | Maximum messages returned across all searched folders, 1..200. |
| **`profileId`** | `string` | Yes | `null` | Mail connector id (from nova.connector_list). |
| **`query`** | `any` | Yes | `null` | Optional IMAP filters combined with AND. Runtime compatibility also accepts one string as the full-text filter. IMAP date search is calendar-day granular. Accepts: object, string. |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_search",
  "arguments": {
    "profileId": "conn-mail-01",
    "query": "FROM billing@vendor.com SINCE 01-Sep-2026",
    "limit": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 message matching query."
    }
  ],
  "structuredContent": {
    "ok": true,
    "matchCount": 1,
    "messageIds": [
      "msg-h9a12b"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Standard IMAP Queries:** Supports standard IMAP search terms (`FROM`, `SUBJECT`, `SINCE`, `UNSEEN`).
* **Limit Bounding:** Always provide `limit` to prevent downloading thousands of search results in a single turn.

---

## 5. Related Tools

* [`nova.mail_read`](nova-mail-read.md)
* [`nova.mail_list`](nova-mail-list.md)
