# Selectors, Shadow DOM & Guarded Actions

> "A selector that breaks on the first Web Component boundary is useless in modern web applications; resilient automation requires crossing shadow trees and validating state transitions atomically."
>
> — Autonomous Web Automation Guidelines

> [!NOTE]
> Web applications increasingly encapsulate user interfaces inside Web Components, open Shadow DOM boundaries, iframes, and dynamic ARIA component frameworks. Standard DOM queries like `document.querySelector()` cannot penetrate Shadow DOM trees or manipulate custom dropdown menus. Nova provides a robust selector resolution engine capable of piercing open shadow roots via the ` >>> ` combinator, calculating cumulative ancestor opacity, manipulating both native and custom dropdowns, and executing composite **Guarded Action Macros** backed by closed-loop verification contracts.

---

## 1. High-Level Selector & Guarded Actions Pipeline

Nova's selector resolution pipeline decouples element query syntax from physical execution:

```mermaid
flowchart TD
    subgraph SelectorEngine["Selector Resolution Pipeline"]
        InputSelector["Selector Query\n(e.g., app-shell >>> user-card >>> button.submit)"]
        ShadowWalker["Shadow DOM Piercing Engine\n(Iterative ' >>> ' Traversal across element.shadowRoot)"]
        FrameScope["Iframe Scope Resolver\n(Scopes queries to same-origin frameId)"]
        OpacityCalc["Cumulative Opacity Evaluator\n(Multiplicative product of all ancestor hosts)"]
        VisibilityRect["Visibility & Bounding Box Calculator\n(Scroll into view, clip rects against viewport)"]
    end

    subgraph ActionsLayer["Target-Based Action Execution"]
        ClickAction["Physical Click\n(nova.click_selector)"]
        TypeAction["Chunked Typing\n(nova.type_selector)"]
        SelectAction["Dropdown Selection\n- Native: nova.select_option\n- Custom: nova.choose_option"]
        GuardedMacro["Guarded Action Macros\n(send_message, submit_form, login, switch_model)"]
    end

    subgraph SafetyGate["Post-Action Safety & Contracts"]
        IdentityCheck["Identity Overlay Detector\n(Detects sprouted phishing overlays)"]
        MenuCheck["Destructive Context Menu Scan\n(Audits right-click menu triggers)"]
        LoopCheck["Loop Guard Barrier\n(Detects loop.blocked_same_action)"]
        CLSContracts["Closed-Loop System (CLS)\nPre- & Post-Condition Transition Contracts"]
    end

    InputSelector --> ShadowWalker --> FrameScope --> OpacityCalc --> VisibilityRect
    VisibilityRect --> ClickAction
    VisibilityRect --> TypeAction
    VisibilityRect --> SelectAction
    VisibilityRect --> GuardedMacro

    ClickAction --> SafetyGate
    TypeAction --> SafetyGate
    GuardedMacro --> SafetyGate
    SafetyGate --> IdentityCheck
    SafetyGate --> MenuCheck
    SafetyGate --> LoopCheck
    SafetyGate --> CLSContracts
```

---

## 2. Shadow DOM Piercing Engine (` >>> `)

The Shadow DOM specification encapsulates a component's internal markup and styles from the outer document. Standard CSS selectors cannot cross a shadow boundary.

Nova extends standard CSS selectors with the **` >>> ` piercing combinator**. Each segment separated by ` >>> ` is an independent CSS selector; each ` >>> ` transitions from the matched element into its open shadow root:

```css
/* Piercing two levels of nested Web Components to click a save button */
app-modal-dialog >>> user-profile-card >>> button.save-changes
```

