# `nova.click_selector`

Executes a verified click on a DOM element matching a CSS selector or CTA handle, featuring deep Shadow-DOM piercing, backdrop dismissal, and postcondition verification.

---

## 1. Overview

`nova.click_selector` is the primary interaction tool for activating buttons, links, toggles, and interactive DOM nodes. Unlike naive browser clicks, Nova enforces **Pre-Click Visibility & Clickability Verification**, **Deep Shadow-DOM Piercing**, and **Postcondition Settlement** to eliminate silent click failures.

* **Shadow-DOM Syntax:** Uses ` >>> ` to pierce through open and closed shadow roots cleanly.
* **Pre-Check Safety:** Verifies element is not covered by modal backdrops or cookie banners.

---

## 2. Key Capabilities & Features

### A. Deep Shadow-DOM Piercing (` >>> `)
Standard CSS selectors fail when an element resides inside a Web Component or Shadow Root. Nova's selector engine supports the deep combinator ` >>> `:
```css
custom-checkout >>> payment-module >>> button.pay-now
```
Nova traverses shadow root boundaries recursively to locate the target node.

### B. Auto-Dismiss Blockers (`autoDismissBlockers: true`)
If a click cannot land because a cookie banner, modal backdrop, or promotional popover covers the element:
* When `autoDismissBlockers: true` is set, Nova automatically identifies the obscuring overlay, dismisses it, and retries the click seamlessly in a single step.

### C. Postcondition Verification (`verify`)
Prevents clicking and immediately declaring victory while the page is still mutating:
* `verify.absent`: Asserts that an element (e.g. the clicked modal or loading spinner) disappears from the DOM.
* `verify.present`: Asserts that the expected success message or resulting container appears.

