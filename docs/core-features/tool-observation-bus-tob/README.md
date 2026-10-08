# Tool Observation Bus (TOB) — Server-Observed Evidence Ledger

> [!NOTE]
> The **Tool Observation Bus (TOB)** is Nova AI Workspace's core observation and evidence infrastructure. Operating server-side within the browser runtime, TOB captures immutable records of what agents actually execute, projects these records into structured observation streams, synthesizes visit windows, and provides verifiable evidence to Agent Awareness Gates (AAG), the Phenomenological Knowledge Store (PKS), and the Episodic Task Memory (ETM) Evidence Ledger.

---

## 1. Executive Summary & The Core Axiom

In traditional agentic environments, an orchestrator relies primarily on what the language model reports:
* *“I have read the checkout policy.”*
* *“I clicked the confirmation button.”*
* *“I verified all 120 items on the list.”*

In reality, language models frequently hallucinate completion: an agent may claim it read a document when navigation failed; it may assert it clicked a button that was blocked by an awareness gate; or it may claim to have reviewed a page after glancing at it for 12 milliseconds without triggering a content read.

**The TOB Guiding Principle:**
> *"What the agent says is a claim. What Nova observes is evidence."*

TOB creates a strict, unbridgeable separation between agent self-reports and server-side execution observations:
* **Content Exposure $\neq$ Comprehension:** Exposing page text proves the agent had access to the data; it does not prove cognitive understanding.
* **Dispatched Click $\neq$ Business Outcome:** Dispatching an input event proves the action was attempted; only closed-loop verification (CLS) confirms the intended state transition occurred.
* **Blocked Calls $\neq$ Execution Failures:** If a preflight awareness gate rejects a tool call, TOB records it as blocked preflight evidence, preventing failed attempts from masquerading as executed actions.

```mermaid
flowchart TD
    subgraph AgentSpace ["Agent Cognitive Space (Unverified)"]
        Claim["Agent Self-Report / Claim<br/>('I verified the document')"]
    end

    subgraph ServerSpace ["Nova Server Runtime (Immutable Evidence)"]
        Dispatch["Tool Dispatch Envelope"] --> PreState["Capture Pre-State"]
        PreState --> Exec["Execute MCP Tool"]
        Exec --> PostState["Capture Post-State in finally"]
        PostState --> Project["TOB Observation Projection"]
    end

    subgraph LedgerSpace ["Consumer Verification"]
        Claim -.-> Compare{"Correlate Claim vs Evidence"}
        Project --> Compare
        Compare --> Grade["Evidence Grade: strong | weak | none | unknown"]
    end
```

### The Four Knowledge & Verification Pillars

| Subsystem | Architectural Role | Core Question Answered |
| :--- | :--- | :--- |
| **TOB (Tool Observation Bus)** | **Execution Evidence Ledger** | *“What actions did the agent actually dispatch, and what content was exposed?”* |
| **[CLS (Closed-Loop System)](../closed-loop-system-cls/README.md)** | **State Transition Enforcement** | *“Did the page state transition match the declared postcondition contract?”* |
| **[PKS (Knowledge Store)](../learning/phenomenological-knowledge-store-pks/README.md)** | **Procedural Memory** | *“How does this interface behave, and which playbooks have proven reliable?”* |
| **[AAG (Awareness Gates)](../agent-awareness-gates-aag/README.md)** | **Pre-Dispatch Safety** | *“Does the agent possess valid situational context to execute this call?”* |

---

## 2. The 5-Layer Bus Architecture

TOB is structured into five distinct architectural layers spanning the execution lifecycle from initial dispatch to high-level policy evaluation:

```mermaid
flowchart TD
    subgraph Layer0 ["Layer 0: Canonical Dispatch Envelope"]
        Env["DispatchObservationEnvelope<br/>Pre-State before execution | Post-State in finally<br/>dispatch_call_id (UUIDv4) | dispatch_seq (Monotonic)"]
    end

    subgraph Layer1 ["Layer 1: Raw Data Sources"]
        Audit["AuditStore (ConversationDb)"]
        OKStore["OK System (pks.db)"]
        LCJ["LCJ Journal (memory.db)"]
        Outbox["tob_lcj_durable_outbox (pks.db)"]
    end

    subgraph Layer2 ["Layer 2: Observation Projection"]
        ToolObs["tob_tool_observation"]
        VisitWin["tob_visit_window"]
        ScopeRun["tob_scope_runtime & tob_scope_binding"]
        Watermark["tob_scope_source_watermark"]
    end

    subgraph Layer3 ["Layer 3: Shared Correlation Primitives"]
        Norm["URL Canonicalization (SiteUrlCanonicalizer)"]
        Hash["SHA-256 Selector Hashing"]
        Prelude["In-Memory Prelude Buffer (Ring)"]
        Epilogue["Epilogue Grace Period (750ms)"]
    end

    subgraph Layer4 ["Layer 4: Consumer Ledgers & Policies"]
        ETM["ETM Evidence Ledger (Task Verification)"]
        AAG["AAG Block-Mode (Preflight Audit)"]
        PKSProof["PKS Autonomous Selector Proof"]
        OKCons["OK Capability Correlation"]
    end

    Env --> Layer1
    Env --> Layer2
    Layer3 --> Layer2
    Layer2 --> Layer4
```

### Detailed Layer Breakdown

