# `nova.mail_mark`

Updates seen and/or flagged status flags for up to 200 messages.

---

## 1. Overview

`nova.mail_mark` updates IMAP server flags (`\Seen`, `\Flagged`) on messages. It supports batch marking of up to 200 messages in a single operation.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Flag Mutation)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`allowInsecure`** | `boolean` | No | `false` | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |
| **`flagged`** | `boolean` | No | `null` | Optional desired Flagged state. true adds the flag; false removes it; omit to leave unchanged. |
| **`messageIds`** | `array` | Yes | `null` | One to 200 handles from one mail account. Duplicate handles are coalesced. Runtime compatibility accepts one string and the singular messageId alias as a one-item batch. |
| **`seen`** | `boolean` | No | `null` | Optional desired Seen state. true adds the flag; false removes it; omit to leave unchanged. |
| **`unattended`** | `boolean` | No | `false` | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_mark",
  "arguments": {
    "messageIds": [
      "msg-h9a12b"
    ],
    "seen": true,
    "flagged": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Marked 1 message as seen and flagged."
    }
  ],
  "structuredContent": {
    "ok": true,
    "updatedCount": 1
  }
}
```

---

## 4. Operational Best Practices

* **Batch Operations:** Collate message IDs to update read statuses in bulk rather than executing per-message calls.

---

## 5. Related Tools

* [`nova.mail_list`](nova-mail-list.md)
* [`nova.mail_move`](nova-mail-move.md)
