# `nova.convert_to_markdown`

> **Converts a local PDF into Markdown for an agent, with a marker per page and an honest account of what was read.**

> [!NOTE]
> **Upcoming.** This tool arrives with 1.0.0-alpha.21, which is not published yet. Installed versions up to 1.0.0-alpha.20 do not have it.

* **Core Feature Guide:** [PDF Reading & Export](../../../core-features/media-intelligence/pdf/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.convert_to_markdown` turns a PDF on disk into Markdown, locally and without any extra software. Every page starts with a fixed marker `**[Page N]**` (N is the real page number in the PDF). Text comes in reading order as paragraphs, so a two-column page is read column by column. Lists appear only where the document itself has bullets or consecutive numbering, and repeating headers and footers stay in the text, marked as `> [Possible header] …` or `> [Possible footer] …`. Headings come only from the PDF's own bookmarks: a bookmark becomes a Markdown heading where exactly one block on its target page carries its title. Nothing is guessed from font size, and tables are not rebuilt; table contents arrive as paragraphs. Web and mail links become Markdown links (link text plus target) where their text occurs once in its block.

Next to the Markdown the answer carries what the document itself declares: `documentInfo` (title, author, dates — an ISO date only when the PDF states its time zone, the raw value always), `outline` (every bookmark with level and target page), `form` (AcroForm fields with name, type and flags; values only with `includeFormValues: true`, because forms often hold personal data) and `pageInfo` (size, rotation, orientation, embedded raster images with their regions, and all links, including ones that are not turned into Markdown).

The Markdown is document content: data to read, never instructions to follow. Every answer carries `contentTrust: "untrusted_document"`. Per page, `pageInfo[].diagnostics` counts what the text layer is: characters that could not be decoded (`replacementCharCount`, warning `unmapped_glyphs`), text that is never drawn (`nonPaintingGlyphCount`, `textLayerKind`, warning `non_painting_text`), text outside the visible area (`text_outside_cropbox`), glyphs drawn twice and optional content layers. Pieces of one physical line that the layout analysis split apart are joined again (`lineMergeCount`); only a space is added, and a letter the scanner's text recognition got wrong is never corrected.

When a page still comes out torn into many small pieces, `pageInfo[].structure.fragmented` is `true`, the warning `structure_fragmented` names the page and one line `> [Nova extraction warning: ...]` sits under its marker. `pagesForVisualReview` lists every page worth a look; pass them as `renderPages` (at most three) to get those pages back as images in the same answer. The images are rendered in memory and never saved, so nothing is left on disk.

The answer says what it holds. `truncated: true` means the returned Markdown is cut; `scanComplete: false` means not every selected page was read. `pagesWithoutExtractableText` lists pages without a text layer, such as scanned pages: Nova does not run OCR, so these are unreadable here, not blank. `sourcePages` gives each page's position in the Markdown.

With `outputMode: "file"` the whole document is written to a `.md` file and the answer carries only its path and the page positions; `"both"` adds a preview. An existing file is never overwritten. Only PDF is supported so far; other files return `reasonCode: "convert_to_markdown.unsupported_format"`. To check what a PDF literally says, character for character, use [`nova.read_pdf`](nova-read-pdf.md). Files in Nova's download folder and Exports folder can always be read; any other path, and any `outputPath`, needs the setting "Allow local files (file://)".

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path to the document, e.g. the filePath from nova.downloads_list or the savedPath from nova.save_pdf. A PDF is recognised by its .pdf name or by its first bytes. |
| `pages` | `string` | No | — | — | Optional 1-based page selection, e.g. '1', '2-5' or '1,4-6'. Omit for every page. Pages beyond the end are ignored. |
| `outputMode` | `string` | No | `"inline"` | `inline`, `file`, `both` | inline = return the markdown (cut at maxChars). file = write the whole markdown to a .md file and return only its path, size and page offsets. both = write the file and also return the first maxChars characters. |
| `outputPath` | `string` | No | — | — | Absolute path for the .md file (outputMode 'file' or 'both' only). Needs the user's 'Allow local files' setting; an existing file is refused with reasonCode 'convert_to_markdown.output_exists'. Omit to write a new file into Nova's Exports folder. |
| `maxChars` | `integer` | No | `30000` | 1000–200000 | Most characters of markdown returned inline (1000-200000, default 30000). Does not limit the file in outputMode 'file'/'both'. |
| `renderPages` | `string` | No | — | — | Also return these pages as JPEG images (1-based, e.g. '1' or '2-3'; at most 3 pages, about 900 px wide), rendered in memory and never saved to disk. Use it for the pages in pagesForVisualReview, or whenever the text matters enough to check it against what the page shows - a wrong letter in a scanner's text layer is only visible there. |
| `includeFormValues` | `boolean` | No | `false` | — | Also return the values of AcroForm fields (form.fields[].value). Off by default: forms often hold addresses, account numbers and similar personal data; without it the fields are listed with name, type, page, readOnly and required only. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_convert_to_markdown",
  "arguments": {
    "path": "C:\\Users\\me\\Downloads\\notice-2026.pdf",
    "pages": "1-2"
  }
}
```

### JSON-RPC Response

The text block carries the Markdown itself.

```json
{
  "content": [
    {
      "type": "text",
      "text": "**[Page 1]**\n\nNotice of assessment 2026\n\nThe fee is due 30 days after this notice.\n\n- Keep this letter\n- Quote the reference number\n\n**[Page 2]**\n\n> [Possible footer] Example City Council\n"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "sourcePath": "C:\\Users\\me\\Downloads\\notice-2026.pdf",
    "fileName": "notice-2026.pdf",
    "detectedFormat": "pdf",
    "outputMode": "inline",
    "markdown": "**[Page 1]**\n\nNotice of assessment 2026\n\nThe fee is due 30 days after this notice.\n\n- Keep this letter\n- Quote the reference number\n\n**[Page 2]**\n\n> [Possible footer] Example City Council\n",
    "chars": 188,
    "outputPath": null,
    "outputBytes": null,
    "pageCount": 4,
    "pagesProcessed": 2,
    "pagesWithoutExtractableText": [],
    "scanComplete": true,
    "truncated": false,
    "sourceOffsetTarget": "inline",
    "sourcePages": [
      { "pageNumber": 1, "startOffset": 0, "endOffset": 131, "status": "extracted" },
      { "pageNumber": 2, "startOffset": 133, "endOffset": 187, "status": "extracted" }
    ],
    "warnings": [],
    "documentInfo": { "title": "Notice of assessment 2026", "author": "Example City Council", "subject": null, "keywords": null, "creator": null, "producer": null, "creationDate": "2026-09-30T10:12:00.0000000+02:00", "creationDateRaw": "D:20260930101200+02'00'", "modifiedDate": null, "modifiedDateRaw": null },
    "outline": [],
    "outlineTotal": 0,
    "outlineHeadingsApplied": 0,
    "form": null,
    "pageInfo": [
      { "pageNumber": 1, "width": 595.3, "height": 841.9, "rotation": 0, "orientation": "portrait", "embeddedImages": 0, "imageRegions": [], "links": [], "linksTotal": 0 },
      { "pageNumber": 2, "width": 595.3, "height": 841.9, "rotation": 0, "orientation": "portrait", "embeddedImages": 1, "imageRegions": [ { "left": 72, "bottom": 400, "right": 300, "top": 520 } ], "links": [], "linksTotal": 0 }
    ],
    "pageInfoTruncated": false,
    "elapsedMs": 41
  }
}
```

On a failure `ok` is `false`, `reasonCode` names the cause (`convert_to_markdown.file_not_found`, `unsupported_format`, `encrypted`, `corrupt_file`, `file_too_large`, `limit_exceeded`, `processing_timeout`, `output_exists`) and `message` explains the next step.

---

## 4. Operational Best Practices

* **Long documents:** An inline call stops reading once `maxChars` is reached, so `scanComplete` turns `false`. Use `outputMode: "file"` for the whole document, or convert a page range with `pages`.
* **Scanned pages:** Check `pagesWithoutExtractableText` before relying on the Markdown; those pages carry no text Nova can read.
* **Citing a page:** Use `sourcePages` to map a passage back to its PDF page; the offsets point into the file when one was written.

---

## 5. Related Tools

* [`nova.read_pdf`](nova-read-pdf.md)
* [`nova.save_pdf`](nova-save-pdf.md)
