# `nova.app_info`

> **Returns runtime environment metadata, version numbers, process uptime, and storage paths.**

* **Security Tier:** Tier 1 (Environment Diagnostics)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.app_info` reports complete host diagnostics: Nova executable version, WebView2 runtime version, Windows OS build, uptime, active profile roots, and memory usage.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_app_info",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Nova AI Workspace v1.4.0 (x64), WebView2 131.0.2903.86, Uptime: 04:12:30."
    }
  ],
  "structuredContent": {
    "ok": true,
    "appVersion": "1.4.0",
    "webView2Version": "131.0.2903.86",
    "osVersion": "Windows 11 Build 26100",
    "uptimeSeconds": 15150
  }
}
```

---

## 4. Operational Best Practices

* **Version Verification:** Call on session initialization to confirm runtime feature compatibility.
* **Runtime Diagnostics:** Check memory consumption and WebView2 versions during troubleshooting.

---

## 5. Related Tools

* [`nova.agent_activity_summary`](nova-agent-activity-summary.md)
* [`nova.setup_status`](nova-setup-status.md)
