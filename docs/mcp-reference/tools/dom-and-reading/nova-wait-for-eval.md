# `nova.wait_for_eval`

> **Polls the target tab until a JavaScript expression evaluates to a truthy value or times out.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 1 (Synchronization)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.wait_for_eval` evaluates a JavaScript predicate periodically until it returns true, enabling synchronization on custom SPA state.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `expression` | `string` | **Yes** | JavaScript expression to evaluate. Polling continues until it returns a truthy value. |
| `includeScreenshot` | `boolean` | No | If true and condition is met, include a screenshot in the response. |
| `pollMs` | `integer` | No | Polling interval in ms. Alias: pollIntervalMs (accepted, normalized to pollMs; pollMs wins when both are sent). |
| `screenshotFormat` | `string` | No | Screenshot format. |
| `screenshotMaxHeight` | `integer` | No | Max screenshot height in pixels. |
| `screenshotMaxWidth` | `integer` | No | Max screenshot width in pixels. |
| `screenshotQuality` | `integer` | No | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `screenshotResponseMode` | `string` | No | Screenshot delivery mode when includeScreenshot=true. inline returns the image directly; reference stores a nova://screenshot resource; thumbnail+reference returns a small preview plus resource; auto lets Nova choose based on budget. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `timeoutMs` | `integer` | No | Max ms to wait before returning timeout. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_wait_for_eval",
  "arguments": {
    "targetId": "tab-1",
    "expression": "window.__dataLoaded === true",
    "timeoutMs": 10000
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Predicate evaluated to true after 1,200ms."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "resolved": true,
    "elapsedMs": 1200
  }
}
```

---

## 4. Operational Best Practices

* **SPA Settlement:** Wait for framework-specific hydration flags before initiating automation.

---

## 5. Related Tools

* [`nova.eval`](nova-eval.md)
* [`nova.wait_for_selector`](../browser-automation/nova-wait-for-selector.md)
