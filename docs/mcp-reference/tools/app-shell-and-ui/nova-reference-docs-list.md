# `nova.reference_docs_list`

> **Lists all internal Nova reference documents available for in-session reading.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.reference_docs_list` lists the small set of bundled reference documents Nova ships (MCP contract, PKS, Operational Knowledge, Episodic Task Memory, Plugins, Crawler, Scheduled Tasks, Browser Memory), each with its content length and a hash, so an agent can decide what to read with `nova.reference_doc_read`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundles: `onboarding`, `system_tools`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_reference_docs_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Nova reference docs available: 8"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "version": "1.4.0",
    "docs": [
      {
        "docId": "etm",
        "name": "ETM",
        "purpose": "Episodic Task Memory.",
        "totalChars": 18420,
        "sha256": "9f2c4e7a1b8d3f60c5e2a7b9d4f1c8e3a6b0d5f2c9e7a4b1d8f3c6e0a2b5d7f9",
        "sourceKind": "embedded",
        "sourcePath": null
      },
      {
        "docId": "mcp",
        "name": "MCP Contract",
        "purpose": "Normative tool contracts and error semantics.",
        "totalChars": 690412,
        "sha256": "4e8a1c6f3b9d2e7a5c0f8b3d6a1e9c4f7b2d5a8e0c3f6b9d1a4e7c2f5b8d0a3e",
        "sourceKind": "embedded",
        "sourcePath": null
      }
    ],
    "readTool": "nova.reference_doc_read"
  }
}
```

The response is truncated above; a real call returns all eight documents.

---

## 4. Operational Best Practices

* **Doc Catalog:** Discover available doc ids before fetching one with `nova.reference_doc_read`.

---

## 5. Related Tools

* [`nova.reference_doc_read`](nova-reference-doc-read.md)
