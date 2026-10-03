# `nova.site_mcp_inspect`

Inspects a discovered MCP server from cached discovery metadata (identity, transport, auth status).

---

## 1. Overview

`nova.site_mcp_inspect` reads cached site discovery data for an MCP server discovered at a web domain. It details transport protocols (SSE, WebSocket), OAuth 2.1 authorization requirements, and tool catalogs.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | Target domain or URL (e.g. 'example.com'). Must have been previously probed via site_discovery_probe. Required. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.site_mcp_inspect",
  "arguments": {
    "domain": "api.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Inspected MCP server on api.example.com: SSE transport, OAuth 2.1 required."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "api.example.com",
    "transport": "sse",
    "endpointUrl": "https://api.example.com/mcp/sse",
    "authRequired": true,
    "authType": "oauth2_1"
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Connection Inspection:** Inspect server capabilities and authentication models before requesting connection.

---

## 5. Related Tools

* [`nova.site_mcp_connect_request`](nova-site-mcp-connect-request.md)
* [`nova.site_discovery_probe`](../crawler-and-discovery/nova-site-discovery-probe.md)
