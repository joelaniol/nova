# `nova.read_resource`

> **Fetches the raw text content of a loaded web resource by its URL.**

* **Security Tier:** Tier 1 (Read-Only Resource Extraction)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.read_resource` retrieves JavaScript sources, CSS style sheets, JSON payloads, or HTML templates cached in the target tab's resource registry.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `url` | `string` | Yes | — | — | Full http/https URL of the page resource to read (as returned by nova.list_resources). For nova://screenshot/... URIs use nova.read_screenshot_resource or MCP resources/read. |
| `frameId` | `string` | No | — | — | Optional frame ID for resources loaded in iframes (as returned by nova.list_resources). Omit for main frame. |
| `maxChars` | `integer` | No | `100000` | 1000–5000000 | Maximum characters for text resource content. |
| `maxBytes` | `integer` | No | `1048576` | 1024–50000000 | Maximum bytes for binary resource content (base64-encoded). |
| `charOffset` | `integer` | No | `0` | 0–50000000 | Start reading a TEXT resource this many characters in, so a match found by nova.grep_resources (which reports index) can be widened without searching again: charOffset=index-500 with maxChars=1200 puts the hit in the middle. The result carries charOffset, nextCharOffset (charOffset + chars) for paging, and sourceChars for the total. An offset at or past the end returns an empty window instead of the file's head; a binary resource has no character window and answers charOffsetApplied=false with charOffsetSkippedReason. |

Capability bundles: `page_read_debug`, `visual_evidence`.
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_read_resource",
  "arguments": {
    "targetId": "tab-1",
    "url": "https://example.com/bundle.js"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Read 45,210 bytes from https://example.com/bundle.js."
    }
  ],
  "structuredContent": {
    "ok": true,
    "url": "https://example.com/bundle.js",
    "sizeBytes": 45210,
    "content": "function init(){console.log(\"App ready\");}..."
  }
}
```

---

## 4. Operational Best Practices

* **Bundle Inspection:** Use to review client-side routing definitions or API contract endpoints.

---

## 5. Related Tools

* [`nova.list_resources`](nova-list-resources.md)
* [`nova.grep_resources`](nova-grep-resources.md)
