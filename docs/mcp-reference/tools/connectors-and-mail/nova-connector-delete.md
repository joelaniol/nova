# `nova.connector_delete`

Deletes a connector profile, associated capability grants, and backing DPAPI secrets.

---

## 1. Overview

`nova.connector_delete` removes a connector profile from the system. If no other connector references the backing credential secret, the encrypted secret is permanently removed from the keystore.

* **Security Tier:** Tier 3 (Destructive Deletion)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | Yes | — | — | Connector id to delete. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
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
      "text": "Deleted connector conn-mail-01 and cleaned up associated capability grants."
    }
  ],
  "structuredContent": {
    "ok": true,
    "id": "conn-mail-01",
    "status": "Deleted"
  }
}
```

---

## 4. Operational Best Practices

* **Verify Dependencies:** Ensure no active scheduled tasks or agents rely on this connector before deletion.
* **Automatic Secret Cleanup:** Backing secrets are safely dereferenced without orphan leaks.

---

## 5. Related Tools

* [`nova.connector_list`](nova-connector-list.md)
* [`nova.connector_create`](nova-connector-create.md)
