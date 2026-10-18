# Guarded Interactions & Form Automation

> [!IMPORTANT]
> In modern reactive web applications, clicking an element or submitting text is rarely a simple, instantaneous event. Submitting a form can trigger client-side validation errors, clicking *"Send"* in an AI chat interface requires waiting for asynchronous models to generate tokens, and logging in can branch into Two-Factor Authentication (2FA) or SSO flows. Naive, blind clicking leads to duplicate form submissions, dropped prompts, and rate-limit lockouts. Nova AI Workspace solves this with **Guarded Interactions**: high-level transactional macros governed by automated Closed-Loop transition contracts, pre-flight readiness gates, and post-action outcome verification.

---

## 1. Overview & Architectural Philosophy

Autonomous web agents fail most frequently at **commit points**—actions that permanently alter application state (sending messages, submitting orders, switching accounts, or logging in).

Traditional automation frameworks dispatch raw pointer clicks with no awareness of the surrounding application state:
1. **Missing Element Readiness:** An agent attempts to click a send button before typing has activated the input, or clicks a disabled form button before required fields pass client-side validation.
2. **Blind Duplicate Submissions:** If a slow network causes a submit button to spin, an unguided agent clicks it repeatedly, resulting in duplicate purchases, duplicate chat prompts, or double API charges.
3. **Silent Rejections & Ambiguous Branches:** A login fails with an inline error flash, or transitions to an MFA/TOTP prompt. A naive script treats this as a generic failure and enters an infinite retry loop.
4. **Dropped User Prompts:** If an error occurs during message dispatch, the typed prompt in the composer is wiped out, losing user input permanently.

Nova addresses these vulnerabilities through **Guarded Interactions**:

```mermaid
flowchart TD
    Start["Agent Invokes Guarded Action\n(e.g. guarded_send_message / guarded_submit_form)"] --> PreCheck{"Stage 1: Precondition Gates"}

    subgraph PreDispatch["Stage 1: Pre-Flight Safety & Validation"]
        PreCheck --> V1["Form Validity Check\n(form.fields.valid == true)"]
        PreCheck --> V2["Composer Surface Discovery\n(Pair input + send button)"]
        PreCheck --> V3["Auth Surface Detection\n(auth.loginWallVisible)"]
        V1 -- "Invalid" --> HaltFail["Precondition Failed:\nHalt with Structured Reason"]
        V2 -- "Missing Input" --> HaltFail
    end

    PreCheck -- "Preconditions Cleared" --> Dispatch["Stage 2: Atomic Dispatch\n(Type with Read-Back + Physical Click)"]

    subgraph PostDispatch["Stage 3: Closed-Loop Transition Verification"]
        Dispatch --> Settle["Stage 3A: Stability Observation Window\n(Wait for animations / network dispatches)"]
        Settle --> PostCheck{"Evaluate Transition Contract"}
        PostCheck -- "Success State Met\n(URL changed / loggedIn / stream started)" --> SuccessDone["Action Verified: OK"]
        PostCheck -- "Explicit Failure Trapped\n(auth.authError / validation error)" --> FailDone["Action Failed: Do Not Retry"]
        PostCheck -- "Ambiguous State Trapped\n(2FA / MFA challenge / indeterminate)" --> AmbiguousDone["Action Indeterminate:\nEscalate to Operator"]
    end
```

---

## 2. Guarded Action Architecture & Tools

Nova provides specialized guarded tools for every major class of high-impact web interactions:

