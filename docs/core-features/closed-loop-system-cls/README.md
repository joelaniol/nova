# Closed-Loop System (CLS)

> [!NOTE]
> The **Closed-Loop System (CLS)** of Nova AI Workspace transforms browser automation from blind, "fire-and-forget" command execution into a deterministic control loop governed by **transition contracts**. Every guarded action follows the immutable cycle: **Expectation $\rightarrow$ Precondition Gate $\rightarrow$ Action Dispatch $\rightarrow$ Stability Verification $\rightarrow$ Outcome Reaction**. Operating in deep synergy with the Tool Observation Bus (TOB) and the Phenomenological Knowledge Store (PKS), CLS guarantees that non-idempotent commits are never blindly retried, transient UI flickers are not mistaken for permanent state, and failed postconditions are detected immediately.

---

## 1. Executive Summary & The Problem of Open-Loop Automation

Conventional browser automation tools (such as Selenium, Puppeteer, or standard CDP scripts) operate in an **open loop**:
1. A script locates an element and fires a click event.
2. The automation driver assumes that because the OS-level or CDP-level click was dispatched without an error, the operation was successful.
3. The script proceeds immediately to the next instruction.

In modern dynamic web applications, open-loop execution is fragile and error-prone:
* **The Modal Stays Open:** A close button (`✕`) is clicked, but an unhandled animation, an API validation error, or a second overlapping overlay prevents the dialog from vanishing. The script attempts to interact with underlying page content and crashes because the element is obstructed.
* **Double Form Submission & Duplicate Billing:** An agent submits a payment or sends an email. A momentary network delay prevents an immediate URL change. An open-loop retry logic clicks "Submit" a second time, charging the user twice or sending duplicate messages.
* **Transient UI Flickers:** An element temporarily toggles a CSS class during a hover animation, tricking naive pollers into reporting success before the interface settles into an error state.
* **Silent Navigation Failures:** A login button is clicked, but due to invalid credentials, an in-page error message appears without a URL change. A script expecting navigation hangs until global execution timeouts expire.

**CLS closes the loop.** An action is defined not merely by what input is sent, but by **what observable state must hold beforehand** and **what state transition must be verified afterwards**.

```mermaid
flowchart TD
    subgraph OpenLoop ["Open-Loop Automation (Fragile)"]
        O1["Dispatch Click"] --> O2["Assume Success"] --> O3["Next Action (Often Fails)"]
    end

    subgraph ClosedLoop ["Closed-Loop System (Deterministic)"]
        C1["Expectation (Contract)"] --> C2["Precondition Gate"]
        C2 -->|Verified| C3["Serialized Dispatch"]
        C2 -->|Violated| C6["Halt: BlockedPrecondition"]
        C3 --> C4["Stability Polling Window"]
        C4 -->|Settled| C5["Verified Outcome & Telemetry"]
    end
```

### Four Interlocking Systems, Distinct Responsibilities

| Subsystem | Core Architectural Responsibility |
| :--- | :--- |
| **[TOB (Tool Observation Bus)](../tool-observation-bus-tob/README.md)** | **Execution Evidence:** Immutable, server-side audit logging of every tool call, parameter, and raw outcome. |
| **[PKS (Knowledge Store)](../learning/phenomenological-knowledge-store-pks/README.md)** | **Procedural Memory:** Stores learned UI playbooks, selector fingerprints, and health ratings across sessions. |
| **[OK (Operational Knowledge)](../learning/operational-knowledge-ok/README.md)** | **Runtime Situational State:** Tracks live tab capabilities, authentication facts, and active DOM context. |
| **CLS (Closed-Loop System)** | **State Transition Enforcement:** Precondition gates, mutex-guarded dispatch, stability polling, and outcome verification. |

---

## 2. The 4-Stage Control Loop Architecture

Every closed-loop interaction—whether explicitly authored by an agent via `transitionContract` on interactive tools like `nova.click_selector`, or implicitly synthesized by compound tools like `nova.guarded_send_message`—executes through a deterministic 4-stage pipeline.

