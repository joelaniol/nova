# `nova.external_tools`

Lists all tools available on an external MCP server, with optional full inputSchema.

---

## 1. Overview

`nova.external_tools` discovers capabilities exposed by a connected external server. By default, it returns tool names and descriptions; passing `includeSchema: true` returns complete JSON Schema definitions required for invocation.

* **Core Architecture Guides:** [External MCP Server Lifecycle & Multi-Transport Architecture](../../../core-features/connectors/external-mcp/server-lifecycle-and-transports/README.md) · [External MCP Architecture Hub](../../../core-features/connectors/external-mcp/README.md)

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
    "allowlistActive": true,
    "hiddenByAllowlist": 2,
    "allowlistUnknown": [],
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

## Related Tools

* [`nova.external_tool_call`](nova-external-tool-call.md) - Execute tool.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool release per server

A server can carry a release list (`allowedTools` on `nova.external_server_add` / `nova.external_server_update`, or the **Tools…** button of the server card in Settings). When it does, this tool lists only the released tools. `hiddenByAllowlist` counts the others without naming them, and `allowlistUnknown` names released tools the server does not offer (typos, renamed tools). The release goes by exact name only: it is not a sandbox and says nothing about whether a tool merely reads.
