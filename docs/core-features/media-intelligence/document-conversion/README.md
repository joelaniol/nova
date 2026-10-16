# Document Conversion (Markdown)

> [!NOTE]
> **Upcoming.** Document conversion arrives with 1.0.0-alpha.21, which is not published yet. Installed versions up to 1.0.0-alpha.20 do not have it.

Nova turns documents on your computer into Markdown that your AI agent can read: PDFs, Word documents, Excel workbooks, PowerPoint presentations, HTML pages, EPUB e-books, CSV tables, JSON and plain text files. The conversion runs inside Nova. Nothing is uploaded, and you do not need Office, Python or any other program besides Nova.

You do not operate this yourself. You ask your agent, and the agent uses the tool [`nova.convert_to_markdown`](../../../mcp-reference/tools/visual-evidence/nova-convert-to-markdown.md).

---

## What you can ask your agent

- "Read the invoice I just downloaded and list every amount with its date."
- "Convert the Excel file in my Downloads folder and tell me which sheet holds the yearly totals."
- "Summarise this presentation slide by slide, including the speaker notes."
- "Turn this Word document into Markdown and save it next to it as a `.md` file."
- "Check whether the contract PDF mentions a cancellation period. If the text looks garbled, look at the page image."
- "Save the article that is open in my current tab as Markdown, with its headings and links."

---

## Supported formats

| Format | Files | What your agent gets | Format name in results |
| --- | --- | --- | --- |
| PDF | `.pdf` | The text page by page in reading order, the document's own bookmarks as headings, links, form fields, tables as Markdown tables where they can be read whole, other text in columns as rows and cells, and on request an image of a page to compare against | `pdf` |
| Word | `.docx`, `.docm`, `.dotx` | Headings, lists and tables as the document defines them | `docx` |
| Excel | `.xlsx`, `.xlsm`, `.xltx` | One table per sheet with the stored values; dates as dates | `xlsx` |
| PowerPoint | `.pptx`, `.pptm`, `.ppsx`, `.potx` | One section per slide with its title, text, tables and speaker notes | `pptx` |
| HTML | `.html`, `.htm`, `.xhtml` | Headings, lists, tables, links and images of the page | `html` |
| E-book | `.epub` | The chapters in reading order with their headings, lists and tables, and the book's title and authors | `epub` |
| CSV / TSV | `.csv`, `.tsv` | One table, including semicolon files from a German Excel | `csv` |
| JSON | `.json` | The data, checked and neatly indented | `json` |
| Plain text | `.txt`, `.text`, `.log` | The text unchanged | `text` |

PDF, Word, Excel, PowerPoint, HTML and EPUB files are recognised by their content, so a downloaded file with a wrong or missing extension is still read correctly.

**Not supported:** old Office files (`.doc`, `.xls`, `.ppt`), password-protected Office files, copy-protected (DRM) e-books, other ZIP archives and images. Scanned PDFs without a text layer cannot be read either, because Nova does not run text recognition (OCR); the agent is told which pages are affected.

### Analysing tables

For larger CSV exports and Excel sheets your agent does not need to read every row. [`nova.data_inspect`](../../../mcp-reference/tools/visual-evidence/nova-data-inspect.md) shows the columns, their types and value ranges; [`nova.data_query`](../../../mcp-reference/tools/visual-evidence/nova-data-query.md) filters, groups and totals the data and returns only the answer - for example the ten best-selling products of a month. The arithmetic runs on your computer and is exact; German and English number formats are both understood, and the answer says when values could not be read.

### Merging and splitting PDFs

Your agent can also rearrange PDF pages without any other program. [`nova.pdf_compose`](../../../mcp-reference/tools/visual-evidence/nova-pdf-compose.md) builds a new PDF from pages of one or more files in the order you want - to merge invoices, drop a page or move one to the front. [`nova.pdf_split`](../../../mcp-reference/tools/visual-evidence/nova-pdf-split.md) cuts a PDF into several files by page range. Your original files stay as they are, and nothing is overwritten. Bookmarks, fillable form fields and digital signatures are not carried into the new files; the agent is told when a source had any.

### Archives and backups

A downloaded ZIP file or a server backup as TAR or `.tar.gz` can be looked into and unpacked first. [`nova.archive_inspect`](../../../mcp-reference/tools/visual-evidence/nova-archive-inspect.md) lists what the archive holds without unpacking it. [`nova.archive_extract`](../../../mcp-reference/tools/visual-evidence/nova-archive-extract.md) unpacks it into a new folder in Nova's Exports folder, in the background and without a fixed size limit: it stops only before the drive runs out of space. It never overwrites a file and never writes entries that would land outside that folder. Your agent can then convert the unpacked documents.

### Pages open in a tab

A web page does not have to be saved first. Your agent can convert the page that is open in a tab, or just one part of it, with [`nova.read_text`](../../../mcp-reference/tools/dom-and-reading/nova-read-text.md) and `format: "markdown"`. This works like the HTML format above, with two differences: links point to the page's real address, and Nova sees which parts of the page the browser hides, even when a style sheet hides them.

---

## Good to know

- **Nothing is invented.** Headings, lists and tables appear only where the document itself defines them. Bold text does not become a heading, and Nova never corrects a wrong letter in a scanned PDF's text; it marks pages that are worth checking against the page image instead.
- **Formulas and macros are never run.** For Excel, the agent sees the results that were saved with the file.
- **Hidden content is included and named.** Hidden text in Word and HTML, text a PDF never draws on the page, hidden sheets, rows and columns in Excel and hidden slides and shapes in PowerPoint are part of the result. The agent is told that they are hidden and also gets that text on its own, so it can see at a glance what the file contains but does not show.
- **Document content is data, not instructions.** Every result is marked as untrusted document content, so your agent treats text in a file as something to read, not as a command.
- **Large documents** can be written to a `.md` file instead of being returned in one answer. Files up to 50 MB are accepted; very large Excel sheets are shortened and the agent is told so.
- **Which folders Nova may read:** files in Nova's download folder and its Exports folder are always readable. For files anywhere else, and for saving the result to a folder of your choice, enable "Allow local files (file://)" in Nova's settings.

---

## For agents and developers

Parameters, the full result structure, warnings and error codes are in the tool reference: [`nova.convert_to_markdown`](../../../mcp-reference/tools/visual-evidence/nova-convert-to-markdown.md). Related: [PDF Reading & Export](../pdf/README.md) for `nova.read_pdf` (exact PDF text) and `nova.save_pdf` (saving a web page as PDF).
