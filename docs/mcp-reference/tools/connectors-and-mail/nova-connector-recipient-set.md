# `nova.connector_recipient_set`

Configures recipient allow-lists for autonomous email sending without human prompts.

---

## 1. Overview

`nova.connector_recipient_set` replaces a mail connector's whole send allow-list: full addresses or bare domains that `nova.mail_send` may message without an extra per-recipient prompt. It always replaces the entire list (read it from `nova.connector_list` first, edit, write back); pass `[]` to clear it. There is no wildcard or regex syntax — a bare domain such as `lieferant.de` or `@lieferant.de` already matches any mailbox at that domain. The user can turn agent editing of this list off in Settings; while off, this tool does not appear in discovery and a direct call fails with error code -32005 and `reasonCode: "recipient_management_disabled"` (sending to already-allowed recipients still works; only Settings can change the list).

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `profileId` | `string` | Yes | — | — | Mail connector id (from nova.connector_list). |
| `recipients` | `array` of `string` | Yes | — | ≤ 200 items | The full new allow-list (addresses and/or bare domains). Replaces the existing list; [] clears it. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_recipient_set",
  "arguments": {
    "profileId": "conn-mail-01",
    "recipients": [
      "company.com",
      "support@vendor.com"
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
      "text": "Recipient allow-list set for 'Work Email': 2 entr(y/ies) stored. Agents may send to these without a prompt."
    }
  ],
  "structuredContent": {
    "profileId": "conn-mail-01",
    "allowedRecipients": [
      "company.com",
      "support@vendor.com"
    ],
    "storedCount": 2,
    "droppedCount": 0,
    "changed": true,
    "status": "updated",
    "reasonCode": null
  }
}
```

---

## 4. Operational Best Practices

* **Bare Domains:** A bare domain entry (e.g. `mycorp.com`) matches any mailbox at that domain; there is no `*@` wildcard syntax.
* **Read Before Write:** This call replaces the whole list, so read the current one from `nova.connector_list` first if you only want to add or remove one entry.
* **Invalid Entries Are Dropped, Not Rejected:** Malformed or duplicate entries are silently dropped and counted in `droppedCount`, not reported individually.

---

## 5. Related Tools

* [`nova.mail_send`](nova-mail-send.md)
* [`nova.connector_grant_set`](nova-connector-grant-set.md)
