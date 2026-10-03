# `nova.dismiss_blockers`

Identifies and removes click-blocking overlays, cookie consent banners, notification prompts, and modal backdrops.

---

## 1. Overview

Autonomously operating agents are frequently halted by popups, promotional modals, cookie consent walls (CMPs), and translucent backdrops that intercept mouse clicks.

`nova.dismiss_blockers` is an active remediation tool that inspects the page for common blocker patterns, triggers polite close buttons or Escape keys, and optionally hides persistent blocking roots to restore page clickability.

* **Capability Bundle:** `browser_automation`, `system_tools`
* **Modes:** Supports `"polite"` (clicks close/reject buttons) and `"aggressive"` (hides stubborn backdrop roots).
* **Return Value:** Reports how many blockers were found, how many were dismissed, and whether the page surface is now clear.

---

## 2. Key Capabilities & Features

### A. Two-Phase Dismissal
1. **Pass 1 (Polite Click):** Searches for standard close buttons (`[aria-label*="close"]`, `button.close`, `.modal-close`, `button:has(svg)`).
2. **Pass 2 (Keyboard Escape):** When `pressEscape: true` is enabled, dispatches an Escape key event to trigger native modal dismiss handlers.
3. **Pass 3 (Aggressive Style Reset):** Under `mode: "aggressive"`, identifies top-layer backdrop containers (`.backdrop`, `.modal-overlay`, fixed zero-content overlays) and temporarily sets their CSS style to `display: none !important`.

### B. CMP Cookie Banner Resolution
If a cookie consent banner belongs to a known vendor (OneTrust, Cookiebot, Klaro, Didomi), prefer calling [`nova.cmp_apply`](../../../core-features/closed-loop-system.md) first to reject optional cookies cleanly. If `cmp_apply` reports `failureCode: "no_adapter"`, fall back to `nova.dismiss_blockers`.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `mode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Dismissal strategy. 'conservative': targets common consent/cookie/GDPR banners only. 'aggressive': also removes overlay divs, fixed-position blockers, and backdrop elements. Start conservative; escalate only if needed. |
| `maxPasses` | `integer` | No | `2` | 1–5 | Maximum dismissal iterations. Each pass scans for and removes one layer of blockers. More passes = more thorough but slower. |
| `pressEscape` | `boolean` | No | `true` | — | If true, also press Escape key to dismiss keyboard-closable modals/dialogs. |
<!-- /generated:parameters -->

---

## 4. Example Call

```json
{
  "name": "nova.dismiss_blockers",
  "arguments": {
    "targetId": "tab-1",
    "mode": "polite",
    "maxPasses": 3
  }
}
```

### Sample Response
```json
{
  "ok": true,
  "blockersDetected": 1,
  "blockersDismissed": 1,
  "surfaceClear": true,
  "actionsTaken": [
    "Clicked button.cookie-dismiss",
    "Dispatched Escape key"
  ]
}
```

---

## 5. Best Practices & Common Traps

* **Use in Guarded Clicks:** You rarely need to call `nova.dismiss_blockers` manually before clicking. Simply pass `autoDismissBlockers: true` to [`nova.click_selector`](nova-click-selector.md), and Nova will invoke blocker dismissal automatically if a backdrop intercepts the click.
* **Aggressive Mode Side Effects:** In `"aggressive"` mode, hiding root overlays may leave `overflow: hidden` on the HTML body. If scrolling feels locked afterwards, re-verify with `nova.scroll_smart`.

---

## See Also

* [`nova.click_selector`](nova-click-selector.md) — Click elements with `autoDismissBlockers: true`.
* [`nova.scroll_smart`](nova-scroll-smart.md) — Natural wheel scrolling.
* [Core Feature: Closed-Loop System (CLS)](../../../core-features/closed-loop-system.md)
