# `nova.wait_for_eval`

> **Polls the target tab until a JavaScript expression evaluates to a truthy value or times out.**

* **Security Tier:** Tier 1 (Synchronization)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.wait_for_eval` evaluates a JavaScript predicate periodically until it returns true, enabling synchronization on custom SPA state.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `expression` | `string` | Yes | — | — | JavaScript expression to evaluate. Polling continues until it returns a truthy value. |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait before returning timeout. |
| `pollMs` | `integer` | No | `250` | 50–2000 | Polling interval in ms. Alias: pollIntervalMs (accepted, normalized to pollMs; pollMs wins when both are sent). |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and condition is met, include a screenshot in the response. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format; 'auto' picks PNG or JPEG per region. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `screenshotResponseMode` | `string` | No | `"inline"` | `inline`, `reference`, `thumbnail+reference`, `auto` | Screenshot delivery mode when includeScreenshot=true. inline returns the image directly; reference stores a nova://screenshot resource; thumbnail+reference returns a small preview plus resource; auto lets Nova choose based on budget. |

Capability bundles: `browser_automation`, `form_submission`, `page_read_debug`.
<!-- /generated:parameters -->

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
