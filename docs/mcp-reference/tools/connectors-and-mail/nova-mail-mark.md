# `nova.mail_mark`

Updates seen and/or flagged status flags for up to 200 messages.

---

## 1. Overview

`nova.mail_mark` sets the seen and/or flagged state for up to 200 messages from one mail account. Requires the account's `organize` capability and Nova's independent MutatingRemote confirmation policy. At least one of `seen`/`flagged` is required; the other is left unchanged. Already-correct flags return `already_done`/`changed: false` rather than reporting a change that did not happen, and an unknown handle returns `not_found` instead of a false success. If an IMAP flag command was dispatched but its final state is uncertain, that item reports `changed: null, actionDispatched: true, reasonCode: "connector_remote_state_indeterminate"` — do not auto-retry, read the message first.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `messageIds` | `array` of `string` | Yes | — | 1–200 items | One to 200 handles from one mail account. Duplicate handles are coalesced. Runtime compatibility accepts one string and the singular messageId alias as a one-item batch. |
| `seen` | `boolean` | No | — | — | Optional desired Seen state. true adds the flag; false removes it; omit to leave unchanged. |
| `flagged` | `boolean` | No | — | — | Optional desired Flagged state. true adds the flag; false removes it; omit to leave unchanged. |
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
      "text": "Mail management completed with status 'updated'. No message body was read; returned folder names are untrusted server metadata."
    }
  ],
  "structuredContent": {
    "ok": true,
    "changed": true,
    "status": "updated",
    "tool": "nova.mail_mark",
    "operation": "mark",
    "profileId": "conn-mail-01",
    "inputCount": 1,
    "resultCount": 1,
    "targetFolder": null,
    "trashFolder": null,
    "requestedSeen": true,
    "requestedFlagged": true,
    "actionDispatched": false,
    "reasonCode": null,
    "message": null,
    "results": [
      {
        "messageId": "msg-h9a12b",
        "ok": true,
        "status": "updated",
        "changed": true,
        "actionDispatched": false,
        "previousFolder": null,
        "currentFolder": "INBOX",
        "seen": true,
        "flagged": true,
        "messageIdStable": true,
        "reasonCode": null,
        "message": null,
        "untrustedRemoteMetadata": true
      }
    ],
    "durationMs": 110,
    "untrustedRemoteMetadata": true
  }
}
```
There is no `updatedCount`; check `results[]` for each message's own `seen`/`flagged` outcome.

---

## 4. Operational Best Practices

* **Batch Operations:** Collate message IDs to update read statuses in bulk rather than executing per-message calls.
* **Omit What You Don't Want to Change:** Leaving `seen` or `flagged` out of the call preserves its current value; only the flags you pass are touched.
* **Check Per-Message Results:** Already-correct flags return `status: "already_done"` for that message, not an error.

---

## 5. Related Tools

* [`nova.mail_list`](nova-mail-list.md)
* [`nova.mail_move`](nova-mail-move.md)
