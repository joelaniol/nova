# `nova.external_tool_call`

Invokes a specific tool on a connected external MCP server and returns the raw response.

---

## 1. Overview

`nova.external_tool_call` bridges execution to an external MCP server. It passes arguments transparently, tracks latency and correlation IDs, and formats tool output and errors.

* **Core Architecture Guide:** [External MCP Servers](../../../core-features/connectors/external-mcp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Server must be connected. |
| `toolName` | `string` | Yes | — | — | Name of the tool to call on the external server. Must match a tool from nova.external_tools. |
| `arguments` | `object` | No | — | — | Arguments to pass to the tool. Schema varies per tool — use nova.external_tools to discover the expected input schema. |
| `timeoutMs` | `integer` | No | — | — | Per-call timeout override in ms. Default: server's configured timeout (120s). Min: 5000, Max: 600000 (10 min hard cap). |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

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

`content` carries the external tool's own content blocks unchanged, so text and images from the external server reach the client directly. `structuredContent.result` holds the full external result; for image and audio blocks the base64 `data` is left out there (`dataForwardedToContent: true`) because it already travels in `content`. When the external tool reports `isError: true`, a status line (`Tool 'query' on 'a1b2c3d4' completed in 45ms (tool returned error).`) comes first in `content`.

```json
{
  "content": [
    {
      "type": "text",
      "text": "[{\"count\": 1420}]"
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