```mermaid
sequenceDiagram
    autonumber
    actor Agent
    participant CLS as CLS Controller
    participant Coord as Action Coordinator
    participant Engine as Assertion Engine & Fact Provider
    participant Page as Web Page / DOM Target

    Agent->>CLS: Invoke tool with transitionContract
    rect rgb(240, 248, 255)
    Note over CLS,Engine: Stage 1: Precondition Gate
    CLS->>Engine: Collect precondition facts
    Engine->>Page: Query DOM, auth, and runtime state
    Engine-->>CLS: Return pre-dispatch fact snapshot
    CLS->>CLS: Evaluate preconditions (Fail-closed)
    end

    rect rgb(255, 250, 240)
    Note over CLS,Coord: Stage 2: Reservation & Baseline
    CLS->>Coord: TryReserve(targetId, priority=Agent)
    Coord-->>CLS: Reservation acquired (Mutex locked)
    CLS->>Engine: Capture baseline snapshot (for forbidden suppression)
    CLS->>Page: Dispatch mutating action (Click, Type, Submit)
    end

    rect rgb(245, 255, 245)
    Note over CLS,Page: Stage 3: Stability Polling Loop
    loop Every 100ms within stabilityWindowMs
        CLS->>Engine: Collect postcondition facts
        Engine->>Page: Poll DOM & runtime facts
        CLS->>CLS: Evaluate forbidden (presence check)
        CLS->>CLS: Evaluate success (must hold continuously for stabilityMs)
        CLS->>CLS: Evaluate ambiguous conditions
    end
    end

    rect rgb(255, 245, 245)
    Note over CLS,Coord: Stage 4: Reaction & Release
    CLS->>Coord: Release reservation
    CLS-->>Agent: Return ClTransitionResult (Status, ReasonCode, Diagnostics, RetryAdvice)
    end
```

### Stage 1: Precondition Verification & Stale Fact Recovery
* **Fail-Closed Execution:** Before any mutating click or input is sent, preconditions are evaluated against live target facts. If preconditions fail (`ClEvalVerdict.Failed`), the action is **never dispatched**, returning `DispatchStatus = BlockedPrecondition` and `VerificationStatus = Skipped`.
* **Stale Fact Recovery:** If an unreadable or stale fact produces an `Unknown` verdict, CLS introduces a brief 200 ms settling pause and re-collects facts once. If preconditions remain indeterminate, execution halts safely, preventing blind mutations on uncertain surfaces.

### Stage 2: Action Coordinator Reservation & Baseline Capture
* **Per-Tab Mutation Mutex:** To prevent race conditions between concurrent agent actions, background crawlers, and Ambient Auto-Apply, the `ActionCoordinator` enforces serialized execution per `targetId`.
* **Baseline Snapshotting:** Immediately prior to action dispatch, CLS captures a baseline snapshot of all facts referenced in the `forbidden` postcondition bucket. This enables **Baseline Suppression** in Stage 3.
* **Dispatch:** The actual mutation (e.g. native mouse click, keystroke sequence, form submit) is executed against the target WebView.

### Stage 3: Outcome Verification & Stability Hold
* **High-Frequency Polling:** CLS enters an asynchronous verification loop polling target facts every **100 ms** up to `stabilityWindowMs` (typically 2,000 to 8,000 ms depending on action class).
* **Baseline Suppression Invariant:** If a forbidden condition was *already present before the action ran* (e.g. the URL is still on the compose page during the brief fraction of a second before a send action navigates away), it is an existing condition that cannot be blamed on the action. The baseline filter suppresses this condition so an action is not falsely marked as failed while transitioning.
* **Continuous Stability Hold (`stabilityMs`):** To prevent false positives from transient UI flickers, animations, or temporary spinner disappearance, success conditions must hold continuously for `stabilityMs` (default 100 to 250 ms) before `verified_success` is declared.
* **Short-Circuit Optimization:** If `ShortCircuitOnSuccess == true` and `stabilityMs == 0`, CLS completes immediately upon the first verified success tick, eliminating artificial latency.

### Stage 4: Diagnostics Projection & Telemetry Feedback
* **Top-Level Wire Projection:** The verification result is projected into top-level MCP response fields: `status`, `reasonCode`, `stage`, `retryable`, `retryAdvice`, and structured `postconditionDiagnostics`.
* **Knowledge Loop Feedback:** Outcomes automatically update PKS phenomenon health records: consistent successes elevate playbooks to higher autonomy levels, while repeated failures demote or deprecate broken selector patterns.

---

## 3. The Pure Assertion Engine (`AssertionEngine`)

At the heart of CLS is the `AssertionEngine`—a purely deterministic, in-memory tri-state evaluation engine with zero I/O side effects.

