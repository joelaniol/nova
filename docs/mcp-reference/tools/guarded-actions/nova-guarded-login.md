# `nova.guarded_login`

High-level guarded macro for login form submissions, featuring integrated Auth Surface Detection (ASD) that distinguishes between authentication rejections and multi-factor (2FA/MFA) follow-up states.

---

## 1. Overview

Logging into websites autonomously is fraught with failure states: incorrect credentials trigger error alerts, rate limits block further attempts, or the application transitions into an intermediate Two-Factor Authentication (2FA/TOTP) screen.

`nova.guarded_login` addresses this by applying an **Authentication-Specific Transition Contract**:
* **Explicit Failure Trapping:** If the server returns bad credentials or invalid password errors, Nova identifies the error element and flags `verifyState: "failed"` with clear error diagnostics.
* **MFA Progression Handling:** If the submission succeeds but advances to a 2FA prompt, SMS code screen, or passkey verification, Nova treats this as an **ambiguous follow-up state** rather than a failure. The agent is guided to retrieve a TOTP code rather than aborting or retrying credentials.
* **Auth State Verification:** Reconciles the tab's login status with Nova's Auth Surface Detection (ASD) engine.

* **2FA / MFA Resilient:** Does not crash or panic when two-factor authentication is requested.
* **Rate-Limit Prevention:** Strict `non_idempotent` retry policy prevents brute-force lockouts.
* **Blocker Clearance:** Automatically removes cookie banners or marketing popups covering login buttons.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `activateIfNeeded` | `boolean` | No | `true` | — | For an explicit concrete inactive targetId, temporarily activate that Nova target before physical pointer dispatch. Defaults true. Omitted/'active' targets are never auto-retargeted, and Nova never foregrounds the app window. |
| `restoreActiveTarget` | `boolean` | No | `true` | — | After automatic activation and an unambiguous non-navigation success, restore the previously active Nova target if no user or competing target switch occurred. Ignored when no automatic activation happened. |
| `selector` | `string` | No | — | — | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). |
| `frameId` | `string` | No | — | — | Optional same-origin frame ID. For selector-based calls, Nova resolves and clicks the selector inside that iframe and also scopes the auto-generated guarded assertions to the same frame. Not supported together with ctaRef. |
| `ctaRef` | `integer` | No | — | — | CTA v3 handle reference (from perceive cta_detection_v3). If set, clicks by ref instead of selector. Requires ctaRev. |
| `ctaRev` | `integer` | No | — | — | CTA revision from perceive response. Required when ctaRef is used. |
| `button` | `string` | No | `"left"` | `left`, `middle`, `right` | Mouse button: 'left' (default), 'middle', 'right'. |
| `clickCount` | `integer` | No | `1` | 1–3 | Click count: 1=single, 2=double, 3=triple click. |
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

Capability bundles: `browser_automation`, `form_submission`, `vault_auth`.
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "selector": "button#submit-login",
  "waitForNavigation": true,
  "autoDismissBlockers": true
}
```

---

## 4. Return Value Structure

### Successful Full Login
```json
{
  "ok": true,
  "actionDispatched": true,
  "verified": true,
  "targetId": "tab-101",
  "authState": "authenticated",
  "currentUrl": "https://example.com/dashboard",
  "verifyState": "verified",
  "retryAdvice": "do_not_retry"
}
```

### Two-Factor (2FA) Progression Detected
```json
{
  "ok": true,
  "actionDispatched": true,
  "verified": false,
  "targetId": "tab-101",
  "authState": "mfa_challenge_presented",
  "currentUrl": "https://example.com/auth/two-factor",
  "verifyState": "indeterminate",
  "retryAdvice": "follow_up",
  "guidance": "Login credentials accepted, but page transitioned to a Two-Factor Authentication challenge. Inspect 2FA input and provide OTP code."
}
```

---

## 5. Related Tools & Documentation

* [`nova.vault_prepare_fill`](../vault-and-security/nova-vault-prepare-fill.md) — Request single-use fill token for stored passwords.
* [`nova.type_selector_secret`](../vault-and-security/nova-type-selector-secret.md) — Inject vault password into login input field.
* [`nova.guarded_submit_form`](nova-guarded-submit-form.md) — Generic form submit macro.
* [Auth Surface Detection (ASD)](../../../core-features/auth-surface-detection.md) — Architectural overview of Nova's login and session tracking.
