# `nova.sandbox_delete`

Permanently removes a sandbox profile and deletes its storage, cookies, and cache.

---

## 1. Overview

`nova.sandbox_delete` deletes a sandbox profile and permanently removes its browser data directory from disk. All tabs belonging to the sandbox are immediately closed.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 3 (Destructive Sandbox Deletion)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`confirm`** | `boolean` | Yes | `null` | Safety confirmation. Must be true to proceed with deletion. |
| **`sandboxId`** | `string` | Yes | `null` | Sandbox ID to delete (e.g. 'C'). |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sandbox_delete",
  "arguments": {
    "sandboxId": "sb-c819a",
    "confirm": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted sandbox sb-c819a and purged its profile data."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sandboxId": "sb-c819a",
    "status": "Deleted"
  }
}
```

---

## 4. Operational Best Practices

* **Confirmation Required:** Requires explicit `confirm: true` to prevent accidental deletion of authenticated browser sessions.

---

## 5. Related Tools

* [`nova.sandbox_create`](nova-sandbox-create.md)
* [`nova.sandbox_context`](nova-sandbox-context.md)
