# `nova.external_tools`

Lists all tools available on an external MCP server, with optional full inputSchema.

---

## 1. Overview

`nova.external_tools` discovers capabilities exposed by a connected external server. By default, it returns tool names and descriptions; passing `includeSchema: true` returns complete JSON Schema definitions required for invocation.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 1 (Safe Discovery)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`serverKey`** | `string` | Yes | `none` | 8-character hex server key. |
| **`includeSchema`** | `boolean` | No | `false` | When `true`, fetches full JSON `inputSchema` for every tool. |
| **`refresh`** | `boolean` | No | `false` | Force fresh discovery instead of using memory cache. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_tools",
  "arguments": {
    "serverKey": "a1b2c3d4",
    "includeSchema": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 1 tool(s) on server 'a1b2c3d4'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "a1b2c3d4",
    "toolCount": 1,
    "tools": [
      {
        "name": "query",
        "description": "Run SQL read query",
        "inputSchema": {
          "type": "object",
          "properties": {
            "sql": {
              "type": "string"
            }
          },
          "required": [
            "sql"
          ]
        }
      }
    ],
    "cached": false,
    "inventoryAgeMs": 0
  }
}
```

---

## 4. Operational Best Practices

* **Always Inspect Schema:** Before calling `nova.external_tool_call`, run `nova.external_tools(includeSchema=true)` to ensure arguments adhere to external parameter specifications.

---

## See Also

* [`nova.external_tool_call`](nova-external-tool-call.md) - Execute tool.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
