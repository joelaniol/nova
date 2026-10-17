# `nova.image_info`

> **Describes a local image file: format, size as shown, animation, transparency and which metadata it carries, with hints for the next step.**

* **Core Feature Guide:** [Local Image Processing](../../../core-features/media-intelligence/image-processing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.image_info` tells your agent what an image file is before it works with it: the format, the width and height as the picture is shown, whether it is animated, whether it has a transparency channel, its colour space, and which metadata it carries. Metadata covers camera data (EXIF), a GPS position, a preview image inside EXIF, XMP, a colour profile, text comments and the stated resolution. It also returns what the file states, without any extra program: when the photo was taken, camera and lens, exposure, the GPS position in decimal degrees, software, artist and copyright, and text comments such as the prompt an image generator stored. Nothing in the file is changed, and nothing is uploaded.

Phone photos are often stored turned and only shown upright because of a note in the file (the EXIF orientation). Nova reports the size as the picture is shown, and the stored size and the orientation separately.

`hints` turns the facts into next steps. Examples: the photo carries a GPS position, so write a copy without it before sharing; the image is very large, so a smaller copy is cheaper to look at; the file is animated, and a transformed copy keeps only the first frame.

Supported: PNG, JPEG, WebP, GIF, BMP, ICO and TIFF; HEIC and JPEG XR only where Windows has the codec. Files in Nova's download and Exports folders can always be read; other paths need "Allow local files (file://)".

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to an image file. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_image_info",
  "arguments": { "path": "C:\\Users\\me\\Pictures\\IMG_2041.jpg" }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "format": "jpeg",
    "width": 4032,
    "height": 3024,
    "storedWidth": 3024,
    "storedHeight": 4032,
    "orientation": 6,
    "frames": 1,
    "alphaChannel": false,
    "colorSpace": "sRGB",
    "metadata": { "exif": true, "gps": true, "exifThumbnail": true, "xmp": false, "colorProfile": true, "textComments": 0, "dpiX": 72, "dpiY": 72 },
    "exifValues": { "taken": "2026-08-14T18:42:07+02:00", "cameraMake": "Apple", "cameraModel": "iPhone 15", "exposureTime": "1/120 s", "fNumber": 1.6, "iso": 64, "gpsLatitude": 47.42345, "gpsLongitude": 10.98512, "gpsAltitudeM": 2962.4 },
    "hints": [
      "The image carries a GPS position (where it was taken). Before sharing or uploading it, write a copy without it: nova.image_transform with stripMetadata=true."
    ]
  }
}
```

---

## 4. Related Tools

* [`nova.image_transform`](nova-image-transform.md) writes a cropped, turned, resized or converted copy, with or without metadata.
* [`nova.ocr_read`](nova-ocr-read.md) reads the text in an image.
