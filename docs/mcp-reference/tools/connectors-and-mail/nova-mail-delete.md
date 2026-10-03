# `nova.mail_delete`

Moves up to 200 messages into the account's Trash folder (non-permanent delete).

---

## 1. Overview

`nova.mail_delete` moves messages to the server's detected Trash folder. It deliberately avoids permanent IMAP expunge operations to ensure deleted messages can be recovered by the user.

* **Security Tier:** Tier 2 (Trash Move)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `messageIds` | `array` of `string` | Yes | — | 1–200 items | One to 200 handles from one mail account. Duplicate handles are coalesced. Runtime compatibility accepts one string and the singular messageId alias as a one-item batch. |
| `unattended` | `boolean` | No | `false` | — | Optional fail-closed hint for a non-interactive caller. Host-attested scheduled-task sessions are unattended even when omitted and can never be made interactive by this field. |
| `allowInsecure` | `boolean` | No | `false` | — | Required as true only when this account's IMAP endpoint explicitly uses plaintext or disabled certificate validation, and only after the user enabled insecure connector connections in Settings. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.mail_delete",
  "arguments": {
    "messageIds": [
      "msg-h9a12b"
    ]
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Moved 1 message to Trash."
    }
  ],
  "structuredContent": {
    "ok": true,
    "deletedCount": 1,
    "trashFolder": "Trash"
  }
}
```

---

## 4. Operational Best Practices

* **Safe Recovery:** Messages can be restored from the Trash folder if deleted by mistake.
* **Max Batch Limit:** Capped at 200 messages per call for safety.

---

## 5. Related Tools

* [`nova.mail_move`](nova-mail-move.md)
* [`nova.mail_list`](nova-mail-list.md)
