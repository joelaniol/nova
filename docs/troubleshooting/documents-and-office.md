# Document Conversion, Word & Excel Generation Troubleshooting

This guide resolves document conversion failures (`nova.convert_to_markdown`), Word document synthesis issues (`nova.docx_create`), Excel workbook generation errors (`nova.xlsx_create`), and formula or image embedding issues across Nova AI Workspace and connected AI agents.

---

## Quick Symptom Checker

| Symptom / Error Code | Root Cause | Primary Resolution |
| :--- | :--- | :--- |
| `docx_create.output_exists` / `xlsx_create.output_exists` | The file specified in `outputPath` already exists on disk. | **Expected behavior.** Nova enforces a strict non-overwriting invariant. Choose an unused destination path or omit `outputPath` to let Nova generate a timestamped file in `Exports/Office/`. |
| `docx_create.file_not_found` / `xlsx_create.file_not_found` | The file passed to `sourcePath` does not exist or the agent passed a relative path without a working directory. | Provide an absolute file path (e.g. from `nova.downloads_list`). If a download is still running, call `nova.downloads_wait` before accessing the file. |
| Formula appears as literal text (e.g. `"=SUM(A1:A5)"`) | The formula was passed as a plain string inside row data instead of a formula object descriptor. | **Formula Safety Invariant.** To prevent spreadsheet formula injection attacks, raw text starting with `=` is always written as a literal string. Use `{ "formula": "SUM(A1:A5)" }` instead. |
| `images_not_embedded` warning | Image paths point to web URLs (`http://`, `https://`), data URIs, or files $> 20\text{ MB}$. | Save remote images locally first (e.g. via `nova.downloads_list` or `nova.chart_create`). Use local absolute paths. Compress oversized images with `nova.image_transform`. |
| `values_kept_as_text` warning | Non-numeric or non-date strings were passed into a column typed as `number`, `currency`, `date`, or `percent`. | Provide clean numeric strings (e.g. `"1200.50"` instead of `"1,200.50 USD"` for currency columns) or ISO dates (`"2026-09-30"`). |
| `text_truncated` warning | A cell string exceeded Excel's structural limit of 32,767 characters. | Split excessive text across multiple rows or store lengthy descriptions in a linked Word document (`nova.docx_create`). |
| Sheet name rejected | Sheet name exceeds 31 characters, contains `[]:*?/\\`, or starts/ends with an apostrophe `'`. | Provide a compliant sheet name (1–31 characters, alphanumeric with spaces or hyphens, no forbidden characters). |
| `xlsx_create.too_many_rows` | A worksheet exceeded Excel's limit of 1,048,576 rows. | Partition large datasets across multiple sheets in `sheets` or filter the dataset before export using `nova.data_query`. |
| `xlsx_create.too_many_columns` | A worksheet exceeded Excel's limit of 16,384 columns. | Transpose your matrix or split wide datasets across multiple sheets. |
| `convert_to_markdown.file_locked` | Word, Excel, or another Windows process holds an exclusive lock on the source document. | Close the file in external desktop applications (Word, Excel) before converting it in Nova. |
| `convert_to_markdown.encrypted` | The Office document or PDF is password-protected or encrypted. | Decrypt or re-export the document without password protection. Nova does not store or prompt for document passwords. |
| `convert_to_markdown.unsupported_format` | Legacy binary Office 97–2003 format (`.doc`, `.xls`, `.ppt`) was passed. | Open the document in modern Office or LibreOffice and save it in modern OpenXML format (`.docx`, `.xlsx`, `.pptx`). |
| `convert_to_markdown.limit_exceeded` | Markdown output exceeds the 2,000,000 character disk write ceiling. | Convert specific page ranges using `pages` (e.g. `pages="1-50"`). |
| PDF-only parameter error (`pages`, `renderPages`, `includeFormValues`) | PDF-specific options were passed while converting a Word, Excel, PowerPoint, or text file. | Remove PDF parameters when converting flow documents (Word, Excel, PPTX, HTML, EPUB, CSV, JSON). |
| `xlsx_create.open_in_tab_unavailable` | `openInTab: true` was requested, but local file preview is unavailable. | Ensure Nova's internal file preview handler is active, or inspect the generated spreadsheet using `nova.data_inspect`. |

---

## 1. Word Document Generation Issues (`nova.docx_create`)