1. **Layer 0 — Canonical Dispatch Envelope:**
   * Every MCP tool invocation is wrapped in a `DispatchObservationEnvelope`.
   * Captures `PreState` immediately before execution and `PostState` inside a guaranteed `finally` block.
   * Assigns an immutable `dispatch_call_id` (UUIDv4), a monotonic `dispatch_seq`, and a short correlation ID (`request_id_short`).
2. **Layer 1 — Raw Data Sources:**
   * Receives envelope copies across independent persistence sinks: `AuditStore` (human-readable audit log), `OKStore` (operational knowledge graph), and `LCJ` (learning candidate journal).
   * Includes `tob_lcj_durable_outbox` in `pks.db` as a reserved durability bridge.
3. **Layer 2 — Observation Projection:**
   * Projects structured observations into relational SQLite tables (`pks.db`, Migrations V14 & V15).
   * Manages scope bindings (`tob_scope_runtime`, `tob_scope_binding`) and tracks barrier progress (`tob_scope_source_watermark`).
4. **Layer 3 — Shared Correlation Primitives:**
   * **URL Normalization:** Canonicalizes query strings, fragments, and route parameters via `SiteUrlCanonicalizer`.
   * **Selector Hashing:** Computes deterministic SHA-256 hashes of normalized CSS selectors.
   * **Prelude Ring Buffer:** Preserves unscoped dispatches in RAM and backfills them upon scope activation.
5. **Layer 4 — Consumers:**
   * **ETM Evidence Ledger:** Computes mathematical evidence grades (`strong`/`weak`/`none`/`unknown`) for task units upon completion.
   * **AAG Block-Mode:** Records preflight blocks without tool dispatch.
   * **PKS Selector Proof:** Autonomously validates UI phenomena in procedural memory without requiring agent claims.

---

## 3. The Dispatch Envelope Lifecycle & Surface Capture

Every tool execution follows a deterministic, fail-safe envelope lifecycle:

```mermaid
sequenceDiagram
    autonumber
    participant Tool as MCP Tool Pipeline
    participant Env as DispatchEnvelopeBuilder
    participant Tab as Target Tab / WebView
    participant Projector as ToolObservationProjector
    participant Buffer as PreludeBuffer

    Tool->>Env: CapturePreState(traceTargetId)
    Env->>Tab: Query active or explicit target info
    Note over Env: Capture URL, Epoch, Tab Version, Timestamps
    
    alt Preflight Blocked by AAG
        Tool->>Projector: TryProjectBlockedObservation()
        Projector-->>Tool: Record blocked_preflight (executed=0)
    else Dispatch Allowed
        Tool->>Tool: Execute tool logic (click, read, navigate)
        Tool->>Env: CapturePostState(traceTargetId) in finally
        Note over Env: Capture post-execution URL, epoch, hints
        Tool->>Projector: TryProjectTobObservation()
        alt Scoped Execution
            Projector->>Projector: Insert into tob_tool_observation
            Projector->>Projector: Update VisitWindowBuilder
            Projector->>Projector: Evaluate TobSelectorProofEmitter
        else Unscoped Execution
            Projector->>Buffer: Enqueue into PreludeBuffer Ring
        end
    end
```

### 3.1 Pre-State and Post-State Capture
* **Pre-State:** Captured immediately before tool dispatch. Records target ID, target session ID, tab state version, navigation epoch (`pageEpoch`), raw URL, normalized route URL, and start timestamp (`started_at_ms`).
* **Post-State:** Captured in a `finally` block, ensuring capture occurs even if the tool throws an unhandled exception, times out, or encounters renderer process termination.
* **Effective Fields:** To handle intermediate navigations cleanly, TOB derives effective attributes (`page_url_effective_norm`, `page_epoch_effective`) using `COALESCE(postState, preState)`.

### 3.2 The Foreign Target Resolution Invariant
> [!IMPORTANT]
> When an agent interacts with a background tab by supplying an explicit `targetId`, TOB **does not borrow the identity of the foreground active tab**.
> 
> In multi-tab workflows, attributing background clicks to the foreground URL corrupts PKS selector proofs, visit windows, and task verification. `DispatchEnvelopeBuilder.CaptureSnapshot` explicitly checks whether `traceTargetId` differs from `ActiveTargetId`. If foreign, it resolves the specific tab's URL and title independently. If unresolvable, the URL fields remain empty rather than falling back to the wrong tab!

---

## 4. Signal Flags & Tool Classification (`ObservationSignalFlags`)

TOB categorizes every tool execution using a 64-bit bitmask (`ObservationSignalFlags`). This bitmask describes exactly what data was exposed to the agent and what mutations were committed to the browser runtime:

| Signal Flag | Bit | Description & Behavioral Meaning |
| :--- | :---: | :--- |
| **`ContentExposed`** | `1 << 0` | Readable text or structured data was returned to the agent context. |
| **`VisualExposed`** | `1 << 1` | A visual image or screenshot was returned to the agent. |
| **`DomExposed`** | `1 << 2` | Raw DOM nodes, layout geometries, or element trees were exposed. |
| **`SelectorTouched`** | `1 << 3` | A specific DOM selector was targeted (clicked, typed, focused). |
| **`NavigationIntent`** | `1 << 4` | Navigation was initiated (URL change, back, forward, reload). |
| **`NavigationCommitted`** | `1 << 5` | Navigation was confirmed committed by the browser engine. |
| **`MutationAttempted`** | `1 << 6` | A DOM mutation was dispatched (click, type, option select). |
| **`MutationCommitted`** | `1 << 7` | DOM mutation was confirmed effective on the target page. |
| **`InputSupplied`** | `1 << 8` | Physical or synthetic user input was provided (keystrokes, text). |
| **`SearchExecuted`** | `1 << 9` | In-page text search or grep query was performed. |
| **`ConsoleExposed`** | `1 << 10` | Browser console logs or errors were returned. |
| **`FileExposed`** | `1 << 11` | External or local file payload was read. |
| **`ViewportOnly`** | `1 << 12` | Read or capture was strictly constrained to the visible viewport. |
| **`FullDocument`** | `1 << 13` | Complete document tree or full-page scroll was exposed. |
| **`TargetResolved`** | `1 << 14` | Target WebView/tab was successfully located and matched. |

### 4.1 Tool-to-Signal Mapping Rules

`ObservationClassifier` inspects the tool name and execution outcome to assign action kinds (`read`, `navigate`, `interact`, `write`, `meta`) and surface types:

* **`nova.perceive`:** Classified as `read` on `webpage`. Flags: `ContentExposed | VisualExposed | DomExposed | TargetResolved`.
* **`nova.read_text` / `nova.read_text_structured`:** Classified as `read` on `dom_node`. Flags: `ContentExposed | DomExposed | TargetResolved`.
* **`nova.read_dom`:** Classified as `read` on `dom_node`. Flags: `ContentExposed | DomExposed | FullDocument | TargetResolved`.
* **`nova.click_selector`:** Classified as `interact` on `dom_node`. Flags: `SelectorTouched | MutationAttempted | (MutationCommitted) | TargetResolved`.
* **`nova.type_selector`:** Classified as `interact` on `dom_node`. Flags: `SelectorTouched | InputSupplied | MutationAttempted | (MutationCommitted) | TargetResolved`.
* **`nova.navigate` / `nova.back` / `nova.forward`:** Classified as `navigate` on `webpage`. Flags: `NavigationIntent | (NavigationCommitted) | TargetResolved`.

### 4.2 The Perceive-First Surface Exposure Filter
To prevent agents from bypassing AAG's `safety.perceive_first` gate with cheap no-ops, TOB enforces a strict surface exposure filter:
* Invocations of `nova.search_text` **do not qualify** as surface exposure, even though they expose text.
* Only substantive observation tools (`nova.perceive`, `nova.read_text`, `nova.read_dom`, `nova.dom_extract`) set `_surfaceExposedByTarget = true`.

### 4.3 The Multi-Channel Click Effect Observation Engine

A persistent flaw in web automation is the "silent dead click": dispatching a synthetic click event onto an unmounted element, an element without an attached event listener, or an element whose handler has not yet bound will return `ok: true`. The language model interprets `ok: true` as proof that the action succeeded, even though the page state never changed.

To solve this, TOB runs a multi-channel effect observer for `nova.click_selector` that monitors **nine distinct observation channels**:

```mermaid
flowchart TD
    Click["nova.click_selector Dispatched"] --> Channels{"Did anything actually happen?"}
    
    subgraph ProbeChannels ["In-Page Probe Channels (DOM / Network)"]
        Channels --> C1["1. dom_mutation: DOM tree or attribute changed"]
        Channels --> C2["2. request_started: Network request initiated"]
        Channels --> C3["3. focus_moved: Focus shifted (ignoring clicked element)"]
        Channels --> C4["4. control_state: IDL state flipped (.checked, select index)"]
    end

    subgraph HostChannels ["Host-Side Channels (Nova Engine)"]
        Channels --> C5["5. url_changed: URL modified"]
        Channels --> C6["6. navigation: Navigation committed"]
        Channels --> C7["7. new_tab: New tab spawned"]
        Channels --> C8["8. popup: Popup opened"]
        Channels --> C9["9. download: File download started"]
    end

    ProbeChannels --> Eval{"Evaluate Outcome"}
    HostChannels --> Eval

    Eval -->|Any Channel Fired| ObservedTrue["observation.Observed = true<br/>Signals enumerated"]
    Eval -->|Probe Armed + All 9 Silent| ObservedFalse["observation.Observed = false<br/>Emit dead-element warning"]
    Eval -->|Probe Failed to Arm + No Host Signal| ObservedNull["observation.Observed = null<br/>Absence of evidence != Evidence of absence"]
```

#### Core Invariants of the Effect Engine:
1. **Host Evidence Trumps Probe Failure:** If host-level events fire (navigation, new tab, popup, download, URL change), the click is confirmed effective (`observation.Observed = true`) even if the in-page JavaScript probe failed to arm.
2. **Absence of Evidence is Not Evidence of Absence:** If the in-page probe fails to inject and no host events fire, Nova records `observation.Observed = null`. It **never** reports `false`, preventing false-positive dead element warnings caused by instrumentation failures.
3. **The Control State Invariant (QM-4150):** Toggling native HTML inputs (e.g. checkbox `.checked` or `<select>` options) modifies DOM IDL properties without necessarily generating MutationObserver attribute mutations or network requests. The probe explicitly checks control state diffs to avoid incorrectly calling working form inputs "dead".
4. **Actionable Dead Element Warnings:** When all 9 channels remain silent and the probe was fully functional, Nova includes an explicit warning enumerating every checked channel (`no DOM mutation, no started request, no focus move, no control state change`). Crucially, the warning suggests verifiable remedies (`verify` or check for asynchronous processing delays) without making unproven assumptions (such as asserting "handler is not wired up").

