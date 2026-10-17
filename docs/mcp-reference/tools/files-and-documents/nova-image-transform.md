# `nova.image_transform`

> **Writes a changed copy of a local image: crop, rotate, flip, resize, convert or remove metadata. The original stays untouched.**

* **Core Feature Guide:** [Local Image Processing](../../../core-features/media-intelligence/image-processing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet.

`nova.image_transform` covers everyday image chores for your agent without an image editor: cut out an area, turn the picture, mirror it, make it smaller, save it as PNG, JPEG, WebP or BMP, or remove personal data and bulky metadata before a photo is shared. Everything runs on your computer with Nova's own image engine.

The copy is always stored upright, even when the source was only shown upright because of a note in the file. The steps run in a fixed order: straighten, crop, rotate, flip, resize, save. Crop coordinates therefore refer to the picture as you see it, matching the width and height that [`nova.image_info`](nova-image-info.md) reports.

Resizing fits the image into a box by default and keeps its proportions. `fill` covers the box and cuts the overflow evenly, `stretch` forces the exact size. A smaller image is not enlarged unless you ask for it.

Metadata stays unless you remove it. `stripMetadata` removes everything. `removeMetadata` removes only the groups you name and keeps the rest:

| Group | What goes |
| :--- | :--- |
| `location` | GPS position |
| `people` | Artist, copyright, Windows author, camera owner |
| `deviceIds` | Serial numbers of camera body and lens, image unique ID |
| `software` | Editing software and the computer name |
| `text` | Description, user comment, Windows title, comment, keywords and subject |
| `makerNotes` | The camera maker's private block, often tens of kilobytes |
| `xmp` | The whole XMP block: edit history, document ancestors, rights, creator tool |
| `dates` | Dates and times |
| `camera` | Camera and lens make and model |

Two presets cover the usual cases. `privacy` removes `location`, `people`, `deviceIds`, `software`, `text`, `makerNotes` and `xmp` and keeps camera, exposure and date, which is the safe choice before a photo is shared. `bloat` removes `makerNotes`, `xmp` and `software`: editing programs such as Photoshop leave a long edit history and lists of earlier documents in XMP that can make a small picture many times larger. The answer lists in `metadataRemoved` what went. XMP repeats much of EXIF; when it repeats a group you removed, it is left out as a whole, so a name or position does not survive there.

Camera data (EXIF) and XMP are carried into JPEG and PNG copies; WebP and BMP copies get none, and the answer says so. Some things are never carried over:

* **The old orientation note.** The pixels are already upright, so the note would turn them twice.
* **The preview image inside EXIF.** In a cropped photo it would still show the whole original.
* **Photoshop's own block and text comments.** The block holds IPTC data, paths and its own previews.

The copy states its own pixel size. XMP that points to attachments behind the picture, like the short video of a motion photo or an HDR gain map, is left out, because the copy does not have them and viewers would otherwise look for them. When the copy keeps a GPS position, the answer names it, so a photo is not shared by accident with the place it was taken.

The original file is never changed and no existing file is overwritten. Without `outputPath` the copy goes to Nova's Exports folder. Before it gets its name, the new file is read back and its size is checked. JPEG cannot store transparency, so transparent areas become white; animations keep only their first frame. Both are reported as warnings.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to the source image. |
| `outputPath` | `string` | No | — | — | Absolute path of the new file; its extension must match format. Default: Exports/Images. |
| `format` | `string` | No | — | `png`, `jpeg`, `webp`, `bmp` | Output format; default from outputPath, else the source format, else png. |
| `crop` | `object` | No | — | — | Area to keep, in pixels of the image as shown. |
| `crop.x` | `integer` | Yes | — | ≥ 0 | — |
| `crop.y` | `integer` | Yes | — | ≥ 0 | — |
| `crop.width` | `integer` | Yes | — | ≥ 1 | — |
| `crop.height` | `integer` | Yes | — | ≥ 1 | — |
| `rotate` | `integer` | No | — | `90`, `180`, `270` | Degrees clockwise. |
| `flip` | `string` | No | — | `horizontal`, `vertical` | — |
| `resize` | `object` | No | — | — | Target size; fit needs width or height, fill and stretch need both. |
| `resize.width` | `integer` | No | — | 1–16383 | — |
| `resize.height` | `integer` | No | — | 1–16383 | — |
| `resize.mode` | `string` | No | `"fit"` | `fit`, `fill`, `stretch` | — |
| `resize.allowUpscale` | `boolean` | No | `false` | — | — |
| `quality` | `integer` | No | — | 1–100 | JPEG (default 90) and WebP (default 85, 100 = lossless). |
| `stripMetadata` | `boolean` | No | `false` | — | Write no EXIF, GPS or XMP into the copy. |
| `removeMetadata` | `array` of `string` | No | — | — | Metadata groups to remove, or the presets privacy (personal data) and bloat (bulk); the rest is kept. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_image_transform",
  "arguments": {
    "path": "C:\\Users\\me\\Pictures\\IMG_2041.jpg",
    "resize": { "width": 1600 },
    "format": "webp",
    "removeMetadata": ["privacy"]
  }
}
```

### JSON-RPC Response

```json
{
  "structuredContent": {
    "ok": true,
    "outputPath": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Exports\\Images\\IMG_2041-20261017-101500.webp",
    "inputFormat": "jpeg",
    "outputFormat": "webp",
    "inputSize": { "width": 3024, "height": 4032 },
    "outputSize": { "width": 1600, "height": 1200 },
    "orientationApplied": 6,
    "size": 148220,
    "metadataWritten": { "exif": false, "gps": false, "exifThumbnail": false, "xmp": false, "colorProfile": true, "textComments": 0 },
    "metadataRemoved": ["artist", "bodySerialNumber", "gps", "makerNotes", "xmp"],
    "warnings": []
  }
}
```

---

## 4. Related Tools

* [`nova.image_info`](nova-image-info.md) shows size, orientation and metadata first.
