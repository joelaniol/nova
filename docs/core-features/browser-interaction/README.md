# Browser Interaction Architecture

> "Dispatching an event is trivial; ensuring the browser accepted it, the DOM updated, and the application state transitioned is where autonomy begins."
>
> — Nova Interaction Philosophy

> [!NOTE]
> Nova AI Workspace (`NovaAIWorkspace.exe`) provides an enterprise-grade browser interaction pipeline designed for autonomous Model Context Protocol (MCP) agents operating in modern, dynamic web applications. Rather than relying on naive JavaScript injections like `element.click()`, Nova delivers physical input directly through the browser engine's DevTools protocol (`isTrusted: true`), automatically restores throttled presentation surfaces, navigates open Shadow DOM trees, handles complex drag-and-drop dynamics, and executes composite guarded macros backed by closed-loop verification contracts.

---

## 1. High-Level Architecture & Interaction Pipeline

The browser interaction subsystem bridges the gap between high-level agent intentions and low-level physical rendering. It decouples target element resolution, window surface maintenance, physical input delivery, and post-action verification into an integrated pipeline:

```mermaid
flowchart TD
    subgraph AgentLayer["Agent Execution & Planning"]
        AgentIntent["Agent Action Intent\n(Click, Type, Drag, Select, Send Message)"]
        TargetSpec["Target Specification\n(CSS Selector, Exact Coordinates, Perceptual CTA Ref)"]
    end

    subgraph SurfaceGate["Surface & Window Pre-Checks"]
        MinCheck["Window Minimization Check\n(Restore window via SW_RESTORE if minimized)"]
        SurfaceRepair["Presentation Surface Repair\n(Synchronize unrendered background viewports)"]
        BlockerCheck["Modal & Blocker Detection\n(Auto-dismiss cookie banners & blocking overlays)"]
    end

    subgraph ResolutionLayer["Target Resolution Engine"]
        ShadowPiercer["Shadow DOM Piercing\n(Iterative ' >>> ' Traversal across open shadow roots)"]
        FrameResolver["Iframe Scope Resolver\n(Resolves target within same-origin frameId)"]
        OpacityFilter["Cumulative Opacity Calculator\n(Multiplicative product of all ancestor hosts)"]
        GeometryCalc["Visible Geometry Calculator\n(Scroll into view, clip rects against viewport)"]
    end

    subgraph DispatchPipeline["Input Dispatch Pipeline"]
        CDPDispatch["Physical DevTools Dispatch\n(Input.dispatchMouseEvent, dispatchKeyEvent)\nisTrusted: true"]
        ChunkedTyping["Chunked Typing Engine\n(Paced typing with render pauses for rich-text editors)"]
        HumanizedDrag["Synthetic Humanized Drag\n(Bézier curves, vertical jitter, overshoot & correction)"]
        HTML5Polyfill["HTML5 Drag & Drop Polyfill\n(Bridges mouse moves to DataTransfer event cascade)"]
    end

    subgraph PostActionGate["Post-Action Safety & Contracts"]
        SafetyScans["Safety Audits\n- Identity Overlay Detector\n- Destructive Context Menu Scan"]
        LoopGuard["Loop Guard Barrier\n(Detects identical action churn: loop.blocked_same_action)"]
        CLSContract["Closed-Loop System (CLS)\nTransition Contract Verification (pre & postconditions)"]
        EVMVisual["Visual Evidence Capture\n(Embedded post-action screenshot & DOM telemetry)"]
    end

    AgentIntent --> TargetSpec
    TargetSpec --> SurfaceGate
    SurfaceGate --> MinCheck --> SurfaceRepair --> BlockerCheck
    BlockerCheck --> ResolutionLayer

    ResolutionLayer --> ShadowPiercer --> FrameResolver --> OpacityFilter --> GeometryCalc
    GeometryCalc --> DispatchPipeline

    DispatchPipeline --> CDPDispatch
    DispatchPipeline --> ChunkedTyping
    DispatchPipeline --> HumanizedDrag
    DispatchPipeline --> HTML5Polyfill

    DispatchPipeline --> PostActionGate
    PostActionGate --> SafetyScans
    PostActionGate --> LoopGuard
    PostActionGate --> CLSContract
    PostActionGate --> EVMVisual
```

---

## 2. The Three-Tier Interaction Hierarchy

Nova provides three distinct interaction tiers tailored to varying levels of UI complexity and safety requirements:

