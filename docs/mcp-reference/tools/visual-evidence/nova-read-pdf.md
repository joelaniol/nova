# `nova.read_pdf`

> **Extracts the text of a local PDF file, optionally per page and for selected pages only.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../core-features/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.read_pdf` reads the text of a PDF on disk, for example a file from `nova.downloads_list` (`filePath`) or one written by `nova.save_pdf` (`savedPath`). It returns the extracted text, the page count, the pages actually read and, with `includePages: true`, the text per page. It does not return document metadata such as title or author, and it does not run OCR: a scanned or image-only PDF returns `reasonCode: "read_pdf.no_extractable_text"`. Password-protected files return `read_pdf.encrypted`, a missing file `read_pdf.not_found`. Files in Nova's download folder and Exports folder can always be read; any other path needs the setting "Allow local files (file://)".

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to the .pdf file, e.g. the filePath from nova.downloads_list or the savedPath from nova.save_pdf. A download that is still running has no final file yet - nova.downloads_wait blocks until it does. |
| `pages` | `string` | No | — | — | Optional 1-based page selection, e.g. '1', '2-5' or '1,4-6'. Omit to read every page. Pages beyond the end are ignored rather than rejected, so '1-10' on a 3-page file reads those three. |
| `maxChars` | `integer` | No | `50000` | 1000–2000000 | Character budget for the returned text. Extraction continues past it so totalChars stays exact; truncated=true then tells you how much was left out. |
| `includePages` | `boolean` | No | `false` | — | Also return the text split per page (pages[{page,text}]) instead of only the concatenated text. Off by default because it roughly doubles the response size. |

Capability bundles: `page_read_debug`, `visual_evidence`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_read_pdf",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\invoice-1042.pdf",
    "pages": "1"
  }
}
```

### JSON-RPC Response

The text block carries the extracted text itself.

```json
{
  "content": [
    {
      "type": "text",
      "text": "INVOICE #1042\nDate: 2026-09-30\nCustomer: Example GmbH\nTotal due: EUR 1,240.00"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "path": "C:\\Users\\me\\Downloads\\invoice-1042.pdf",
    "fileName": "invoice-1042.pdf",
    "pageCount": 3,
    "pagesRead": [
      1
    ],
    "text": "INVOICE #1042\nDate: 2026-09-30\nCustomer: Example GmbH\nTotal due: EUR 1,240.00",
    "totalChars": 77,
    "chars": 77,
    "truncated": false,
    "pages": null,
    "outputBudget": {
      "effectiveLimit": 50000,
      "returnedChars": 77,
      "truncated": false
    }
  }
}
```

On a failure (`not_found`, `blocked`, `empty`, `error`) `ok` is `false`, `text` is empty and `message` explains the next step.

---

## 4. Operational Best Practices

* **Verify generated files:** Pair with `nova.save_pdf` or a finished download (`nova.downloads_wait`) to check that a document contains what it should.
* **Large files:** Raise `maxChars` or read a page range with `pages` when `truncated` is `true`; `totalChars` tells how much text the selection holds.

---

## 5. Related Tools

* [`nova.save_pdf`](nova-save-pdf.md)
