# `nova.external_server_add`

Registers a new external MCP server with stdio, HTTP, or SSE transport.

---

## 1. Overview

`nova.external_server_add` registers a secondary MCP server. For `stdio`, Nova launches and monitors a local sub-process with an isolated workspace; for `http` and `sse`, Nova connects over network streams.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 3 (High-Impact)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`displayName`** | `string` | Yes | `none` | Human-readable server name. |
| **`transport`** | `string` | Yes | `none` | Protocol transport: `"stdio"`, `"http"`, or `"sse"`. |
| **`command`** | `string` | Conditional | `none` | Launch command for `stdio` (`npx`, `python`, `node`, `docker`, `uvx`). |
| **`args`** | `string` | No | `null` | Command line arguments string for `stdio`. |
| **`endpointUrl`** | `string` | Conditional | `none` | Endpoint URL for `http` or `sse`. |
| **`cwd`** | `string` | No | `Workspace dir` | Working directory for `stdio` process. |
| **`env`** | `object` | No | `null` | Environment variables map (e.g. `{"API_KEY": "..."}`). |
| **`headers`** | `object` | No | `null` | Custom HTTP headers map. |
| **`authMode`** | `string` | No | `"none"` | Authentication mode: `"none"` or `"bearer"`. |
| **`bearerToken`** | `string` | No | `null` | Bearer token when `authMode: "bearer"`. |
| **`autoStart`** | `boolean` | No | `false` | Auto-start process on Nova startup (`stdio`). |
| **`autoConnect`** | `boolean` | No | `true` | Auto-connect on Nova startup (`http`/`sse`). |
| **`restartOnCrash`** | `boolean` | No | `false` | Auto-restart if process crashes (`stdio`). |
| **`startupTimeoutMs`** | `integer` | No | `30000` | Handshake timeout in ms (5,000 - 120,000). |
| **`_meta`** | `object` | Yes | `none` | Audit intent metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_add",
  "arguments": {
    "displayName": "Filesystem MCP",
    "transport": "stdio",
    "command": "npx",
    "args": "-y @modelcontextprotocol/server-filesystem C:\\Data",
    "autoStart": false,
    "_meta": {
      "intent": "Add local filesystem MCP server for report export"
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
      "text": "External MCP server 'Filesystem MCP' (e4f5a6b7) added."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "e4f5a6b7",
    "displayName": "Filesystem MCP",
    "transport": "stdio"
  }
}
```

---

## 4. Operational Best Practices

* **Process Sandboxing:** External `stdio` processes default to a persistent per-server workspace outside Nova install folders, protecting user profiles.
* **Handshake Verification:** Call `nova.external_server_start` after adding to verify that the server completes the MCP initialize handshake without errors.

---

## See Also

* [`nova.external_server_start`](nova-external-server-start.md) - Start server.
* [`nova.external_server_remove`](nova-external-server-remove.md) - Remove server.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
