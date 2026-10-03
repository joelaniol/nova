# `nova.grep_resources`

> **Searches loaded page resources (scripts, stylesheets, HTML) for matching literal text or regex patterns.**

* **Security Tier:** Tier 1 (Read-Only Inspection)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.grep_resources` performs regex or substring matching across all in-memory network resources captured for a browser tab. Ideal for finding hidden API keys, endpoints, or DOM selectors.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `pattern` | `string` | Yes | — | — | Literal search text by default, or a .NET/ECMAScript-compatible regex when regex=true. |
| `source` | `string` | No | `"auto"` | `auto`, `cdp`, `performance`, `dom` | Resource discovery method. 'auto': merges the CDP resource tree with the Performance timeline (deduplicated by URL), then falls back to DOM tags. 'cdp': CDP resource tree only. 'performance': Performance API entries only. 'dom': scans DOM tags. Only what discovery listed is scanned - discoverySources and completenessHint in the result say so. |
| `types` | `array` of `string` | No | `["Script","Stylesheet","Document"]` | — | Resource types to search. Defaults to text-oriented scripts, stylesheets, and documents. |
| `caseSensitive` | `boolean` | No | `false` | — | If true, literal or regex matching is case-sensitive. |
| `regex` | `boolean` | No | `false` | — | If true, treat pattern as a regex. Invalid regex patterns fail with -32602. |
| `maxItems` | `integer` | No | `200` | 1–2000 | Maximum resources to enumerate before searching. |
| `maxResourceChars` | `integer` | No | `100000` | 1000–5000000 | Maximum characters to read from each text resource before searching. |
| `maxMatches` | `integer` | No | `100` | 1–2000 | Maximum total matches to return across all resources. |
| `contextChars` | `integer` | No | `120` | 0–2000 | Characters of context to include before and after each match. |
| `maxChars` | `integer` | No | `100000` | 1000–5000000 | Maximum serialized response characters before truncation. Defaults shrink automatically under context pressure unless explicitly provided. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

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
