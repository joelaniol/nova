# `nova.connector_delete`

Deletes a connector profile, associated capability grants, and backing DPAPI secrets.

---

## 1. Overview

`nova.connector_delete` removes a connector profile and its capability grants. A backing password/passphrase secret is removed only when no other connector still references it. The result always reports `found` explicitly — a missing connector id is never answered with a silent success.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Connector id to delete. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.connector_delete",
  "arguments": {
    "id": "conn-mail-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Connector 'conn-mail-01' deleted (2 grant(s) removed, 1 secret(s) cleaned up)."
    }
  ],
  "structuredContent": {
    "id": "conn-mail-01",
    "deleted": true,
    "found": true,
    "changed": true,
    "status": "deleted",
    "reasonCode": null,
    "grantsRemoved": 2,
    "secretsDeleted": ["conn-mail-01-password"],
    "secretsKept": [],
    "cleanupIncomplete": false,
    "cleanupError": null
  }
}
```

---

## 4. Operational Best Practices

* **Verify Dependencies:** Ensure no active scheduled tasks or agents rely on this connector before deletion.
* **Check `found`, not just success:** A nonexistent id still returns a normal (non-error) result with `found: false`; check that field instead of assuming the delete happened.
* **Watch `cleanupIncomplete`:** If grant or secret cleanup fails partway, `status` is `cleanup_incomplete` and `cleanupError` names what is left; nothing is silently dropped.

---

## 5. Related Tools

* [`nova.connector_list`](nova-connector-list.md)
* [`nova.connector_create`](nova-connector-create.md)
