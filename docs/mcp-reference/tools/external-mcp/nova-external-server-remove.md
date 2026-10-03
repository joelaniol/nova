# `nova.external_server_remove`

Deletes an external MCP server registration, stopping it if running.

---

## 1. Overview

`nova.external_server_remove` unregisters a server from Nova. If the server is currently running, it is stopped before removal.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 3 (High-Impact)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`serverKey`** | `string` | Yes | `none` | 8-character hex server key to delete. |
| **`_meta`** | `object` | Yes | `none` | Audit intent metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_remove",
  "arguments": {
    "serverKey": "e4f5a6b7",
    "_meta": {
      "intent": "Decommission temporary filesystem MCP server"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Server 'e4f5a6b7' removed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "e4f5a6b7",
    "removed": true
  }
}
```

---

## 4. Operational Best Practices

* **Graceful Stop:** Nova attempts a graceful stdio shutdown before purging configuration records.

---

## See Also

* [`nova.external_server_stop`](nova-external-server-stop.md) - Stop server without removing.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
