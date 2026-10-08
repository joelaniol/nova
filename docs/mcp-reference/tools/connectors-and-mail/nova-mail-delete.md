# `nova.mail_delete`

Moves up to 200 messages into the account's Trash folder (non-permanent delete).

---

## 1. Overview

`nova.mail_delete` moves up to 200 messages from one mail account into its detected Trash folder. This is deliberately not permanent deletion: Nova never sets the IMAP Deleted flag and never expunges. Requires the account's `organize` capability and Nova's independent MutatingRemote confirmation policy. Trash resolution prefers the server's SPECIAL-USE Trash folder, then conservative exact localized leaf-name matches; if no selectable Trash folder can be identified, nothing is changed and the call fails with `reasonCode: "mail_trash_folder_not_found"`. Native IMAP MOVE is required, with no copy/delete/expunge fallback. Per-message results preserve `changed`/`already_done`/`not_found` truth; an uncertain dispatched move reports `changed: null, actionDispatched: true` and must not be auto-retried.

* **Core Architecture Guide:** [Mail: IMAP & SMTP](../../../core-features/connectors/mail/README.md)

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Mail management completed with status 'updated'. No message body was read; returned folder names are untrusted server metadata."
    }
  ],
  "structuredContent": {
    "ok": true,
    "changed": true,
    "status": "updated",
    "tool": "nova.mail_delete",
    "operation": "delete",
    "profileId": "conn-mail-01",
    "inputCount": 1,
    "resultCount": 1,
    "targetFolder": null,
    "trashFolder": "Trash",
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
        "currentFolder": "Trash",
        "seen": false,
        "flagged": false,
        "messageIdStable": true,
        "reasonCode": null,
        "message": null,
        "untrustedRemoteMetadata": true
      }
    ],
    "durationMs": 150,
    "untrustedRemoteMetadata": true
  }
}
```
There is no `deletedCount`; the resolved Trash folder is `trashFolder` at the top level, and each message's own outcome is in `results[]`.

---

## 4. Operational Best Practices

* **Safe Recovery:** Messages can be restored from the Trash folder if deleted by mistake; nothing is expunged by this tool.
* **Max Batch Limit:** Capped at 200 messages per call.
* **No Trash Folder Is a Failure, Not a Silent No-Op:** if Nova cannot identify a selectable Trash folder, the call fails with `reasonCode: "mail_trash_folder_not_found"` instead of moving messages anywhere else.

---

## 5. Related Tools

* [`nova.mail_move`](nova-mail-move.md)
* [`nova.mail_list`](nova-mail-list.md)
