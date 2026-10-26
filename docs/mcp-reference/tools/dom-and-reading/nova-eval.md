# `nova.eval`

> **Evaluates an arbitrary JavaScript expression in the main page world or isolated world.**

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
| `expression` | `string` | Yes | — | — | JS to run; result is JSON-serialized. Several statements are fine and the last expression's value comes back. Top-level 'return' or 'await' work too: the code then runs as an async function body and must end with 'return <value>' (otherwise null and a missing-return warning). |
| `timeoutMs` | `integer` | No | `10000` | 1000–30000 | Max ms for the evaluation; keep a margin above any wait inside it. After a timeout the outcome is unknown - do not retry blindly. |
| `isolate` | `boolean` | No | `true` | — | Main world only: wrap in a function scope. Ignored in the isolated world. |
| `functionBody` | `boolean` | No | — | — | true: treat expression as an async function body - then you must end with 'return', or the result is null (warning result_undefined_missing_return). Omit otherwise. |
| `frameScope` | `string` | No | `"top"` | `top`, `active`, `allVisible` | Without frameId: 'top' (default), 'allVisible' = top plus same-origin child frames. Prefer frameId for one iframe. |
| `frameId` | `string` | No | — | — | Frame from nova.perceive(deep=true): frames[].frameId (same origin) or opaqueFrames[].frameId (other site, read-only). Same-origin frameId needs worldMode='isolated'. Gone frame: eval.frame_not_found - get fresh ids. |
| `worldMode` | `string` | No | `"isolated"` | `isolated`, `main` | 'isolated' (default): CSP-safe DOM access, no page JS globals. 'main': page globals (window.monaco, app stores), may hit CSP. Worlds share the DOM but not JS state: a property you set in one world reads undefined in the other. If a global read comes back empty, the response says page_global_main_world_only - repeat with 'main'. |
| `includeShadow` | `boolean` | No | `false` | — | Main-world traversal only: also run in open shadow roots (variable `root`). |
| `redact` | `array` of `string` | No | — | ≤ 20 items | Property names whose values return as [redacted] (case-insensitive substring match on names). Masked in the page, never logged. Off unless set. Works only in worldMode='isolated' (default) or with isolate=true. |
| `maxChars` | `integer` | No | `50000` | 1000–5000000 | Max characters of the returned result (default 50000; lower under context pressure). A longer result comes back shortened but still valid JSON (long strings, arrays and objects cut evenly, each cut marked) and flagged truncated; resultTruncation says how. |
| `resultDelivery` | `string` | No | `"inline"` | `inline`, `file` | 'inline' (default): result in the response, shortened to fit maxChars. 'file': whole result to a file; response has only resultFile (path, bytes, sha256, preview), result=null. Use for large data. |
| `outputDetail` | `string` | No | `"compact"` | `full`, `compact` | 'compact' (default) leaves out echoes of your own arguments and 'chars'; result, truncated and all warnings stay. 'full' adds them. A compact answer carries outputDetail='compact': a missing field was not sent, not absent. |

Capability bundles: `browser_automation`, `visual_evidence`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.eval",
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
