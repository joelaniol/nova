# `nova.tools_bundle`

> **Discovers, searches, and activates curated MCP tool capability bundles or queries tools by natural language.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tools_bundle` is Nova's capability-discovery tool. It has three mutually exclusive lookup modes: load a curated bundle by id or alias, look up a single tool by its exact canonical name, or search tool names and descriptions with a free-text query (terms are OR'd and ranked; if nothing matches every term, the closest matches come back with `partialMatch: true`). Omitting `bundle`, `toolName`, and `query` defaults to the `browser_automation` bundle.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `bundle` | `string` | No | — | — | Bundle ID or alias (e.g. 'browser_automation', 'automation', 'plugin_management', 'pks_learning', 'scheduled_tasks'). Omit bundle, toolName, and query to use browser_automation; no schema default is published because the lookup modes are mutually exclusive. |
| `toolName` | `string` | No | — | ≥ 1 characters | Optional non-empty exact canonical tool name from Nova's tool registry. Mutually exclusive with bundle. Exact lookup returns only this tool and defaults to its declared inputSchema plus outputSchema (when present), without the description, avoiding a whole-bundle schema payload. |
| `query` | `string` | No | — | 1–200 characters | Optional non-empty capability search across canonical tool names and descriptions. Plain language works: search terms are combined with OR and ranked, so a term that matches nothing does not empty the result. When no tool matches every term, the closest matches are returned and partialMatch is true. Mutually exclusive with bundle and toolName. Returns a bounded names-only result unless descriptions or schemas are explicitly requested. |
| `maxResults` | `integer` | No | `20` | 1–50 | Maximum capability-query matches to return. Has no effect on exact toolName or curated bundle lookup. |
| `includeDescriptions` | `boolean` | No | `false` | — | If true, include each tool description and the bundle's full contract text. Without it a bundle lookup returns the bundle's one-line summary and fullDescriptionChars says how long the full text is. |
| `includeInputSchema` | `boolean` | No | — | — | If true, include inputSchema for each tool (larger payload); exact toolName lookup also includes a declared outputSchema. Runtime default: true for exact lookup, false for bundle lookup; no unconditional schema default is published. |
| `includeUnavailable` | `boolean` | No | `true` | — | If true, include tool names that are part of the bundle but not available in the current runtime. |
| `includeCatalog` | `boolean` | No | `true` | — | If true (default), a bundle lookup also returns the discovery index: knownBundles plus bundleCatalog. Pass false once you have read it - the tools of the requested bundle are returned either way, so nothing you need to call them is lost. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Capability search 'download files and monitor transfer progress' returned 5/5 match(es); 5 available."
    }
  ],
  "structuredContent": {
    "ok": true,
    "requestedQuery": "download files and monitor transfer progress",
    "resolvedBundle": null,
    "description": "Bounded capability search over canonical tool names and descriptions.",
    "toolNames": [
      "nova.downloads_list",
      "nova.downloads_wait",
      "nova.downloads_pause",
      "nova.downloads_resume",
      "nova.downloads_cancel"
    ],
    "availableCount": 5,
    "requestedCount": 5,
    "hasMore": false,
    "partialMatch": false,
    "maxResults": 20,
    "includeDescriptions": false,
    "includeInputSchema": false,
    "includeCatalog": true
  }
}
```

A bundle lookup (`bundle: "downloads"`) returns the same `toolNames` shape plus the bundle's `description` and, with `includeCatalog` left at its default, `knownBundles` and `bundleCatalog` for further discovery.

---

## 4. Operational Best Practices

* **Context Conservation:** Load a curated bundle instead of keeping every tool schema in context; pass `includeInputSchema`/`includeDescriptions` only when the schema detail is actually needed.
* **Natural Language Discovery:** Search by intent keywords (`query`) when the right bundle or exact tool name is not known yet.

---

## 5. Related Tools

* [`nova.get_instructions`](nova-get-instructions.md)
