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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Server must be connected. |
| `includeSchema` | `boolean` | No | — | — | Include full inputSchema per tool. Default: false (only name + description). This forces a fresh tools/list because the summary cache stores no schemas. |
| `refresh` | `boolean` | No | — | — | Force fresh tools/list fetch from server instead of using cache. Default: false. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

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
