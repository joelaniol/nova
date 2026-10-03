# `nova.mail_folder_create`

Creates a top-level personal IMAP message folder.

---

## 1. Overview

`nova.mail_folder_create` creates a new folder on the IMAP server under the account's personal namespace. Requires the account's `organize` capability.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 2 (Folder Creation)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

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
      "text": "Created IMAP folder 'Vendor Invoices'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-mail-01",
    "folderName": "Vendor Invoices"
  }
}
```

---

## 4. Operational Best Practices

* **Naming Conventions:** Avoid forward slashes or special hierarchy delimiters reserved by the IMAP server implementation.

---

## 5. Related Tools

* [`nova.mail_folders`](nova-mail-folders.md)
* [`nova.mail_move`](nova-mail-move.md)
