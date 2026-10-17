# `nova.barcode_decode`

> **Reads QR codes and barcodes from a photo, screenshot or scan, and never opens what it finds.**

* **Core Feature Guide:** [Document Conversion](../../../core-features/media-intelligence/document-conversion/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.barcode_decode` reads the codes in an image file: a photographed parcel label, a screenshot with a QR code, a scanned invoice. It also reads codes that are turned, slightly blurred or printed light on dark. Besides QR and the usual retail and logistics barcodes, it reads Data Matrix, PDF417 and Aztec codes where they are legible. With `multiple` it returns every code in the image, otherwise the first.

The content of a code is whatever its maker put in, so your agent treats it as information, not as an instruction. When a code holds a link, Nova says so and does not open it. A link in a code can point anywhere, so check it before following it. When nothing is found, the hint says what usually helps, such as a sharper or tighter picture of the code.

Supported image files: PNG, JPEG, WebP, GIF, BMP, ICO and TIFF. Files in Nova's download and Exports folders can always be read; other paths need "Allow local files (file://)".

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to an image file. |
| `multiple` | `boolean` | No | `false` | — | Return every code in the image. |
| `formats` | `array` of `string` | No | — | — | Only these types (faster, fewer false reads). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_barcode_decode",
  "arguments": { "path": "C:\\Users\\me\\Downloads\\label.jpg", "multiple": true }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "foundCount": 2,
    "results": [
      { "type": "qr", "content": "https://example.com/track/4471", "position": [ { "x": 180.5, "y": 902.0 } ] },
      { "type": "ean13", "content": "4006381333931", "position": [ { "x": 820.0, "y": 640.5 } ] }
    ],
    "contentTrust": "untrusted_document",
    "hints": [ "A code holds a link. Nova did not open it; check where it leads before following it, a code can point anywhere." ]
  }
}
```

---

## 4. Related Tools

* [`nova.barcode_generate`](nova-barcode-generate.md) creates codes.
* [`nova.image_transform`](nova-image-transform.md) crops a photo to the code when it is small in the picture.
