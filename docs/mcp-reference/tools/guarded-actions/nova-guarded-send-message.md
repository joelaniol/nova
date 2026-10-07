# `nova.guarded_send_message`

High-level guarded macro for chat interfaces (ChatGPT, Claude.ai, Gemini, Slack, Teams): auto-discovers the composer, types text with read-back verification, resolves the send button, clicks it, and verifies delivery in a single atomic operation.

---

## 1. Overview

Sending a prompt or chat message in modern AI interfaces involves complex interactions: locating the contenteditable or textarea container, waiting for disabled send buttons to become active, handling focus state transitions, and verifying that the message was actually dispatched.

`nova.guarded_send_message` unifies this entire workflow into a **single guarded atomic action**:
1. **Composer Auto-Discovery:** Locates the chat input field (handling Shadow DOM and embedded iframes).
2. **Typing & Read-Back Verification:** Types the message text and reads it back from the DOM to assert complete transmission before clicking.
3. **Send-Button Resolution:** Automatically pairs the composer with its nearby send button, tolerating `disabled` buttons that activate only after typing.
4. **Closed-Loop Postcondition Verification:** Asserts that the composer cleared, the send button transitioned to a stop/streaming state, or the user's message bubble appeared in the transcript feed.

* **Zero Selector Guessing:** When `selector` is omitted, Nova automatically locates both the composer input and the send button.
* **Closed-Loop Safety:** Injects an automated `transitionContract` ensuring messages are never submitted blindly or duplicated.
* **Blocker Clearance:** Can automatically clear cookie banners or dialogs obscuring the composer (`autoDismissBlockers: true`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `selector` | `string` | No | — | — | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). Optional for nova.guarded_send_message when auto-discovery should locate the send button. Omit together with ctaRef only on nova.guarded_send_message to trigger send-button auto-discovery. |
| `frameId` | `string` | No | — | — | Optional same-origin frame ID. For selector-based calls, Nova resolves and clicks the selector inside that iframe and also scopes the auto-generated guarded assertions to the same frame. On nova.guarded_send_message without selector/ctaRef, the same frame scope is used for send-button auto-discovery. Not supported together with ctaRef. |
| `ctaRef` | `integer` | No | — | — | CTA v3 handle reference (from perceive cta_detection_v3). If set, clicks by ref instead of selector. Requires ctaRev. |
| `ctaRev` | `integer` | No | — | — | CTA revision from perceive response. Required when ctaRef is used. |
| `button` | `string` | No | `"left"` | `left` | Mouse button. nova.guarded_send_message only supports 'left' because send actions are modeled as a single semantic commit. |
| `clickCount` | `integer` | No | `1` | 1–1 | Click count. nova.guarded_send_message only allows 1 because repeated dispatch would risk duplicate sends. |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait for element to appear before failing. |
| `autoDismissBlockers` | `boolean` | No | `false` | — | If true, explicitly auto-dismiss overlays/modals blocking the target element. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `pksMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | PKS phenomenon matching: 'off' suppresses, 'match' returns compact hints, 'telemetry' returns full PKS payload. |
| `pksAdviceMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | Controls verbosity of pksAdvice in the response. |
| `verify` | `string` | No | — | — | Optional post-click JS verification expression. |
| `verifyTimeout` | `integer` | No | `3000` | 0–30000 | Max ms to wait for verify expression to become truthy. Only used when verify is set. |
| `waitForNavigation` | `boolean` | No | `false` | — | If true, wait for URL change + page load after clicking. |
| `navigationStrict` | `boolean` | No | `false` | — | If true (with waitForNavigation), ok is true only when click and navigation both succeed. |
| `waitForNavigationTimeoutMs` | `integer` | No | `5000` | 0–30000 | Max ms to wait for navigation (0-30000). Only used when waitForNavigation=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and navigation completes, include a screenshot in the response. |
| `screenshotPolicy` | `string` | No | `"smart"` | `smart`, `always`, `on_failure`, `on_partial_or_failure`, `off` | Capture policy. smart=partial/failure always + sampled success. always=every call. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `outputDetail` | `string` | No | `"compact"` | `compact`, `full`, `minimal` | Response verbosity. 'compact': core fields only. 'full': includes diagnostics and telemetry. 'minimal': lean envelope — core contract + actionDispatched/verified + page/target info + never-suppressible safety warnings only; strips guardedCommit, composerResolution, pksAdvice and other inline telemetry. |
| `transitionContract` | `object` | No | — | — | Optional extension for the auto-generated guarded transition contract. Use this only to add or tighten assertions around the built-in guarded macro template. On nova.guarded_send_message, built-in send preconditions, success assertions, and retryPolicy stay pinned while your extra assertions are merged additively. Every assertion bucket has the shape { all?, any?, forbidden? }, each a non-empty array of { factKey: string, operator: eq\|not_eq\|neq\|exists\|not_exists\|contains\|gt\|lt\|gte\|lte, expected?: any, frameId?: string }. Full schema and semantics: nova.reference_doc_read(docId='mcp'). |
| `transitionContract.actionKind` | `string` | No | — | `dismiss_overlay`, `send_message`, `submit_form`, `select_option`, `custom` | Action classification for stability defaults. 'dismiss_overlay' tunes for blocker removal, 'send_message' for chat send actions, 'submit_form' for classic submits, 'select_option' for model/sandbox/style switches, 'custom' for caller-defined flows. |
| `transitionContract.preconditions` | `object` | No | — | — | Assertions checked before dispatch. Use this to prove the page is in the expected pre-action state. |
| `transitionContract.postconditions` | `object` | No | — | — | Assertions checked after dispatch. Commit-point actions must include at least one non-empty success/forbidden/ambiguous bucket so Nova can verify the outcome instead of skipping verification. |
| `transitionContract.retryPolicy` | `string` | No | `"non_idempotent"` | `idempotent`, `non_idempotent`, `no_retry` | Retry safety. 'idempotent' is safe to repeat, 'non_idempotent' allows only cautious retry advice, 'no_retry' suppresses re-dispatch advice. |
| `transitionContract.ambiguityPolicy` | `string` | No | `"signal"` | `signal`, `retry_once`, `abort` | How ambiguous postcondition matches should be labeled. 'signal' reports indeterminate, 'retry_once' prefers one safe retry when retryPolicy allows it, 'abort' reports do_not_retry. |
| `transitionContract.stabilityWindowMs` | `integer` | No | — | — | Optional stability observation window in milliseconds. Runtime clamps extreme values to guarded-safe bounds. |
| `transitionContract.stabilityMs` | `integer` | No | — | — | Optional stability hold duration in milliseconds. Success must remain true for this long before verification passes. |
| `text` | `string` | No | — | — | Optional text to type into the chat composer before sending. When provided, Nova auto-discovers the input field, types the text, verifies via read-back, then clicks send. No length limit — long text is auto-chunked. When text is set, selector/ctaRef are ignored for input discovery but can still override send-button resolution. |
| `message` | `string` | No | — | — | Alias for 'text'. Accepted for convenience — many agents use 'message' instinctively. If both 'text' and 'message' are provided, 'text' wins. |

