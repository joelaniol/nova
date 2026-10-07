# `nova.fetch_resource`

> **Downloads one or more URLs with the tab's session cookies and saves them to files.**

* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tool-observation-bus-tob/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.fetch_resource` downloads one URL (`url`) or up to 50 URLs (`urls`) from inside the tab and writes them to disk. The request runs as a page-side `fetch` with the tab's credentials, so it carries the tab's cookies like the page itself would; it is bound by CORS for cross-origin URLs like any other page request and does not bypass it. `blob:` URLs that are live in the tab work too.

The response body never comes back through MCP: Nova writes the bytes to a file and returns only the path, size, HTTP status and content type. Without `savePath`/`saveDir`, files go into Nova's Exports folder; a path of your own needs the 'Allow local files' setting. In bulk mode the result lists each URL in `results` with `savedCount` and `failedCount`.

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

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
    "savePath": "C:\\Temp\\profile.json"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Fetched 2048 bytes from https://app.example.com/api/v1/user/profile -> C:\\Temp\\profile.json"
    }
  ],
  "structuredContent": {
    "ok": true,
    "url": "https://app.example.com/api/v1/user/profile",
    "status": 200,
    "httpOk": true,
    "contentType": "application/json",
    "filePath": "C:\\Temp\\profile.json",
    "bytes": 2048,
    "deliveryMode": "file"
  }
}
```

---

## 4. Operational Best Practices

* **Session-Bound Downloads:** Pull files from an authenticated tab without exporting its cookies; the agent only sees the saved file path.
* **Read the File Separately:** The body is not in the response; open the saved file if its content is needed.

---

## 5. Related Tools

* [`nova.stream_url`](nova-stream-url.md)
* [`nova.network_read`](nova-network-read.md)
