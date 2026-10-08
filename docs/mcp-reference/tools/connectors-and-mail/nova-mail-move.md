# `nova.mail_move`

Moves up to 200 messages from one mail account to an exact IMAP destination folder.

---

## 1. Overview

`nova.mail_move` moves up to 200 messages from one mail account to one exact IMAP folder. Requires the account's `organize` capability and Nova's independent MutatingRemote confirmation policy. Native IMAP MOVE support is required; without it the call is rejected before dispatch rather than falling back to a copy/delete/expunge sequence. Every input handle gets its own ordered result (`changed`/`already_done`/`not_found`); if the server accepted the move but did not confirm a destination UID, that item reports `changed: null, actionDispatched: true, reasonCode: "connector_remote_state_indeterminate"` — do not auto-retry, list the destination folder first.

* **Core Architecture Guide:** [Mail: IMAP & SMTP](../../../core-features/connectors/mail/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `messageIds` | `array` of `string` | Yes | — | 1–200 items | One to 200 handles from one mail account. Duplicate handles are coalesced. Runtime compatibility accepts one string and the singular messageId alias as a one-item batch. |
| `targetFolder` | `string` | Yes | — | ≤ 1024 characters | Exact destination folder fullName returned by nova.mail_folders. It must already exist and be selectable. |
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
  "name": "nova.mail_move",
  "arguments": {
    "messageIds": [
      "msg-h9a12b"
    ],
    "targetFolder": "Archive"
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
    "tool": "nova.mail_move",
    "operation": "move",
    "profileId": "conn-mail-01",
    "inputCount": 1,
    "resultCount": 1,
    "targetFolder": "Archive",
    "trashFolder": null,
    "requestedSeen": null,
    "requestedFlagged": null,
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
        "previousFolder": "INBOX",
        "currentFolder": "Archive",
        "seen": false,
        "flagged": false,
        "messageIdStable": true,
        "reasonCode": null,
        "message": null,
        "untrustedRemoteMetadata": true
      }
    ],
    "durationMs": 180,
    "untrustedRemoteMetadata": true
  }
}
```
There is no `movedCount`/`destination` pair at the top level — check `results[]` for each message's own outcome; `ok`/`changed`/`status` at the top summarize across the whole batch.

---

## 4. Operational Best Practices

* **Folder Verification:** Always verify target folder existence using [`nova.mail_folders`](nova-mail-folders.md) before moving messages.
* **Check Per-Message Results:** A batch can partially succeed; read each entry in `results[]` rather than only the top-level `status`.
* **Treat `messageIdStable: false` Carefully:** if the server didn't return a destination UID, the handle may not resolve for a follow-up `mail_mark`/`mail_read` until you re-list the folder.

---

## 5. Related Tools

* [`nova.mail_folders`](nova-mail-folders.md)
* [`nova.mail_delete`](nova-mail-delete.md)