### 3.1 The Frozen Truth Table
Every individual assertion evaluates to `true` (Satisfied), `false` (Failed), or `null` (Unknown). Unknown is treated with strict mathematical rigor:

| Assertion Bucket | All Children `true` | At Least One `true`, None `false` | At Least One `false` | Any `null` (Unknown), None `false` |
| :--- | :--- | :--- | :--- | :--- |
| **`all`** | **Satisfied** (`true`) | Unknown (`null`) | **Failed** (`false`) | Unknown (`null`) |
| **`any`** | **Satisfied** (`true`) | **Satisfied** (`true`) | Failed (`false`) | Unknown (`null`) |
| **`forbidden`** | **Failed** (`false` - Violation!) | **Failed** (`false` - Violation!) | **Satisfied** (`true` - Clean) | Unknown (`null`) |

### 3.2 Precedence Hierarchy
When combining bucket outcomes, CLS enforces strict precedence:
$$\text{Forbidden Violation} > \text{Success Match} > \text{Ambiguous Signal} > \text{Unknown / Timeout}$$

If a forbidden condition fires (e.g. `auth.authError == true` or `form.errorBanner.visible == true`), it immediately overrides any partial success signals, terminating the verification loop with `verified_fail`.

### 3.3 The 10 Comparison Operators

| Operator | Syntax | Supported Types | Evaluation Behavior |
| :--- | :--- | :--- | :--- |
| **`eq`** | `"eq"` | All JSON types | Structural deep-equality. Recursively checks objects and arrays; strict value match on primitives. |
| **`not_eq`** / **`neq`** | `"not_eq"` | All JSON types | Negation of deep-equality. `true` if types or contents differ. |
| **`exists`** | `"exists"` | Any | `true` if the fact is present and neither `null` nor `undefined`. |
| **`not_exists`** | `"not_exists"` | Any | `true` if the fact is missing, `null`, or `undefined`. |
| **`contains`** | `"contains"` | String | Substring match (`haystack.Contains(needle, Ordinal)`). Fails on non-strings. |
| **`gt`** | `"gt"` | Number | Numeric greater than ($a > b$). |
| **`lt`** | `"lt"` | Number | Numeric less than ($a < b$). |
| **`gte`** | `"gte"` | Number | Numeric greater than or equal ($a \ge b$). |
| **`lte`** | `"lte"` | Number | Numeric less than or equal ($a \le b$). |

### 3.4 Fact Degradation & Unreadable Handling
When a fact provider encounters an element that cannot be queried or a probe that throws an exception, it reports the fact as JSON `null`.
* **No False Mismatches:** Comparing an unreadable `null` fact against a concrete expected value (e.g. checking if `composer.textEmpty == true`) yields **Unknown (`null`)**, not `false`. This prevents an infrastructure probe failure from masquerading as a confirmed state mismatch.
* **Diagnostic Trace Error Codes:** Every evaluated assertion generates an immutable trace containing one of:
  * `fact_not_found`: The requested fact key was not produced by any provider.
  * `stale_fact`: The fact was marked stale by renderer/navigation lifecycle transitions.
  * `fact_unreadable`: The DOM element or property could not be resolved.
  * `frame_mismatch`: The fact was observed in a different frame than the asserted `frameId`.
  * `type_mismatch`: Operator cannot compare the observed and expected types (e.g. `gt` on strings).

---

## 4. The Fact Key Vocabulary

To prevent subtle authoring bugs where an agent guesses a fact key (e.g. typing `dom.text` instead of `composer.hasText`) and runs into an uninformative timeout, Nova enforces a strict fact key vocabulary. Known prefixes with unrecognized names are rejected up front with JSON-RPC error `-32602`.

