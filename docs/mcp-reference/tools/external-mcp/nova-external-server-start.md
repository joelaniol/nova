# `nova.external_server_start`

Launches an external MCP server, runs initialize handshake, and discovers available tools.

---

## 1. Overview

`nova.external_server_start` initiates the server process or network connection, exchanges MCP initialization capabilities, and queries tools/list. Returns PID, duration, and tool count on success.

* **Core Architecture Guide:** [External MCP Servers](../../../core-features/connectors/external-mcp/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Get from nova.external_servers(). |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_start",
  "arguments": {
    "serverKey": "a1b2c3d4"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Server 'Postgres Gateway' started (PID 14820, 5 tools, 420ms)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "result": {
      "serverKey": "a1b2c3d4",
      "displayName": "Postgres Gateway",
      "status": "Connected",
      "pid": 14820,
      "toolCount": 5,
      "startupDurationMs": 420,
      "serverName": "postgres-mcp",
      "serverVersion": "0.4.1",
      "protocolVersion": "2025-03-26"
    }
  }
}
```

On failure, `ok` is `false`, `result.status` is `"Failed"`, `result.pid` is omitted, and `result` instead carries `errorPhase`, `errorMessage`, an optional `exitCode`/`stderr`, and `suggestions` (a short list of likely fixes that follow the observed cause).

`result.reasonCode` names that cause:

| `reasonCode` | Meaning | Extra field |
| :--- | :--- | :--- |
| `no_response` | No answer arrived within `startupTimeoutMs`. Only here does a longer timeout help. | — |
| `response_id_mismatch` | The server answered, but with an id Nova never sent (JSON-RPC requires the request id unchanged). Nova never assigns such an answer to a request. If the server handles numeric ids correctly, `numericRequestIds=true` on `nova.external_server_update` makes Nova send numbers; the suggestions say so when the stray id was a number. | `uncorrelatedResponse` (`idKind`, `id`, `isError`, `awaitingIds`) |
| `upstream_error` | The server answered `initialize` with a JSON-RPC error. | `upstreamError` (`code`, `message`, `data`; message and data are length-bounded) |
| `http_status` | The server answered with an HTTP error status. | `httpStatus` |
| `connection_reset` | The server accepted the connection and closed it before answering. | — |
| `connection_refused` | Nothing accepts connections at the endpoint. Nova connects to HTTP/SSE servers but does not start them. | — |
| `connection_failed` | Any other network failure before an answer. | — |
| `protocol_error` | The answer broke the transport contract (for example HTTP 401, an oversized body, an SSE stream without `endpoint` event). | — |

Example of a server that returns its own id instead of the request id:

```json
{
  "ok": false,
  "result": {
    "status": "Failed",
    "errorPhase": "timeout",
    "reasonCode": "response_id_mismatch",
    "errorMessage": "The server sent a response with id 0 (number) while Nova waited for id \"1\" (string). Nova does not assign a response to a request it did not send.",
    "uncorrelatedResponse": { "idKind": "number", "id": "0", "isError": false, "awaitingIds": ["1"] }
  }
}
```

---

## 4. Operational Best Practices

* **Pre-check Tool Inventory:** On start, Nova automatically populates its cached tool inventory. Call `nova.external_tools` to inspect schema details.

---

## See Also

* [`nova.external_server_stop`](nova-external-server-stop.md) - Stop server.
* [`nova.external_server_logs`](nova-external-server-logs.md) - View server stderr logs.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
