# `nova.external_server_update`

Updates configuration, environment variables, or transport settings of an existing server.

---

## 1. Overview

`nova.external_server_update` updates configuration for a registered server identified by `serverKey`. Running servers must be restarted for updated environment variables or arguments to take effect.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 3 (High-Impact)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`serverKey`** | `string` | Yes | `none` | 8-character hex server key from `nova.external_servers`. |
| **`displayName`** | `string` | No | `unchanged` | Updated display name. |
| **`command`** | `string` | No | `unchanged` | Updated executable command. |
| **`args`** | `string` | No | `unchanged` | Updated argument string. |
| **`endpointUrl`** | `string` | No | `unchanged` | Updated endpoint URL. |
| **`env`** | `object` | No | `unchanged` | Environment updates (keys mapped to `null` are deleted). |
| **`headers`** | `object` | No | `unchanged` | New HTTP headers map. |
| **`enabled`** | `boolean` | No | `unchanged` | Enable or disable server. |
| **`_meta`** | `object` | Yes | `none` | Audit intent metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_update",
  "arguments": {
    "serverKey": "e4f5a6b7",
    "restartOnCrash": true,
    "_meta": {
      "intent": "Enable automatic crash restart for filesystem gateway"
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
      "text": "Server 'e4f5a6b7' updated."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "e4f5a6b7",
    "updated": true
  }
}
```

---

## 4. Operational Best Practices

* **Environment Merging:** When updating `env`, existing variables are preserved unless explicitly set to `null`.

---

## See Also

* [`nova.external_servers`](nova-external-servers.md) - Inspect current configurations.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