```mermaid
flowchart LR
    FactKey["Fact Key Request"] --> Prefix{"Prefix Category"}
    Prefix -->|dom.*| F1["dom.<css-selector> (Dynamic DOM existence & state)"]
    Prefix -->|page.*| F2["page.url, page.title, page.readyState, page.route, page.urlChanged"]
    Prefix -->|form.*| F3["form.fields.valid, form.successIndicator.visible"]
    Prefix -->|chat.*| F4["chat.streamActive, chat.assistantTurnCreated, chat.outboundMessageAppeared"]
    Prefix -->|composer.*| F5["composer.hasText, composer.textEmpty, composer.sendButton.clickable"]
    Prefix -->|model.*| F6["model.selected, model.dropdown.visible"]
    Prefix -->|overlay.*| F7["overlay.blocking, overlay.primary.visible"]
    Prefix -->|auth.*| F8["auth.loggedIn, auth.loginWallVisible, auth.mfaChallenge, auth.authError, auth.stage"]
    Prefix -->|sandbox.*| F9["sandbox.selected, sandbox.selected.changed, sandbox.target.exists"]
    Prefix -->|runtime.*| F10["runtime.domEpoch, runtime.frameId, runtime.rendererHealthy"]
    Prefix -->|Unprefixed| F11["OK Store Dynamic Facts (nova.ok_observe)"]
```

### Complete Prefix Reference

| Prefix Group | Supported Fact Keys | Typical Usage & Verification Target |
| :--- | :--- | :--- |
| **`dom.<selector>`** | Arbitrary CSS selectors (e.g. `dom.#modal-close`, `dom.button.submit`) | Resolves directly against target DOM. Combined with `exists` or `not_exists` to verify element appearance or removal. |
| **`page.*`** | `page.url`<br>`page.title`<br>`page.readyState`<br>`page.route`<br>`page.urlChanged` | Navigation verification; URL change detection; client-side route tracking. |
| **`form.*`** | `form.fields.valid`<br>`form.successIndicator.visible` | Form validation state; submission confirmation banners. |
| **`chat.*`** | `chat.streamActive`<br>`chat.streamActive.started`<br>`chat.assistantTurnCreated`<br>`chat.outboundMessageAppeared` | AI chat completion tracking; streaming response detection; messenger turn creation. |
| **`composer.*`** | `composer.hasText`<br>`composer.textEmpty`<br>`composer.sendButton.clickable` | Text entry validation; composer clearing confirmation post-send. |
| **`model.*`** | `model.selected`<br>`model.dropdown.visible` | AI model picker switching and dropdown visibility. |
| **`overlay.*`** | `overlay.blocking`<br>`overlay.primary.visible` | Modal blocker detection; cookie banner verification. |
| **`auth.*`** | `auth.assessment`<br>`auth.stage`<br>`auth.loggedIn`<br>`auth.loginWallVisible`<br>`auth.authError`<br>`auth.mfaChallenge` | Authentication state; sign-in wall detection; MFA challenge prompts; login error verification. |
| **`sandbox.*`** | `sandbox.selected`<br>`sandbox.selected.changed`<br>`sandbox.target.exists` | Multi-sandbox profile switching and target binding verification. |
| **`runtime.*`** | `runtime.domEpoch`<br>`runtime.frameId`<br>`runtime.rendererHealthy` | DOM revision tracking; subframe identification; renderer liveness. |

---

## 5. Contract Authoring & Stability Profiles

Agents specify transition contracts using the `transitionContract` parameter. Nova configures timing defaults based on the declared `actionKind`.

```json
{
  "actionKind": "submit_form",
  "retryPolicy": "non_idempotent",
  "ambiguityPolicy": "signal",
  "stabilityWindowMs": 8000,
  "stabilityMs": 200,
  "preconditions": {
    "all": [
      { "factKey": "form.fields.valid", "op": "eq", "value": true }
    ]
  },
  "postconditions": {
    "success": {
      "any": [
        { "factKey": "page.urlChanged", "op": "eq", "value": true },
        { "factKey": "form.successIndicator.visible", "op": "eq", "value": true }
      ]
    },
    "forbidden": {
      "any": [
        { "factKey": "dom.div.form-error-banner", "op": "exists" }
      ]
    },
    "ambiguous": {
      "any": [
        { "factKey": "auth.mfaChallenge", "op": "eq", "value": true }
      ]
    }
  }
}
```

### Action Stability Templates (`ClStabilityTemplates`)

| Action Kind (`actionKind`) | Default `WindowMs` | Default `StabilityMs` | Short-Circuit on Success | Primary Operational Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **`dismiss_overlay`** | 3,000 ms | 250 ms | `true` | Closing modals, cookie banners, tooltips, dialogs. Requires 250 ms hold to ensure blocker does not bounce back. |
| **`send_message`** | 5,000 ms | 0 ms | `true` | Sending chat or messenger prompts. Immediate return once composer clears or assistant turn starts. |
| **`submit_form`** | 8,000 ms | 0 ms | `true` | Checkout, registration, form submission. Extended window accommodates server-side processing latency. |
| **`select_option`** | 2,000 ms | 100 ms | `true` | Dropdowns, model switches, tab selection. Fast verification with brief settling debounce. |
| **`custom`** | 5,000 ms | 250 ms | `true` | User-defined multi-step workflows and ad-hoc transition assertions. |

