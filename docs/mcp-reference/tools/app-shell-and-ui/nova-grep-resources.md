# `nova.grep_resources`

> **Searches loaded page resources (scripts, stylesheets, HTML) for matching literal text or regex patterns.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Inspection)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.grep_resources` performs regex or substring matching across all in-memory network resources captured for a browser tab. Ideal for finding hidden API keys, endpoints, or DOM selectors.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `caseSensitive` | `boolean` | No | If true, literal or regex matching is case-sensitive. |
| `contextChars` | `integer` | No | Characters of context to include before and after each match. |
| `maxChars` | `integer` | No | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |
| `maxItems` | `integer` | No | Maximum resources to enumerate before searching. |
| `maxMatches` | `integer` | No | Maximum total matches to return across all resources. |
| `maxResourceChars` | `integer` | No | Maximum characters to read from each text resource before searching. |
| `pattern` | `string` | **Yes** | Literal search text by default, or a .NET/ECMAScript-compatible regex when regex=true. |
| `regex` | `boolean` | No | If true, treat pattern as a regex. Invalid regex patterns fail with -32602. |
| `source` | `string` | No | Resource discovery method. 'auto': merges the CDP resource tree with the Performance timeline (deduplicated by URL), then falls back to DOM tags. 'cdp': CDP resource tree only. 'performance': Performance API entries only. 'dom': scans DOM tags. Only what discovery listed is scanned - discoverySources and completenessHint in the result say so. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `types` | `array` | No | Resource types to search. Defaults to text-oriented scripts, stylesheets, and documents. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_grep_resources",
  "arguments": {
    "targetId": "tab-1",
    "pattern": "api_v2_endpoint",
    "isRegex": false
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 3 matches across 2 resources."
    }
  ],
  "structuredContent": {
    "ok": true,
    "matchesCount": 3,
    "resources": [
      {
        "url": "https://example.com/app.js",
        "line": 142,
        "match": "api_v2_endpoint = \"/api/v2\";"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Reverse Engineering:** Find obfuscated frontend routes without manual source file parsing.
* **Regex Performance:** Use specific anchors to limit search time over huge bundled JS bundles.

---

## 5. Related Tools

* [`nova.list_resources`](nova-list-resources.md)
* [`nova.read_resource`](nova-read-resource.md)
