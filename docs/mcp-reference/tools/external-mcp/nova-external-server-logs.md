# `nova.external_server_logs`

Reads recent stderr log lines captured from an external MCP server process.

---

## 1. Overview

`nova.external_server_logs` retrieves stderr diagnostic lines captured in Nova's circular buffer (up to 500 lines per server), enabling quick troubleshooting of crashes, missing dependencies, or bad arguments.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols.md) (section 7, "External MCP Servers")

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Get from nova.external_servers(). |
| `lines` | `integer` | No | — | — | Number of most recent lines to return. Default: 50. Max: 500. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_logs",
  "arguments": {
    "serverKey": "a1b2c3d4",
    "lines": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 log line(s) for server 'a1b2c3d4'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "a1b2c3d4",
    "lineCount": 2,
    "lines": [
      {
        "ts": "2026-10-02T21:15:00.120Z",
        "text": "[postgres-mcp] Connecting to database..."
      },
      {
        "ts": "2026-10-02T21:15:00.340Z",
        "text": "[postgres-mcp] Ready on stdio."
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Diagnosing Startup Failure:** When `nova.external_server_start` fails or times out, immediately inspect `nova.external_server_logs` to read Node/Python tracebacks.

---

## See Also

* [`nova.external_server_start`](nova-external-server-start.md) - Start server.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
