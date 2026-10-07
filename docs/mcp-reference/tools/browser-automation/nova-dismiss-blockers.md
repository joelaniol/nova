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
2. **Click pass:** Among buttons, `[role="button"]` elements, submit/button inputs, and links inside a detected blocker, scores candidates by their label and only clicks one that looks like a safe dismiss/reject action; in `"conservative"` mode it will not click an action that does not look dismissive.
3. **Escape pass:** When `pressEscape: true` (default) and a blocker was seen, dispatches an Escape keydown/keyup pair after the click pass.
4. **Aggressive hide:** Only in `mode: "aggressive"`, remaining overlay roots get `display: none !important` set directly on their style, tagged internally as an `aggressive_overlay_hide` action.

### B. CMP Cookie Banner Resolution
If a cookie consent banner belongs to a known vendor (OneTrust, Cookiebot, Klaro, Didomi), prefer calling [`nova.cmp_apply`](../../../core-features/closed-loop-system-cls/README.md) first to reject optional cookies cleanly. If `cmp_apply` reports `failureCode: "no_adapter"`, fall back to `nova.dismiss_blockers`.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `mode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Dismissal strategy. 'conservative': targets common consent/cookie/GDPR banners only. 'aggressive': also removes overlay divs, fixed-position blockers, and backdrop elements. Start conservative; escalate only if needed. |
| `maxPasses` | `integer` | No | `2` | 1–5 | Maximum dismissal iterations. Each pass scans for and removes one layer of blockers. More passes = more thorough but slower. |
| `pressEscape` | `boolean` | No | `true` | — | If true, also press Escape key to dismiss keyboard-closable modals/dialogs. |

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

* **Use in Guarded Clicks:** You rarely need to call `nova.dismiss_blockers` manually before clicking. Simply pass `autoDismissBlockers: true` to [`nova.click_selector`](nova-click-selector.md), and Nova will invoke blocker dismissal automatically if a backdrop intercepts the click.
* **Aggressive Mode Side Effects:** In `"aggressive"` mode, hiding root overlays may leave `overflow: hidden` on the HTML body. If scrolling feels locked afterwards, re-verify with `nova.scroll_smart`.

---

## See Also

* [`nova.click_selector`](nova-click-selector.md) — Click elements with `autoDismissBlockers: true`.
* [`nova.scroll_smart`](nova-scroll-smart.md) — Natural wheel scrolling.
* [Core Feature: Closed-Loop System (CLS)](../../../core-features/closed-loop-system-cls/README.md)