Nova's Word generation engine compiles Markdown AST directly into standard OpenXML WordprocessingML packages (`.docx`) without requiring Microsoft Word or third-party runtimes.

### Error: `output_exists`

#### Symptom
```json
{
  "structuredContent": {
    "ok": false,
    "status": "error",
    "reasonCode": "docx_create.output_exists",
    "errorCode": "output_exists",
    "message": "C:\\Reports\\Summary.docx already exists; Nova never overwrites a file."
  }
}
```

#### Root Cause
Nova enforces an immutable file safety invariant: file generation tools never overwrite existing files to prevent accidental loss of user data.

#### Resolution
1. Specify an unused file path in `outputPath`.
2. Omit `outputPath` completely: Nova will automatically assign a sanitized, timestamped path inside `Exports/Office/` (e.g. `Exports/Office/Summary-20261107-101500.docx`).

---

### Warning: `images_not_embedded`

#### Symptom
The response succeeds with warning `images_not_embedded`, and the Word document contains italic alt text `[Chart]` instead of the image graphic:
```json
{
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "details": {
      "headings": 2,
      "paragraphs": 4,
      "images": 0,
      "imagesNotEmbedded": [
        {
          "url": "https://example.com/assets/chart.png",
          "reason": "web and data addresses are not downloaded; save the image locally and use its path"
        }
      ]
    },
    "warnings": [
      {
        "code": "images_not_embedded",
        "detail": "Some images were not embedded; their alt text stands in their place. details.imagesNotEmbedded names each one and why."
      }
    ]
  }
}
```

#### Root Causes and Rules
Nova inspects image paths using strict offline security rules:
1. **Remote Web URLs & Data URIs:** Nova refuses to download remote web images (`http://`, `https://`, `data:`) during document compilation. Remote web fetching during file authoring could leak operator IP addresses or trigger unintended network requests.
2. **Relative Paths without `sourcePath`:** If `markdown` is provided as inline text, relative paths cannot be resolved because there is no base directory.
3. **File Size Limits:** Individual images cannot exceed $20\text{ MB}$ (`MaxDocxImageBytes`), and the total image payload in a single document cannot exceed $100\text{ MB}$ (`MaxDocxImagesTotalBytes`).
4. **Unsupported Formats:** Only PNG, JPEG, GIF, and BMP are supported. SVG or WebP images must be converted first.

#### Resolution
* Save charts and remote images to a local directory before invoking `nova.docx_create`.
* Use fully qualified local file paths in Markdown: `![Sales Chart](C:/Reports/chart.png)`.
* If using relative image paths, pass the Markdown via `sourcePath` rather than inline `markdown`.
* Use `nova.image_transform` to convert WebP or SVG assets into PNG or JPEG before embedding.

---

### Error: `write_failed` / Read-Back Assertion Failure

#### Symptom
```json
{
  "structuredContent": {
    "ok": false,
    "status": "error",
    "reasonCode": "docx_create.write_failed",
    "errorCode": "write_failed",
    "message": "Nova could not read back the Word file it wrote: ... Nothing was kept."
  }
}
```

#### Root Cause (Two-Phase Commit Invariant)
Nova writes documents to a temporary `.nova-part` file and executes an immediate in-memory read-back verification using its internal document converter before finalizing the file. If XML serialization or OpenXML relationship validation fails, the `.nova-part` file is deleted immediately, ensuring that corrupt files never touch the operator's disk.

#### Resolution
* Check for illegal non-printable control characters in your Markdown source. Nova strips control characters below `0x20` (except tabs and line breaks), but malformed Unicode surrogate pairs can trigger XML parser faults.
* Ensure nested tables or malformed pipe tables contain balanced row boundaries.

---

## 2. Excel Workbook Generation Issues (`nova.xlsx_create`)

Nova streams tabular data directly into native OpenXML SpreadsheetML packages (`.xlsx`) with automated header formatting, freeze panes, and custom column widths.

### The Formula Injection Trap (Formula Appears as Literal Text)

#### Symptom
An agent generates a spreadsheet with calculation formulas:
```json
{
  "name": "nova.xlsx_create",
  "arguments": {
    "sheets": [
      {
        "name": "Q3",
        "columns": ["Item", "Cost"],
        "rows": [
          ["Widget", 45.00],
          ["Gadget", 55.00],
          ["Total", "=SUM(B2:B3)"]
        ]
      }
    ]
  }
}
```
When opened in Microsoft Excel, cell `B4` displays the literal text `"=SUM(B2:B3)"` without calculating the sum.

