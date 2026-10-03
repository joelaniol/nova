# `nova.cdp`

> **Executes a raw Chrome DevTools Protocol (CDP) method directly on the target WebView2 instance.**

* **Security Tier:** Tier 3 (Low-Level Diagnostic & Protocol Passthrough)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.cdp` provides low-level escape-hatch access to the Chromium DevTools Protocol. It bypasses high-level Nova abstractions to invoke raw CDP domains (e.g. Page, Network, Emulation).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `method` | `string` | Yes | — | — | Chrome DevTools Protocol method name, e.g. 'Network.enable', 'Runtime.evaluate', 'DOM.getDocument'. See chromedevtools.github.io/devtools-protocol/. |
| `params` | `object` | No | — | — | CDP method parameters object. Exact allowed keys depend on `method`; discover the precise shape in the CDP spec for that method. The documented common keys here cover the highest-volume Nova workflows such as Runtime.evaluate, DOM/Overlay node targeting, Input.dispatch*, Emulation overrides, Network headers, and Page screenshots. |
| `params.expression` | `string` | No | — | — | Runtime.evaluate expression. |
| `params.awaitPromise` | `boolean` | No | — | — | Runtime.evaluate flag: await returned promises before replying. |
| `params.returnByValue` | `boolean` | No | — | — | Runtime.evaluate flag: JSON-serialize the result instead of returning a remote object handle. |
| `params.userGesture` | `boolean` | No | — | — | Runtime/Input flag: execute as if triggered by a user gesture when the CDP method supports it. |
| `params.contextId` | `integer` | No | — | — | Runtime execution context ID for Runtime.evaluate or related calls. |
| `params.objectId` | `string` | No | — | — | Remote object handle for Runtime.callFunctionOn, DOM.resolveNode, and related methods. |
| `params.nodeId` | `integer` | No | — | — | DOM node ID for DOM/Overlay methods. |
| `params.backendNodeId` | `integer` | No | — | — | Backend DOM node ID for DOM/Overlay methods. |
| `params.frameId` | `string` | No | — | — | Frame identifier for Page/Runtime/DOM methods that scope to a frame. |
| `params.x` | `number` | No | — | — | Input/Page coordinate in CSS pixels. |
| `params.y` | `number` | No | — | — | Input/Page coordinate in CSS pixels. |
| `params.deltaX` | `number` | No | — | — | Wheel delta in CSS pixels. |
| `params.deltaY` | `number` | No | — | — | Wheel delta in CSS pixels. |
| `params.button` | `string` | No | — | — | Pointer button literal such as left, middle, or right for Input.dispatchMouseEvent. |
| `params.buttons` | `integer` | No | — | — | Pressed-button bitmask for Input.dispatchMouseEvent. |
| `params.clickCount` | `integer` | No | — | — | Click count for Input.dispatchMouseEvent. |
| `params.key` | `string` | No | — | — | Keyboard key literal for Input.dispatchKeyEvent. |
| `params.text` | `string` | No | — | — | Typed text payload for Input.insertText or key events. |
| `params.modifiers` | `integer` | No | — | — | Modifier bitmask for Input events. |
| `params.url` | `string` | No | — | — | URL used by Page.navigate or Network methods. |
| `params.headers` | `object` | No | — | — | HTTP header map for Network.setExtraHTTPHeaders or related methods. |
| `params.userAgent` | `string` | No | — | — | User agent override for Emulation.setUserAgentOverride. |
| `params.width` | `integer` | No | — | — | Viewport width for Emulation/Page methods. |
| `params.height` | `integer` | No | — | — | Viewport height for Emulation/Page methods. |
| `params.deviceScaleFactor` | `number` | No | — | — | Device scale factor for emulation methods. |
| `params.mobile` | `boolean` | No | — | — | Mobile emulation flag. |
| `params.maxTouchPoints` | `integer` | No | — | — | Touch-point count for touch emulation methods. |
| `params.format` | `string` | No | — | — | Screenshot/image format such as png or jpeg. |
| `params.quality` | `integer` | No | — | — | Screenshot quality for jpeg captures. |
| `maxChars` | `integer` | No | `800000` | 1000–5000000 | Maximum characters for the CDP response. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

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
