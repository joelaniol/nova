# `nova.fetch_resource`

> **Fetches content from a URL inside the browser tab context, inheriting session cookies and origin credentials.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 2 (Network Fetch)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.fetch_resource` executes a fetch HTTP request from inside the tab, bypassing CORS restrictions and automatically attaching session cookies and authorization headers.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID of the authenticated tab from nova.tabs, or 'active' / 'activeBrowserTab'. |
| `url` | `string` | No | — | — | Single absolute http(s) URL, or a blob: URL live in this tab, to fetch. Mutually exclusive with 'urls'. |
| `urls` | `array` of `string` | No | — | 1–50 items | Bulk list of URLs to fetch sequentially; http(s) and blob: entries may be mixed. Mutually exclusive with 'url'. Per-call cap 50. |
| `savePath` | `string` | No | — | — | Single mode only: absolute file path to write the resource to. Requires 'Allow local files'. Omit to write into Nova's Exports folder with a name derived from the URL. |
| `saveDir` | `string` | No | — | — | Bulk mode (or single): absolute directory to write resources into. Requires 'Allow local files'. Omit to use Nova's Exports folder. File names are derived from URL basenames — for blob: URLs from the handle plus an extension guessed from the MIME type — and made collision-free. |
| `maxBytes` | `integer` | No | `10485760` | 1–26214400 | Maximum bytes per resource. Resources larger than this are reported as errors instead of saved. Default 10 MB, ceiling 25 MB (the body travels base64-through-CDP, so larger pulls cost multiplied transient memory). |
| `timeoutMs` | `integer` | No | `30000` | 1000–120000 | Per-resource fetch timeout in milliseconds. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_fetch_resource",
  "arguments": {
    "targetId": "tab-1",
    "url": "https://app.example.com/api/v1/user/profile",
    "method": "GET"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Fetched 200 OK from /api/v1/user/profile."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": 200,
    "contentType": "application/json",
    "body": "{\"id\": 101, \"name\": \"Admin\"}"
  }
}
```

---

## 4. Operational Best Practices

* **Session-Bound API Calls:** Call internal endpoints without extracting or leaking session cookies to LLM context.

---

## 5. Related Tools

* [`nova.stream_url`](nova-stream-url.md)
* [`nova.network_read`](nova-network-read.md)