#### Why This Happens (Formula Safety Invariant)
Raw CSV and web data frequently contain untrusted user inputs. If an attacker injects strings like `=cmd|' /C calc'!A0` or `=HYPERLINK(...)`, executing them as formulas poses an immediate security risk.

To prevent spreadsheet formula injection attacks, Nova enforces an invariant: **Raw string values beginning with `=` are always stored as inline text strings (`<c t="inlineStr">`). Excel displays them verbatim and never evaluates them.**

#### Resolution
Formulas must be explicitly declared using a formula object descriptor `{ "formula": "..." }`:
```json
{
  "name": "nova.xlsx_create",
  "arguments": {
    "sheets": [
      {
        "name": "Q3",
        "columns": ["Item", { "name": "Cost", "format": "currency" }],
        "rows": [
          ["Widget", 45.00],
          ["Gadget", 55.00],
          ["Total", { "formula": "SUM(B2:B3)" }]
        ]
      }
    ]
  }
}
```
When written with `{ "formula": "..." }`, Nova stores the expression inside `<f>SUM(B2:B3)</f>` and instructs Excel to recalculate values on load via `<calcPr fullCalcOnLoad="1"/>`.

---

### Sheet Name Validation Errors

#### Symptom
```json
{
  "message": "Invalid params: sheet name 'Report: Q3/2026 [Final]' must not contain [ ] : * ? / \\."
}
```

#### Rules for Excel Sheet Names
Microsoft Excel enforces rigid sheet naming constraints:
1. **Length:** Must be between 1 and 31 characters.
2. **Forbidden Characters:** Must not contain `[`, `]`, `:`, `*`, `?`, `/`, or `\`.
3. **Apostrophes:** Must not begin or end with an apostrophe `'`.
4. **Uniqueness:** All sheet names within the workbook must be unique (case-insensitive).

#### Resolution
Sanitize sheet names before creating workbooks:
```json
{
  "name": "nova.xlsx_create",
  "arguments": {
    "sheets": [
      {
        "name": "Report Q3-2026 Final",
        "columns": ["Metric", "Value"],
        "rows": [["Uptime", "99.98%"]]
      }
    ]
  }
}
```

---

### Warning: `values_kept_as_text`

#### Symptom
The response contains warning `values_kept_as_text`:
```json
{
  "code": "values_kept_as_text",
  "sheet": "Revenue",
  "detail": "2 values in date or number columns were not dates or numbers and were written as text."
}
```

#### Root Cause
Columns defined with typed formatting (`integer`, `decimal`, `currency`, `percent`, `date`, `datetime`) encounter cell values that cannot be parsed as valid numbers or dates. Instead of failing the entire write, Nova falls back to storing the cell as plain text.

#### Resolution
* **Numbers & Currency:** Pass raw numeric values or clean number strings without currency symbols or thousand separators:
  * Incorrect: `"$1,500.00"` or `"1.500,00 €"`
  * Correct: `1500.00` or `"1500.00"` (use parameter `currencySymbol: "€"` to apply symbols via cell formatting).
* **Dates:** Pass standard ISO-8601 strings (`"2026-09-30"`, `"2026-09-30T14:30:00"`) or date objects `{ "date": "2026-09-30" }`.

---

## 3. Document Conversion Issues (`nova.convert_to_markdown`)

`nova.convert_to_markdown` transforms local PDF, Word, Excel, PowerPoint, HTML, EPUB, CSV, and plain text files into clean Markdown for AI reasoning.

### Error: `file_locked`

#### Symptom
```json
{
  "structuredContent": {
    "ok": false,
    "status": "error",
    "reasonCode": "convert_to_markdown.file_locked",
    "errorCode": "file_locked",
    "message": "The file could not be opened, usually because another program (Word, Excel) has it open: The process cannot access the file because it is being used by another process."
  }
}
```

#### Root Cause
Desktop Office applications on Windows (such as Microsoft Word or Excel) lock opened files with exclusive file sharing flags (`FileShare.None`), preventing other processes from reading them.

#### Resolution
1. Close the document in Word, Excel, or PowerPoint before calling `nova.convert_to_markdown`.
2. Alternatively, make a local copy of the file and convert the duplicate.

