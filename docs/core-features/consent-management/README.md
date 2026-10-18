# Consent Management & Blocker Clearance

> [!IMPORTANT]
> Autonomous agents navigating the modern web face a constant obstacle: cookie consent banners, Consent Management Platform (CMP) dialogs, newsletter popups, and translucent click-intercepting backdrops. Naive UI-clicking frequently falls victim to dark patterns, cross-origin iframe boundaries, and hijacked buttons. Nova AI Workspace solves this with a **two-tier architecture**: programmatic vendor API dispatch via `nova.cmp_apply` backed by ground-truth state verification, and intelligent heuristic remediation via `nova.dismiss_blockers`.

---

## 1. Overview & Architectural Philosophy

When an autonomous agent interacts with a web page, modal banners and cookie walls introduce three critical failure modes:

1. **Click Hijacking & Dark Patterns:** Websites deliberately disguise acceptance buttons, use deceptive phrasing (such as *"Reject only essential cookies and continue"*), or style the *"Accept All"* button with high visual contrast while hiding *"Reject All"* inside nested accordions.
2. **Cross-Origin Iframe Boundaries:** Enterprise CMPs frequently render their UI inside third-party iframes (such as Sourcepoint TCF v2). Standard DOM queries executed in the top frame fail to reach these elements, while unconstrained cross-frame clicking introduces security and injection risks.
3. **State Mutation vs. Visual Dismissal:** Closing a modal visually (via DOM deletion or CSS hiding) does not register a legal consent choice. Many websites halt script loading or withhold core page functionality until a valid consent signal is emitted through the vendor's JavaScript runtime API.

Nova's architecture decouples **privacy policy application** from **visual DOM remediation**:

```mermaid
flowchart TD
    Start["Page Navigation / Modal Encountered"] --> Detect{"Recognized CMP Vendor API?"}

    subgraph Tier1["Tier 1: Programmatic CMP Engine (nova.cmp_apply)"]
        Detect -- "Yes (OneTrust, Sourcepoint, Cookiebot)" --> ReadPre["Read Pre-State ConsentStateVector"]
        ReadPre --> CheckPolicy{"Intent Mode?"}
        CheckPolicy -- "RejectOptional (Default)" --> DispatchAPI["Execute Vendor Runtime API\n(e.g. OneTrust.RejectAll, __tcfapi)"]
        CheckPolicy -- "AcceptAll" --> GateBlock["Reject with -32035\n(Autonomous Accept Blocked)"]
        DispatchAPI --> Settle["Settle Debounce (50ms)"]
        Settle --> ReadPost["Read Post-State ConsentStateVector"]
        ReadPost --> Verify{"State Mutated & Verified?"}
        Verify -- "Yes" --> CheckHidden{"Banner Visually Hidden?"}
        CheckHidden -- "Yes" --> DoneSuccess["Consent Applied & Cleared"]
        CheckHidden -- "No" --> FallbackDismiss["Pass to Blocker Dismissal"]
    end

    subgraph Tier2["Tier 2: Heuristic Blocker Remediation (nova.dismiss_blockers)"]
        Detect -- "No (Unknown / Custom / Overlay)" --> BlockerScan["Scan DOM for Dialogs & Overlays\n(role=dialog, aria-modal, fixed backdrops)"]
        Verify -- "Failed" --> BlockerScan
        FallbackDismiss --> BlockerScan
        BlockerScan --> HijackPreCheck["Run 3-Stage Hijack Protection\n(Polarity Scorer & Sibling Contrast)"]
        HijackPreCheck --> AutoClick{"Safe Reject Action Found?"}
        AutoClick -- "Yes (Conservative Mode)" --> ClickBtn["Click Verified Reject Button"]
        AutoClick -- "No / Ambiguous" --> EscCheck{"Aggressive Mode?"}
        EscCheck -- "Yes" --> HideOverlay["Hide Overlay Roots (display: none)\n+ Unlock Body Scroll (overflow: auto)"]
        EscCheck -- "No" --> EscKey["Dispatch Keyboard Escape"]
        ClickBtn --> SettlePass["Evaluate Residual Blockers"]
        HideOverlay --> SettlePass
        EscKey --> SettlePass
        SettlePass --> RemediationDone["Interaction Restored"]
    end
```

