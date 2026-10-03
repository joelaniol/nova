# `nova.list_resources`

> **Lists all network resources (scripts, stylesheets, frames, images) loaded by the target tab.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.list_resources` enumerates cached assets and external documents associated with the active web page, including MIME types and byte sizes.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `maxItems` | `integer` | No | Maximum number of resources to return. |
| `source` | `string` | No | Discovery method. 'auto': merges the CDP resource tree with the Performance timeline (deduplicated by URL) and falls back to DOM tags - use it, because a tree rebuilt after a reattach forgets lazily loaded chunks the timeline still knows. 'cdp': CDP resource tree only. 'performance': Performance API entries only. 'dom': scans DOM tags (script/link/img). The result reports sources/sourceCounts and a hint when the merge added entries. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `types` | `array` | No | Resource types to include. Common values: Script, Stylesheet, Document, Image, Font, XHR, Fetch, Media, WebSocket. |

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
      "text": "Loaded resources: 24 scripts, 5 stylesheets, 1 document."
    }
  ],
  "structuredContent": {
    "ok": true,
    "resourcesCount": 30,
    "resources": [
      {
        "url": "https://example.com/main.js",
        "type": "Script",
        "size": 120540
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Targeted Reading:** Use this list to pick specific resource URLs for `nova.read_resource` or `nova.grep_resources`.

---

## 5. Related Tools

* [`nova.read_resource`](nova-read-resource.md)
* [`nova.grep_resources`](nova-grep-resources.md)
