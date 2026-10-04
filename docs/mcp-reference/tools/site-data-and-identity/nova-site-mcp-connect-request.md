# `nova.site_mcp_connect_request`

Requests an authenticated OAuth 2.1 connection to a website's discovered MCP server.

---

## 1. Overview

`nova.site_mcp_connect_request` starts an OAuth 2.1 + PKCE authorization flow for a domain previously probed with `nova.site_discovery_probe`. It registers a dynamic OAuth client, builds the authorization URL, and starts a local callback listener, then returns the URL for the agent to open in a tab (`nova.tab_new`). The token exchange and vault storage happen in the background after the user completes consent; call `nova.site_discovery_get` afterward to confirm the connection succeeded. Requires an authorization server that supports Dynamic Client Registration and S256 PKCE — the call fails otherwise.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `domain` | `string` | Yes | — | — | Target domain or URL. Must have OAuth metadata from a prior site_discovery_probe. Required. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "{\n  \"origin\": \"https://api.example.com\",\n  \"status\": \"authorization_required\",\n  \"authorizationUrl\": \"https://auth.example.com/oauth/authorize?response_type=code&client_id=...&redirect_uri=...&code_challenge=...&code_challenge_method=S256&state=...\",\n  \"callbackPort\": 51234,\n  \"authServer\": \"https://auth.example.com\",\n  \"scopes\": [\"mcp.read\", \"mcp.tools\"],\n  \"instruction\": \"Open authorizationUrl in a browser tab (nova.tab_new). User will authenticate and grant permissions. After consent completes, tokens are stored automatically. Call nova.site_discovery_get to check if connection succeeded (trustState becomes 'user_approved').\"\n}"
    }
  ],
  "structuredContent": {
    "origin": "https://api.example.com",
    "status": "authorization_required",
    "authorizationUrl": "https://auth.example.com/oauth/authorize?response_type=code&client_id=...&redirect_uri=...&code_challenge=...&code_challenge_method=S256&state=...",
    "callbackPort": 51234,
    "authServer": "https://auth.example.com",
    "scopes": ["mcp.read", "mcp.tools"],
    "instruction": "Open authorizationUrl in a browser tab (nova.tab_new). User will authenticate and grant permissions. After consent completes, tokens are stored automatically. Call nova.site_discovery_get to check if connection succeeded (trustState becomes 'user_approved')."
  }
}
```

This response has no `ok` field. The call returns as soon as the authorization URL is ready — it does not wait for the user to finish consent.

---

## 4. Operational Best Practices

* **PKCE Security:** Authorization code flows use RFC 7636 PKCE to protect tokens without storing client secrets.
* **Open the URL, Then Poll:** Open `authorizationUrl` with [`nova.tab_new`](../browser-automation/nova-tab-new.md), then call [`nova.site_discovery_get`](../crawler-and-discovery/nova-site-discovery-get.md) to check whether consent completed.
* **Dynamic Tool Bridging:** Once consent completes, Nova can auto-register the server; its tools then become callable via [`nova.external_tool_call`](../external-mcp/nova-external-tool-call.md).

---

## 5. Related Tools

* [`nova.site_mcp_inspect`](nova-site-mcp-inspect.md)
* [`nova.external_server_add`](../external-mcp/nova-external-server-add.md)