```mermaid
sequenceDiagram
    autonumber
    actor Agent as Autonomous Agent
    participant Nova as Nova Selector Resolver
    participant Host1 as <app-modal-dialog> (Host 1)
    participant Shadow1 as Host 1 shadowRoot
    participant Host2 as <user-profile-card> (Host 2)
    participant Shadow2 as Host 2 shadowRoot
    participant Button as <button.save-changes>

    Agent->>Nova: nova.click_selector("app-modal-dialog >>> user-profile-card >>> button.save-changes")
    Nova->>Host1: document.querySelector("app-modal-dialog")
    Nova->>Shadow1: Host1.shadowRoot.querySelector("user-profile-card")
    Nova->>Shadow2: Host2.shadowRoot.querySelector("button.save-changes")
    Shadow2-->>Nova: Matched DOM Element
    Nova->>Button: Scroll into view, compute geometry, dispatch physical click
    Nova-->>Agent: Action Outcome & Diagnostics
```

### Traversal Invariants & Geometry Calculations

1. **Open Shadow Roots Only:**
   Traversal follows `element.shadowRoot`. Because browser engines expose this property only for open shadow roots, closed shadow roots cannot be crossed via CSS selectors. For elements encapsulated in closed shadow roots, agents should use perceptual Call-To-Action handles (`ctaRef` from `nova.perceive`) or coordinate-based input.
2. **Cumulative Ancestor Opacity:**
   An element's effective visual opacity depends on its entire ancestor hierarchy. Nova computes the multiplicative product of the target element's CSS `opacity` and all ancestor hosts across shadow boundaries:
   $$\text{Effective Opacity} = \text{Opacity}_{\text{target}} \times \prod_{i=1}^{n} \text{Opacity}_{\text{ancestor}_i}$$
   - **Click & Upload Exception:** Elements with an effective opacity of 0 (such as an invisible `<input type="file">` overlaid on top of a styled upload button) remain valid click and file upload targets.
   - **Screenshot Refusal:** Element-scoped screenshot captures of fully transparent elements are refused, as capturing them would show only the background layer behind them.
3. **Visible Bounding Rectangles & Viewport Clipping:**
   Before dispatching pointer actions, Nova automatically scrolls the target element into view, computes its visible bounding rectangle, and clips it against ancestor overflow containers (`overflow: hidden/auto/scroll`) and viewport boundaries.
4. **Iframe Scope Resolver:**
   Queries can be targeted directly within embedded frames by supplying a `frameId` parameter, scoping element resolution to the same-origin frame's document context.

---

## 3. Dropdown Selection: Native vs. Custom Components

Modern web frameworks implement dropdowns in two fundamentally different ways:

```mermaid
graph TD
    DropdownType{"What kind of dropdown\nis on the page?"}

    DropdownType -->|Native HTML <select>| NativeSelect["nova.select_option\n- Manipulates <select> by value attribute\n- Emulates change and input events\n- Matches technical value strings"]

    DropdownType -->|Custom UI Component\n(Radix, Headless UI, React Select, AntD)| CustomSelect["nova.choose_option\n- Matches by visible label, substring, or index\n- Auto-opens menu, scrolls item into view, selects\n- Verifies popover closure\n- Dual-compatible with native <select>"]
```

### 1. Native `<select>` Elements (`nova.select_option`)

Targets standard HTML `<select>` elements and chooses an `<option>` by its `value` attribute. It updates the DOM property and dispatches both `input` and `change` events so that framework two-way bindings update immediately.

### 2. Universal Custom Dropdowns (`nova.choose_option`)

Most enterprise web applications (React, Angular, Vue) replace native `<select>` tags with custom ARIA-based component libraries (such as Radix UI, Headless UI, React Select, Ant Design, Material-UI, or Tailwind Comboboxes). These components do not possess `<select>` tags or `value` attributes.

`nova.choose_option` provides universal dropdown interaction:
- **Identification:** Matches options by visible text, case-insensitive substring, or 0-based index.
- **Autonomous Interaction:** Automatically detects if the dropdown menu is closed, clicks the trigger element to open the list, scrolls the desired item into view, selects it, and verifies closure of the dropdown popover.
- **Dual Compatibility:** If given a native `<select>`, it seamlessly handles it by matching the visible option label rather than requiring technical value strings.

---

## 4. Guarded Action Macros

