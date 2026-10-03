# `nova.site_mcp_connect_request`

Requests an authenticated OAuth 2.1 connection to a website's discovered MCP server.

---

## 1. Overview

`nova.site_mcp_connect_request` triggers an interactive OAuth 2.1 authorization flow with a discovered MCP server. Nova opens a user consent tab, completes the authorization code exchange with PKCE, and registers the server into Nova's external MCP host.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (OAuth Bridge)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | Yes | `null` | Target domain or URL. Must have OAuth metadata from a prior site_discovery_probe. Required. |

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
