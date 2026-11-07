# Heuristic Detection & Blocker Remediation

> [!NOTE]
> When websites deploy non-standard consent dialogs, promotional overlays, newsletter subscription walls, or translucent backdrops lacking a recognized vendor runtime API, programmatic dispatch via `nova.cmp_apply` is impossible. Nova activates its intelligent fallback engine: [`nova.dismiss_blockers`](../../../../mcp-reference/tools/guarded-actions/nova-dismiss-blockers.md). It executes a multi-pass heuristic detection pipeline, deploys conservative vs. aggressive remediation strategies, and automatically repairs orphaned scroll locks.

---

## 1. The Overlay & Blocker Landscape

In modern automated browsing, visual overlays present severe operational hurdles for autonomous agents:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        Common Blocker Archetypes                       │
├──────────────────────────────────┬─────────────────────────────────────┤
│ Blocker Type                     │ Runtime Impact on Autonomous Agents │
├──────────────────────────────────┼─────────────────────────────────────┤
│ Translucent Modal Backdrops      │ A fixed <div> with high z-index and │
│ (e.g. .backdrop, .modal-mask)    │ pointer-events intercepts all mouse │
│                                  │ clicks intended for underlying UI.  │
├──────────────────────────────────┼─────────────────────────────────────┤
│ Promotional & Newsletter Popups  │ Dynamic dialogs appearing seconds   │
│                                  │ after page load, shifting focus.    │
├──────────────────────────────────┼─────────────────────────────────────┤
│ Body Scroll Lock Locks           │ CSS rule `overflow: hidden` applied │
│                                  │ to <body>, freezing all page scroll.│
├──────────────────────────────────┼─────────────────────────────────────┤
│ Custom Cookie Walls              │ Non-standard consent UI lacking a   │
│                                  │ recognized vendor JavaScript API.   │
├──────────────────────────────────┼─────────────────────────────────────┤
│ Age Verification Gates           │ Full-screen barriers requiring      │
│                                  │ interaction before showing content. │
└──────────────────────────────────┴─────────────────────────────────────┘
```

The remediation engine must resolve these obstructions without crashing Single-Page Applications (SPAs) or corrupting underlying form states.

---

## 2. Multi-Pass Remediation Pipeline

When invoked, `nova.dismiss_blockers` executes up to `maxPasses` (default: 2, configurable 1–5) sequential remediation passes. Each pass executes a deterministic three-tier sequence:

```mermaid
flowchart TD
    StartPass["Start Remediation Pass"] --> Step1["Step 1: Heuristic Structural Scan"]

    subgraph Scan["Structural Scan Hierarchy"]
        Step1 --> S1["1. Semantic Dialogs\n([role='dialog'], [aria-modal='true'], dialog[open])"]
        S1 --> S2["2. Class & ID Markers\n(*cookie*, *consent*, *modal*, *popup*, *overlay*)"]
        S2 --> S3["3. Geometric Overlay Probe\n(position: fixed, z-index >= 1000, covers viewport > 30%)"]
    end

    Scan --> Step2["Step 2: Candidate Action Evaluation"]

    subgraph CandidateAction["Action Resolution & Mode Filter"]
        Step2 --> FindControls["Identify Interactive Elements\n(buttons, links, inputs with role='button')"]
        FindControls --> ScoreCandidates["Score Labels via Polarity Tokens\n(dismiss, close, reject, ablehnen, etc.)"]
        ScoreCandidates --> ModeCheck{"Execution Mode?"}
        ModeCheck -- "conservative" --> FilterStrict["Filter for Verified Dismiss/Reject Only"]
        ModeCheck -- "aggressive" --> FilterBroad["Include Secondary Dismiss & Close Icons"]
    end

    FilterStrict --> ClickAction{"Action Found?"}
    FilterBroad --> ClickAction

    ClickAction -- "Yes" --> ClickDispatch["Dispatch Synthetic Click to Best Candidate"]
    ClickAction -- "No" --> EscapeCheck{"pressEscape == true?"}

    ClickDispatch --> SettleWait["Wait 150ms DOM Mutation Settle"]
    SettleWait --> ResidualCheck{"Blockers Still Intercepting?"}

    EscapeCheck -- "Yes" --> EscapeDispatch["Dispatch Synthetic Escape (keydown + keyup)"]
    EscapeCheck -- "No" --> AggressiveCheck{"mode == 'aggressive'?"}

    EscapeDispatch --> SettleWait
    ResidualCheck -- "Yes" --> AggressiveCheck
    ResidualCheck -- "No" --> PassDone["Pass Successful (Unblocked)"]

    AggressiveCheck -- "Yes" --> HideRoots["Apply display: none !important to Blocker Roots\n+ Restore Body Scroll (overflow: auto)"]
    AggressiveCheck -- "No" --> PassDone

    HideRoots --> SettleWait
