# `nova.site_mcp_connect_request`

Requests an authenticated OAuth 2.1 connection to a website's discovered MCP server.

---

## 1. Overview

`nova.site_mcp_connect_request` triggers an interactive OAuth 2.1 authorization flow with a discovered MCP server. Nova opens a user consent tab, completes the authorization code exchange with PKCE, and registers the server into Nova's external MCP host.

* **Security Tier:** Tier 2 (OAuth Bridge)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | Target domain or URL. Must have OAuth metadata from a prior site_discovery_probe. Required. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.site_mcp_connect_request",
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
      "text": "Initiated OAuth 2.1 connection request for api.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "api.example.com",
    "status": "ConsentTabOpened",
    "authFlow": "oauth2_pkce"
  }
}
```

---

## 4. Operational Best Practices

* **PKCE Security:** Authorization code flows use RFC 7636 PKCE to protect tokens without storing client secrets.
* **Dynamic Tool Bridging:** Once authorized, tools exposed by the site MCP server become callable via [`nova.external_tool_call`](../external-mcp/nova-external-tool-call.md).

---

## 5. Related Tools

* [`nova.site_mcp_inspect`](nova-site-mcp-inspect.md)
* [`nova.external_server_add`](../external-mcp/nova-external-server-add.md)
