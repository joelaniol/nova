# `nova.list_resources`

> **Lists all network resources (scripts, stylesheets, frames, images) loaded by the target tab.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.list_resources` enumerates the scripts, stylesheets, documents, and other resources a tab has loaded, merging the CDP resource tree with the Performance timeline by default (a rebuilt tree can forget lazily loaded chunks the timeline still knows) and falling back to a DOM scan. Each entry carries its frame id, URL, type, and discovery source; CDP-sourced entries also carry a MIME type and content size.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `source` | `string` | No | `"auto"` | `auto`, `cdp`, `performance`, `dom` | Discovery method. 'auto': merges the CDP resource tree with the Performance timeline (deduplicated by URL) and falls back to DOM tags - use it, because a tree rebuilt after a reattach forgets lazily loaded chunks the timeline still knows. 'cdp': CDP resource tree only. 'performance': Performance API entries only. 'dom': scans DOM tags (script/link/img). The result reports sources/sourceCounts and a hint when the merge added entries. |
| `types` | `array` of `string` | No | `["Script","Stylesheet","Document"]` | — | Resource types to include. Common values: Script, Stylesheet, Document, Image, Font, XHR, Fetch, Media, WebSocket. |
| `maxItems` | `integer` | No | `200` | 1–2000 | Maximum number of resources to return. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_list_resources",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "{ ... same JSON as structuredContent, pretty-printed ... }"
    }
  ],
  "structuredContent": {
    "profileId": "tab-1",
    "source": "cdp",
    "sources": ["cdp", "performance"],
    "sourceCounts": { "cdp": 24, "performance": 6 },
    "rootFrameId": "frame-abc",
    "truncated": false,
    "hint": "performance knew 6 resource(s) the cdp listing did not (cdp: 24, performance: 24). Both are included. Lazily loaded chunks drop out of the CDP tree after a reattach, so a short listing is not proof the page does not load them.",
    "resources": [
      {
        "frameId": "frame-abc",
        "url": "https://example.com/main.js",
        "type": "Script",
        "mimeType": "application/javascript",
        "contentSize": 120540,
        "discoverySource": "cdp"
      }
    ]
  }
}
```

The `hint` field is only present when the Performance timeline added entries the CDP tree did not have. Entries discovered via the Performance timeline carry `initiatorType`/`transferSize`/`decodedBodySize` instead of `mimeType`/`contentSize`; DOM-fallback entries carry only `frameId`, `url`, `type`, and `discoverySource`.

---

## 4. Operational Best Practices

* **Targeted Reading:** Use this list to pick specific resource URLs for `nova.read_resource` or `nova.grep_resources`.

---

## 5. Related Tools

* [`nova.read_resource`](nova-read-resource.md)
* [`nova.grep_resources`](nova-grep-resources.md)