```

---

## 3. Structural Scan Hierarchy

To avoid destroying essential site navigation or application forms, candidate blockers must satisfy strict structural criteria:

### Priority 1: Semantic Dialogs
Nova queries for standard W3C WAI-ARIA modal landmarks:
* `[role="dialog"]`
* `[role="alertdialog"]`
* `[aria-modal="true"]`
* `<dialog open>`

### Priority 2: Class & ID Lexicon Probes
If semantic landmarks are absent, the scanner probes container classes and IDs using add-only pattern lexicons:
* `*cookie*`, `*consent*`, `*gdpr*`, `*privacy*`
* `*modal*`, `*popup*`, `*overlay*`, `*dialog*`
* `*backdrop*`, `*scrim*`, `*interstitial*`

### Priority 3: Geometric Viewport Probing
For obfuscated or unclassed wrappers, Nova evaluates physical geometry via `getBoundingClientRect()`:
* **Position:** Computed CSS `position: fixed` or `position: absolute`.
* **Stacking Context:** `z-index >= 1000` or higher than the primary main content container.
* **Viewport Coverage:** Element area covers $> 30\%$ of the active viewport area ($W \times H$).
* **Hit-Testing Interception:** Calls `document.elementFromPoint(centerX, centerY)` to verify that the element intercepts pointer events directed at underlying content.

### Open Shadow-Root Traversal
Modern web components and third-party consent providers (such as Usercentrics v3 `#usercentrics-cmp-ui`) encapsulate modal barriers and consent dialogs inside open shadow roots (`element.shadowRoot`). Nova's structural scan recursively inspects open shadow DOM boundaries across all three priority tiers:
* Evaluates semantic ARIA attributes and custom elements within shadow trees.
* Discovers and scores polarity on interactive buttons inside encapsulated shadow DOM.
* Applies geometric overlay hit-testing across shadow boundary roots, ensuring complete dismiss action coverage before falling back to aggressive styling overrides.

---

## 4. Stage 1 Consent Guard: Pre-Interaction Safety & Tab Aliasing

Before any synthetic click or pointer action is dispatched to dismiss a candidate blocker element, Nova passes the candidate through an authoritative, pure-function decision gate: the **Stage 1 Consent Guard** (`ConsentDecisionGuard`).

### 4.1 The Core Invariant: Automation Never Increases Consent
Modern consent dark patterns frequently manipulate button semantics to coerce visitors into tracking opt-ins. Nova's architecture enforces a non-negotiable principle:

> [!IMPORTANT]
> **Automatik erhöht nie die Einwilligung (Automation never increases consent).**  
> An autonomous action never agrees to anything (`accept`, `agree`, *"Got it"*, *"I understand"*). Within a consent dialog or privacy wall, Nova clicks only a rejection button whose legitimacy is conclusively proven either by its own stated scope or by direct contrast against a neighboring acceptance button.

```mermaid
flowchart TD
    Candidate["Candidate Button in Overlay"] --> Guard["Stage 1: ConsentDecisionGuard"]

    subgraph Inspection["Multi-Attribute Candidate Inspection"]
        Guard --> TextCheck{"Visible Text vs.\nAccessible Name Conflict?"}
        TextCheck -- "Conflict (e.g. text 'Reject' vs ARIA 'Accept')" --> DenyMismatch["DENY_LABEL_MISMATCH\n(Hijack / Dark Pattern Blocked)"]
        TextCheck -- "Consistent" --> PolarityCheck{"Polarity == Accept?"}
        PolarityCheck -- "Yes ('agree', 'accept', 'got it')" --> DenyAgree["DENY_AGREE\n(Never Consent Automatically)"]
        PolarityCheck -- "No" --> DismissiveCheck{"Candidate is Dismissive?"}
        DismissiveCheck -- "No" --> DenyNotDismissive["DENY_NOT_DISMISSIVE"]
        DismissiveCheck -- "Yes" --> ContextCheck{"Consent Context Active?\n(cookie / privacy / CMP banner)"}
    end

    ContextCheck -- "No (Newsletter, Promo, Modal)" --> SafeDismiss["SAFE_DISMISS\n(Action Permitted)"]
    ContextCheck -- "Yes (Privacy / Tracking Wall)" --> RejectCheck{"Polarity == Reject?"}

    RejectCheck -- "No (Close, Later, Escape, X)" --> DenyClose["DENY_CONSENT_CLOSE\n(Closing banner counts as implicit tracking)"]
    RejectCheck -- "Yes" --> ProofCheck{"Proven by Scope OR\nProven by Sibling Contrast?"}

    ProofCheck -- "Neither Proven" --> DenyUnproven["DENY_CONSENT_REJECT_UNPROVEN\n(Refuse unverified reject)"]
    ProofCheck -- "Proven" --> ConsentReject["CONSENT_REJECT\n(Verified Rejection Action Permitted)"]
```

