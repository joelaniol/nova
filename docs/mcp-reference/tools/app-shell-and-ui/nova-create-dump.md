# `nova.create_dump`

> **Generates a forensic debug bundle for a browser tab (screenshot, DOM snapshot, console logs, resources).**

* **Security Tier:** Tier 2 (Diagnostic Evidence Bundle)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.create_dump` captures a comprehensive snapshot of a tab's internal state for offline debugging and post-mortem analysis. Outputs are written to the profile diagnostic directory.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `mode` | `string` | No | `"full"` | `full`, `fast` | Dump depth. 'full': screenshot + DOM + MHTML + inline scripts + resources. 'fast': screenshot + DOM only (no network fetches, much faster). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_create_dump",
  "arguments": {
    "targetId": "tab-1",
    "tag": "checkout-failure-repro"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Diagnostic dump created at dumps/tab-1-20261002-checkout.zip."
    }
  ],
  "structuredContent": {
    "ok": true,
    "dumpPath": "dumps/tab-1-20261002-checkout.zip",
    "screenshotIncluded": true,
    "domNodesCount": 1420,
    "consoleErrorsCount": 2
  }
}
```

---

## 4. Operational Best Practices

* **Post-Incident Analysis:** Trigger whenever an agent encounters an unrecoverable navigation or script error.
* **Privacy Check:** Redact authentication headers and tokens if sharing dumps across external systems.

---

## 5. Related Tools

* [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md)
* [`nova.console_read`](../dom-and-reading/nova-console-read.md)
