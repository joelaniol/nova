# `nova.barcode_generate`

> **Creates a QR code or barcode as a PNG or SVG file, crisp and checked by reading it back.**

* **Core Feature Guide:** [Document Conversion](../../../core-features/media-intelligence/document-conversion/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.barcode_generate` makes the codes an everyday task needs: a QR code for a link, a Wi-Fi login or any text (including umlauts and other scripts), and the barcodes of retail and logistics: Code 128 for article and order numbers, EAN-13, EAN-8 and UPC-A for product numbers. Everything runs on your computer.

Codes are drawn the way scanners like them. Every module is a whole number of pixels, never blurred, with the empty margin around the code that the standard requires. The size you ask for is a target, so the result can be a little smaller and stays sharp. The answer gives the real size.

Retail numbers are checked, not repaired. If the last digit (the check digit) is wrong, Nova refuses and names the right one, because a quietly "fixed" number would label the wrong product. If you leave the check digit out, Nova adds it and says so.

Before the file is written, Nova reads the drawn code back and compares it with the content. SVG files are plain shapes with no scripts and no external references. The file goes to Nova's Exports folder unless you name a path, and no existing file is overwritten.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `content` | `string` | Yes | — | — | Text, link or number to encode. |
| `type` | `string` | No | `"qr"` | `qr`, `code128`, `ean13`, `ean8`, `upca` | — |
| `format` | `string` | No | — | `png`, `svg` | Default: from outputPath, else png. |
| `outputPath` | `string` | No | — | — | Absolute path of the new file (.png or .svg). Default: Exports/Codes. |
| `width` | `integer` | No | — | 20–4000 | Target width in pixels (default 400). |
| `height` | `integer` | No | — | 20–4000 | Target height of a barcode in pixels; a QR code is square. |
| `errorCorrection` | `string` | No | `"M"` | `L`, `M`, `Q`, `H` | QR only: how much damage the code survives (L 7 %, M 15 %, Q 25 %, H 30 %). |
| `includeText` | `boolean` | No | — | — | Print the content under a barcode; default on for EAN/UPC, off otherwise. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_barcode_generate",
  "arguments": { "content": "https://nova-cognitive.com", "type": "qr", "errorCorrection": "H", "width": 600 }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "type": "qr",
    "encodedContent": "https://nova-cognitive.com",
    "outputPath": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Codes\\qr-20261017-101500.png",
    "format": "png",
    "width": 594,
    "height": 594,
    "moduleSize": 18,
    "verified": true
  }
}
```

---

## 4. Related Tools

* [`nova.barcode_decode`](nova-barcode-decode.md) reads codes from images.