---

## 6. Verification Verdicts, Indeterminate Reasons & Retry Advice

CLS strictly separates the questions: *"Did the action dispatch?"*, *"Was the intended outcome verified?"*, and *"Is it safe to retry?"*

### 6.1 Verification Statuses

| Verification Status | Definition & Operational Meaning |
| :--- | :--- |
| **`verified_success`** | All required success assertions passed and held continuously for `stabilityMs`. |
| **`verified_fail`** | A forbidden assertion matched, dispatch threw an exception, or preconditions definitively failed. |
| **`indeterminate`** | The outcome could not be definitively confirmed within the observation window. **Never treated as success.** |
| **`skipped`** | Verification was not performed (preconditions blocked execution or no postconditions were specified). |

### 6.2 Dissecting Indeterminate Reasons (`ClIndeterminateReason`)
When an outcome is indeterminate, CLS provides exact diagnostic attribution:

* **`postcondition_mismatch` (Contract Mismatch vs. Timeout):**
  > [!IMPORTANT]
  > Nova distinguishes between "no usable signal arrived" and "Nova read the resulting state and it definitively did not match what the caller asserted".
  > 
  > If the polling window closes while the success assertion evaluated to `Failed`, Nova reports `postcondition_mismatch` instead of a generic `timeout`. This informs the agent that the action *already executed* and page state was readable, preventing disastrous double-submissions caused by overly narrow assertions on successful non-idempotent commits!
* **`timeout`:** The polling window elapsed without receiving a definitive signal (e.g. slow network response).
* **`ambiguous_signal`:** An explicit ambiguity assertion matched (e.g. an unexpected 2FA challenge after login).
* **`page_navigated`:** Top-level navigation destroyed the page context before postconditions settled.
* **`frame_destroyed`:** An iframe containing the target element was detached during execution.
* **`eval_error`:** Renderer exception during fact evaluation.

### 6.3 Retry Policies & Derived Advice

| Configured `retryPolicy` | Observed Outcome | Generated `retryAdvice` | `retryable` | Actionable Agent Guidance |
| :--- | :--- | :--- | :--- | :--- |
| **`idempotent`** | Failure or Timeout | `safe_to_retry` | `true` | The action has no cumulative side effects (e.g. closing a modal, selecting an option). Safe to dispatch again. |
| **`non_idempotent`** | Any non-success | `check_postcondition_first` | `false` | Consequential action (e.g. sending mail, charging payment). **Do not blindly retry.** Re-read page state first. |
| **`no_retry`** | Any non-success | `do_not_retry` | `false` | Action must not be repeated under any circumstances. |
| Any | `verified_fail` | `do_not_retry` | `false` | Explicit forbidden violation detected. Repeating the same action will fail identically. |

---

## 7. Action Coordinator & Tab Concurrency Protection

Autonomous browser environments frequently host competing actors:
1. Interactive agent tool calls (clicking, typing).
2. Background Ambient Auto-Apply routines (dismissing cookie banners).
3. Telemetry and probe background workers.

If an Ambient Auto-Apply routine clicks a cookie banner button at the exact millisecond the agent clicks a payment button, the resulting click coordinate collision or focus shift can corrupt execution.

Nova's **`ActionCoordinator`** resolves this:

```mermaid
flowchart TD
    Request["Mutation Request on Tab"] --> Check{"Is targetId reserved?"}
    Check -->|Already Reserved| Busy["Reject / Back-off (BlockedCoordinator)"]
    Check -->|Available| Reserve["Acquire Reservation with Priority"]

    Reserve --> Exec["Execute Guarded Action & Verification Loop"]
    Exec --> Release["Release Reservation (Mutex Unlocked)"]

    subgraph PriorityHierarchy ["Priority Hierarchy (Lower Integer = Higher Priority)"]
        P0["Agent Priority (0) — Highest"]
        P1["Ambient Auto-Apply Priority (1)"]
        P2["Telemetry Priority (2) — Lowest"]
    end
```