```mermaid
graph TD
    Decision{"What kind of interaction\nis required?"}

    Decision -->|Exact Viewport Positions| LowLevel["Tier 1: Coordinate-Based Dispatch\n- Exact Viewport Positions (x, y)\n- Physical Hardware Events (isTrusted: true)\n- Zero DOM dependencies\n(nova.input_click, input_move, input_wheel, input_text)"]

    Decision -->|Semantic Element Targeting| ElementLevel["Tier 2: Selector-Based Actions\n- Open Shadow DOM Piercing ( >>> )\n- Ancestor Opacity & Visibility Filtering\n- Chunked Typing with Read-Back\n- Native & Custom Dropdown Selection\n(nova.click_selector, type_selector, choose_option)"]

    Decision -->|Composite / High-Risk Mutation| GuardedLevel["Tier 3: Guarded Action Macros\n- Atomic Multi-Step Workflows\n- Chat Composer Auto-Discovery & Pairing\n- Tolerates Initially Disabled Buttons\n- Enter-Key Send Fallback\n- Built-in Transition Contracts\n(nova.guarded_send_message, guarded_submit_form, guarded_login)"]
```

### Tier 1: Coordinate-Based Low-Level Dispatch

Operates directly on viewport pixel coordinates $(x, y)$ without querying the Document Object Model:
- **Primary Use Cases:** HTML5 Canvas applications, interactive WebGL viewports, mapping interfaces, custom visual controls, and perceptual Call-To-Action handles (`ctaRef` from `nova.perceive`).
- **Characteristics:** Dispatches physical Chromium DevTools Protocol (CDP) packets. Events arrive with `isTrusted: true`.
- **Operational Trade-Off:** Bypasses DOM mutation observers and layout queries, but requires coordinates adjusted for current scroll offsets and device scale factors.

### Tier 2: Element-Based Semantic Actions

Dynamically queries and resolves DOM targets using standard CSS selectors or Shadow DOM piercing expressions:
- **Primary Use Cases:** Standard web applications, forms, navigation menus, Web Components, and responsive Single Page Applications (SPAs).
- **Characteristics:** Automatically scrolls target elements into view, computes visible bounding boxes clipped by parent overflow containers, checks cumulative ancestor opacity, and handles rich-text editor inputs with chunked typing and read-back verification.

### Tier 3: Guarded Action Macros

High-level composite actions that encapsulate discovery, input, verification, and commit execution into an atomic operation:
- **Primary Use Cases:** Conversational AI interfaces (ChatGPT, Claude.ai, Gemini, Slack), login surfaces, form submissions, and model switching.
- **Characteristics:** Eliminates script race conditions. Automatically discovers paired submit controls, tolerates initially disabled buttons, provides Enter-key fallback on icon-only buttons, and attaches [Closed-Loop System (CLS)](../closed-loop-system-cls/README.md) transition contracts.

---

## 3. Window State & Presentation Surface Protection

Browser automation frequently fails because the host operating system throttles background or minimized windows. Nova implements strict host-level surface repair mechanisms prior to every input dispatch:

```mermaid
sequenceDiagram
    autonumber
    actor Agent as Autonomous Agent
    participant Nova as Nova Input Manager
    participant WinUI as WinUI 3 Window Host
    participant Core as WebView2 Runtime Engine
    participant Page as Web Page DOM

    Agent->>Nova: nova.input_click(x=450, y=320)
    Nova->>WinUI: Query Window State (IsIconic Check)
    alt Window is Minimized
        WinUI->>WinUI: Restore Window (ShowWindow SW_RESTORE)
        Note over WinUI,Core: Minimization suspends Chromium frame rendering loops!
    end

    Nova->>Core: Inspect Viewport Presentation Surface
    alt Target Tab is Inactive / Viewport Deferred
        Nova->>Core: Presentation Surface Repair Transaction
        Core-->>Nova: Geometry Synchronized & Layout Refreshed
    end

    Nova->>Core: Input.dispatchMouseEvent (move -> press -> 16ms delay -> release)
    Core->>Page: Physical Event Delivered (event.isTrusted === true)
    Nova-->>Agent: Action Outcome & Diagnostics
```

### 1. Automatic Minimization Restoration

When a browser window is minimized to the taskbar, Chromium activates aggressive power-saving optimizations:
- Frame rendering loops (`requestAnimationFrame`) are paused.
- JavaScript timers are throttled to 1-second intervals or suspended entirely.
- Pointer event dispatch can be dropped or desynchronized from the true DOM layout.

Before dispatching any pointer or keyboard input, Nova inspects the window handle. If minimized, Nova restores the window (`SW_RESTORE`) to guarantee that layout geometry and rendering loops are fully active before coordinates are evaluated.

### 2. Presentation Surface Repair

When interacting with background tabs or inactive sandboxes whose visual presentation was deferred, the target viewport may not have computed its latest layout geometry. Nova initiates a presentation surface repair transaction that forces Chromium to compute layout geometry, update CSS transforms, and synchronize viewport metrics before mouse coordinates are resolved.

