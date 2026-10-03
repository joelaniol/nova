# `nova.page_blobs_list`

> **Lists in-memory Blob and Object URLs (blob:http://...) created by the page.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Read-Only Resource State)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.page_blobs_list` enumerates client-side blob instances, revealing downloadable exports, generated images, or media streams.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `limit` | `integer` | No | Maximum number of blobs to return (1-200, default 50). totalFound and truncated report the overflow. |
| `probeMetadata` | `boolean` | No | Verify each handle by fetching it in the page, which fills in mimeType/sizeBytes and drops revoked handles. Set false to skip verification: faster, but mimeType/sizeBytes are null and dead handles may be listed. |
| `targetId` | `string` | No | Target ID of the tab to inspect from nova.tabs, or 'active' / 'activeBrowserTab'. |
| `watch` | `boolean` | No | Install a recorder for URL.createObjectURL in this document so blobs created from now on are listed even before they are attached to an element. Off by default; a page nobody asked about pays nothing. Already-created blobs cannot be recovered retroactively, so install the watch before triggering the action. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_page_blobs_list",
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
      "text": "Found 2 blob URLs: blob:https://example.com/3f8a-..."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "blobs": [
      {
        "url": "blob:https://example.com/3f8a-9b10",
        "mimeType": "application/pdf",
        "sizeBytes": 154200
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Dynamic Exports:** Locate generated CSV/PDF files created in-memory by Single Page Applications.

---

## 5. Related Tools

* [`nova.fetch_resource`](nova-fetch-resource.md)
* [`nova.save_pdf`](../visual-evidence/nova-save-pdf.md)