### Frozen Coordination Invariants
1. **Non-Preemptive In-Flight Guarantee:** Once a guarded action begins execution, it **cannot be preempted** by any other process—even a higher priority agent request—until verification completes or the timeout expires.
2. **Priority Ordering:** `Agent (0) > AutoApply (1) > Telemetry (2)`. If an agent issues a command, Ambient Auto-Apply immediately steps aside.
3. **PKS Execution Within Mutex:** Ambient Auto-Apply acquires its coordinator reservation *before* inspecting playbooks, ensuring no state changes occur between matching and execution.
4. **Deadman TTL Expiration:** Every reservation carries an explicit timeout (up to 15,000 ms). If an action process crashes, the coordinator automatically purges the expired reservation, preventing permanent tab deadlocks.

---

## 8. Ambient Auto-Apply Runtime

Building on CLS, Nova features **Ambient Auto-Apply**: an autonomous background remediation engine that cleans up common web obstacles (such as cookie consent banners, notification popups, and newsletter overlays) without interrupting the agent's primary task.

```mermaid
flowchart LR
    Nav["Page Navigation / Route Change"] --> Detect["Fingerprint Detection (SilentVerify)"]
    Detect -->|Match Found| Policy{"Confirm Mode Policy?"}
    Policy -->|NeverAsk| Run["Execute Guarded Playbook under ActionCoordinator"]
    Policy -->|OncePerSession| CheckGrant{"Session Grant Active?"}
    CheckGrant -->|Yes| Run
    CheckGrant -->|No| Prompt["Request User Confirmation"]
    Policy -->|AlwaysAsk| Prompt
    Prompt -->|Approved| Run
    Run --> Outcome["Update PKS Health & Telemetry"]
```

### 8.1 Execution Mechanics
* **Trigger Points:** Evaluated automatically upon navigation (`nova.navigate`, `nova.back`, `nova.forward`), client-side route changes (`nova.route`), or DOM mutations settling.
* **Guarded Execution:** Auto-Apply does not use unverified scripts. It compiles a guarded `nova.phenomenon_apply` call backed by a verified `transitionContract` (verifying that the overlay actually disappears).
* **Confirmation Policies:**
  * `NeverAsk`: Fully autonomous background resolution for trusted, verified low-risk blockers.
  * `OncePerSession`: Prompts operator once per domain/session; reuses session grant for subsequent occurrences.
  * `AlwaysAsk`: Demands operator approval before dispatching remediation.
* **Tab-Claim Session Binding:** Ambient session grants are cryptographically bound to the active tab-claim owner session, preventing cross-session privilege escalation.

---

## 9. The Family of Guarded Compound Tools

While agents can manually attach a `transitionContract` to any interactive tool (`nova.click_selector`, `nova.type_selector`, `nova.input_click`), Nova provides native **guarded compound tools** that automatically synthesize domain-specific contracts:

| Guarded Tool | Action Kind | Automated Precondition | Automated Verification Postconditions |
| :--- | :--- | :--- | :--- |
| **`nova.guarded_send_message`** | `send_message` | `composer.hasText == true`<br>`composer.sendButton.clickable == true` | **Success:** `composer.textEmpty == true`<br>AND (`chat.streamActive.started == true` OR `chat.assistantTurnCreated == true` OR `chat.outboundMessageAppeared == true`). |
| **`nova.guarded_submit_form`** | `submit_form` | `form.fields.valid == true` | **Success:** `page.url` changed OR `form.successIndicator.visible == true`. |
| **`nova.guarded_login`** | `submit_form` | `auth.loginWallVisible == true` | **Success:** `auth.loggedIn == true`.<br>**Forbidden:** `auth.authError == true`.<br>**Ambiguous:** `auth.mfaChallenge == true` OR `auth.stage == "identity_step"`. |
| **`nova.guarded_switch_model`** | `select_option` | Target dropdown exists | **Success:** `model.selected` matches target model name. |
| **`nova.guarded_switch_sandbox`** | `select_option` | Sandbox profile exists | **Success:** `sandbox.selected` changed AND `page.route` updated. |

### Subframe Scoping (`frameId`)
All guarded tools accept an optional `frameId` parameter. If a form or chat composer lives inside an embedded same-origin `<iframe>`, Nova scopes both selector resolution and fact assertions directly to that frame context.

---

## 10. Wire Response & Diagnostics Specification