| Tool | Target Interaction Scope | Key Built-In Safety Mechanisms |
| :--- | :--- | :--- |
| [`nova.guarded_send_message`](../../mcp-reference/tools/guarded-actions/nova-guarded-send-message.md) | Chat interfaces (ChatGPT, Claude.ai, Gemini, Slack, Teams) | Composer auto-discovery, type-first recovery, read-back verification, Enter-key fallback, `ReplyWatchObserverScript` streaming observation, text retention on error. |
| [`nova.guarded_submit_form`](../../mcp-reference/tools/guarded-actions/nova-guarded-submit-form.md) | Transactional forms, checkouts, settings saves | Client-side validation scanning (`:invalid`, `aria-invalid`), duplicate submit protection via `non_idempotent` retry policy, post-submit navigation verification. |
| [`nova.guarded_login`](../../mcp-reference/tools/guarded-actions/nova-guarded-login.md) | Authentication surfaces & login walls | Integrated Auth Surface Detection (ASD), explicit credential error trapping (`auth.authError`), and 2FA/MFA challenge branching (`verifyState="indeterminate"`). |
| [`nova.guarded_switch_model`](../../mcp-reference/tools/guarded-actions/nova-guarded-switch-model.md) | Model switchers in web AI interfaces | Verifies open model selector menu before clicking, and confirms that the active model label changed afterwards. |
| [`nova.guarded_switch_sandbox`](../../mcp-reference/tools/guarded-actions/nova-guarded-switch-sandbox.md) | Multi-tenant workspace & organization switchers | Asserts active workspace dropdown before clicking, and verifies tenant identifier transition after selection. |

---

## 3. Comprehensive Documentation Index

The guarded interaction subsystem is organized into three specialized architectural areas and six deep-dive technical guides:

```
public/docs/core-features/guarded-interactions/
├── README.md                                         # This master hub
├── chat-macro/
│   ├── README.md                                     # Autonomous chat engine & reply-watch hub
│   ├── compose-and-send-pipeline/
│   │   └── README.md                                 # 6-step pipeline, type-first recovery, read-back verification
│   └── reply-watch-and-streaming/
│       └── README.md                                 # __nova_reply_watch, ReplyReducer, SSE tracking, continuation
├── form-submission/
│   ├── README.md                                     # Transactional form submissions & auth gates hub
│   ├── form-validation-and-idempotency/
│   │   └── README.md                                 # HTML5 :invalid scanning, ARIA checks, non_idempotent defenses
│   └── auth-surface-and-mfa-gates/
│       └── README.md                                 # ASD integration, 3-way outcome matrix, 2FA/MFA branching
└── transition-contracts/
    ├── README.md                                     # Closed-loop transition contracts hub
    ├── contract-anatomy-and-operators/
    │   └── README.md                                 # JSON schema, all/any trees, fact operators, stability holds
    └── contract-merging-and-cls/
        └── README.md                                 # Additive contract merging, pinned invariants, CLS engine
```

