# `nova.guarded_login`

High-level guarded macro for login form submissions, featuring integrated Auth Surface Detection (ASD) that distinguishes between authentication rejections and multi-factor (2FA/MFA) follow-up states.

---

## 1. Overview

Logging into websites autonomously is fraught with failure states: incorrect credentials trigger error alerts, rate limits block further attempts, or the application transitions into an intermediate Two-Factor Authentication (2FA/TOTP) screen.

`nova.guarded_login` addresses this by applying an **Authentication-Specific Transition Contract**:
* **Explicit Failure Trapping:** If the server returns bad credentials or invalid password errors, Nova identifies the error element and flags `verifyState: "failed"` with clear error diagnostics.
* **MFA Progression Handling:** If the submission succeeds but advances to a 2FA prompt, SMS code screen, or passkey verification, Nova treats this as an **ambiguous follow-up state** rather than a failure. The agent is guided to retrieve a TOTP code rather than aborting or retrying credentials.
* **Auth State Verification:** Reconciles the tab's login status with Nova's Auth Surface Detection (ASD) engine.

* **Capability Bundle:** `form_submission`, `vault_auth`, `guarded_actions`
* **2FA / MFA Resilient:** Does not crash or panic when two-factor authentication is requested.
* **Rate-Limit Prevention:** Strict `non_idempotent` retry policy prevents brute-force lockouts.
* **Blocker Clearance:** Automatically removes cookie banners or marketing popups covering login buttons.

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | No | `null` | CSS selector for the login submit button. Supports ` >>> `. |
| **`ctaRef`** | `integer`| No | `null` | Optional CTA handle reference (from `nova.perceive`). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`waitForNavigation`**| `boolean`| No | `false` | Wait for URL transition and page load after login submission. |
| **`navigationStrict`** | `boolean`| No | `false` | When `true`, requires both click and navigation to succeed. |
| **`autoDismissBlockers`**| `boolean`| No | `false` | Automatically dismiss modals or banners blocking the login button. |
| **`timeoutMs`** | `integer` | No | `10000` | Max milliseconds to wait for element appearance (0–300,000 ms). |
| **`includeScreenshot`**| `boolean`| No | `false` | Capture visual evidence after login submission settles. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

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