---

## 2. The Two-Tier Clearance Model

Nova divides consent and overlay handling into two distinct MCP tools, each designed for a specific layer of the browser stack:

| Dimension | Tier 1: Programmatic CMP Engine | Tier 2: Heuristic Blocker Remediation |
| :--- | :--- | :--- |
| **Primary MCP Tool** | [`nova.cmp_apply`](../../mcp-reference/tools/guarded-actions/nova-cmp-apply.md) | [`nova.dismiss_blockers`](../../mcp-reference/tools/guarded-actions/nova-dismiss-blockers.md) |
| **Execution Layer** | Vendor JavaScript runtime APIs (`window.OneTrust`, `__tcfapi`, `window.Cookiebot`) | DOM tree traversal, CSS styling overrides, synthetic click/key dispatch |
| **Vendor Scope** | Standardized Enterprise CMPs (OneTrust, Sourcepoint / TCF v2, Cookiebot) | Universal: custom cookie walls, newsletter modals, age gates, backdrops |
| **Ground-Truth Verification** | Yes: captures cryptographic TC strings, vendor group states, and purpose flags | Visual & structural: checks whether elements still intercept pointer events |
| **Dark Pattern Resilience** | Complete: bypasses DOM UI entirely via direct runtime method calls | Algorithmic: 3-stage polarity scoring and sibling contrast classification |
| **DOM Side Effects** | Zero DOM mutation: vendor scripts manage their own banner teardown | Controlled DOM mutation: element removal, `display: none`, scroll restoration |

---

## 3. Comprehensive Documentation Index

The Consent Management & Blocker Clearance architecture is organized into three specialized domain areas and six deep-dive architecture subguides:

```
consent-management/
├── README.md                                                       # Master Architectural Hub
├── cmp-engine/                                                     # Domain 1: Programmatic CMP Engine Hub
│   ├── README.md
│   ├── execution-pipeline-and-adapters/
│   │   └── README.md                                               # 8-step pipeline, adapter priorities, protocols
│   └── consent-state-and-safety-gates/
│       └── README.md                                               # ConsentStateVector, anti-spoofing, AcceptAll gate
├── hijack-protection/                                              # Domain 2: Hijack & Dark Pattern Defense Hub
│   ├── README.md
│   ├── polarity-scoring-and-contrast/
│   │   └── README.md                                               # Polarity margin >= 0.40, cluster classifications
│   └── cross-origin-and-privilege-boundaries/
│       └── README.md                                               # Iframe boundaries, host-only matching, policy gates
└── blocker-dismissal/                                              # Domain 3: Blocker & Overlay Remediation Hub
    ├── README.md
    ├── heuristic-detection-and-remediation/
    │   └── README.md                                               # Multi-pass scanner, conservative vs aggressive, scroll unlock
    └── guarded-click-integration/
        └── README.md                                               # autoDismissBlockers hit-testing and in-flight healing
```

### Complete Subsystem Guide Index