Capability bundles: `browser_automation`, `form_submission`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Calls

### Fully Automated Prompt Dispatch (Auto-Discovery)
```json
{
  "text": "Please summarize the key takeaways of the uploaded financial report in three bullet points."
}
```

### Explicit Selector with Blocker Clearance
```json
{
  "text": "Confirm order and proceed to invoice generation.",
  "selector": "button[data-testid='send-button']",
  "autoDismissBlockers": true
}
```

---

## 4. Return Value Structure

```json
{
  "ok": true,
  "actionDispatched": true,
  "verified": true,
  "targetId": "tab-101",
  "effectiveSelector": "button[data-testid='send-button']",
  "mode": "compose_and_send",
  "composerResolution": {
    "input": { "selector": "div[contenteditable='true']", "source": "auto_discovery", "confidence": 0.95 },
    "send": { "selector": "button[data-testid='send-button']", "source": "auto_discovery", "scopeKind": "document" },
    "pairConfidence": 0.9,
    "ambiguityMargin": 0.4,
    "typedChars": 84
  },
  "verifyState": "verified",
  "retryAdvice": "do_not_retry"
}
```
`composerResolution` and `mode: "compose_and_send"` only appear when `text`/`message` was supplied so Nova did the type-then-send flow itself; a call that only clicks an already-typed composer's send button (explicit `selector`/`ctaRef`, no `text`) omits them.

---

## 5. Common Errors & Troubleshooting

| Reason Code | Cause | Corrective Action |
| :--- | :--- | :--- |
| `action.no_input_field_found` | No visible chat composer textarea or contenteditable found. | Check if the chat page is finished loading using [`nova.wait_for_selector`](../browser-automation/nova-wait-for-selector.md). |
| `action.no_send_button_found` | Composer was found, but no send button could be paired with it. | Provide explicit `selector` for the send button. |
| `action.no_chat_surface_pair_found` | Neither composer nor send button could be resolved as a pair. | Pass an explicit `selector` for the send button, or inspect the page with `nova.perceive`. |
| `action.ambiguous_input_field` | Multiple input fields exist on page with equal pairing confidence. | Pass an explicit `selector` to identify the desired input. |

These are reported as a failed action outcome (not an invalid-params error).

---

## 6. Related Tools & Documentation

* [`nova.click_selector`](../browser-automation/nova-click-selector.md) — Low-level single-element click execution.
* [`nova.type_selector`](../browser-automation/nova-type-selector.md) — Low-level text input typing.
* [`nova.guarded_submit_form`](nova-guarded-submit-form.md) — Guarded form submissions.
* [Agent Awareness Gates (AAG)](../../../core-features/agent-awareness-gates-aag/README.md) — Pre-action and post-action verification contracts.