---

## 5. Scope Lifecycle State Machine & The 8 Core Invariants

To prevent unbounded database growth during regular interactive browsing, TOB observations are **scope-gated**: they are only projected to SQLite when an active workflow scope exists (such as a running ETM task instance or a tab claim lease).

```mermaid
stateDiagram-v2
    [*] --> Open: OpenScope(request)
    Open --> Active: TryActivate(scopeId) / Drain Prelude
    Active --> Closing: BeginClosing(epilogueGraceMs=750)
    Closing --> Flushing: MarkFlushing(barrierSeq)
    Flushing --> Closed: MarkClosed(ingestionComplete)
    Flushing --> Active: ReactivateScope() (on evidence rejection)
    Open --> Faulted: Fault(reason)
    Active --> Faulted: Fault(reason)
    Closing --> Faulted: Fault(reason)
    Flushing --> Faulted: Fault(reason)
    Closed --> [*]
    Faulted --> [*]
```

### The 8 Frozen Scope Invariants
1. **Single Identity Invariant:** Every dispatch receives exactly one `dispatch_call_id` and monotonic `dispatch_seq`.
2. **Bracketing Guarantee:** Pre-State is captured strictly before tool execution; Post-State is captured strictly in `finally`.
3. **Single Scope Binding:** A dispatch may bind to at most one workflow scope (`WorkflowScopeBinding`).
4. **Mutual Exclusion per Target:** Only one scope in states `open | active | closing` may exist for any given `target_session_id`.
5. **No Binding in Flushing:** Once a scope enters `flushing`, no new dispatches can bind to it.
6. **Frozen Sequence Barrier:** `barrier_seq` is strictly frozen upon entering `flushing`; all dispatches with `seq <= barrier_seq` must commit before correlation runs.
7. **Complete Ingestion Prerequisite:** Grade `none` may only be assigned when data ingestion and projection are 100% complete; any gap degrades to `unknown`.
8. **Retention Precedence:** Scope retention never prunes records before the task's final `evidence_snapshot_json` is generated.

### 5.1 In-Memory Prelude Buffer
When an agent performs setup calls (navigating to a starting URL, dismissing an initial popup) *before* explicitly creating an ETM task instance, those dispatches are unscoped.
* Unscoped dispatches are held in an in-memory ring buffer (`PreludeBuffer`: max 512 per target, max 4,096 globally, 60s TTL).
* When `OpenScope` is invoked, TOB drains the last 30 seconds (`PreludeWindowMs = 30_000`) of matching dispatches and backfills them into `tob_tool_observation` with `binding_mode = 'prelude_backfill'`.
* **Per-Target Overflow Isolation:** The ring buffer tracks buffer overflows strictly per target (`_overflowByTarget[targetKey]`). An overflow on an unrelated tab does not mark another tab's prelude drain as incomplete, preventing artificial degradation to `unknown`.

### 5.2 Epilogue Grace Window
When a task requests completion, the agent may have issued a final verification call that is still in transit.
* `BeginClosing` initiates an `epilogue_grace_ms` period (default **750 ms**).
* Any calls completing within this grace window bind with `binding_mode = 'epilogue_grace'` before the sequence barrier is locked.

### 5.3 Scope Reactivation on Evidence Rejection
When an agent attempts task completion, Nova flushes the sequence barrier and evaluates the Evidence Ledger. If the evidence gate rejects the completion (e.g. required strong evidence but observed weak or none), the scope is **not closed or aborted**:
1. `TobFlushCoordinator.ReactivateScopeAfterRejection` closes existing visit windows to prevent dwell times from bleeding across the rejection boundary.
2. The scope coordinator transitions the scope from `Flushing` back to `Active`.
3. The barrier is cleared (`BarrierDispatchSeq = null`), allowing new tool dispatches to bind to the **same** workflow scope.
4. The agent receives the specific rejection diagnostic and can perform additional verification actions before attempting completion again.
5. Only upon passing the evidence gate does `CloseScopeAfterGate` mark the scope as `Closed`.

### 5.4 Crash Recovery Invariant (`RecoverFromDb`)
If Nova AI Workspace terminates unexpectedly while scopes are active, `EvidenceScopeCoordinator.RecoverFromDb()` runs on startup:
* Recovers all scopes in states `open`, `active`, `closing`, or `flushing` from `tob_scope_runtime`.
* Restores them to `Active` in memory, rebuilding reverse target indexes (`ActiveBindings`) so target tabs are not deadlocked against new scopes.

### 5.5 Process-Wide Static Isolation in Tests (`ResetTobStaticsForSelfTest`)
In production, `McpServer` is a single process singleton. However, in test suites, multiple `McpServer` instances are constructed within a single process.
* To prevent cross-test contamination where a newly instantiated test server inadvertently hijacks the static scope coordinator of a previous test (QM-3836), Nova provides `ResetTobStaticsForSelfTest()` and `InstallTobScopeCoordinatorForSelfTest()`.
* Every isolated unit test starts with a completely clean static slate.

