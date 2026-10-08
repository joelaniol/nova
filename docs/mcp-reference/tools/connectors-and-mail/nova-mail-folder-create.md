# `nova.mail_folder_create`

Creates a top-level personal IMAP message folder.

---

## 1. Overview

`nova.mail_folder_create` creates one top-level personal IMAP message folder. Requires the account's `organize` capability and Nova's independent MutatingRemote confirmation policy. The name is limited to one visually stable child name without hierarchy separators; an existing exact name returns `already_done`/`changed: false` instead of an error. If creation was dispatched but the final state is uncertain, the result reports `changed: null, actionDispatched: true` — list folders before retrying. The returned folder name is untrusted server metadata.

* **Core Architecture Guide:** [Mail: IMAP & SMTP](../../../core-features/connectors/mail/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
| `name` | `string` | Yes | — | ≤ 255 characters | One new top-level child-folder name. Hierarchy separators, control/invisible formatting characters, and leading/trailing whitespace are rejected. |
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
  "name": "nova.mail_folder_create",
  "arguments": {
    "profileId": "conn-mail-01",
    "name": "Vendor Invoices"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "The mail folder was created. The returned folder name is untrusted server metadata."
    }
  ],
  "structuredContent": {
    "ok": true,
    "changed": true,
    "status": "created",
    "profileId": "conn-mail-01",
    "folderFullName": "Vendor Invoices",
    "alreadyDone": false,
    "actionDispatched": false,
    "reasonCode": null,
    "message": null,
    "durationMs": 140,
    "untrustedRemoteMetadata": true
  }
}
```
The field is `folderFullName`, not `folderName`. An existing folder with the same name returns `changed: false`, `status: "already_done"`, `alreadyDone: true` rather than an error.

---

## 4. Operational Best Practices

* **Naming Conventions:** Hierarchy separators, control/invisible formatting characters, and leading/trailing whitespace in `name` are rejected before the call reaches the server.
* **Idempotent by Design:** Calling this again with the same name is safe — it reports `already_done` instead of failing or creating a duplicate.

---

## 5. Related Tools

* [`nova.mail_folders`](nova-mail-folders.md)
* [`nova.mail_move`](nova-mail-move.md)
