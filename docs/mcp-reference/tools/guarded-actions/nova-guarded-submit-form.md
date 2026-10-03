# `nova.guarded_submit_form`

High-level guarded macro for form submissions, wrapping click dispatch in an automated transition contract to verify validation rules, prevent duplicate submissions, and confirm post-submit transitions.

---

## 1. Overview

Clicking a form submit button naively often leads to undetected failures: client-side validation errors pop up under inputs, the submit button remains disabled, or the page reloads with error flashes.

`nova.guarded_submit_form` wraps the submit action in an automated **Closed-Loop Transition Contract**:
1. **Pre-Submit Validation:** Verifies the submit button is interactive and not covered by modal backdrops.
2. **Atomic Dispatch:** Dispatches a physical CDP click to trigger standard browser form submission.
3. **Postcondition Settlement:** Asserts that either navigation away from the form completed, a success banner appeared, or validation errors fired. If validation errors occur, Nova reports them immediately with retry advice rather than falsely reporting success.

* **Capability Bundle:** `form_submission`, `guarded_actions`
* **Automated Postconditions:** Pre-configured to detect navigation away from the form or appearance of confirmation modals.
* **Idempotency Safeguard:** Prevents agents from rapidly double-clicking payment or order buttons.
* **Iframe Scoping (`frameId`):** Can submit forms embedded inside cross-origin checkout or login frames.

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | No | `null` | CSS selector for the submit button. Supports ` >>> `. |
| **`ctaRef`** | `integer`| No | `null` | Optional CTA handle reference (from `nova.perceive`). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`waitForNavigation`**| `boolean`| No | `false` | Wait for URL transition and page load after submission. |
| **`navigationStrict`** | `boolean`| No | `false` | When `true`, requires both click and navigation to succeed. |
| **`autoDismissBlockers`**| `boolean`| No | `false` | Automatically dismiss modals or banners blocking the submit button. |
| **`timeoutMs`** | `integer` | No | `10000` | Max milliseconds to wait for element appearance (0–300,000 ms). |
| **`includeScreenshot`**| `boolean`| No | `false` | Capture visual evidence after submission settles. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 3. Example Calls

### Submit Form and Await Page Navigation
```json
{
  "selector": "form#checkout-form button[type='submit']",
  "waitForNavigation": true,
  "autoDismissBlockers": true
}
```

### Submit Embedded Contact Form via CTA Reference
```json
{
  "ctaRef": 4,
  "ctaRev": 12,
  "waitForNavigation": false
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
  "navigationCompleted": true,
  "previousUrl": "https://example.com/checkout/step-2",
  "currentUrl": "https://example.com/checkout/confirmation",
  "verifyState": "verified",
  "retryAdvice": "do_not_retry"
}
```

---

## 5. Related Tools & Documentation

* [`nova.click_selector`](../browser-automation/nova-click-selector.md) — Unwrapped single click action.
* [`nova.guarded_send_message`](nova-guarded-send-message.md) — Guarded message dispatch for chat interfaces.
* [`nova.guarded_login`](nova-guarded-login.md) — Guarded authentication submissions.
* [Agent Awareness Gates (AAG)](../../../core-features/aag.md) — Deep dive into transition contracts and verification.
