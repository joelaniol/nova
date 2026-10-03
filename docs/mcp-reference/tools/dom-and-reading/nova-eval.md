# `nova.eval`

> **Evaluates an arbitrary JavaScript expression in the main page world or isolated world.**

* **Capability Bundle:** `page_read_debug`
* **Security Tier:** Tier 2 (JavaScript Execution)
* **Core Feature Guide:** [DOM Perception & Semantic Extraction](../../../core-features/tob.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.eval` executes custom JavaScript inside the target tab context, returning serialized return values. Supports both main world and isolated script execution.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `expression` | `string` | Yes | — | — | JavaScript expression to evaluate. Result is JSON-serialized. Use 'return ...' or 'await ...' for multi-statement async probes (auto-detects function body mode). Has access to page globals (document, window, etc.). |
| `timeoutMs` | `integer` | No | `10000` | 1000–30000 | Maximum time in milliseconds for Runtime.evaluate. Keep a safety margin above any wait performed by the expression. A timeout has an unknown execution outcome and must not be retried blindly. |
| `isolate` | `boolean` | No | `true` | — | Legacy main-world only: if true, wraps eval in a short function scope to avoid variable collisions between calls. Ignored for worldMode='isolated', which is already scope-isolated without eval(). |
| `functionBody` | `boolean` | No | — | — | Controls execution mode. true: treat expression as an async function body (supports top-level 'return' and 'await'); a function body without 'return' yields undefined, so the response carries result=null plus the warning 'result_undefined_missing_return' - end multi-statement scripts with an explicit 'return'. Omit it (the default) for everything else: the isolated world then evaluates your code for its completion value, so several statements are fine and the value of the last expression comes back without a 'return'. |
| `frameScope` | `string` | No | `"top"` | `top`, `active`, `allVisible` | Evaluation scope when frameId is omitted. In worldMode='isolated', top evaluates the top frame and allVisible evaluates top plus capped same-origin child frames; pass frameId for precise iframe targeting. In worldMode='main', this keeps the legacy JS-DOM same-origin traversal. |
| `frameId` | `string` | No | — | — | Optional same-origin frame ID from nova.perceive(deep=true).structuredContent.frames[].frameId. When provided with worldMode='isolated', Nova evaluates directly in that frame's isolated world; this takes precedence over frameScope. |
| `worldMode` | `string` | No | `"isolated"` | `isolated`, `main` | Execution world. 'isolated' (default) uses CDP Page.createIsolatedWorld + Runtime.evaluate(contextId) and is CSP-hardened for DOM automation. 'main' preserves legacy page-global semantics and may be blocked by CSP unsafe-eval when isolate/functionBody wrappers are used. The worlds share the DOM but not JavaScript state, and that includes your own properties on DOM nodes: a document.__myFlag set in 'main' reads back as undefined in 'isolated'. The call still succeeds, so the result looks like your code never ran - keep a set and its read in the same world. |
| `includeShadow` | `boolean` | No | `false` | — | If true, legacy main-world frame traversal evaluates in open shadow roots and exposes the current root as variable `root`. For precise iframe work prefer frameId plus selectors/read tools. |
| `redact` | `array` of `string` | No | — | ≤ 20 items | Property names whose values come back as [redacted], e.g. ['accessHash','token']. Matching is by name (case-insensitive substring), never by value - guessing what a secret looks like would hide things you did not ask to hide. Off unless you pass it: for debugging, the plain value is usually the point. The masking runs in the page before serialization, so a redacted value never reaches the transport or Nova's action log. Needs a wrapped expression: worldMode='isolated' (the default) or isolate=true. |
| `maxChars` | `integer` | No | `50000` | 1000–5000000 | Maximum characters for the serialized result. Defaults shrink automatically under context pressure unless explicitly provided. |
| `outputDetail` | `string` | No | `"full"` | `full`, `compact` | Response verbosity. 'compact' omits the echoes of your own arguments (isolate, frameScope, frameId, worldMode, includeShadow) and 'chars', which outputBudget.returnedChars already reports. result, truncated, outputBudget and every warning field are unaffected - this setting can never hide a warning. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_eval",
  "arguments": {
    "targetId": "tab-1",
    "expression": "document.querySelectorAll(\".card\").length",
    "worldMode": "main"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Evaluated expression: returned 12."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "result": 12
  }
}
```

---

## 4. Operational Best Practices

* **Prefer Native Extractors:** Use `nova.dom_extract` or `nova.read_text_structured` whenever possible for lower token footprint.
* **World Mode:** Use `worldMode: "main"` when interacting with page globals or window objects.

---

## 5. Related Tools

* [`nova.wait_for_eval`](nova-wait-for-eval.md)
* [`nova.dom_extract`](nova-dom-extract.md)
