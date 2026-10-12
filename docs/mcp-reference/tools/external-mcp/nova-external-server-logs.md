# `nova.external_server_logs`

Reads recent stderr log lines captured from an external MCP server process, plus the server's connection history (transport events).

---

## 1. Overview

`nova.external_server_logs` retrieves stderr diagnostic lines captured in Nova's circular buffer (up to 500 lines per server), enabling quick troubleshooting of crashes, missing dependencies, or bad arguments.

`transportEvents` holds the connection history for every transport (up to 100 entries per server): each start attempt with its duration and outcome (`phase`, `reasonCode`, HTTP status and content type) and each disconnect with its kind. HTTP and SSE servers write no stderr, so their failures show up here. Nova records only its own outcome lines: no tool arguments, tokens, headers or message bodies.

* **Core Architecture Guide:** [External MCP Servers](../../../core-features/connectors/external-mcp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Get from nova.external_servers(). |
| `lines` | `integer` | No | — | — | Number of most recent stderr lines (and transport events) to return. Default: 50. Max: 500. |

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
      "text": "2 stderr line(s) and 1 transport event(s) for server 'a1b2c3d4'."
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
    ],
    "transportEventCount": 1,
    "transportEvents": [
      {
        "ts": "2026-10-02T21:15:00.410Z",
        "text": "start ok in 290 ms: protocol 2025-03-26, 5 tools"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Diagnosing Startup Failure:** When `nova.external_server_start` fails or times out, inspect `nova.external_server_logs`: `lines` shows Node/Python tracebacks of a stdio server, `transportEvents` shows what happened on the connection (for HTTP/SSE servers the only source).

---

## See Also

* [`nova.external_server_start`](nova-external-server-start.md) - Start server.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
