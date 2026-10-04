# `nova.page_blobs_list`

> **Lists in-memory Blob and Object URLs (blob:http://...) created by the page.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.page_blobs_list` enumerates client-side blob instances, revealing downloadable exports, generated images, or media streams.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID of the tab to inspect from nova.tabs, or 'active' / 'activeBrowserTab'. |
| `watch` | `boolean` | No | `false` | — | Install a recorder for URL.createObjectURL in this document so blobs created from now on are listed even before they are attached to an element. Off by default; a page nobody asked about pays nothing. Already-created blobs cannot be recovered retroactively, so install the watch before triggering the action. |
| `probeMetadata` | `boolean` | No | `true` | — | Verify each handle by fetching it in the page, which fills in mimeType/sizeBytes and drops revoked handles. Set false to skip verification: faster, but mimeType/sizeBytes are null and dead handles may be listed. |
| `limit` | `integer` | No | `50` | 1–200 | Maximum number of blobs to return (1-200, default 50). totalFound and truncated report the overflow. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.page_blobs_list",
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
      "text": "1 live blob: URL(s) across 1 frame(s) (1 from the DOM, 0 from the createObjectURL watch)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "count": 1,
    "totalFound": 1,
    "limit": 50,
    "truncated": false,
    "coverage": "dom_only",
    "watchActive": false,
    "watchInstalled": false,
    "probeMetadata": true,
    "scannedFrames": 1,
    "inaccessibleFrames": 0,
    "droppedUnresolvable": 0,
    "revokedTotal": null,
    "revokedSinceLastCall": null,
    "revokedUrls": [],
    "mediaHints": {
      "audioElements": 0,
      "videoElements": 0,
      "mediaElementsWithBlobSrc": 0,
      "mediaElementsWithoutBlobSrc": 0,
      "mediaSourceSupported": true,
      "webAudioSupported": true,
      "audioContextsCreated": null,
      "decodeAudioDataCalls": null,
      "advice": ""
    },
    "blobs": [
      {
        "url": "blob:https://example.com/3f8a-9b10",
        "mimeType": "application/pdf",
        "sizeBytes": 154200,
        "source": "dom",
        "ownerSelector": "#invoice-link",
        "ownerTag": "a",
        "ownerAttribute": "href",
        "framePath": null,
        "sequence": null,
        "createdAtMs": null
      }
    ]
  }
}
```

There is no `targetId` field in the response (only in the request). `revokedTotal`/
`revokedSinceLastCall` stay `null` unless `watch: true` was passed on a previous call — null means
"not measured", not "zero revocations".

---

## 4. Operational Best Practices

* **Dynamic Exports:** Locate generated CSV/PDF files created in-memory by Single Page Applications.

---

## 5. Related Tools

* [`nova.fetch_resource`](nova-fetch-resource.md)
* [`nova.save_pdf`](../visual-evidence/nova-save-pdf.md)
