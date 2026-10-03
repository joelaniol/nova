# `nova.guarded_switch_model`

> **Safely switches the model in an AI web provider interface (ChatGPT, Claude, Gemini) with verification.**

* **Capability Bundle:** `form_submission`
* **Security Tier:** Tier 2 (Provider UI Control)
* **Core Feature Guide:** [Autonomous Agent Guard (AAG)](../../../core-features/aag.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.guarded_switch_model` navigates web provider dropdowns, selects the requested model version, and verifies that the model indicator updated before sending prompts.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `activateIfNeeded` | `boolean` | No | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `autoDismissBlockers` | `boolean` | No | If true, explicitly auto-dismiss overlays/modals blocking the target element. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `button` | `string` | No | Mouse button: 'left' (default), 'middle', 'right'. |
| `clickCount` | `integer` | No | Click count: 1=single, 2=double, 3=triple click. |
| `ctaRef` | `integer` | No | CTA v3 handle reference (from perceive cta_detection_v3). If set, clicks by ref instead of selector. Requires ctaRev. |
| `ctaRev` | `integer` | No | CTA revision from perceive response. Required when ctaRef is used. |
| `frameId` | `string` | No | Optional same-origin frame ID. For selector-based calls, Nova resolves and clicks the selector inside that iframe and also scopes the auto-generated guarded assertions to the same frame. Not supported together with ctaRef. |
| `includeScreenshot` | `boolean` | No | If true and navigation completes, include a screenshot in the response. |
| `navigationStrict` | `boolean` | No | If true (with waitForNavigation), ok is true only when click and navigation both succeed. |
| `outputDetail` | `string` | No | Response verbosity. 'compact': core fields only. 'full': includes diagnostics and telemetry. 'minimal': lean envelope — core contract + actionDispatched/verified + page/target info + never-suppressible safety warnings only; strips guardedCommit, composerResolution, pksAdvice and other inline telemetry. |
| `pksAdviceMode` | `string` | No | Controls verbosity of pksAdvice in the response. |
| `pksMode` | `string` | No | PKS phenomenon matching: 'off' suppresses, 'match' returns compact hints, 'telemetry' returns full PKS payload. |
| `restoreActiveTarget` | `boolean` | No | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `screenshotFormat` | `string` | No | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotMaxHeight` | `integer` | No | Max screenshot height in pixels. |
| `screenshotMaxWidth` | `integer` | No | Max screenshot width in pixels. |
| `screenshotPolicy` | `string` | No | Capture policy. smart=partial/failure always + sampled success. always=every call. |
| `screenshotQuality` | `integer` | No | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `selector` | `string` | No | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `timeoutMs` | `integer` | No | Max ms to wait for element to appear before failing. |
| `transitionContract` | `object` | No | Optional extension for the auto-generated guarded transition contract. Use this only to add or tighten assertions around the built-in guarded macro template. On nova.guarded_send_message, built-in send preconditions, success assertions, and retryPolicy stay pinned while your extra assertions are merged additively. Every assertion bucket has the shape { all?, any?, forbidden? }, each a non-empty array of { factKey: string, operator: eq|not_eq|neq|exists|not_exists|contains|gt|lt|gte|lte, expected?: any, frameId?: string }. Full schema and semantics: nova.reference_doc_read(docId='mcp'). |
| `verify` | `string` | No | Optional post-click JS verification expression. |
| `verifyTimeout` | `integer` | No | Max ms to wait for verify expression to become truthy. Only used when verify is set. |
| `waitForNavigation` | `boolean` | No | If true, wait for URL change + page load after clicking. |
| `waitForNavigationTimeoutMs` | `integer` | No | Max ms to wait for navigation (0-30000). Only used when waitForNavigation=true. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_guarded_switch_model",
  "arguments": {
    "targetId": "tab-1",
    "model": "gpt-4o"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Switched model to gpt-4o."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "activeModel": "gpt-4o",
    "verified": true
  }
}
```

---

## 4. Operational Best Practices

* **Verification Gate:** ASD verifies that the model dropdown closed and the new model pill is active.

---

## 5. Related Tools

* [`nova.guarded_send_message`](nova-guarded-send-message.md)
* [`nova.guarded_switch_sandbox`](nova-guarded-switch-sandbox.md)