High-level composite actions that encapsulate discovery, input, verification, and commit execution into an atomic operation. Guarded macros eliminate script race conditions and prevent partial-action failures:

```mermaid
flowchart TD
    subgraph GuardedSend["nova.guarded_send_message Lifecycle"]
        DiscoverInput["1. Auto-Discover Composer Input\n(Finds chat input or contenteditable)"]
        TypeVerify["2. Chunked Typing + Read-Back\n(Ensures text persists without dropped chars)"]
        ResolveButton["3. Re-Resolve Send Button\n(Tolerates initially disabled buttons)"]
        CommitBranch{"Send Button Found?"}
        CommitBranch -- "Yes" --> CommitClick["4a. Single-Click Commit (Left Button)\n(Guarantees exactly one click event)"]
        CommitBranch -- "No (Icon-Only Button)" --> EnterSend["4b. Enter-Key Send Fallback\n(Re-types with clear=true & dispatches Enter)"]
        CommitClick & EnterSend --> VerifyState["5. Transition Contract Evaluation\n(Preconditions, Postconditions, sentTextAppeared)"]
    end

    DiscoverInput --> TypeVerify --> ResolveButton --> CommitBranch
```

### 1. Guarded Message Dispatch (`nova.guarded_send_message`)

Specifically optimized for generative AI and chat surfaces (ChatGPT, Claude.ai, Gemini, Slack, Discord):

- **Selectorless Auto-Discovery:** When `selector` and `ctaRef` are omitted, Nova automatically scans the document (or iframe) to identify the chat composer input field and its paired send button.
- **Tolerates Initially Disabled Send Buttons:** In modern chat interfaces, the send button is disabled (`aria-disabled="true"` or `disabled`) when the composer is empty. Nova's auto-discovery accounts for this: it discovers the disabled send button, types the message, verifies that the button becomes enabled, and then commits the click.
- **Single-Click Commit Invariant:** Disallows double-clicking or non-left buttons (`button='left'`, `clickCount=1`), preventing accidental duplicate message transmissions.
- **Enter-Key Send Fallback:** Many modern chat interfaces feature pure icon buttons without accessible names or identifiable classes (e.g., Lumo, UPDF AI, NoteGPT). When a send button cannot be paired after typing, Nova automatically falls back to submitting via the **Enter key**. It re-types the message with `clear=true` (guaranteeing that text is never doubled in the composer) and verifies submission via the transition contract.
- **Composer Text Probe Near Send:** Nova reads the composer's text immediately prior to commit, capturing the exact text payload to satisfy the `chat.sentTextAppeared` contract signal even on sites with dynamic or obfuscated markup.
- **Structured Failure Reason Codes:** If discovery fails, Nova returns structured diagnostic reason codes rather than generic errors:
  - `action.no_input_field_found`: No chat composer field was identified.
  - `action.no_send_button_found`: Composer input was found, but no send button could be paired with it.
  - `action.no_chat_surface_pair_found`: Elements found, but could not be definitively paired.
  - `action.ambiguous_input_field`: Multiple competing chat inputs found with equal confidence.

### 2. Guarded Form Submission (`nova.guarded_submit_form`)

Wraps form submission buttons with a built-in submit transition contract template. It verifies that required fields are valid before clicking and monitors for post-submit state transitions (e.g., modal closure, success alerts, or URL changes).

### 3. Guarded Authentication (`nova.guarded_login`)

Automates login form submission. Integrates directly with [Auth Surface Detection (ASD)](../../auth-surface-detection-asd/README.md) to detect whether login succeeded, failed due to bad credentials, or encountered a multi-factor authentication (MFA) challenge.

### 4. Guarded Model & Workspace Switching (`nova.guarded_switch_model`, `nova.guarded_switch_sandbox`)

Handles switching AI model selectors or active sandbox workspaces with automatic pre-condition checks and option selection verification.

### 5. Inspecting Composer State (`nova.composer_state`)

A non-mutating inspection tool that reports the exact state of the chat composer: active input text, placeholder strings, send button enabled status, and paired container identifiers.

