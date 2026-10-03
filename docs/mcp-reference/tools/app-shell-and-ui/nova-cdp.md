# `nova.cdp`

> **Executes a raw Chrome DevTools Protocol (CDP) method directly on the target WebView2 instance.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 3 (Low-Level Diagnostic & Protocol Passthrough)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.cdp` provides low-level escape-hatch access to the Chromium DevTools Protocol. It bypasses high-level Nova abstractions to invoke raw CDP domains (e.g. Page, Network, Emulation).

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional metadata. Provide _meta.intent (a short reason) for high-impact tools. A tool's annotations.intentRequired in tools/list tells you up front: 'always' means intent is mandatory, 'conditional' means it becomes mandatory for certain arguments (e.g. includeValues=true), absent means never. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `maxChars` | `integer` | No | Maximum characters for the CDP response. |
| `method` | `string` | **Yes** | Chrome DevTools Protocol method name, e.g. 'Network.enable', 'Runtime.evaluate', 'DOM.getDocument'. See chromedevtools.github.io/devtools-protocol/. |
| `params` | `object` | No | CDP method parameters object. Exact allowed keys depend on `method`; discover the precise shape in the CDP spec for that method. The documented common keys here cover the highest-volume Nova workflows such as Runtime.evaluate, DOM/Overlay node targeting, Input.dispatch*, Emulation overrides, Network headers, and Page screenshots. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_cdp",
  "arguments": {
    "targetId": "tab-1",
    "method": "DOM.getDocument",
    "params": {
      "depth": 1
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "CDP command executed successfully."
    }
  ],
  "structuredContent": {
    "ok": true,
    "result": {
      "root": {
        "nodeId": 1,
        "nodeType": 9,
        "nodeName": "#document"
      }
    }
  }
}
```

---

## 4. Operational Best Practices

* **Prefer Native Nova Tools:** Use `nova.navigate`, `nova.dom_extract`, and `nova.eval` when possible; reserve `nova.cdp` for protocol features without high-level wrappers.
* **Session Lifecycle:** Raw CDP subscriptions must be handled carefully to avoid unhandled async event flooding.

---

## 5. Related Tools

* [`nova.devtools_open`](nova-devtools-open.md)
* [`nova.eval`](../dom-and-reading/nova-eval.md)
