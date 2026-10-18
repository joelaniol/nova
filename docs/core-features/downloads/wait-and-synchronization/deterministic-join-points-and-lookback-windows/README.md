# Deterministic Join Points & Anchored Lookback Windows

> **Bridging browser actions and verified file system artifacts — eliminating heuristic sleeps, the Anchored Window Invariant, and terminal state evaluation.**

---

## 1. The Agent Synchronization Dilemma

In autonomous browser automation, triggering an action and operating on its resultant file on disk are inherently asynchronous and decoupled:

1. **The Heuristic Sleep Trap:** An autonomous agent clicks an "Export Report" button and executes a fixed sleep (e.g. `sleep 5000`). If the network is slow or the server takes 6 seconds to generate the file, the agent wakes up, finds no file, and fails. Conversely, if the download completes in 200ms, the agent wastes 4.8 seconds of idle latency.
2. **The Race Condition Hazard:** If an agent polls the file system directly, it risks reading a partial download segment (`.crdownload` or temporary file lock) before Chromium flushes and renames the file to its final extension, resulting in corrupt data parsing.
3. **The Sliding Window Trap:** If a polling loop queries downloads within the "last 5 seconds" on every iteration, the lookback cutoff slides forward with time. By the time the download finishes, the initiation timestamp has fallen outside the sliding window, causing the wait to drop the file and time out.

Nova resolves these issues with **`nova.downloads_wait`**, creating a deterministic synchronization join point backed by the **Anchored Window Invariant**.

```mermaid
sequenceDiagram
    autonumber
    participant Agent as AI Agent
    participant Nova as Nova MCP Dispatcher
    participant DL as Download Pipeline
    participant Disk as Local File System

    Agent->>Nova: nova.click_selector("button#export-csv")
    Nova-->>Agent: Click Action Delivered OK
    
    rect rgb(240, 248, 255)
        Note over Agent,Nova: Deterministic Join Point
        Agent->>Nova: nova.downloads_wait(sinceMs=5000, timeoutMs=30000)
        Note over Nova: Fixed Anchor: Cutoff = DateTime.UtcNow - 5000ms<br/>(NEVER slides forward during polling)
    end

    loop Every 100ms
        Nova->>DL: Query candidate downloads >= Cutoff
        DL-->>Nova: [ { id: "dl-91", status: "in_progress", bytes: 45000 } ]
    end

    DL->>Disk: Finalize byte stream & release temp lock
    DL-->>Nova: [ { id: "dl-91", status: "completed", filePath: "C:\\...\\export.csv" } ]
    
    Nova-->>Agent: { ok: true, status: "completed", downloads: [ { filePath: "..." } ] }
    Agent->>Disk: Safely parse complete, unlocked "export.csv"
```

---

## 2. The Anchored Window Invariant

The core architectural guarantee of `nova.downloads_wait` in lookback mode is the **Fixed Anchor**:

```mermaid
flowchart LR
    subgraph BadPattern ["Sliding Window (Anti-Pattern)"]
        S1["T=0: Cutoff = T-5s"] --> S2["T=3: Cutoff = T-2s"]
        S2 --> S3["T=6: Cutoff = T+1s<br/>(Initiation point lost!)"]
    end

    subgraph GoodPattern ["Anchored Window (Nova Architecture)"]
        A1["Call Received at T=0<br/>Anchor = UtcNow - sinceMs"] --> A2["T=3s Poll: Filter >= Anchor"]
        A2 --> A3["T=6s Poll: Filter >= Anchor<br/>(Initiation point securely preserved!)"]
    end
```

> [!IMPORTANT]
> When `nova.downloads_wait` receives a `sinceMs` argument (default: `10000` ms), the cutoff timestamp (`DateTime.UtcNow - TimeSpan.FromMilliseconds(sinceMs)`) is computed **exactly once** at the beginning of the call.
> 
> During the subsequent 100ms polling loop, this cutoff is **strictly immutable**. Even if a large download takes 45 seconds to stream, its initiation timestamp remains comfortably after the fixed anchor, guaranteeing that Nova never loses track of the transfer.

---

## 3. Dual Modes of Operation

`nova.downloads_wait` operates in one of two mutually exclusive modes:

| Dimension | Single Download Mode (`id`) | Lookback Window Mode (`sinceMs`) |
| :--- | :--- | :--- |
| **Primary Trigger** | Download ID is already known (from `downloads_list` or API). | Immediately follows a UI action (click, form submit). |
| **Target Filter** | Exact GUID matching. | All transfers initiated $\ge$ the fixed anchor cutoff. |
| **Batch Arrival Grace**| **Skipped** (immediate return upon settlement). | **Active** (evaluates 400ms late-arrival grace period). |
| **Mutual Exclusivity** | Must not include `sinceMs`. | Must not include `id`. |

