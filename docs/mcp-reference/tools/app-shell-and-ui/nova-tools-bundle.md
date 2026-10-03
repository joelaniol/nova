# `nova.tools_bundle`

> **Discovers, searches, and activates curated MCP tool capability bundles or queries tools by natural language.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Tool Discovery & Bundle Management)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tools_bundle` enables dynamic tool management. Agents can query available tools by intent (e.g. "take screenshot and download PDF") or load pre-curated tool sets to conserve context window tokens.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `bundle` | `string` | No | Bundle ID or alias (e.g. 'browser_automation', 'automation', 'plugin_management', 'pks_learning', 'scheduled_tasks'). Omit bundle, toolName, and query to use browser_automation; no schema default is published because the lookup modes are mutually exclusive. |
| `includeCatalog` | `boolean` | No | If true (default), a bundle lookup also returns the discovery index: knownBundles plus bundleCatalog. Pass false once you have read it - the tools of the requested bundle are returned either way, so nothing you need to call them is lost. |
| `includeDescriptions` | `boolean` | No | If true, include each tool description and the bundle's full contract text. Without it a bundle lookup returns the bundle's one-line summary and fullDescriptionChars says how long the full text is. |
| `includeInputSchema` | `boolean` | No | If true, include inputSchema for each tool (larger payload); exact toolName lookup also includes a declared outputSchema. Runtime default: true for exact lookup, false for bundle lookup; no unconditional schema default is published. |
| `includeUnavailable` | `boolean` | No | If true, include tool names that are part of the bundle but not available in the current runtime. |
| `maxResults` | `integer` | No | Maximum capability-query matches to return. Has no effect on exact toolName or curated bundle lookup. |
| `query` | `string` | No | Optional non-empty capability search across canonical tool names and descriptions. Plain language works: search terms are combined with OR and ranked, so a term that matches nothing does not empty the result. When no tool matches every term, the closest matches are returned and partialMatch is true. Mutually exclusive with bundle and toolName. Returns a bounded names-only result unless descriptions or schemas are explicitly requested. |
| `toolName` | `string` | No | Optional non-empty exact canonical tool name from Nova's tool registry. Mutually exclusive with bundle. Exact lookup returns only this tool and defaults to its declared inputSchema plus outputSchema (when present), without the description, avoiding a whole-bundle schema payload. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tools_bundle",
  "arguments": {
    "query": "download files and monitor transfer progress"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Discovered bundle 'downloads' (15 tools matched)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "matchedBundle": "downloads",
    "toolsCount": 15,
    "tools": [
      "nova.downloads_list",
      "nova.downloads_wait",
      "nova.downloads_pause"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Context Conservation:** Instead of keeping all 408 tool schemas in system prompts, query `nova.tools_bundle` dynamically to activate only necessary tools.
* **Natural Language Discovery:** Search by intent keywords when facing unfamiliar automation tasks.

---

## 5. Related Tools

* [`nova.get_instructions`](nova-get-instructions.md)
