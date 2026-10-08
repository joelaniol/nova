# `nova.external_tools`

Lists all tools available on an external MCP server, with optional full inputSchema.

---

## 1. Overview

`nova.external_tools` discovers capabilities exposed by a connected external server. By default, it returns tool names and descriptions; passing `includeSchema: true` returns complete JSON Schema definitions required for invocation.

* **Core Architecture Guide:** [External MCP Servers](../../../core-features/connectors/external-mcp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Server must be connected. |
| `includeSchema` | `boolean` | No | — | — | Include full inputSchema per tool. Default: false (only name + description). This forces a fresh tools/list because the summary cache stores no schemas. |
| `refresh` | `boolean` | No | — | — | Force fresh tools/list fetch from server instead of using cache. Default: false. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "1 tool(s) on server 'a1b2c3d4' (fresh)."
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
    "fromCache": false,
    "inventoryAge": null,
    "includeSchema": true,
    "refresh": false,
    "effectiveRefresh": true
  }
}
```

`inventoryAge` is a human-readable age string (e.g. `"5s"`, `"2m"`) when `fromCache` is `true`, and `null` on a fresh fetch. `effectiveRefresh` is `true` whenever `refresh` or `includeSchema` was requested, since the summary cache never stores schemas.

---

## 4. Operational Best Practices

* **Always Inspect Schema:** Before calling `nova.external_tool_call`, run `nova.external_tools(includeSchema=true)` to ensure arguments adhere to external parameter specifications.

---

## See Also

* [`nova.external_tool_call`](nova-external-tool-call.md) - Execute tool.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
