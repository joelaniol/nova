# `nova.site_discovery_probe`

Probes a website for modern AI and MCP discovery endpoints (llms.txt, /.well-known/mcp.json, A2A).

---

## 1. Overview

`nova.site_discovery_probe` investigates a target domain for modern agentic web interfaces and machine-readable metadata. It probes for:
* **MCP Server Card:** `/.well-known/mcp.json` or direct SSE/WebSocket MCP endpoints.
* **Agent-to-Agent (A2A) Protocols:** Direct agent discovery and delegation endpoints.
* **Context Files:** `/llms.txt` and `/llms-full.txt` for structured LLM site maps.
* **OAuth Protected Resources:** RFC 8414 authorization server metadata.

Results are cached locally to provide sub-millisecond retrieval on future visits.

* **Security Tier:** Tier 1 (Discovery Probe)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `url` | `string` | Yes | — | — | Target URL or origin (e.g. 'https://example.com'). Required. |
| `forceRefresh` | `boolean` | No | — | — | If true, bypass cache and re-probe. Default: false. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.site_discovery_probe",
  "arguments": {
    "url": "https://api.example.com",
    "forceRefresh": false
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Discovery probe on api.example.com completed: found llms.txt and MCP server card."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "api.example.com",
    "hasMcpServerCard": true,
    "mcpEndpoint": "https://api.example.com/mcp/sse",
    "hasLlmsTxt": true,
    "llmsTxtUrl": "https://api.example.com/llms.txt",
    "hasA2aCard": false,
    "cached": false
  }
}
```

---

## 4. Operational Best Practices

* **Proactive Discovery:** Run `nova.site_discovery_probe` upon first encountering a domain to check if direct MCP tools or llms.txt shortcuts are available.
* **Bridge Direct Endpoints:** If `mcpEndpoint` is discovered, connect it as an external secondary MCP server via [`nova.external_server_add`](../external-mcp/nova-external-server-add.md).
* **Cache Awareness:** Probes are cached for 24 hours unless `forceRefresh: true` is explicitly provided.

---

## 5. Related Tools

* [`nova.site_discovery_get`](nova-site-discovery-get.md) — Retrieve cached probe results.
* [`nova.external_server_add`](../external-mcp/nova-external-server-add.md) — Connect discovered MCP servers.
