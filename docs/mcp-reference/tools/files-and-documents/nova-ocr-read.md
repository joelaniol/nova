# `nova.ocr_read`

> **Reads the text of a scanned PDF or an image by text recognition, locally and offline, and says per page how far it can be trusted.**

* **Core Feature Guide:** [Offline Optical Character Recognition (OCR)](../../../core-features/media-intelligence/ocr/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.ocr_read` is for documents that have no text of their own: scanned letters, photographed receipts, faxes, screenshots, image-only PDF exports. [`nova.read_pdf`](nova-read-pdf.md) and [`nova.convert_to_markdown`](nova-convert-to-markdown.md) report such pages as having no text layer; this tool reads them. Recognition runs on your computer with engines Nova ships. Nothing is uploaded, and you do not need to install anything.

Nova has two recognition engines, and your agent can choose:

| Engine | Strong on |
| :--- | :--- |
| Tesseract | Clean printed pages: letters, contracts, notices, book pages. Keeps paragraphs. Fast. |
| PaddleOCR | Receipts and thermal paper, dense forms, photos of paper, faded, skewed or noisy scans, small print. Keeps an item and its amount on one line. |

By default (`engine: "auto"`), every page is read with Tesseract first. When Tesseract is unsure, the page is read again with PaddleOCR and the clearly better reading is kept. A much shorter reading never replaces a longer one on a small difference. `engine: "both"` returns both readings side by side, which is useful when names, numbers or amounts matter. Neither engine reads handwriting reliably.

Every page is turned upright before it is read. For each page the answer gives the engine used, a quality rating (`good`, `uncertain`, `poor` or `empty`), the engines' confidence and a short hint on what the result means and what to try next. A list of advice covers the whole answer: which pages are left, which pages are worth comparing, and which pages already have a text layer that another tool reads exactly.

A page takes about 2 to 12 seconds. When the answer reaches its size limit (`maxChars`) or the time budget runs out, you get the pages read so far, marked as partial, plus the pages still to do.

The text is returned exactly as recognised. It is never corrected or smoothed, so a misread digit stays visible as a misread digit. Formats: PDF, PNG, JPEG, TIFF (all pages), BMP, GIF and WebP. Files in Nova's download and Exports folders can always be read; other paths need "Allow local files (file://)". Nothing is written or kept.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to a PDF or image file. |
| `pages` | `string` | No | — | — | 1-based pages and ranges in reading order, e.g. '1-3,7'; default all. Frames for a multi-page TIFF. |
| `engine` | `string` | No | `"auto"` | `auto`, `tesseract`, `paddle`, `both` | auto: Tesseract, PaddleOCR where Tesseract is unsure. tesseract: clean printed pages. paddle: receipts, forms, photos, faded or noisy scans. both: both readings to compare. |
| `maxChars` | `integer` | No | `60000` | 1000–400000 | Stop after the page that reaches this many characters; the rest is listed in pagesNotRead. |
| `timeoutSeconds` | `integer` | No | `180` | 10–540 | Time budget for the whole call. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ocr_read",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\receipts.pdf",
    "pages": "1-2"
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "complete": true,
    "kind": "pdf",
    "pageCount": 12,
    "engineRequested": "auto",
    "source": "ocr",
    "pages": [
      {
        "page": 1,
        "engine": "tesseract",
        "quality": "good",
        "confidence": 0.92,
        "tesseractConfidence": 0.92,
        "hint": null,
        "text": "Invoice no. 2020-4471 ..."
      },
      {
        "page": 2,
        "engine": "paddle",
        "quality": "uncertain",
        "confidence": 0.87,
        "tesseractConfidence": 0.51,
        "paddleConfidence": 0.87,
        "hint": "Tesseract was unsure (0.51), so PaddleOCR's reading is shown. Probably readable but with errors; check names, numbers and amounts. engine='both' returns both readings to compare.",
        "text": "Milk 3.5%  0,99 A\nCoffee  7,99 A\n..."
      }
    ],
    "advice": [
      "Page 2 is not reliably read. Before using names, numbers or amounts from it, compare both engines with engine='both' pages='2', or look at the page itself."
    ]
  }
}
```

---

## 4. Related Tools

* [`nova.convert_to_markdown`](nova-convert-to-markdown.md) and [`nova.read_pdf`](nova-read-pdf.md) for PDFs that have a text layer: exact text, no recognition errors.