| Domain Area | Specialized Architecture Guide | Key Focus Areas & Technical Invariants |
| :--- | :--- | :--- |
| **Programmatic CMP Engine**<br>([Domain Hub](cmp-engine/README.md)) | **[Execution Pipeline & Vendor Adapters](cmp-engine/execution-pipeline-and-adapters/README.md)** | The 8-stage execution pipeline, ordered adapter detection priority (Sourcepoint $\rightarrow$ Cookiebot $\rightarrow$ OneTrust), runtime protocols, cryptographic TC string hashing, and event bus listener guards. |
| | **[Consent State & Safety Gates](cmp-engine/consent-state-and-safety-gates/README.md)** | Ground-truth verification via `ConsentStateVector`, anti-spoofing data provenance (`OneTrust.GetDomainData().Groups`), strongly-typed `ConsentIntent`, autonomous `AcceptAll` barrier (-32035), user choice preservation, and visual hidden probing. |
| **Hijack & Dark Pattern Defense**<br>([Domain Hub](hijack-protection/README.md)) | **[Polarity Scoring & Contrast](hijack-protection/polarity-scoring-and-contrast/README.md)** | The consent hijack threat model, 3-stage validation cascade, `CmpPolarityScorer` (8 sub-scores in 5 languages), polarity margin $\ge 0.40$, scope threshold $\ge 0.50$, and `CmpSiblingContrastClassifier` cluster taxonomy (`TcfThreeButton`, `RejectAcceptPair`, `SingleButton`, `AmbiguousTwoButton`). |
| | **[Cross-Origin & Privilege Boundaries](hijack-protection/cross-origin-and-privilege-boundaries/README.md)** | Third-party iframe isolation (Sourcepoint, Didomi), `PrivilegedCrossOriginCmpInteractionEnabled` policy gate, strict `Uri.Host` matching against substring exploits, symmetric frame routing, and persistent security audit trails. |
| **Blocker & Overlay Remediation**<br>([Domain Hub](blocker-dismissal/README.md)) | **[Heuristic Detection & Remediation](blocker-dismissal/heuristic-detection-and-remediation/README.md)** | Multi-pass remediation pipeline (maxPasses 1–5), structural scan hierarchy (semantic, lexical, geometric), conservative vs. aggressive modes, synthetic Escape key injection, and automated `overflow: hidden` body scroll restoration. |
| | **[Guarded Click Integration](blocker-dismissal/guarded-click-integration/README.md)** | In-flight self-healing via `autoDismissBlockers: true`, coordinate hit-testing mechanics (`elementFromPoint`), interception detection, automatic conservative remediation passes, and structured response transparency. |

---

## 4. Operational Decision Matrix for Agents

When designing autonomous browser navigation workflows, agents should follow this deterministic sequence:

1. **Step 1: Check for Known CMP via `nova.cmp_apply`**
   ```json
   {
     "targetId": "tab-101",
     "mode": "auto",
     "intent": { "mode": "RejectOptional" }
   }
   ```
   * If `status: "ok"` and `verified: true`: The consent policy is legally registered in the vendor's engine. If `bannerVisuallyHidden: true`, proceed immediately to browsing.
   * If `status: "ok"` but `bannerVisuallyHidden: false`: The consent state was updated, but the banner DOM remains rendered. Call `nova.dismiss_blockers` to clean up the residual UI.
2. **Step 2: Fall Back on `failureCode: "no_adapter"`**
   If `nova.cmp_apply` returns `failureCode: "no_adapter"`, the website uses a custom or unsupported consent mechanism. Immediately escalate to:
   ```json
   {
     "targetId": "tab-101",
     "mode": "conservative"
   }
   ```
3. **Step 3: Escalate to Aggressive Mode if Pointer Events Remain Intercepted**
   If `blocked: true` persists after conservative dismissal (often caused by stubborn backdrops or newsletter overlays):
   ```json
   {
     "targetId": "tab-101",
     "mode": "aggressive",
     "maxPasses": 3
   }
   ```
4. **Step 4: Leverage Guarded Click Automation**
   For standard interactions, manual blocker clearance is rarely necessary. Passing `autoDismissBlockers: true` to [`nova.click_selector`](../../mcp-reference/tools/browser-automation/nova-click-selector.md) enables automatic on-demand blocker dismissal whenever a backdrop intercepts a click.

---

## Related Documentation

* [Programmatic CMP Engine Architecture](cmp-engine/README.md)
* [3-Stage Hijack & Dark Pattern Defense](hijack-protection/README.md)
* [Blocker & Overlay Remediation](blocker-dismissal/README.md)
* [Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md)
* [Closed-Loop System (CLS)](../closed-loop-system-cls/README.md)
* [Tool Catalog: Guarded Actions & Blocker Clearance](../../mcp-reference/tools/guarded-actions/README.md)
