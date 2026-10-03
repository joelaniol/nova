# `nova.mail_folders`

Lists the personal IMAP folder tree with total and unread message counts.

---

## 1. Overview

`nova.mail_folders` connects to the configured IMAP server and retrieves folder structures, hierarchy delimiters, total message counts, and unread counts.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`profileId`** | `string` | Yes | `null` | Mail connector id (from nova.connector_list). |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_folders",
  "arguments": {
    "profileId": "conn-mail-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Retrieved 3 IMAP folders for conn-mail-01."
    }
  ],
  "structuredContent": {
    "ok": true,
    "folders": [
      {
        "name": "INBOX",
        "unreadCount": 4,
        "totalCount": 142
      },
      {
        "name": "Archive",
        "unreadCount": 0,
        "totalCount": 890
      },
      {
        "name": "Trash",
        "unreadCount": 0,
        "totalCount": 12
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Folder Discovery:** Run `mail_folders` first to discover canonical folder names before calling `mail_list` or `mail_search`.
* **Read-Only Safe:** Folder inspection does not alter read states or server flags.

---

## 5. Related Tools

* [`nova.mail_list`](nova-mail-list.md)
* [`nova.mail_search`](nova-mail-search.md)
