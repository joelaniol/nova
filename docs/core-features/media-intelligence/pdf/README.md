# PDF Reading & Export

Nova provides two separate PDF operations: reading text from a local PDF and exporting the current webpage as a PDF. Ask your agent to read a downloaded document, or to save a webpage and report the resulting file path.

## Read text from a PDF

[`nova.read_pdf`](../../../mcp-reference/tools/visual-evidence/nova-read-pdf.md) extracts existing text from a local PDF. It returns the page count and pages read, with optional per-page text. A page selection such as `2-5` or `1,4-6` narrows the extraction; page numbers are one-based.

| Result or constraint | What it means |
| :--- | :--- |
| `truncated=true` | The response's text budget was reached; some extracted text is omitted. |
| `read_pdf.no_extractable_text` | No extractable text was found. Scanned or image-only pages require a separate OCR workflow. |
| `read_pdf.encrypted` | The file is password-protected and cannot be read by this tool. |
| `read_pdf.not_found` | The requested file does not exist at that path. |

The tool does not perform OCR, return page images, or extract document metadata such as title and author. Files in Nova's Downloads and Exports folders are readable through this tool; other locations require **Allow local files (file://)**. Wait for a download to finish before requesting its final path.

Extracted text can support document research, but it does not preserve every visual relationship or prove that a quotation was interpreted correctly. Review the relevant page when layout matters.

## Export a webpage as PDF

[`nova.save_pdf`](../../../mcp-reference/tools/visual-evidence/nova-save-pdf.md) prints the active webpage to a PDF on disk. Options include orientation, backgrounds, page ranges, paper size, margins and print styling. It returns a file path rather than embedding the PDF as a large response.

This operation renders the webpage; it does not extract an existing PDF's text or turn scanned pages into searchable text. The webpage's print styles can differ from its screen layout, so inspect the exported document when presentation matters.

## Related topics

* [Evidence Verification Mode (EVM) & Visual Evidence](../../../research/evidence-verification-mode-evm/README.md) — Evidence for factual claims and visible results.
* [Image Viewer](../image-viewer/README.md) — Viewing website images, distinct from PDF extraction.
* [Downloads user guide](../../../user-guide/browser/downloads.md) — Finding downloaded files.

[Media Intelligence overview](../README.md) · [All core features](../../README.md)