### Argument Validation Error (-32602)
Supplying both `id` and `sinceMs` in the same call is an invalid state:
```json
// Error response
{
  "code": -32602,
  "message": "Invalid parameters: Provide either 'id' or 'sinceMs', not both."
}
```

---

## 4. Polling Cycle & Terminal Status Settlement

During the wait execution, Nova checks the download state engine every 100 milliseconds:

```mermaid
flowchart TD
    PollStart["100ms Polling Tick"] --> FilterMatches["Filter candidate downloads >= Anchor"]
    FilterMatches --> AnyMatch{"Any downloads found?"}

    AnyMatch -- "Yes" --> CheckTerminal{"Are all matched downloads settled?<br/>(completed, failed, cancelled)"}
    CheckTerminal -- "Yes" --> BatchGrace{"Batch Grace Check<br/>(Has 400ms elapsed with no new siblings?)"}
    BatchGrace -- "Settled & Stable" --> ReturnSettled["Return ok: true<br/>status: 'completed' / 'failed'"]
    BatchGrace -- "Waiting Grace" --> SleepTick["Wait 100ms"] --> PollStart

    CheckTerminal -- "No" --> CheckAllPaused{"Are all pending downloads paused?"}
    CheckAllPaused -- "Yes" --> ReturnPaused["Early Exit: status: 'paused'"]
    CheckAllPaused -- "No" --> CheckTimeout

    AnyMatch -- "No" --> CheckBlockedRegistry{"BlockedAutomaticDownloads logged?"}
    CheckBlockedRegistry -- "Yes" --> ReturnBlocked["Early Exit: status: 'blocked'"]
    CheckBlockedRegistry -- "No" --> CheckTimeout{"Elapsed >= timeoutMs?"}

    CheckTimeout -- "Yes" --> ReturnTimeout["Return ok: false<br/>status: 'timeout'"]
    CheckTimeout -- "No" --> SleepTick
```

### Settlement Classifications

1. **`completed`:** All matching downloads transferred their complete byte payload, passed integrity verification, and finalized their destination disk paths.
2. **`failed`:** At least one matching download terminated with an error (e.g. `NETWORK_FAILED`, `SERVER_FORBIDDEN`). The error code and reason are populated in the response array.
3. **`cancelled`:** The user or an agent explicitly called `nova.downloads_cancel` on the operation.
4. **`paused`:** The wait detected that all active transfers have been suspended and halts early to avoid burning timeout latency.

---

## 5. Practical Tool Recipes

### Recipe 1: Click, Wait, and Parse
Trigger a CSV export and synchronously retrieve the resolved file path:

```json
// Step 1: Click the export button
// nova.click_selector
{
  "selector": "button#download-sales-csv"
}

// Step 2: Synchronize with download pipeline
// nova.downloads_wait
{
  "sinceMs": 5000,
  "timeoutMs": 30000
}
```

Example successful response:
```json
{
  "ok": true,
  "status": "completed",
  "reasonCode": "none",
  "waitedMs": 1420,
  "downloadCount": 1,
  "completedCount": 1,
  "failedCount": 0,
  "cancelledCount": 0,
  "pendingCount": 0,
  "pausedCount": 0,
  "downloads": [
    {
      "id": "f8a1c3e4-2b9d-47a6-91e0-8c2d5e7b3a1f",
      "fileName": "sales_q3_2026.csv",
      "filePath": "C:\\Users\\Operator\\Downloads\\sales_q3_2026.csv",
      "status": "completed",
      "bytesReceived": 2841902,
      "totalBytes": 2841902,
      "url": "https://dashboard.corp/api/sales/export"
    }
  ],
  "truncated": false,
  "resumable": false
}
```

---

## 6. Related Architecture Guides

* [Batch Grace Periods & Resumable Watches](../batch-grace-periods-and-resumable-watches/README.md): 400ms batch buffer, early-exit heuristics, and resumable watch continuation.
* [Wait Synchronization Hub](../README.md): High-level domain overview for deterministic wait synchronization.
* [Dual-Engine Transfers & Parked WebViews](../../lifecycle-and-queue/dual-engine-transfers-and-parked-webviews/README.md): Stream mechanics and tab closure parking.
* [Executable Gates & Security Prompts](../../security-and-policy/executable-gates-and-security-prompts/README.md): Pre-flight executable verification.
* [Downloads Master Hub](../../README.md): Master subsystem architectural catalog.
