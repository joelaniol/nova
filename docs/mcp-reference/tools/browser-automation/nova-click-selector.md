# `nova.click_selector`

Executes a verified click on a DOM element matching a CSS selector or CTA handle, featuring deep Shadow-DOM piercing, backdrop dismissal, and postcondition verification.

* **Interaction Guide:** [Selectors & Shadow DOM](../../../core-features/browser-interaction/selectors-and-shadow-dom/README.md)

---

## 1. Overview

`nova.click_selector` is the primary interaction tool for activating buttons, links, toggles, and interactive DOM nodes. Unlike naive browser clicks, Nova enforces **Pre-Click Visibility & Clickability Verification**, **Deep Shadow-DOM Piercing**, and **Postcondition Settlement** to eliminate silent click failures.

* **Shadow-DOM Syntax:** Uses ` >>> ` to pierce through open shadow roots (closed shadow roots are not reachable this way).
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
Prevents clicking and immediately declaring victory while the page is still mutating: `verify` takes a JS expression (e.g. `'!document.querySelector(".ad-showing")'`) that Nova polls until truthy, confirming the click had the expected effect. Pair it with `transitionContract` for commit-point actions (send, submit, login) that need stronger pre/postcondition checks.

### D. Multi-Match Strictness (`strict: true`)
If multiple visible elements match the selector and `strict: true` is passed, Nova refuses the click (`ok: false`, `reasonCode: "selector.ambiguous"`) and reports `matchCount`/`candidateCount` instead of clicking the wrong element arbitrarily. If Nova cannot count matches at all (e.g. across shadow-DOM chains), it refuses with `reasonCode: "selector.uniqueness_unverified"` instead.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `observe` | `object` | No | — | — | See what this action set off, in the same call: requests started by page JavaScript (fetch, XHR, WebSocket, sendBeacon) with method, url, status, ok and duration, whether the page navigated, and optionally the state of an element afterwards. Waits until no request is in flight and nothing new arrived for quietMs, at most waitMs. Pass {} for the defaults. Replaces network_read before and after the action plus dom_extract. Document navigations and images are not listed. |
| `observe.waitMs` | `integer` | No | `3000` | 0–15000 | Longest wait for the traffic to settle after the action. |
| `observe.quietMs` | `integer` | No | `500` | 100–5000 | How long nothing may be in flight or arrive before the traffic counts as settled. |
| `observe.urlContains` | `string` | No | — | ≤ 500 characters | List only requests whose URL contains this text (counts still cover all). |
| `observe.maxRequests` | `integer` | No | `20` | 1–100 | Most requests listed; requestsOmitted counts the rest. |
| `observe.after` | `object` | No | — | — | Read an element once the traffic settled, like nova.dom_extract: {selector, properties}. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit inactive targetId: briefly bring that tab to the front for the click (default true); the person sees that tab for the moment of the click. Never retargets 'active', never foregrounds the window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After such an activation and a clear non-navigating success, give the user's previous tab back (default true). |
| `selector` | `string` | No | — | — | CSS selector; ' >>> ' pierces shadow DOM (e.g. 'my-comp >>> .btn'). |
| `frameId` | `string` | No | — | — | Click inside an iframe: frames[] or opaqueFrames[] frameId from nova.perceive(deep=true). Not with ctaRef. Other-site frames can be switched off by the user (frame.cross_origin_interaction_off); scaled/rotated/nested ones return unsupported_frame_geometry. |
| `button` | `string` | No | `"left"` | `left`, `middle`, `right` | 'left' (default), 'middle' (new tab), 'right' (context menu). |
| `clickCount` | `integer` | No | `1` | 1–3 | 1 single, 2 double (select word), 3 triple (select line). |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait for the element to appear. Left unset, the click stops early (stoppedEarly says why) when an open modal dialog covers the element, or when nothing matches on a loaded page that stopped changing; set it to wait the full time for content that appears later. |
| `autoDismissBlockers` | `boolean` | No | `false` | — | true: remove overlays blocking the element before clicking. Default false - prefer nova.cmp_apply / dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | 'conservative': common banners only. 'aggressive': any overlay/fixed blocker. |
| `pksMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | PKS matching: off \| match (compact hints) \| telemetry (full). |
| `pksAdviceMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | Detail of pksAdvice: off \| match \| telemetry. |
| `verify` | `string` | No | — | — | JS expression polled after the click until truthy - proves the effect. E.g. 'document.querySelector(".modal") === null'. |
| `verifyTimeout` | `integer` | No | `3000` | 0–30000 | Max ms to wait for verify (default 3000). |
| `waitForNavigation` | `boolean` | No | `false` | — | Wait for URL change + page load after the click. |
| `navigationStrict` | `boolean` | No | `false` | — | With waitForNavigation: ok only if the navigation happened too. |
| `strict` | `boolean` | No | `false` | — | Click only if exactly one visible element matches; otherwise refuse (selector.ambiguous / selector.uniqueness_unverified), nothing clicked. Default: click best visible match and warn. |
| `expectText` | `string` | No | — | 1–300 characters | Click the element that reads this text (visible text, else aria-label/value/title; case and spacing ignored). When the selector matches several, Nova picks the one with this text - a whole-label match wins over partial ones - so 'li > button' plus expectText clicks one entry of a list. None reads it: selector.text_mismatch; several do: selector.text_ambiguous; nothing clicked either way. Also guards buttons that share generic classes ('Move to list' vs 'Delete selected'). Selector clicks only, not ctaRef. |
| `expectTextExact` | `boolean` | No | `false` | — | With expectText or expectTextAny: the whole text must equal it instead of containing it. |
| `expectTextAny` | `array` of `string` | No | — | 1–10 items | Like expectText, for an element whose label changes: any one of these texts is enough, e.g. ['Choose your category', 'Choose another category'] for a link that reads differently once suggestions load. Can be combined with expectText. |
| `waitForNavigationTimeoutMs` | `integer` | No | `5000` | 0–30000 | Max ms to wait for navigation (0-30000). |
| `includeScreenshot` | `boolean` | No | `false` | — | Add a screenshot after navigation. Optional sidecar: if only the capture fails (screenshotStatus/screenshotReasonCode), the click result still stands - do not repeat the click. |
| `screenshotPolicy` | `string` | No | `"smart"` | `smart`, `always`, `on_failure`, `on_partial_or_failure`, `off` | With includeScreenshot: smart (failures always, successes sampled) \| always \| on_failure \| on_partial_or_failure \| off. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width px. Above 512 (or screenshotMaxHeight above 320) the screenshot comes inline at that size instead of as a 512 px thumbnail plus resource link. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height px. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | png (default) \| jpeg \| auto. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality 1-100. |
| `ctaRef` | `integer` | No | — | — | CTA handle from nova.perceive; needs ctaRev. |
| `ctaRev` | `integer` | No | — | — | CTA revision from the same perceive; stale refs error. |
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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
    "verify": "document.querySelector('.order-confirmation-badge') !== null",
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
* [`nova.dismiss_blockers`](../guarded-actions/nova-dismiss-blockers.md) — Standalone modal and banner dismissal.
* [Core Feature: Browser Interaction](../../../core-features/browser-interaction/README.md)
