# `nova.reference_doc_read`

> **Reads the complete text content of an allowlisted internal Nova reference document.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.reference_doc_read` reads one of Nova's bundled reference documents (see `nova.reference_docs_list` for the available ids) in pages, using `cursor`/`maxChars` to move through longer documents. Nova prefers a matching source checkout on disk and falls back to a copy embedded in the app when no checkout is found, so the call works even without access to Nova's repository.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `docId` | `string` | Yes | — | — | Document id from nova.reference_docs_list, e.g. 'mcp', 'pks', 'plugins', or 'browser_memory'. |
| `cursor` | `integer` | No | `0` | ≥ 0 | Zero-based character offset to start reading from. Use nextCursor from the previous response to continue. |
| `maxChars` | `integer` | No | `60000` | 1–200000 | Maximum characters to return in this page. Values above Nova's maximum are clamped and reported as maxChars in the response. |

Capability bundles: `onboarding`, `system_tools`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_reference_doc_read",
  "arguments": {
    "docId": "etm"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Nova reference doc 'etm' (0-8000/18420)"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "docId": "etm",
    "purpose": "Episodic Task Memory.",
    "sourceKind": "embedded",
    "sourcePath": null,
    "totalChars": 18420,
    "sha256": "9f2c4e7a1b8d3f60c5e2a7b9d4f1c8e3a6b0d5f2c9e7a4b1d8f3c6e0a2b5d7f9",
    "cursor": 0,
    "maxChars": 8000,
    "content": "... (truncated; first 8000 characters of the document) ...",
    "hasMore": true,
    "nextCursor": 8000
  }
}
```

Requesting an unknown `docId` returns `ok: false`, `status: "not_found"`, `reasonCode: "reference_doc_not_found"` instead of throwing a protocol error.

---

## 4. Operational Best Practices

* **Offline Documentation:** Reading works even when Nova cannot find a matching source checkout, because it falls back to the embedded copy.
* **Pagination:** For a doc larger than `maxChars`, keep calling with `cursor` set to the previous response's `nextCursor` until `hasMore` is `false`.

---

## 5. Related Tools

* [`nova.reference_docs_list`](nova-reference-docs-list.md)
* [`nova.get_instructions`](nova-get-instructions.md)