---

### Error: `encrypted` (Password Protection)

#### Symptom
```json
{
  "structuredContent": {
    "ok": false,
    "status": "blocked",
    "reasonCode": "convert_to_markdown.encrypted",
    "errorCode": "encrypted",
    "message": "This Office file is password-protected and cannot be opened. Nova does not prompt for or store document passwords."
  }
}
```

#### Root Cause
The file is an encrypted OLE package or password-protected PDF. Nova does not crack passwords or store encryption keys.

#### Resolution
Open the file in its native application, remove the password or encryption setting, and re-export the file before converting it with Nova.

---

### Error: `unsupported_format` (Legacy Office 97–2003 Documents)

#### Symptom
```json
{
  "structuredContent": {
    "ok": false,
    "status": "unsupported",
    "reasonCode": "convert_to_markdown.unsupported_format",
    "errorCode": "unsupported_format",
    "message": "This is a legacy Office file (.doc/.xls/.ppt, Office 97-2003). Only the current formats .docx, .xlsx and .pptx are converted; save it in one of them first."
  }
}
```

#### Root Cause
Nova's native parsing engines target modern ISO OpenXML standards (`.docx`, `.xlsx`, `.pptx`). Proprietary binary OLE formats from Office 97–2003 are intentionally unsupported.

#### Resolution
Open the document in Word, Excel, or LibreOffice and choose **Save As → Modern Word Document (.docx)** or **Excel Workbook (.xlsx)**.

---

### Error: `limit_exceeded`

#### Symptom
```json
{
  "structuredContent": {
    "ok": false,
    "status": "error",
    "reasonCode": "convert_to_markdown.limit_exceeded",
    "errorCode": "limit_exceeded",
    "message": "The Markdown would be 2450120 characters; the file limit is 2000000. Convert a page range with 'pages' instead."
  }
}
```

#### Root Cause
When writing Markdown output to disk (`outputMode: "file"` or `"both"`), Nova enforces a safety ceiling of 2,000,000 characters (`MaxMarkdownOutputChars`) to guard against disk exhaustion or denial-of-service from massive documents.

#### Resolution
* For PDFs, convert document slices using page ranges: `nova.convert_to_markdown(path="contract.pdf", pages="1-50")`.
* For tabular data, use `nova.data_inspect` and `nova.data_query` to query the data with SQL rather than dumping the entire file to Markdown.

---

### PDF-Specific Parameters Passed to Flow Documents

#### Symptom
```json
{
  "message": "Invalid params: 'renderPages' applies to PDF only; this file is a Word document."
}
```

#### Root Cause
Parameters such as `pages`, `renderPages`, and `includeFormValues` exist exclusively for fixed-layout PDF documents. Flow documents (Word, Excel, PowerPoint, HTML, EPUB, CSV, JSON) have dynamic layouts and do not have native fixed page boundaries.

#### Resolution
Omit `pages`, `renderPages`, and `includeFormValues` when converting non-PDF files:
```json
{
  "name": "nova.convert_to_markdown",
  "arguments": {
    "path": "C:\\Reports\\QuarterlyReview.docx",
    "outputMode": "inline",
    "maxChars": 50000
  }
}
```

---

## 4. Technical Reference: Parameter & Limits Matrix

| Parameter / Limit | Word (`nova.docx_create`) | Excel (`nova.xlsx_create`) | Markdown (`nova.convert_to_markdown`) |
| :--- | :--- | :--- | :--- |
| **Max Input Size** | 20 MB / 5,000,000 chars | 50 sheets / 100,000 inline rows | 50 MB / 2,000 pages (PDF) |
| **Max Output Size** | Unlimited (disk-bound) | 1,048,576 rows / 16,384 columns | 2,000,000 chars (file output) |
| **Max Image Size** | 20 MB per image / 100 MB total | N/A | 3 rendered pages (`renderPages`) |
| **Atomic Part Commit** | Yes (`.nova-part`) | Yes (`.nova-part`) | Yes (atomic rename) |
| **Read-Back Validation** | Yes (`DocxMarkdownConverter`) | Yes (`XlsxWorkbook.Open`) | Yes (format verification) |
| **Formula Injection Guard** | Plain text only | Inline text string (`<c t="inlineStr">`) | Untrusted document invariant |
