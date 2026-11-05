# `nova.dismiss_blockers`

Identifies and removes click-blocking overlays, cookie consent banners, notification prompts, and modal backdrops.

---

## 1. Overview

Autonomously operating agents are frequently halted by popups, promotional modals, cookie consent walls (CMPs), and translucent backdrops that intercept mouse clicks.

`nova.dismiss_blockers` is an active remediation tool that inspects the page for common blocker patterns, clicks a dismiss/reject control when it can identify one safely, optionally presses Escape, and in aggressive mode hides persistent blocking roots to restore page clickability.

* **Modes:** Supports `"conservative"` (targets common consent/cookie/GDPR banners only) and `"aggressive"` (also removes overlay divs, fixed-position blockers, and backdrop elements).
* **Return Value:** Reports whether the page is still blocked, whether a dismiss action was taken, a verdict, and the dismiss actions that were attempted.

---

## 2. Key Capabilities & Features

### A. Detection and Dismissal
1. **Blocker detection:** Looks for semantic dialogs (`[role="dialog"]`, `[aria-modal="true"]`, `dialog[open]`), then for floating elements whose id/class names suggest a consent, cookie, privacy, modal, overlay, or popup layer, then falls back to a broader heuristic scan of `div`/`section`/`aside`/`dialog` elements that behave like an overlay (fixed/high z-index, covers a large area, sits in the viewport).
2. **Click pass:** Among buttons, `[role="button"]` elements, submit/button inputs, and links inside a detected blocker, scores candidates by their label and only clicks one that looks like a safe dismiss/reject action. In every mode it never agrees to anything: no accept, agree or "got it", and on a consent dialog no close button either, only a reject the dialog shows as one. Right before the click Nova checks that the button is still the same one in the same place; otherwise it clicks nothing. Every refused button is listed in `actionsTried` with its `reasonCode`.
3. **Escape pass:** When `pressEscape: true` (default) and a blocker was seen, dispatches an Escape keydown/keyup pair after the click pass, but never to a consent dialog.
4. **Aggressive hide:** Only in `mode: "aggressive"`, remaining overlay roots get `display: none !important` set directly on their style, tagged internally as an `aggressive_overlay_hide` action. Hiding answers nothing, so it gives no consent.
5. **A click that opens another page** ends the call with `verdict: "NAVIGATED"`: read the new page before acting; Nova does not click a second time.

### B. CMP Cookie Banner Resolution
If a cookie consent banner belongs to a known vendor (OneTrust, Sourcepoint / TCF v2, Cookiebot, Usercentrics v3), prefer calling [`nova.cmp_apply`](nova-cmp-apply.md) first to reject optional cookies programmatically (see the [Consent Management Guide](../../../core-features/consent-management/README.md)). If `cmp_apply` reports `failureCode: "no_adapter"`, fall back to `nova.dismiss_blockers`.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `mode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Dismissal strategy. 'conservative': targets common consent/cookie/GDPR banners only. 'aggressive': also hides overlay divs, fixed-position blockers, and backdrop elements it may not answer (hiding gives no consent); it still clicks only close/reject buttons. Start conservative; escalate only if needed. |
| `maxPasses` | `integer` | No | `2` | 1–5 | Maximum dismissal iterations. Each pass scans for and removes one layer of blockers. More passes = more thorough but slower. |
| `pressEscape` | `boolean` | No | `true` | — | If true, also press Escape key to dismiss keyboard-closable modals/dialogs. Never on a consent dialog: closing it is no reject. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Call

```json
{
  "name": "nova.dismiss_blockers",
  "arguments": {
    "targetId": "tab-1",
    "mode": "conservative",
    "maxPasses": 3
  }
}
```

### Sample Response
```json
{
  "content": [
    { "type": "text", "text": "Blocker pass completed. clicked=1, hidden=0, verdict=NOOP" }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "mode": "conservative",
    "ok": true,
    "status": "ok",
    "didDismiss": true,
    "blocked": false,
    "verdict": "NOOP",
    "actionsTriedTotal": 1
  }
}
```

---

## 5. Best Practices & Common Traps

* **Use in Guarded Clicks:** You rarely need to call `nova.dismiss_blockers` manually before clicking. Simply pass `autoDismissBlockers: true` to [`nova.click_selector`](../browser-automation/nova-click-selector.md), and Nova will invoke blocker dismissal automatically if a backdrop intercepts the click.
* **Aggressive Mode Side Effects:** In `"aggressive"` mode, hiding root overlays may leave `overflow: hidden` on the HTML body. If scrolling feels locked afterwards, re-verify with `nova.scroll_smart`.

---

## Related Tools

* [`nova.cmp_apply`](nova-cmp-apply.md) — Programmatic vendor API dispatch for recognized CMPs.
* [`nova.click_selector`](../browser-automation/nova-click-selector.md) — Click elements with `autoDismissBlockers: true`.
* [`nova.scroll_smart`](../browser-automation/nova-scroll-smart.md) — Natural wheel scrolling with scroll-lock resilience.
* [Consent Management & Blocker Clearance Architecture](../../../core-features/consent-management/README.md) — High-level architecture overview.
* [Blocker & Overlay Remediation Architecture](../../../core-features/consent-management/blocker-dismissal/README.md) — Deep dive into multi-pass heuristics and scroll recovery.
