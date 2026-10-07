# `nova.external_server_update`

Updates configuration, environment variables, or transport settings of an existing server.

---

## 1. Overview

`nova.external_server_update` updates configuration for a registered server identified by `serverKey`. Running servers must be restarted for updated environment variables or arguments to take effect.

* **Core Architecture Guide:** [Connectors & External Protocol Gateways](../../../core-features/connectors-and-protocols/README.md) (section 7, "External MCP Servers")

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `serverKey` | `string` | Yes | — | — | Stable server identity (8-char hex). Get from nova.external_servers(). |
| `displayName` | `string` | No | — | — | New display name. |
| `command` | `string` | No | — | — | New launch command (stdio). |
| `args` | `string` | No | — | — | New command-line arguments (stdio). |
| `cwd` | `string` | No | — | — | New working directory (stdio). |
| `env` | `object` | No | — | — | Environment variable updates. Set a key to null to remove it. Merged with existing vars. |
| `endpointUrl` | `string` | No | — | — | New endpoint URL (http/sse). |
| `authMode` | `string` | No | — | `none`, `bearer` | New auth mode. |
| `bearerToken` | `string` | No | — | — | New bearer token. |
| `headers` | `object` | No | — | — | New custom headers. Replaces all existing headers. |
| `enabled` | `boolean` | No | — | — | Enable or disable the server definition. |
| `autoConnect` | `boolean` | No | — | — | Change auto-connect behavior. |
| `autoStart` | `boolean` | No | — | — | Change auto-start behavior. |
| `restartOnCrash` | `boolean` | No | — | — | Change restart-on-crash behavior. |
| `startupTimeoutMs` | `integer` | No | — | — | New startup timeout in ms. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `external_mcp` (load it with `nova.tools_bundle(bundle='external_mcp')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_update",
  "arguments": {
    "serverKey": "e4f5a6b7",
    "restartOnCrash": true,
    "_meta": {
      "intent": "Enable automatic crash restart for filesystem gateway"
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
      "text": "Server 'Filesystem MCP' (e4f5a6b7) updated."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "e4f5a6b7",
    "displayName": "Filesystem MCP",
    "transport": "stdio",
    "status": "Stopped"
  }
}
```

---

## 4. Operational Best Practices

* **Environment Merging:** When updating `env`, existing variables are preserved unless explicitly set to `null`.

---

## See Also

* [`nova.external_servers`](nova-external-servers.md) - Inspect current configurations.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