### 3. Modal & Cookie Blocker Dismissal

When interacting with web pages, popups, cookie consent notices, and promotional dialogs frequently obscure the target element. All high-level interaction tools support `autoDismissBlockers: true`, which automatically detects dismissible overlays, clicks their dismissal button, and retries target resolution seamlessly.

---

## 4. Post-Action Safety Scans & Loop Guard

Every interactive dispatch undergoes automated post-action auditing to safeguard the user against deceptive websites and automation lockups:

```mermaid
flowchart LR
    Action["Input Action Dispatched"] --> Audit{"Safety Audits Evaluated"}
    Audit --> S1["Identity Overlay Detector\n(Detects newly spawned phishing overlays)"]
    Audit --> S2["Destructive Context Menu Scan\n(Audits right-clicks for account deletion triggers)"]
    Audit --> S3["Loop Guard Barrier\n(Detects identical action churn: loop.blocked_same_action)"]
```

1. **Identity Overlay Detector:**
   Following an input action or form submission, Nova inspects newly appeared DOM elements to verify whether an overlay attempts to mimic a native operating system login dialog, corporate Single Sign-On prompt, or credential capture form.
2. **Destructive Context Menu Scan:**
   Right-click actions (`button="right"`) undergo an automated inspection of the resulting context menu. If the menu exposes destructive actions (e.g., account deletion, data purge, token revocation), Nova includes explicit warnings in the tool outcome.
3. **Loop Guard Barrier (`loop.blocked_same_action`):**
   If an agent repeatedly executes the exact same failing action at the same URL (e.g., clicking a disabled button in an infinite loop), Nova's loop guard halts execution, prevents further click dispatch, and provides actionable remediation guidance.

---

## 5. Verification & Outcome Guarantees

> [!IMPORTANT]
> **Dispatch $\neq$ Acceptance:**
> Successful delivery of a mouse click or keystroke confirms only that the browser engine accepted the physical input. It **does not prove** that the web application processed the request, that a backend server acknowledged the transaction, or that the application state changed.

To establish true execution certainty, agents must combine browser interaction with Nova's verification subsystems:

1. **[Closed-Loop System (CLS) Transition Contracts](../closed-loop-system-cls/README.md):**
   Declare explicit preconditions and postconditions (e.g., asserting that `page.url` changes, or that `@css=div.alert-success` becomes visible).
2. **[Evidence Verification Mode (EVM)](../../research/evidence-verification-mode-evm/README.md):**
   Request `includeScreenshot: true` on pointer actions to capture visual proof of state transitions.
3. **[Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md):**
   Preemptive gates that prevent blind mutations when tabs or accounts are ambiguous.

---

## 6. Comprehensive Documentation Index

The browser interaction subsystem is organized into three specialized architectural areas and six deep-dive technical guides:

```
public/docs/core-features/browser-interaction/
├── README.md                                         # This master hub
├── drag-and-drop/
│   ├── README.md                                     # Drag & drop architecture & polyfill hub
│   ├── physical-and-humanized-drag/
│   │   └── README.md                                 # Physical CDP drag vs humanized Bézier drag, jitter, overshoot
│   └── webview2-html5-polyfill/
│       └── README.md                                 # WinUI 3 WebView2 limitation, __novaDragPolyfillBegin handover, CultureInfo
├── input-dispatch/
│   ├── README.md                                     # Low-level input dispatch hub
│   ├── pointer-and-keyboard-pipelines/
│   │   └── README.md                                 # Physical pointer sequence, ~16ms delays, chunked typing, Monaco/CodeMirror adapters
│   └── advanced-scrolling-mechanisms/
│       └── README.md                                 # Smart scrolling container auto-detection, saturation signals, rebound recovery
└── selectors-and-shadow-dom/
    ├── README.md                                     # Selectors, shadow DOM & custom components hub
    ├── shadow-dom-and-ancestor-opacity/
    │   └── README.md                                 # Shadow DOM >>> combinator, cumulative ancestor opacity product, clipping
    └── dropdowns-and-component-selection/
        └── README.md                                 # Native select vs custom ARIA comboboxes, nova.choose_option, safety audits
```