---

## 5. Post-Action Safety Scans & Loop Guard

Every selector-based click is audited immediately post-dispatch:

```mermaid
flowchart LR
    Click["Click Dispatched"] --> Audits{"Safety Audits Evaluated"}
    Audits --> A1["Identity Overlay Detector\n(Detects sprouted phishing overlays)"]
    Audits --> A2["Destructive Context Menu Scan\n(Audits right-click menu triggers)"]
    Audits --> A3["Loop Guard Barrier\n(Halts repeated identical actions)"]
```

1. **Identity Overlay Detector:** Detects if a newly opened overlay mimics an external authentication provider or phishing prompt.
2. **Destructive Context Menu Scan:** If a right-click is dispatched, Nova scans the resulting context menu for dangerous triggers (e.g., delete, clear all, revoke tokens) and attaches explicit safety warnings.
3. **Loop Guard Barrier (`loop.blocked_same_action`):** Prevents automated scripts from executing identical failed actions repeatedly at the same URL, halting execution with actionable remediation guidance.

---

## 6. Complete Tool Reference for Selectors & Guarded Actions

All tools belong to the `browser_automation` and `guarded_actions` capability bundles:

| Tool | Core Parameters | Output / Diagnostics |
| :--- | :--- | :--- |
| [`nova.click_selector`](../../../mcp-reference/tools/browser-automation/nova-click-selector.md) | `selector`, `ctaRef`, `button`, `clickCount`, `autoDismissBlockers`, `verify` | Action outcome, effective selector, verified state, blocker dismissal status, overlay detection warnings |
| [`nova.type_selector`](../../../mcp-reference/tools/browser-automation/nova-type-selector.md) | `selector`, `text`, `clearFirst`, `verify` | Chunked typing outcome, verified read-back text, chunk count, typing latency |
| [`nova.select_option`](../../../mcp-reference/tools/browser-automation/nova-select-option.md) | `selector`, `value` | Native select outcome, verified selected value |
| [`nova.choose_option`](../../../mcp-reference/tools/browser-automation/nova-choose-option.md) | `selector`, `text`, `index` | Custom dropdown outcome, matched option label, popover menu state |
| [`nova.guarded_send_message`](../../../mcp-reference/tools/guarded-actions/nova-guarded-send-message.md) | `text`, `selector` (optional), `autoDismissBlockers` | Guarded commit status, effective selector, verification state, retry advice, Enter fallback status |
| [`nova.guarded_submit_form`](../../../mcp-reference/tools/guarded-actions/nova-guarded-submit-form.md) | `selector`, `transitionContract` | Form submission outcome, contract verification results |
| [`nova.guarded_login`](../../../mcp-reference/tools/guarded-actions/nova-guarded-login.md) | `selector`, `transitionContract` | Authentication progression state, error classification |
| [`nova.guarded_switch_model`](../../../mcp-reference/tools/guarded-actions/nova-guarded-switch-model.md) | `selector`, `modelName` | Model switch outcome and verification state |
| [`nova.guarded_switch_sandbox`](../../../mcp-reference/tools/guarded-actions/nova-guarded-switch-sandbox.md) | `selector`, `sandboxId` | Sandbox transition outcome |
| [`nova.composer_state`](../../../mcp-reference/tools/dom-and-reading/README.md) | `targetId` | Composer input text, send button enabled status, container info |

---

## 7. Related Documentation

- [Browser Interaction Overview](../README.md) — Master interaction architecture and tier hierarchy.
- [Input Dispatch](../input-dispatch/README.md) — DevTools physical input pipeline, chunked typing, and scrolling.
- [Drag & Drop](../drag-and-drop/README.md) — Physical and humanized drag profiles and HTML5 polyfill.
- [Closed-Loop System (CLS)](../../closed-loop-system-cls/README.md) — State transition contracts and outcome verification.
- [Auth Surface Detection (ASD)](../../auth-surface-detection-asd/README.md) — Login detection and authentication progression.

[All core features](../../README.md)