When an agent executes an action with a transition contract, Nova returns detailed verification telemetry in the response payload:

```json
{
  "ok": false,
  "status": "partial",
  "applied": true,
  "stage": "postcondition_check",
  "reasonCode": "guarded_commit.postcondition_mismatch",
  "retryable": false,
  "retryAdvice": "check_postcondition_first",
  "verificationStatus": "indeterminate",
  "message": "The action was dispatched and Nova could read the resulting state — this is NOT an unknown outcome and NOT a failed dispatch. The observed state simply never matched the success assertion this call supplied. Check the postcondition before attempting another send.",
  "postconditionDiagnostics": {
    "contractName": "guarded_commit.postconditions",
    "factKey": "composer.textEmpty",
    "op": "eq",
    "expectedState": true,
    "observedState": false,
    "assertionError": null,
    "elapsedMs": 5012,
    "outcomeVerdict": "failed"
  }
}
```

### Diagnostic Field Reference
* **`applied` (`bool`):** Indicates whether the action mutation was actually dispatched to the target page.
* **`verificationStatus` (`string`):** One of `verified_success`, `verified_fail`, `indeterminate`, `skipped`.
* **`reasonCode` (`string`):** Specific failure identifier (e.g. `guarded_commit.postcondition_mismatch`, `guarded_commit.postcondition_failed`, `guarded_commit.timeout`, `guarded_commit.ambiguous_signal`).
* **`retryable` (`bool | null`):** Explicit Boolean indicating whether an automated retry is safe.
* **`retryAdvice` (`string`):** `safe_to_retry`, `do_not_retry`, or `check_postcondition_first`.
* **`postconditionDiagnostics` (`object`):**
  * `factKey`: The exact assertion fact key that failed or mismatched.
  * `op`: The comparison operator used.
  * `expectedState`: The expected value asserted in the contract.
  * `observedState`: The actual value observed on the page.
  * `elapsedMs`: Total observation duration before settling or timing out.
  * `outcomeVerdict`: Final tri-state verdict of the evaluated assertion set.

---

## 11. Summary: The CLS Architectural Matrix

| Architectural Layer | Core Responsibility | Invariant / Guarantee | Primary Failure Mode Addressed |
| :--- | :--- | :--- | :--- |
| **Assertion Engine** | Pure tri-state mathematical evaluation. | Frozen truth table; unreadable facts degrade to `Unknown`, not `Failed`. | Prevents false negative mismatches caused by DOM query errors. |
| **Precondition Gate** | Pre-flight validation prior to mutation. | Fail-closed; mutating actions are blocked if preconditions fail. | Prevents sending inputs to non-ready or missing forms. |
| **Action Coordinator** | Mutex serialization per tab. | Non-preemptive in-flight execution; Priority: Agent > AutoApply. | Prevents concurrent click collisions and race conditions. |
| **Baseline Suppression** | Filters pre-existing failure states. | Forbidden states present before dispatch cannot fail the transition. | Eliminates false failures during transitional page navigations. |
| **Stability Hold** | Debounces transient UI states. | Success conditions must remain true continuously for `stabilityMs`. | Prevents false positives caused by temporary animation flickers. |
| **Diagnostic Attribution** | Differentiates timeout from mismatch. | Distinguishes `postcondition_mismatch` from network infrastructure `timeout`. | Prevents duplicate non-idempotent commits (e.g. sending mail twice). |
| **Ambient Auto-Apply** | Background blocker mitigation. | Executes PKS playbooks under coordinator reservation with verified contracts. | Clears cookie banners without agent distraction. |

---

## Related Documentation

* **[Agent-Native Affordances](../agent-native-affordances/README.md)** — Compound interaction primitives and closed-loop execution patterns.
* **[Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md)** — Pre-execution situational awareness and tab leases.
* **[Tool Observation Bus (TOB)](../tool-observation-bus-tob/README.md)** — Server-side immutable record of executed actions and verification traces.
* **[Auth Surface Detection (ASD)](../auth-surface-detection-asd/README.md)** — Heuristic authentication state detection and persistence gating.
* **[Phenomenological Knowledge Store (PKS)](../learning/phenomenological-knowledge-store-pks/README.md)** — Procedural UI memory, playbooks, and health tracking.
* **[Ambient Auto-Apply](../learning/ambient-auto-apply/README.md)** — Autonomous background blocker remediation.

[All core features](../README.md)
