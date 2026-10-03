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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `displayName` | `string` | Yes | — | — | Human-readable name for this server (e.g. 'Playwright', 'My DB Server'). |
| `transport` | `string` | Yes | — | `stdio`, `http`, `sse` | Transport protocol. 'stdio' = Nova launches and manages the process. 'http' = Streamable HTTP (MCP 2025-03-26+). 'sse' = Legacy SSE (MCP 2024-11-05). |
| `command` | `string` | No | — | — | Launch command for stdio transport (e.g. 'npx', 'python', 'node', 'docker', 'uvx'). Required when transport='stdio'. |
| `args` | `string` | No | — | — | Command-line arguments as a single string (e.g. '-y @playwright/mcp'). Optional, stdio only. |
| `cwd` | `string` | No | — | — | Working directory for the stdio process. Optional; defaults to a persistent Nova-owned per-server workspace outside the app install directory. |
| `env` | `object` | No | — | — | Environment variables for the stdio process (e.g. {"API_KEY": "xxx"}). Optional. |
| `endpointUrl` | `string` | No | — | — | Server endpoint URL (e.g. 'http://localhost:3000/mcp'). Required when transport='http' or 'sse'. |
| `authMode` | `string` | No | — | `none`, `bearer` | Authentication mode. |
| `bearerToken` | `string` | No | — | — | Bearer token for authentication. Only used when authMode='bearer'. |
| `headers` | `object` | No | — | — | Custom HTTP headers (e.g. {"X-API-Key": "xxx"}). Optional, http/sse only. |
| `enabled` | `boolean` | No | — | — | Whether this server definition is active. Default: true. |
| `autoConnect` | `boolean` | No | — | — | Auto-connect on Nova startup (http/sse). Default: true. |
| `autoStart` | `boolean` | No | — | — | Auto-start the process on Nova startup (stdio). Default: false. |
| `restartOnCrash` | `boolean` | No | — | — | Automatically restart if the process crashes (stdio). Default: false. |
| `startupTimeoutMs` | `integer` | No | — | — | Timeout in ms for the MCP initialize handshake. Default: 30000. Min: 5000, Max: 120000. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.
<!-- /generated:parameters -->

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