| Area | Architecture Guide | Scope & Key Concepts | Primary Components |
| :--- | :--- | :--- | :--- |
| **Chat Engine** | **[Autonomous Chat Engine Hub](chat-macro/README.md)** | Architectural role, challenge taxonomy, subsystem layout, and core invariants for LLM chat platforms. | `McpServer.ComposeAndSend`<br>`__nova_reply_watch`<br>`ReplyReducer` |
| | **[The 6-Step Compose-and-Send Pipeline](chat-macro/compose-and-send-pipeline/README.md)** | Composer auto-discovery across ProseMirror/Lexical/textarea, Shadow DOM piercing, type-first wake-up recovery, read-back verification against input traps, send-button click & `EnterKeySend` fallback, and zero-data-loss prompt text retention. | `TypeFirstRecovery`<br>`ReadBackVerifier`<br>`EnterKeySend`<br>`composer.text.empty` |
| | **[Reply-Watch & Streaming Architecture](chat-macro/reply-watch-and-streaming/README.md)** | In-page isolated Chromium JavaScript world observer (`__nova_reply_watch`), tamper-proof execution invariants, document replacement detection, C# host streaming reducer (`ReplyReducer`), dual DOM/network stream evaluation, and asynchronous continuation via `reply.watchId`. | `ReplyWatchObserverScript`<br>`ReplyReducer`<br>`ReplyTimeline`<br>`reply.watchId` |
| **Form & Auth** | **[Transactional Form Submissions Hub](form-submission/README.md)** | Architectural overview, pre-scan validation strategy, and three-way authentication outcome model. | `McpServer.InputInteractionGuardedTools`<br>`AuthSurfaceDetector`<br>`GuardedCommitPoint` |
| | **[Form Validation & Idempotency Safeguards](form-submission/form-validation-and-idempotency/README.md)** | Pre-dispatch HTML5 `:invalid` and `aria-invalid="true"` scanning, `form.fields.valid` precondition evaluation, atomic pointer dispatch, URL and success indicator postcondition checks, and `non_idempotent` duplicate submission defenses. | `form.fields.valid`<br>`form.successIndicator.visible`<br>`non_idempotent` |
| | **[Auth Surface & MFA Gates](form-submission/auth-surface-and-mfa-gates/README.md)** | Direct integration with Auth Surface Detection (ASD), the three-way outcome matrix (`verified`, `failed`, `indeterminate`), forbidden credential error trapping (`auth.authError`), 2FA/MFA challenge branching preventing account lockouts, and guarded model/workspace switchers. | `AuthSurfaceDetector`<br>`auth.loggedIn`<br>`auth.authError`<br>`auth.mfaChallenge` |
| **Contracts** | **[Closed-Loop Transition Contracts Hub](transition-contracts/README.md)** | Protocol-level verification philosophy, deterministic assertion models, and system safety invariant pinning. | `TransitionContract`<br>`MergeWithProvidedTransitionContract`<br>`ClosedLoopSystem` |
| | **[Contract Anatomy & Fact Operators](transition-contracts/contract-anatomy-and-operators/README.md)** | Transition contract JSON schema, `actionKind`, `retryPolicy`, `ambiguityPolicy`, condition tree logic (`all` vs `any`), complete catalog of assertion operators (`eq`, `neq`, `exists`, `not_exists`, `contains`, `gt`, `gte`, `lt`, `lte`), and temporal stability windows (`stabilityWindowMs` vs `stabilityMs`). | `TransitionContract`<br>`FactAssertion`<br>`stabilityWindowMs`<br>`stabilityMs` |
| | **[Contract Merging & Closed-Loop System (CLS)](transition-contracts/contract-merging-and-cls/README.md)** | Additive contract merging mechanics (`MergeWithProvidedTransitionContract`), combining built-in macro templates with agent extensions, pinned security invariants, Closed-Loop System (CLS) fact extraction and verification engine integration, and ambiguity resolution policies. | `MergeWithProvidedTransitionContract`<br>`ClosedLoopSystem`<br>`FactExtractionPipeline`<br>`ambiguityPolicy` |

---

## 4. Operational Invariants for Autonomous Agents

When building autonomous workflows that mutate external application state, agents must adhere to the following principles:

1. **Prefer Guarded Macros over Raw Clicks for State Mutations:**
   Never use bare `nova.input_click` or `nova.click_selector` to submit a form, send a message, or log into a portal. Raw clicks provide zero feedback on whether validation failed or whether duplicate submissions occurred.
2. **Respect `non_idempotent` Retry Policies:**
   All guarded macros declare `retryPolicy: "non_idempotent"`. If a call fails or reports `indeterminate`, **never immediately re-dispatch the exact same submit click**. Re-inspect the page using `nova.perceive` to determine whether the transaction was committed before taking corrective action.
3. **Use Reply-Watch Continuation for Long Generations:**
   When invoking `nova.guarded_send_message` with `waitForReplyMs`, long generations that exceed the timeout return a `reply.watchId`. Do not send the prompt again. Continue monitoring the existing generation using:
   ```json
   {
     "targetId": "tab-101",
     "mode": "conversation",
     "replyWatchId": "rw-123456789",
     "waitMs": 30000
   }
   ```
4. **Leverage Integrated Blocker Clearance:**
   If a cookie consent banner or modal backdrop obscures a form submit button or chat composer, pass `autoDismissBlockers: true` to the guarded tool. Nova will resolve the blocker in-flight without aborting the interaction sequence.

---

## Related Documentation

* [Autonomous Chat Engine & Reply Watch Architecture](chat-macro/README.md)
* [Transactional Form Submissions & Auth Gates](form-submission/README.md)
* [Closed-Loop Transition Contracts](transition-contracts/README.md)
* [Auth Surface Detection (ASD) Architecture](../auth-surface-detection-asd/README.md)
* [Closed-Loop System (CLS)](../closed-loop-system-cls/README.md)
* [Tool Catalog: Guarded Actions & Blocker Clearance](../../mcp-reference/tools/guarded-actions/README.md)
