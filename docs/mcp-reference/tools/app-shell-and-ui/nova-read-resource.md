# `nova.read_resource`

> **Fetches the raw text content of a loaded web resource by its URL.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.read_resource` fetches the content of an http/https resource a tab has loaded (scripts, stylesheets, JSON, HTML, and similar), preferring CDP's cached resource content and falling back to a page-side `fetch()` when CDP cannot serve it. Binary content comes back base64-encoded; `nova://screenshot/...` URIs are rejected here with a pointer to `nova.read_screenshot_resource` or the MCP `resources/read` method.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "function init(){console.log(\"App ready\");}..."
    }
  ],
  "structuredContent": {
    "profileId": "tab-1",
    "source": "cdp",
    "frameId": "frame-abc",
    "url": "https://example.com/bundle.js",
    "mimeType": "application/javascript",
    "ok": true,
    "status": null,
    "reasonCode": null,
    "base64Encoded": false,
    "truncated": false,
    "chars": 45210,
    "bytes": null,
    "charOffset": 0,
    "charOffsetApplied": true,
    "charOffsetSkippedReason": null,
    "nextCharOffset": 45210,
    "resourceText": "function init(){console.log(\"App ready\");}...",
    "resourceBase64": null,
    "outputBudget": { "...": "..." }
  }
}
```

A binary resource (`base64Encoded: true`) carries its content in `resourceBase64` instead of `resourceText`, has no `nextCharOffset`, and `charOffsetApplied` is `false` with a `charOffsetSkippedReason`. `source` is `"fetch"` instead of `"cdp"` when Nova falls back to a page-side fetch; that path also fills `status` (HTTP status) and, on failure, `reasonCode`.

---

## 4. Operational Best Practices

* **Bundle Inspection:** Use to review client-side routing definitions or API contract endpoints.

---

## 5. Related Tools

* [`nova.list_resources`](nova-list-resources.md)
* [`nova.grep_resources`](nova-grep-resources.md)
