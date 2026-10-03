# `nova.connector_recipient_set`

Configures recipient allow-lists for autonomous email sending without human prompts.

---

## 1. Overview

`nova.connector_recipient_set` establishes trusted recipient email addresses or domain wildcards. Outbound emails sent to approved recipients proceed autonomously; emails to unlisted recipients trigger interactive confirmation prompts.

* **Security Tier:** Tier 2 (Permission Configuration)
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
      "*@company.com",
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
      "text": "Updated recipient allow-list for conn-mail-01: 2 entries configured."
    }
  ],
  "structuredContent": {
    "ok": true,
    "profileId": "conn-mail-01",
    "allowedRecipients": [
      "*@company.com",
      "support@vendor.com"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Domain Wildcards:** Use wildcard syntax (e.g. `*@mycorp.com`) to allow internal team communications without prompt fatigue.
* **Anti-Spam Safeguard:** Out-of-allowlist destinations will always raise a `connector_approval_required` prompt.

---

## 5. Related Tools

* [`nova.mail_send`](nova-mail-send.md)
* [`nova.connector_grant_set`](nova-connector-grant-set.md)
