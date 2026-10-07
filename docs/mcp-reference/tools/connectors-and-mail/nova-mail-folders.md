# `nova.mail_folders`

Lists the personal IMAP folder tree with total and unread message counts.

---

## 1. Overview

`nova.mail_folders` lists the configured account's personal IMAP folder tree with message and unread counts. It opens folders read-only and never changes messages or flags. Folder names and counts are remote-controlled metadata and are marked untrusted. An effective "always" read grant may restrict exact folders and sender addresses/domains; unrelated folders are omitted from the tree, navigation-only ancestors expose no counts, and a sender-restricted grant hides aggregate counts that would include other senders — `structuredContent.grantFilter` reports the applied boundary.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
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
      "text": "Listed 3 folder(s) for 'Work Email'. Folder names and counts are untrusted server metadata in structuredContent."
    }
  ],
  "structuredContent": {
    "profileId": "conn-mail-01",
    "folders": [
      {
        "name": "INBOX",
        "fullName": "INBOX",
        "parentFullName": null,
        "specialUse": null,
        "canOpen": true,
        "messageCount": 142,
        "unreadCount": 4,
        "children": []
      },
      {
        "name": "Trash",
        "fullName": "Trash",
        "parentFullName": null,
        "specialUse": "Trash",
        "canOpen": true,
        "messageCount": 12,
        "unreadCount": 0,
        "children": []
      }
    ],
    "folderCount": 2,
    "grantFilter": { "restricted": false, "allowedFolders": [], "allowedSenders": [] },
    "durationMs": 220,
    "untrustedRemoteMetadata": true
  }
}
```
There is no top-level `ok` field; a failed call is reported as `isError: true` instead. `folders` is a tree (nested under `children`), not a flat list — `folderCount` counts every node in it.

---

## 4. Operational Best Practices

* **Folder Discovery:** Run `mail_folders` first to discover canonical `fullName` values before calling `mail_list` or `mail_search`.
* **Read-Only Safe:** Folder inspection does not alter read states or server flags.
* **Respect the Grant Filter:** When `grantFilter.restricted` is true, folders outside the allowed set are omitted entirely rather than shown with hidden counts.

---

## 5. Related Tools

* [`nova.mail_list`](nova-mail-list.md)
* [`nova.mail_search`](nova-mail-search.md)
