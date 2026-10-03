# `nova.connector_delete`

Deletes a connector profile, associated capability grants, and backing DPAPI secrets.

---

## 1. Overview

`nova.connector_delete` removes a connector profile from the system. If no other connector references the backing credential secret, the encrypted secret is permanently removed from the keystore.

* **Capability Bundle:** `connector_ops`
* **Security Tier:** Tier 3 (Destructive Deletion)
* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`id`** | `string` | Yes | `null` | Connector id to delete. |

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