---

## 6. The Flush & Barrier Protocol (`TobFlushCoordinator`)

Before an evidence consumer (such as the ETM Evidence Ledger) can grade task completion, it must guarantee that all asynchronous background worker threads have flushed their data to disk.

```mermaid
sequenceDiagram
    autonumber
    participant Consumer as ETM Task Completion Gate
    participant Coord as TobFlushCoordinator
    participant Scope as EvidenceScopeCoordinator
    participant OK as OK Store Worker
    participant LCJ as LCJ Worker
    participant TOB as ToolObservationProjector Worker
    participant Win as VisitWindowBuilder

    Consumer->>Coord: FlushScopeAsync(scopeId)
    Coord->>Scope: BeginClosing(epilogueGraceMs=750)
    Note over Coord: Sleep 750ms for in-flight calls to land
    Coord->>Scope: MarkFlushing(barrierSeq = LastBoundDispatchSeq)
    
    par Concurrently wait for barrierSeq
        Coord->>OK: WaitForOkFlushAsync(barrierSeq)
        Coord->>LCJ: WaitForLcjFlushAsync(barrierSeq)
        Coord->>TOB: WaitForFlushAsync(barrierSeq)
    end
    
    Coord->>Win: CloseAllWindows(scopeId)
    Note over Win: Force-materialize open in-memory visit window!
    Coord-->>Consumer: Return FlushResult (ingestionComplete, projectionComplete)
```

### 6.1 The In-Memory Visit Window Flush Invariant
> [!IMPORTANT]
> The visit window of the page the agent is currently sitting on resides *purely in memory* (`VisitWindowBuilder._openWindows`) until a page change occurs or the scope closes.
> 
> If the flush protocol did not explicitly close the window, the current page would never count as a materialized visit window in SQLite! `TobFlushCoordinator` calls `_visitWindowBuilder.CloseAllWindows(scopeId)` before returning, ensuring the open window is inserted into `tob_visit_window` ahead of the correlation query.

### 6.2 The Barrier Non-Stall Guarantee
In `ToolObservationProjector`, database writes execute asynchronously on a background worker thread.
* If an insertion fails due to an unexpected SQLite exception or disk constraint, the sequence counter advancement (`AdvanceCommittedSeq`) and projected count increment still execute inside a guaranteed `finally` block.
* This ensures that `WaitForFlushAsync` will **never hang indefinitely or stall the barrier**. The missing observation may result in an `unknown` grade, but the execution pipeline remains fully operational.

---

## 7. Database Schema & Storage Architecture (`pks.db`)

All TOB tables reside in `pks.db` and are initialized via Migrations V14 and V15:

```mermaid
erDiagram
    tob_scope_runtime ||--o{ tob_scope_binding : "binds"
    tob_scope_runtime ||--o{ tob_scope_source_watermark : "tracks"
    tob_scope_runtime ||--o{ tob_tool_observation : "projects"
    tob_scope_runtime ||--o{ tob_visit_window : "aggregates"
    tob_scope_runtime ||--o{ tob_claim_event : "audits"
    task_instance ||--o{ task_instance_unit_locator : "locates"

    tob_tool_observation {
        text observation_id PK
        text workflow_scope_id FK
        text dispatch_call_id
        integer dispatch_seq
        text tool_name
        text action_kind
        integer signal_flags
        integer ok
        text page_url_effective_norm
        text selector_hash
        text outcome_kind
        integer executed
        text gate_id
    }

    tob_visit_window {
        text window_id PK
        text workflow_scope_id FK
        text page_url_norm
        text route_key_norm
        integer started_at_ms
        integer dwell_time_ms
        integer observation_count
        integer read_count
        integer union_signal_flags
    }
```

### 7.1 Relational Table Catalog

| Table Name | Primary Role | Retention Policy |
| :--- | :--- | :--- |
| **`tob_tool_observation`** | Relational projection of executed or blocked tool calls. | Scope End + 7d (normal) / 30d (problematic) |
| **`tob_visit_window`** | Materialized, coalesced page visits with dwell times and read counts. | Scope End + 7d (normal) / 30d (problematic) |
| **`tob_claim_event`** | Audit log of agent status claims (`unit_checked`). | Scope End + 30d |
| **`tob_scope_runtime`** | Scope lifecycle state machine and barrier metadata. | Scope End + 30d |
| **`tob_scope_binding`** | Multi-target session and tab bindings for scopes. | Cascades on scope deletion |
| **`tob_scope_source_watermark`** | Ingestion barrier watermarks per data pipeline. | Cascades on scope deletion |
| **`task_instance_unit_locator`** | Typed locator definitions for ETM work units. | Task Instance Lifetime |
| **`tob_lcj_durable_outbox`** | Reserved durability bridge for future LCJ integration. | Scope End + 7d / 30d |

### 7.2 The Outbox Durability Bridge Semantics (`tob_lcj_durable_outbox`)
The `tob_lcj_durable_outbox` table records selector interactions alongside dispatch call IDs and outcomes.
* **Current Status:** This table is currently write-only (with severity recorded as a literal `0` placeholder). It is an architectural reservation designed as a durable persistence bridge for future out-of-process LCJ consumers.
* Today, LCJ consumes observations in-memory via `McpServer.ExecutionLcjObservation`. The outbox table is reaped by `TobRetentionPolicy` and must not be treated by external clients as an active bidirectional queue.

