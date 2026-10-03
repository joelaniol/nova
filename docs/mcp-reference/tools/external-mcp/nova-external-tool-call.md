# `nova.external_tool_call`

Invokes a specific tool on a connected external MCP server and returns the raw response.

---

## 1. Overview

`nova.external_tool_call` bridges execution to an external MCP server. It passes arguments transparently, tracks latency and correlation IDs, and formats tool output and errors.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 2 (External Invocation)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`serverKey`** | `string` | Yes | `none` | 8-character hex server key. |
| **`toolName`** | `string` | Yes | `none` | Name of the tool on the external server. |
| **`arguments`** | `object` | No | `{}` | Parameters matching the tool's `inputSchema`. |
| **`timeoutMs`** | `integer` | No | `120000` | Timeout in ms (5,000 - 600,000). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_tool_call",
  "arguments": {
    "serverKey": "a1b2c3d4",
    "toolName": "query",
    "arguments": {
      "sql": "SELECT count(*) FROM users;"
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
      "text": "Tool 'query' on 'a1b2c3d4' completed in 45ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "a1b2c3d4",
    "toolName": "query",
    "durationMs": 45,
    "isError": false,
    "result": {
      "content": [
        {
          "type": "text",
          "text": "[{\"count\": 1420}]"
        }
      ]
    }
  }
}
```

---

## 4. Operational Best Practices

* **Trust Gate:** For safety, Nova enforces trust-gating on discovered secondary servers; only user-approved servers may execute tools.
* **Timeout Handling:** On timeout, returns `ok: false` with `reasonCode: "external_tool.timeout"` rather than breaking the host process.

---

## See Also

* [`nova.external_tools`](nova-external-tools.md) - Discover tool schemas.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
