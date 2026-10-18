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

QR codes can carry a design. `style` gives the data modules rounded corners or turns them into dots, `foreground` and `background` set the colours, `gradientTo` lets the modules fade into a second colour (diagonal, horizontal, vertical or from the centre outwards), `finderColor` gives the three large corner squares their own colour, `logoPath` puts your logo in the centre, and `caption` prints a call to action such as "Scan me" under or above the code, in any font installed on the computer, in its own colour, bold or regular, in capitals or small letters and in three sizes; a line too wide for the image is set smaller, and the answer says so. The three large corner squares and the other structure patterns always stay plain, because that is what a phone camera looks for first. Nova refuses designs that scan badly and says why: colours with too little contrast (for a gradient, every shade along the way counts), light modules on a dark background, a logo on a code too long to leave room for it, or a print size with modules smaller than a quarter of a millimetre. With a logo the code switches to the strongest error correction (H) by itself.

Every QR code is then checked the way a camera would see it: smaller, compressed, blurred, turned, tilted and unevenly lit. `quality` sums it up: `robust` when all eight checks pass, `verified` when at most two fail, `experimental` when more fail. Then test it with a real phone before printing. The checks are a simulation, not a guarantee for every phone.

Instead of writing the content yourself, `data` builds it from fields in the exact format phones expect:

| `data.kind` | Fields | Notes |
| :--- | :--- | :--- |
| `wifi` | `ssid`, `password`, `security` (wpa, wep, nopass), `hidden` | Joins the network when scanned. The password is not repeated in the answer. |
| `vcard` | `name`, `firstName`, `lastName`, `organization`, `title`, `phone`, `mobile`, `email`, `url`, `address`, `note` | Contact card (vCard 3.0). |
| `mecard` | The same fields as `vcard`, without `title` | Contact card as a MeCard: about half as long, so the code gets fewer and larger squares and scans more easily when printed small. Phones read both formats. |
| `epc` | `name`, `iban`, `bic`, `amount`, `reference` or `text` | SEPA transfer (GiroCode). The IBAN check digits are verified and a wrong IBAN is refused, never corrected. Banking apps read it; the camera app usually does not. No logo. |
| `email` | `to`, `subject`, `body` | Opens a prepared e-mail. |
| `tel` | `number` | Calls the number. |
| `sms` | `number`, `body` | Opens a prepared text message. |
| `geo` | `latitude`, `longitude` | Opens the place in a map app. |
| `event` | `title`, `start`, `end`, `location`, `description` | Offers to add an appointment to the calendar. A date like `2026-10-20` makes an all-day event; a time like `2026-10-20T09:30` uses the phone's time zone, `+02:00` or `Z` fixes it. |

Before the file is written, Nova reads the drawn code back and compares it with the content. SVG files are plain shapes with no scripts and no external references. The file goes to Nova's Exports folder unless you name a path, and no existing file is overwritten.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `content` | `string` | No | — | — | Text, link or number to encode. For a QR code, data can build it instead. |
| `data` | `object` | No | — | — | QR only, instead of content: kind plus its fields (see the description) - wifi, vcard, mecard, epc, event, email, tel, sms or geo. |
| `data.kind` | `string` | Yes | — | `wifi`, `vcard`, `mecard`, `epc`, `email`, `tel`, `sms`, `geo`, `event` | — |
| `type` | `string` | No | `"qr"` | `qr`, `code128`, `ean13`, `ean8`, `upca` | — |
| `format` | `string` | No | — | `png`, `svg` | Default: from outputPath, else png. |
| `outputPath` | `string` | No | — | — | Absolute path of the new file (.png or .svg). Default: Exports/Codes. |
| `width` | `integer` | No | — | 20–4000 | Target width in pixels (default 400). |
| `height` | `integer` | No | — | 20–4000 | Target height of a barcode in pixels; a QR code is square. |
| `errorCorrection` | `string` | No | `"M"` | `L`, `M`, `Q`, `H` | QR only: how much damage the code survives (L 7 %, M 15 %, Q 25 %, H 30 %). |
| `includeText` | `boolean` | No | — | — | Print the content under a barcode; default on for EAN/UPC, off otherwise. |
| `style` | `string` | No | `"classic"` | `classic`, `rounded`, `dots` | QR only: shape of the data modules. |
| `foreground` | `string` | No | `"#000000"` | — | QR only: module colour #RRGGBB, darker than the background. |
| `background` | `string` | No | `"#FFFFFF"` | — | QR only: background colour #RRGGBB. |
| `gradientTo` | `string` | No | — | — | QR only: the modules fade from foreground to this colour #RRGGBB. |
| `gradientDirection` | `string` | No | `"diagonal"` | `diagonal`, `horizontal`, `vertical`, `radial` | QR only, with gradientTo: direction of the fade; radial runs from the centre outwards. |
| `finderColor` | `string` | No | — | — | QR only: colour #RRGGBB of the three corner squares. |
| `logoPath` | `string` | No | — | — | QR only: absolute path to a PNG or JPEG logo for the centre (error correction H). |
| `caption` | `string` | No | — | ≤ 40 characters | QR only: text under the code, e.g. 'Scan me'. |
| `captionFont` | `string` | No | `"Segoe UI"` | — | QR only, with caption: an installed font family, e.g. 'Georgia', 'Bahnschrift', 'Consolas'. |
| `captionColor` | `string` | No | — | — | QR only, with caption: text colour #RRGGBB; default the module colour. |
| `captionBold` | `boolean` | No | `true` | — | QR only, with caption: bold text. |
| `captionPosition` | `string` | No | `"below"` | `below`, `above` | QR only, with caption: above or below the code. |
| `captionCase` | `string` | No | `"asWritten"` | `asWritten`, `upper`, `lower` | QR only, with caption: as written, all upper case or all lower case. |
| `captionSize` | `string` | No | `"medium"` | `small`, `medium`, `large` | QR only, with caption: text size relative to the code. |
| `printWidthMm` | `number` | No | — | 5–2000 | QR only: printed width in mm including the white border, to check the module size. |

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