### 7.3 Single-Worker DB Channel & Deadlock Prevention
`PksStore.GetDb()` operates over a single-worker asynchronous queue.
* To prevent deadlocks, lightweight status queries (`task_instance_get`, `get_instructions`) invoke `EvidenceLedger.CorrelateSummary()` instead of the full `Correlate()` method.
* For completed instances, `CorrelateSummary()` reads the pre-compiled `evidence_snapshot_json` via fast JSON parsing without touching SQLite queries.
* For active instances, it queries unit counts on the already-open connection directly without invoking nested `ExecuteAsync` calls on the worker channel.

---

## 8. Evidence Ledger & Task Verification (`EvidenceLedger`)

When an autonomous task instance completes, the **Evidence Ledger** evaluates whether the agent's claims are backed by physical evidence:

```mermaid
flowchart TD
    Unit["Claimed 'checked' Unit"] --> LocCheck{"Has Locators?"}
    LocCheck -->|No Locators| Unknown["Grade: unknown (no_locator)"]
    LocCheck -->|Yes| DetCheck{"Deterministic Locator?"}
    DetCheck -->|No| Unknown2["Grade: unknown (no_deterministic_locator)"]
    DetCheck -->|Yes| ObsCheck{"Matching Observations in Scope?"}

    ObsCheck -->|None Found| IngestionCheck{"Ingestion & Projection Complete?"}
    IngestionCheck -->|Incomplete / Gap| Unknown3["Grade: unknown (source_gap / incomplete)"]
    IngestionCheck -->|Complete| NoneGrade["Grade: none (Proven Missing Evidence)"]

    ObsCheck -->|Observations Found| WinCheck{"Visit Window with Read Signal & Dwell >= 1s?"}
    WinCheck -->|Yes + Exact URL/Route| Strong["Grade: strong (Verified Content Exposure)"]
    WinCheck -->|No / Selector-only| Weak["Grade: weak (Interacted but Not Proven Read)"]
```

### 8.1 Evidence Grades

| Evidence Grade | Required Criteria | Practical Meaning |
| :---: | :--- | :--- |
| **`strong`** | Matching visit window in `tob_visit_window` with `read_count > 0`, `dwell_ms >= 1000` (1 second), and exact URL or route locator match. | Strong proof that the target page was loaded, displayed, and content was returned to the agent for at least 1 second. |
| **`weak`** | Matching observation exists in `tob_tool_observation`, but lacks a substantive read signal, lacks a visit window, or is located *only* by selector hash or URL prefix. | The agent touched or interacted with the target, but content exposure or dwell time was not established. |
| **`none`** | Deterministic locators exist, data ingestion and projection are 100% complete, and zero matching observations exist. | **Proven fabrication / omission:** The agent claimed completion, but Nova observed zero corresponding actions. |
| **`unknown`** | No deterministic locators exist, or a measurement gap occurred (`unknown_due_to_source_gap`, `projection_incomplete`, `scope_binding_missing`). | Indeterminate: Nova cannot prove or disprove the claim due to missing instrumentation. |

### 8.2 The "Strong" Grade Ceiling Invariant
> [!IMPORTANT]
> Grade `strong` is **strictly achievable only for locator types `url_exact` and `route_key`**.
> 
> In `EvidenceLedger.CountStrongVisitWindows`, visit windows are evaluated via:
> ```sql
> SELECT COUNT(*) FROM tob_visit_window
> WHERE workflow_scope_id = @scope AND read_count > 0 AND dwell_ms >= 1000 AND (page_url_norm = @val OR route_key_norm = @val)
> ```
> Because `tob_visit_window` coalesces page-level interactions and does not maintain a selector index, work units whose sole deterministic locator is a DOM selector (`selector_hash`) or a URL prefix (`url_prefix`) can at most achieve grade `weak`. Individual element interactions prove execution, but only visit windows prove sustained page dwell time.

### 8.3 Unit Locator Inference & Normalization Engine (`TobUnitLocatorWriter`)

Work units defined in ETM are automatically analyzed to infer typed locators:

| Unit Kind / Input Pattern | Inferred Locator Type | Normalization Algorithm | Match Key | Achievable Grade Ceiling |
| :--- | :--- | :--- | :--- | :---: |
| `unit_kind: "selector"` | `selector` | `SelectorNormalizer.NormalizeSelector` | SHA-256 Hex Hash | `weak` |
| `unit_kind: "document"` or `"pdf"` | `document_page` | Trimmed string | Trimmed string | `weak` |
| Starts with `http://` or `https://` | `url_exact` | `SiteUrlCanonicalizer.Canonicalize` | Route URL without query/hash | `strong` |
| Starts with `#`, `.`, `[`, or contains `>`, `+`, `~` | `selector` | `SelectorNormalizer.NormalizeSelector` | SHA-256 Hex Hash | `weak` |
| Starts with `/` or path-like string | `route_key` | Trimmed lowercase without slashes | `null` | `strong` |
| Domain-like string (contains `.`) | `url_exact` | Canonical route URL | Scheme + Host + Path | `strong` |

### 8.4 The Complete Exception Reason Code Catalog (`perUnitExceptions`)

When a checked work unit does not achieve `strong`, the ledger records precise diagnostic reason codes:

| Reason Code | Grade | Cause & Trigger Condition |
| :--- | :---: | :--- |
| **`visit_window_missing`** | `weak` | Read observations were recorded, but no visit window on that URL met the dwell threshold (`dwell_ms >= 1000`). |
| **`no_read_like_observation`** | `weak` | Tool interactions occurred on the locator (e.g. clicks or input), but no content-reading tool was executed. |
| **`scope_binding_missing`** | `unknown` | The task instance lacked an active workflow scope ID. |
| **`no_locator`** | `unknown` | The work unit definition contained zero locators. |
| **`no_deterministic_locator`** | `unknown` | Locators exist, but none belong to the `declared` or `derived` deterministic classes. |
| **`unknown_due_to_source_gap`** | `unknown` | Upstream ingestion (OK or LCJ) timed out or encountered an uncommitted buffer gap. |
| **`projection_incomplete`** | `unknown` | Tool observation projection did not reach the sequence barrier within the flush timeout. |
| **`no_matching_observation`** | `none` | Deterministic locators exist and data pipelines were 100% complete, but zero matching tool calls occurred. |

### 8.5 The Evidence Snapshot Schema (`evidence_snapshot_json`)
Upon task completion, the ledger compiles an immutable JSON summary saved to `task_instance.evidence_snapshot_json`:

```json
{
  "schemaVersion": 1,
  "workflowScopeId": "scope-9f8a2b1c",
  "completedAtMs": 1728394000120,
  "completeness": {
    "ingestionComplete": true,
    "projectionComplete": true,
    "budgetTruncated": false
  },
  "counts": {
    "claimedCheckedUnits": 12,
    "observedCheckedUnits": 11,
    "strong": 10,
    "weak": 1,
    "none": 1,
    "unknown": 0
  },
  "perUnitExceptions": {
    "itemCount": 2,
    "items": [
      {
        "unitKey": "doc-terms-page",
        "evidenceGrade": "weak",
        "reasonCodes": ["no_read_like_observation"]
      },
      {
        "unitKey": "doc-refund-policy",
        "evidenceGrade": "none",
        "reasonCodes": ["no_matching_observation"]
      }
    ]
  }
}
```

---

## 9. Autonomous PKS Selector Proof (`TobSelectorProofEmitter`)

When an agent interacts with web pages, TOB autonomously validates and promotes UI patterns in the Phenomenological Knowledge Store (PKS) without requiring the agent to self-report:

```mermaid
flowchart LR
    ToolCall["Scoped Tool Call Succeeds (ok=1)"] --> FlagCheck{"Has SelectorTouched flag?"}
    FlagCheck -->|Yes| Hash["Extract SelectorHash (SHA-256)"]
    Hash --> Scope["Normalize Page Scope"]
    Scope --> Match{"Matches known PKS Phenomenon?"}
    Match -->|Yes| Throttle{"Throttled? (< 60s since last proof)"}
    Throttle -->|No| Emit["Emit 'tob_verified' Telemetry under _pksWriteLock"]
    Emit --> Health["Increment PKS Health & Success Count"]
```

* **Zero Agent Overhead:** Operates entirely in the background. If a scoped call touches a selector whose SHA-256 hash matches a known phenomenon on that domain, TOB reports `tob_verified`.
* **60-Second Throttle:** Emits at most one proof per `(scope, phenomenon)` pair per 60 seconds (`ThrottleIntervalMs = 60_000`), preventing rapid loops from skewing health statistics.
* **Thread-Safe Telemetry:** Held under `_pksWriteLock` to prevent concurrent `pks_upsert` calls from overwriting health counters.
* **Alternative Selector Splitting:** When phenomena contain OR-alternatives (`#btn-submit OR .action-btn`), `TobSelectorProofIndex` normalizes and indexes each sub-selector individually, matching single agent dispatches cleanly.

---

## 10. AAG Preflight Block Recording (Migration V15)

When an Agent Awareness Gate (such as `setup.bootstrap_required` or `safety.perceive_first`) halts a tool call, the tool implementation never executes. However, recording this attempt is vital for debugging and compliance.

TOB handles this via **Blocked Preflight Projections** (`TryProjectBlocked`):
* **Schema Fields:** `ok = 0`, `executed = 0`, `outcome_kind = 'blocked_preflight'`, `block_stage = 'aag_preflight'`, `error_code = 'aag_blocked:<gateId>'`.
* **Unscoped Projection:** Blocked calls are written unscoped (`workflow_scope_id = NULL`), as an awareness failure occurs before scope binding can take place.
* **Gate Mode Separation:** The configured gate mode (`Block`, `ShadowBlock`, `Warn`) is **not stored** in the database row; it is resolved dynamically from settings to prevent stale data.

---

## 11. Dual-Tier Retention Policy (`TobRetentionPolicy`)

To maintain high SQLite query performance and prevent database file bloat, TOB implements an automated, dual-tier retention policy:

```mermaid
flowchart TD
    Job["Retention Job (Fire-and-Forget)"] --> Classify{"Scope Status & Class"}
    Classify -->|Clean Normal Scope (closed)| R1["Delete if closed_at_ms > 7 Days"]
    Classify -->|Problematic Scope (none, unknown, incomplete, faulted)| R2["Delete if closed_at_ms > 30 Days"]
    Classify -->|Unscoped Blocked Calls (blocked_preflight)| R3["Delete if projected_at_ms > 30 Days"]

    R1 --> Prune["Delete from tob_scope_runtime & Cascade to Children"]
    R2 --> Prune
    R3 --> Prune
    Prune --> Orphan["Delete Orphaned Observations & Visit Windows"]
```