### 4.2 Guard Verdicts & Machine-Readable Reason Codes

The guard evaluates six candidate dimensions: candidate label, rendered visible text, ARIA accessible name, immediate sibling group labels, the consent context flag (`ConsentContext`), and the dismissive flag:

| Reason Code | Permitted? | Evaluation Condition | Threat Neutralized |
| :--- | :---: | :--- | :--- |
| **`SAFE_DISMISS`** | **YES** | Candidate is in a non-consent dialog (newsletter popup, marketing modal, age gate) and carries a dismissive label. | Routine modal dismissal without privacy implications. |
| **`CONSENT_REJECT`** | **YES** | Candidate is inside a consent context, has verified `Reject` polarity, and is proven either by explicit scope (*"Reject all"*, *"Nur notwendige"*) or by sibling contrast against an accept button. | Legitimate cookie rejection on non-standard banners. |
| **`DENY_LABEL_MISMATCH`** | **NO** | Rendered visible text conflicts with the element's ARIA accessible name (e.g., visible label displays *"Decline"*, but screen-reader attribute says *"Accept All"*). | **Consent Hijack:** Prevents clicking buttons disguised to fool users or OCR scrapers while committing legal opt-in. |
| **`DENY_AGREE`** | **NO** | Candidate or its visible text exhibits `Accept` polarity (*"agree"*, *"accept"*, *"allow"*, *"got it"*). | **Forced Opt-In:** Prevents automated agents from agreeing to tracking or commercial profiling. |
| **`DENY_NOT_DISMISSIVE`** | **NO** | Element lacks dismissive characteristics (e.g., navigation link or form input). | Prevents clicking arbitrary elements within dialog containers. |
| **`DENY_CONSENT_CLOSE`** | **NO** | Inside a consent context, an element is classified as `Close`, *"later"*, or an *✕* icon. | **Implicit Consent Trap:** On many European websites, closing a cookie modal without making an explicit choice legally defaults to continued tracking. |
| **`DENY_CONSENT_REJECT_UNPROVEN`** | **NO** | Inside a consent context, a reject button has neither explicit scope nor a contrasting accept button in its immediate decision group. | **Ambiguous Rejection:** Rejects standalone buttons where the legal scope of the action cannot be established. |

### 4.3 The Synchronous Act Phase Invariant

A common flaw in automated click implementations is a race condition between element discovery and click dispatch: an element may detach, re-render, shift coordinates, or be covered by an interstitial between discovery and execution.

Nova enforces the **Synchronous Act Phase Invariant** (`OnlyTheActPhaseClicks`):
* Candidate selection, DOM attachment verification, visibility re-evaluation, label sanity checking, and coordinate hit-testing occur in the **exact same synchronous execution pass** as the synthetic pointer dispatch (`DismissBlockerScriptBuilder`).
* If an element's position shifts, opacity drops to 0, or another element intercepts the target coordinates between passes, the click is refused fail-closed.
* No click path exists in the script engine outside this guarded act phase.

### 4.4 Target Tab Aliasing

When orchestrating blocker clearance across multiple tabs or sandboxes, agents are not restricted to exact GUIDs. The `targetId` parameter for [`nova.dismiss_blockers`](../../../../mcp-reference/tools/guarded-actions/nova-dismiss-blockers.md) (and all guarded action tools) supports canonical tab aliases:
* `activeBrowserTab`
* `active_browser_tab`
* `active-tab`
* `browserTabActive`
* `tabActive`
* `"active"` (or omitting `targetId`)

All of the above aliases resolve deterministically to the user's currently focused browser tab, allowing agents to execute immediate clearance without pre-querying `nova.tabs`.

---

## 5. Remediation Modes: Conservative vs. Aggressive

Nova provides two distinct remediation modes to balance DOM stability against clearance success:

```mermaid
flowchart LR
    ModeChoice{"Select Remediation Mode"}

    ModeChoice -- "mode: 'conservative' (Default)" --> Cons["Conservative Mode:\n- Verified reject/dismiss clicks only\n- Synthetic Escape key dispatch\n- Zero DOM style injection\n- High SPA stability"]

    ModeChoice -- "mode: 'aggressive'" --> Aggr["Aggressive Mode:\n- Fallback CSS display: none injection\n- Body scroll unlock (overflow: auto)\n- Forced removal of lingering backdrops\n- Guaranteed clearance for stubborn walls"]
```

### 5.1 Conservative Mode (`mode: "conservative"`)
* **Default Mode:** Recommended starting point for all standard automated browsing flows.
* **Click Discipline:** Strictly refuses to click any button unless its label passes the 3-stage polarity scoring check (`AllowRejectClick`).
* **Zero Style Mutation:** Does not inject inline CSS or remove DOM nodes; relies purely on native UI triggers and keyboard events.
* **Best Suited For:** Legitimate news portals, e-commerce checkouts, and web apps where preserving JavaScript component state is critical.

### 5.2 Aggressive Mode (`mode: "aggressive"`)
* **Escalation Mode:** Activated when conservative mode reports `blocked: true` (e.g., persistent backdrops or paywalls).
* **Forced Display Overrides:** For blocker roots that do not dismiss via clicks or Escape, Nova injects inline CSS overrides:
  ```css
  element.style.setProperty('display', 'none', 'important');
  ```
* **Audit Tagging:** All modified elements are recorded in the structured response as `aggressive_overlay_hide` actions.
* **Best Suited For:** Aggressive marketing popups, dead overlay backdrops, and uncooperative cookie walls.

---

## 6. Synthetic Escape Key Injection (`pressEscape`)

Many modern web dialog libraries (Bootstrap, Tailwind UI, Material UI, React Modal) bind keyboard event listeners to the `Escape` key (`keyCode: 27`, `key: "Escape"`).

When enabled (`pressEscape: true`, default in conservative mode), Nova dispatches a full synthetic keyboard sequence targeting the active element or document root:

```javascript
// Synthetic Escape event dispatch sequence
const target = document.activeElement || document.body;
target.dispatchEvent(new KeyboardEvent('keydown', {
    key: 'Escape',
    code: 'Escape',
    keyCode: 27,
    which: 27,
    bubbles: true,
    cancelable: true
}));
target.dispatchEvent(new KeyboardEvent('keyup', {
    key: 'Escape',
    code: 'Escape',
    keyCode: 27,
    which: 27,
    bubbles: true,
    cancelable: true
}));
```

If the dialog dismisses in response to the Escape sequence, the engine registers `escape_pressed` and verifies that pointer events are restored.

---

## 7. Automated Scroll-Lock Recovery

A common failure mode of web modal dismissal is the **orphaned scroll lock**:

1. When a modal opens, frameworks frequently lock scrolling by modifying the root document styles:
   ```css
   body, html {
     overflow: hidden !important;
     position: fixed !important;
     width: 100%;
   }
   ```
2. If the overlay is dismissed via Escape or removed via aggressive `display: none`, the framework's cleanup routine may not fire, leaving the document frozen in place.
3. The agent is left unable to scroll the page using `nova.scroll_smart` or `nova.scroll_by`.

Nova's remediation engine detects this orphaned state automatically. In aggressive mode or when backdrop elements are cleared, Nova evaluates the computed styles of `document.body` and `document.documentElement`:

```javascript
// Automated scroll-lock restoration executed by Nova
if (window.getComputedStyle(document.body).overflow === 'hidden') {
    document.body.style.setProperty('overflow', 'auto', 'important');
}
if (window.getComputedStyle(document.documentElement).overflow === 'hidden') {
    document.documentElement.style.setProperty('overflow', 'auto', 'important');
}
if (document.body.style.position === 'fixed') {
    document.body.style.removeProperty('position');
}
```

This guarantees that following a blocker pass, vertical and horizontal scrolling functions normally.

---

## Related Documentation

* [Domain Hub: Blocker & Overlay Remediation](../README.md)
* [Subguide: Guarded Click & Blocker Integration](../guarded-click-integration/README.md)
* [Domain Hub: CMP Vendor API Engine](../../cmp-engine/README.md)
* [Domain Hub: 3-Stage Hijack & Dark Pattern Defense](../../hijack-protection/README.md)
* [Tool Reference: `nova.dismiss_blockers`](../../../../mcp-reference/tools/guarded-actions/nova-dismiss-blockers.md)
