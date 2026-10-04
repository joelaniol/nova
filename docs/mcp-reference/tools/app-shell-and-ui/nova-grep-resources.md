# `nova.grep_resources`

> **Searches the text of a tab's loaded resources (scripts, stylesheets, documents) for literal text or a regex.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.grep_resources` lists the resources of a browser tab (same discovery as `nova.list_resources`), reads the text of each one up to `maxResourceChars`, and returns the matches with line, column and surrounding context. Only resources that discovery listed are scanned: zero matches means the pattern is absent from those resources, not that the page never loads it (`completenessHint` says so in the result). Useful for finding endpoints, configuration values or selectors in bundled frontend code.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
    "regex": false
  }
}
```

### JSON-RPC Response
`content[0].text` carries the scan result as JSON text; `structuredContent.result` carries the same object. Abridged example:

```json
{
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "pattern": "api_v2_endpoint",
    "regex": false,
    "caseSensitive": false,
    "source": "auto",
    "types": ["Script", "Stylesheet", "Document"],
    "listedResources": 14,
    "scannedResources": 14,
    "matchedResources": 1,
    "matchedResourcesReturned": 1,
    "matchedResourcesOmitted": 0,
    "skippedResources": 0,
    "totalMatches": 1,
    "listTruncated": false,
    "matchesTruncated": false,
    "completenessHint": null,
    "truncated": false,
    "result": {
      "matches": [
        {
          "url": "https://example.com/app.js",
          "type": "Script",
          "resourceChars": 48210,
          "matchCount": 1,
          "truncated": false,
          "matches": [
            {
              "index": 5120,
              "line": 142,
              "column": 7,
              "match": "api_v2_endpoint",
              "contextBefore": "const ",
              "contextAfter": " = \"/api/v2\";"
            }
          ]
        }
      ]
    }
  }
}
```

---

## 4. Operational Best Practices

* **Narrow before widening:** Restrict `types` or tighten `pattern` when a scan hits `maxMatches` or the response is truncated; there is no cursor to continue a truncated scan.
* **Regex validity:** With `regex: true`, an invalid pattern fails with `-32602` before any resource is read.

---

## 5. Related Tools

* [`nova.list_resources`](nova-list-resources.md)
* [`nova.read_resource`](nova-read-resource.md)