| Area | Architecture Guide | Scope & Key Concepts | Primary Components |
| :--- | :--- | :--- | :--- |
| **Drag & Drop** | **[Drag & Drop Architecture Hub](drag-and-drop/README.md)** | Architectural role, the modern drag-and-drop divide, execution pipelines, and polyfill overview. | `nova.input_drag`<br>`nova.input_drag_humanized`<br>`HTML5Polyfill` |
| | **[Physical vs. Humanized Drag](drag-and-drop/physical-and-humanized-drag/README.md)** | Comparison of physical hardware events (`isTrusted: true`) vs synthetic humanized profiles (`mode: "humanized_js"`), cubic Bézier easing curves, perpendicular physiological jitter ($\pm 2$ px), deliberate overshoot ($3$–$8$ px) with pullback corrections, and post-drag outcome verification via `nova.wait_for_eval`. | `nova.input_drag`<br>`nova.input_drag_humanized`<br>`BézierEasing`<br>`isTrusted: true` |
| | **[WinUI 3 WebView2 HTML5 Polyfill](drag-and-drop/webview2-html5-polyfill/README.md)** | Addressing the WebView2 limitation where CDP mouse events fail to trigger native OS drag sessions on `draggable="true"` elements, deterministic script handover (`window.__novaDragPolyfillBegin`), culture-invariant floating-point serialization (`CultureInfo.InvariantCulture`), and simulated `DataTransfer` object cascade. | `__novaDragPolyfillBegin`<br>`NovaDataTransfer`<br>`CultureInfo.InvariantCulture`<br>`draggable="true"` |
| **Input Dispatch** | **[Low-Level Input Dispatch Hub](input-dispatch/README.md)** | Event trust comparison, CDP pipeline overview, hardware frame timing, and code editor adapters overview. | `McpServer.InputInteractionHandlers`<br>`isTrusted: true`<br>`Input.dispatchMouseEvent` |
| | **[Pointer & Keyboard Pipelines](input-dispatch/pointer-and-keyboard-pipelines/README.md)** | Physical DevTools pointer dispatch (`isTrusted: true`), calibrated ~16 ms hardware frame delays, click count semantics (single, double, triple), window minimization restoration (`SW_RESTORE`), chunked typing with paced micro-delays for rich-text editors, Monaco and CodeMirror model adapters, and strict modifier depression/release ordering. | `nova.input_click`<br>`nova.type_selector`<br>`nova.input_shortcut`<br>`MonacoModelAdapter`<br>`CodeMirrorModelAdapter` |
| | **[Advanced Scrolling Mechanisms](input-dispatch/advanced-scrolling-mechanisms/README.md)** | Why window-level scrolling fails in modern component architectures, smart scrolling container auto-detection and scoring (`nova.scroll_smart`), feed saturation signal diagnostics, stalled-loader rebound recovery for infinite feeds, route container caching, relative scrolling (`nova.scroll_by`), and physical coordinate wheel events (`nova.input_wheel`). | `nova.scroll_smart`<br>`nova.scroll_by`<br>`nova.scroll_element`<br>`nova.input_wheel`<br>`ReboundManeuver` |
| **Selectors & DOM** | **[Selectors & Shadow DOM Hub](selectors-and-shadow-dom/README.md)** | Selector resolution pipeline, open shadow roots, cumulative ancestor opacity, and custom dropdown selection overview. | `ShadowCombinator`<br>`nova.click_selector`<br>`nova.choose_option` |
| | **[Shadow DOM & Ancestor Opacity](selectors-and-shadow-dom/shadow-dom-and-ancestor-opacity/README.md)** | Piercing open Shadow DOM boundaries via ` >>> `, iframe query scoping (`frameId`), multiplicative cumulative ancestor opacity calculations, exceptions for invisible click/upload overlays (`opacity: 0`), and visible bounding box viewport clipping. | `ShadowCombinator`<br>`CumulativeOpacityEvaluator`<br>`IframeScopeResolver`<br>`nova.click_selector` |
| | **[Dropdowns & Custom Component Selection](selectors-and-shadow-dom/dropdowns-and-component-selection/README.md)** | Comparison of native `<select>` elements (`nova.select_option`) vs custom ARIA comboboxes (`nova.choose_option`), matching options by visible label, substring, or index, autonomous popover menu opening/closing verification, and post-action safety audits (Identity Overlay, Loop Guard). | `nova.choose_option`<br>`nova.select_option`<br>`IdentityOverlayDetector`<br>`LoopGuard` |

---

## 7. Related Documentation

- [Closed-Loop System (CLS)](../closed-loop-system-cls/README.md) — Precondition and postcondition transition contracts.
- [Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md) — Preemptive action safety and policy validation.
- [Auth Surface Detection (ASD)](../auth-surface-detection-asd/README.md) — Login surface recognition and authentication progression.
- [Evidence Verification Mode (EVM)](../../research/evidence-verification-mode-evm/README.md) — Visual evidence verification and screenshot comparisons.
- [Browser Automation Tools Catalog](../../mcp-reference/tools/browser-automation/README.md) — Complete MCP tool schemas and parameter reference.

[All core features](../README.md)