### D. Multi-Match Strictness (`strict: true`)
If multiple elements match the selector and `strict: true` is passed, Nova fails-fast with `-32602` and reports the count and locations rather than clicking the wrong element arbitrarily.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `selector` | `string` | No | — | — | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). |
| `frameId` | `string` | No | — | — | Optional same-origin frame ID for selector-based clicks. When set, Nova resolves the selector inside that iframe and dispatches the click at the translated top-document coordinates. Not supported together with ctaRef. |
| `button` | `string` | No | `"left"` | `left`, `middle`, `right` | Mouse button: 'left' (default), 'middle' (new tab), 'right' (context menu). |
| `clickCount` | `integer` | No | `1` | 1–3 | Click count: 1=single click, 2=double click (select word), 3=triple click (select line). |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait for element to appear before failing. |
| `autoDismissBlockers` | `boolean` | No | `false` | — | If true, explicitly auto-dismiss overlays/modals blocking the target element before clicking. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `pksMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | PKS phenomenon matching: 'off' suppresses, 'match' returns compact hints, 'telemetry' returns full PKS payload. |
| `pksAdviceMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | Controls verbosity of pksAdvice in the response. |
| `verify` | `string` | No | — | — | JS expression to evaluate after clicking. If provided, polls until truthy (confirms click had effect). Example: '!document.querySelector(".ad-showing")' or 'document.querySelector(".skip-btn") === null'. |
| `verifyTimeout` | `integer` | No | `3000` | 0–30000 | Max ms to wait for verify expression to become truthy (default 3000). Only used when verify is set. |
| `waitForNavigation` | `boolean` | No | `false` | — | If true, wait for URL change + page load after clicking. |
| `navigationStrict` | `boolean` | No | `false` | — | If true (with waitForNavigation=true), ok is true only when click and navigation both succeed. |
| `strict` | `boolean` | No | `false` | — | If true, click only when the selector matches exactly ONE visible element (like Playwright's strict mode, but hidden duplicates such as a collapsed mobile menu do not count). Several visible matches refuse with reasonCode selector.ambiguous and nothing is clicked; a selector whose uniqueness Nova cannot count (shadow-DOM chains) refuses with selector.uniqueness_unverified. matchCount/candidateCount say what was found. Default false keeps the usual behaviour: click the best-scoring visible match and warn. |
| `waitForNavigationTimeoutMs` | `integer` | No | `5000` | 0–30000 | Max ms to wait for navigation (0-30000). Only used when waitForNavigation=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and navigation completes, include a screenshot in the response. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotPolicy` | `string` | No | `"smart"` | `smart`, `always`, `on_failure`, `on_partial_or_failure`, `off` | Capture policy when includeScreenshot=true. smart=partial/failure always + sampled success. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `ctaRef` | `integer` | No | — | — | CTA v3 handle reference (from perceive cta_detection_v3). If set, clicks by ref instead of selector. Requires ctaRev. |
| `ctaRev` | `integer` | No | — | — | CTA revision from perceive response. Required when ctaRef is used. Stale refs return error. |
| `outputDetail` | `string` | No | `"compact"` | `compact`, `full`, `minimal` | Response verbosity. 'compact' (default): core fields only (status, nav summary, page state, side-effects). 'full': includes navEvidence, telemetry, diagnostics, dismiss details for debugging. 'minimal': lean envelope — only the core contract (ok/status/reasonCode/stage/retryable), actionDispatched/verified, page/target info, and never-suppressible safety warnings; strips pksAdvice, guardedCommit, fileInputRisk, popup/download flags and other inline telemetry. |
| `transitionContract` | `object` | No | — | — | Closed-loop transition contract for guarded commit points. When provided, preconditions are verified before the click and postconditions are verified after. Required for commit-point actions like send, submit, login, and other state-changing clicks. Response includes 'guardedCommit' with dispatchStatus, verificationStatus, and retryAdvice. Every assertion bucket has the shape { all?, any?, forbidden? }, each a non-empty array of { factKey: string, operator: eq\|not_eq\|neq\|exists\|not_exists\|contains\|gt\|lt\|gte\|lte, expected?: any, frameId?: string }. Full schema and semantics: nova.reference_doc_read(docId='mcp'). |
| `transitionContract.actionKind` | `string` | No | — | `dismiss_overlay`, `send_message`, `submit_form`, `select_option`, `custom` | Action classification for stability defaults. 'dismiss_overlay' tunes for blocker removal, 'send_message' for chat send actions, 'submit_form' for classic submits, 'select_option' for model/sandbox/style switches, 'custom' for caller-defined flows. |
| `transitionContract.preconditions` | `object` | No | — | — | Assertions checked before dispatch. Use this to prove the page is in the expected pre-action state. |
| `transitionContract.postconditions` | `object` | No | — | — | Assertions checked after dispatch. Commit-point actions must include at least one non-empty success/forbidden/ambiguous bucket so Nova can verify the outcome instead of skipping verification. |
| `transitionContract.retryPolicy` | `string` | No | `"non_idempotent"` | `idempotent`, `non_idempotent`, `no_retry` | Retry safety. 'idempotent' is safe to repeat, 'non_idempotent' allows only cautious retry advice, 'no_retry' suppresses re-dispatch advice. |
| `transitionContract.ambiguityPolicy` | `string` | No | `"signal"` | `signal`, `retry_once`, `abort` | How ambiguous postcondition matches should be labeled. 'signal' reports indeterminate, 'retry_once' prefers one safe retry when retryPolicy allows it, 'abort' reports do_not_retry. |
| `transitionContract.stabilityWindowMs` | `integer` | No | — | — | Optional stability observation window in milliseconds. Runtime clamps extreme values to guarded-safe bounds. |
| `transitionContract.stabilityMs` | `integer` | No | — | — | Optional stability hold duration in milliseconds. Success must remain true for this long before verification passes. |

Capability bundles: `browser_automation`, `form_submission`.
<!-- /generated:parameters -->

---

## 4. Example Calls

### Standard Button Click with Verification
```json
{
  "name": "nova.click_selector",
  "arguments": {
    "targetId": "tab-1",
    "selector": "button#submit-order",
    "verify": {
      "present": ".order-confirmation-badge"
    },
    "timeoutMs": 10000
  }
}
```

### Shadow-DOM Click with Blocker Dismissal
```json
{
  "name": "nova.click_selector",
  "arguments": {
    "targetId": "tab-1",
    "selector": "app-root >>> user-profile >>> button.save-changes",
    "autoDismissBlockers": true,
    "strict": true
  }
}
```

---

## 5. Best Practices & Common Traps

* **The Shadow-DOM Trap:** If `document.querySelector` fails in regular browsers, check if the button is hosted inside a Web Component. Use `host >>> target` syntax.
* **Navigation Timeouts:** When clicking a link that opens a new tab (`target="_blank"`), the originating tab does not navigate. Inspect the response payload: Nova reports `newTabOpened: true` and `newTabIds: [...]` instead of timing out.

---

## See Also

* [`nova.type_selector`](nova-type-selector.md) — Type text into inputs.
* [`nova.scroll_smart`](nova-scroll-smart.md) — Bring off-screen elements into view.
* [`nova.dismiss_blockers`](nova-dismiss-blockers.md) — Standalone modal and banner dismissal.
* [Core Feature: Humanized Input Engine](../../../core-features/humanized-input-engine.md)
