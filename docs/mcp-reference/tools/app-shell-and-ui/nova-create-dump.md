# `nova.create_dump`

> **Generates a forensic debug bundle for a browser tab (screenshot, DOM snapshot, console logs, resources).**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Diagnostic Evidence Bundle)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.create_dump` captures a comprehensive snapshot of a tab's internal state for offline debugging and post-mortem analysis. Outputs are written to the profile diagnostic directory.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `mode` | `string` | No | Dump depth. 'full': screenshot + DOM + MHTML + inline scripts + resources. 'fast': screenshot + DOM only (no network fetches, much faster). |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

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
