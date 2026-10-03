# `nova.reference_doc_read`

> **Reads the complete text content of an allowlisted internal Nova reference document.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Documentation)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.reference_doc_read` retrieves bundled technical documentation, architecture whitepapers, or protocol specifications directly via MCP.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `docId` | `string` | Yes | — | — | Document id from nova.reference_docs_list, e.g. 'mcp', 'pks', 'plugins', or 'browser_memory'. |
| `cursor` | `integer` | No | `0` | ≥ 0 | Zero-based character offset to start reading from. Use nextCursor from the previous response to continue. |
| `maxChars` | `integer` | No | `60000` | 1–200000 | Maximum characters to return in this page. Values above Nova's maximum are clamped and reported as maxChars in the response. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_reference_doc_read",
  "arguments": {
    "docId": "etm-and-task-memory"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded document 'etm-and-task-memory.md' (18,420 bytes)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "docId": "etm-and-task-memory",
    "title": "Episodic Task Memory Architecture"
  }
}
```

---

## 4. Operational Best Practices

* **Offline Documentation:** Fetch reference guides even when local repository sources are inaccessible.

---

## 5. Related Tools

* [`nova.reference_docs_list`](nova-reference-docs-list.md)
* [`nova.get_instructions`](nova-get-instructions.md)
