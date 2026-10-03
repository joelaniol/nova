# `nova.read_pdf`

> **Extracts plain text and page metadata from a locally saved PDF document.**

* **Capability Bundle:** `visual_evidence`
* **Security Tier:** Tier 1 (Read-Only Document Extraction)
* **Core Feature Guide:** [Visual Evidence & Auditing](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.read_pdf` parses PDF files on disk without external tools, returning extracted text per page, author metadata, and page counts.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `includePages` | `boolean` | No | Also return the text split per page (pages[{page,text}]) instead of only the concatenated text. Off by default because it roughly doubles the response size. |
| `maxChars` | `integer` | No | Character budget for the returned text. Extraction continues past it so totalChars stays exact; truncated=true then tells you how much was left out. |
| `pages` | `string` | No | Optional 1-based page selection, e.g. '1', '2-5' or '1,4-6'. Omit to read every page. Pages beyond the end are ignored rather than rejected, so '1-10' on a 3-page file reads those three. |
| `path` | `string` | **Yes** | Absolute path to the .pdf file, e.g. the filePath from nova.downloads_list or the savedPath from nova.save_pdf. A download that is still running has no final file yet - nova.downloads_wait blocks until it does. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_read_pdf",
  "arguments": {
    "filePath": "E:\\Reports\\Invoice_2026.pdf",
    "maxPages": 5
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Extracted text from 3 pages in Invoice_2026.pdf."
    }
  ],
  "structuredContent": {
    "ok": true,
    "pagesCount": 3,
    "title": "Invoice #1042",
    "text": "Invoice details..."
  }
}
```

---

## 4. Operational Best Practices

* **Verification Pipeline:** Pair with `nova.save_pdf` to verify generated report contents automatically.

---

## 5. Related Tools

* [`nova.save_pdf`](nova-save-pdf.md)
