# `nova.site_discovery_get`

Retrieves cached MCP and AI discovery probe results for a domain without network traffic.

---

## 1. Overview

`nova.site_discovery_get` reads previously cached AI/MCP discovery probe findings for a domain from local storage. It does not initiate any network requests, returning `null` if no probe has been executed yet.

* **Capability Bundle:** `crawler_ops`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Autonomous Crawler & Surface Explorer](../../../core-features/crawler-and-discovery.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`domain`** | `string` | Yes | `none` | Target domain or URL (e.g. `"example.com"`, `"https://api.example.com"`). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.site_discovery_get",
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
      "text": "Retrieved cached discovery probe for api.example.com."
    }
  ],
  "structuredContent": {
    "ok": true,
    "domain": "api.example.com",
    "hasMcpServerCard": true,
    "mcpEndpoint": "https://api.example.com/mcp/sse",
    "hasLlmsTxt": true,
    "cachedAt": "2026-10-02T15:20:00Z"
  }
}
```

---

## 4. Operational Best Practices

* **Zero Network Overhead:** Ideal for fast pre-flight checks before navigating or crawling.
* **Fall Back to Probe:** If `nova.site_discovery_get` returns `null` or `ok: false`, invoke [`nova.site_discovery_probe`](nova-site-discovery-probe.md) to perform live network discovery.

---

## 5. Related Tools

* [`nova.site_discovery_probe`](nova-site-discovery-probe.md) — Perform live network discovery probe.