* **Normal Scopes (7 Days):** Cleanly completed scopes with full ingestion and zero exceptions are purged after 7 days.
* **Problematic Scopes (30 Days):** Scopes containing `none` or `unknown` grades, incomplete ingestion, or faulted terminations are retained for 30 days to facilitate operator audits.
* **Unscoped Blocked Calls (30 Days):** AAG blocked-call observations are pruned after 30 days based on `projected_at_ms`.
* **Defensive CASCADE Deletion:** Explicitly pre-deletes child rows in `tob_scope_binding` and `tob_scope_source_watermark` before removing runtime rows, protecting legacy databases against SQLite Error 19 foreign key failures.

---

## 12. Operational Health Metrics (`TobHealthMetrics`)

To diagnose whether a poor task verification score was caused by agent incompetence or browser infrastructure delays, TOB tracks atomic operational metrics:

| Metric Name | Type | Diagnostic Meaning |
| :--- | :---: | :--- |
| `ScopeGatedCallCount` | Counter | Total tool calls evaluated against active scopes. |
| `BackfilledPreludeCallCount` | Counter | Unscoped calls rescued from the prelude buffer and bound to a new scope. |
| `ProjectedObservations` | Counter | Total observations written to `tob_tool_observation`. |
| `VisitWindowsFlushed` | Counter | Total visit windows materialized to `tob_visit_window`. |
| `ClaimEventsWritten` | Counter | Total agent claim events recorded in `tob_claim_event`. |
| `FlushTimeouts` | Counter | Number of times a sequence barrier timed out waiting for subsystem flushes. |
| `IngestionIncompleteCompletions` | Counter | Tasks completed while data pipelines had uncommitted in-flight dispatches. |
| `UnscopedDropCount` | Counter | Unscoped calls discarded after prelude buffer overflow. |
| `SelectorProofEmitted` | Counter | Total autonomous PKS selector proof telemetry events dispatched. |

---

## 13. Summary: The TOB Architectural Matrix

| Layer / Component | Core Responsibility | Invariant / Guarantee | Primary Failure Mode Addressed |
| :--- | :--- | :--- | :--- |
| **Dispatch Envelope** | Atomic before/after capture. | Captures post-state in guaranteed `finally`; unique UUIDv4 call ID. | Prevents unrecorded dispatches on unhandled tool crashes. |
| **Foreign Target Resolver** | Multi-tab identity binding. | Traced background target never borrows active foreground tab URL. | Prevents attributing background clicks to the foreground URL. |
| **Effect Observer** | Multi-channel click impact evaluation. | Checks 9 distinct channels; probe failure yields `null` (never false). | Prevents treating dead/unbound click handlers as successful effects. |
| **Prelude Buffer** | Unscoped call preservation. | Holds up to 512 dispatches per target in RAM; drains upon scope activation. | Captures setup navigations executed prior to formal task creation. |
| **Epilogue Grace Window** | In-flight completion grace. | Delays barrier freezing by 750 ms for late verification calls. | Prevents dropping final verification clicks from task evidence. |
| **Flush Coordinator** | Multi-subsystem synchronization. | Waits for OK, LCJ, and Projector up to frozen `barrier_seq`. | Eliminates race conditions between async DB writes and task evaluation. |
| **Visit Window Builder** | Temporal interaction aggregation. | Coalesces continuous interactions; splits on inactivity > 2.5s. | Synthesizes true dwell time from individual discrete tool calls. |
| **Evidence Ledger** | Mathematical proof grading. | Grade `none` strictly prohibited unless ingestion is 100% complete. | Prevents falsely accusing an agent of omission during telemetry lag. |
| **Selector Proof Emitter** | Autonomous PKS promotion. | Auto-emits `tob_verified` on selector hash match; 60s throttle. | Continuously validates UI playbooks without agent self-reporting. |
| **AAG Block Projector** | Preflight block audit trail. | Projects blocked calls with `outcome_kind = 'blocked_preflight'`. | Distinguishes awareness-gate blocks from tool execution failures. |
| **Dual-Tier Retention** | SQLite bloat & prune control. | 7-day clean / 30-day problematic retention; pre-delete CASCADE safety. | Prevents SQLite disk space exhaustion and query latency degradation. |

---

## Related Documentation

* **[Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md)** — Precondition gates and tab leasing in the MCP dispatch pipeline.
* **[Closed-Loop System (CLS)](../closed-loop-system-cls/README.md)** — Transition contracts, stability verification, and outcome reaction.
* **[Phenomenological Knowledge Store (PKS)](../learning/phenomenological-knowledge-store-pks/README.md)** — Procedural UI memory, playbooks, and autonomous health tracking.
* **[Episodic Task Memory (ETM)](../learning/episodic-task-memory-etm/README.md)** — Work unit tracking, task URL coverage, and evidence ledger consumers.
* **[Agent Learning Pipeline (ALP)](../learning/agent-learning-pipeline-alp/README.md)** — Knowledge promotion and journal evaluation.

[All core features](../README.md)
