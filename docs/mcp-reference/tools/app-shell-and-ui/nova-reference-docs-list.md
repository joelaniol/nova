# `nova.reference_docs_list`

> **Lists all internal Nova reference documents available for in-session reading.**

* **Security Tier:** Tier 1 (Read-Only Documentation Catalog)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.reference_docs_list` enumerates bundled markdown guides, architectural blueprints, and protocol reference IDs.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundles: `onboarding`, `system_tools`.
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
      "text": "Available reference documents: 14 docs found."
    }
  ],
  "structuredContent": {
    "ok": true,
    "docs": [
      {
        "docId": "etm-and-task-memory",
        "title": "Episodic Task Memory"
      },
      {
        "docId": "native-dialogs-and-prompts",
        "title": "Native Dialogs & UI Prompts"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Doc Catalog:** Discover available guide topics before fetching specific doc IDs.

---

## 5. Related Tools

* [`nova.reference_doc_read`](nova-reference-doc-read.md)
