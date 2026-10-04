# `nova.app_info`

> **Returns runtime environment metadata: app version, WebView2/OS runtime info, MCP endpoint, and storage paths.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.app_info` reports host diagnostics: the Nova version and build metadata, .NET/OS runtime description (including the WebView2 runtime version where available), the MCP endpoint and port, storage paths (settings file, logs, dumps), whether autofill is enabled, and autostart/activation info (whether an agent may relaunch a closed Nova, which sandbox a cold autostart targets, and which sandbox is active right now).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "{ \"appName\": \"Nova\", \"version\": \"1.4.0\", ... }"
    }
  ],
  "structuredContent": {
    "appName": "Nova",
    "version": "1.4.0",
    "build": { "configuration": "Release", "product": "Nova AI Workspace" },
    "runtime": {
      "osDescription": "Microsoft Windows 10.0.26100",
      "osVersion": "Microsoft Windows NT 10.0.26100.0",
      "processArchitecture": "X64",
      "webView2RuntimeVersion": "131.0.2903.86"
    },
    "endpoint": "http://127.0.0.1:27183/mcp",
    "configuredPort": 27183,
    "boundPort": 27183,
    "protocolVersion": "2025-06-18",
    "storageBaseDir": "%LOCALAPPDATA%\\NovaBrowser",
    "autofillEnabled": true,
    "autostartAllowed": true,
    "automationProfileUid": null,
    "activeSandboxUid": "sandbox-a"
  }
}
```
The text block is the same object, pretty-printed as JSON; field names above are as returned by the handler. `automationProfileUid` is the sandbox a cold autostart would target (`null` means last-active); `activeSandboxUid` is the sandbox currently active.

---

## 4. Operational Best Practices

* **Version Verification:** Call on session initialization to confirm runtime feature compatibility.
* **Sandbox/Autostart Checks:** Compare `activeSandboxUid` against the sandbox you expect before relying on autostart behavior.

---

## 5. Related Tools

* [`nova.agent_activity_summary`](nova-agent-activity-summary.md)
* [`nova.setup_status`](nova-setup-status.md)
