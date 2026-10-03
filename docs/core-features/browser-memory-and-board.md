# Browser Memory & Knowledge Board (User Context & Team Collaboration)

> [!NOTE]
> **Browser Memory** (`NovaBrowser.Core.BrowsingMemoryRepository`) and the **Knowledge Board** (`NovaBrowser.Core.KnowledgeBoard`) form the user-centric and collaborative memory tier of Nova AI Workspace. They preserve cross-session operator preferences with biological time-decay and allow multi-agent swarms to share intermediate findings on a synchronized whiteboard.

---

## 1. Problem Statement & Motivation

Cognitive browser automation architectures typically distinguish only site mechanics (PKS) and transient tab state (OK):
1. **Loss of Personal Context:** An operator reviews pull request #42 on `github.com` and records notes about unresolved discussion points. Following a browser reboot, the agent forgets these notes, forcing the user to restate the entire context.
2. **Missing Time-Decay:** Notes that were critical 6 months ago (e.g. a temporary layout workaround) permanently pollute prompt context if they never expire.
3. **Absence of Multi-Agent Coordination:** When multiple subagents conduct concurrent research (e.g. competitive pricing audits), they lack a shared scratchpad where Agent A can post discoveries for Agent B.

**Nova AI Workspace** resolves this through a dual-layer memory architecture:
* **Browser Memory:** Domain-bound personal operator notes with mathematically calibrated half-lives.
* **Knowledge Board:** A global, thread-safe whiteboard for asynchronous multi-agent coordination.

---

## 2. The Mathematical Decay Model

Browser Memory implements an exponential forgetting curve modeled after biological retention:
$$\text{Relevance}(t) = \text{InitialWeight} \times e^{-\lambda \cdot \Delta t}$$

Each memory category is calibrated with a tailored half-life:

| Memory Category | Half-Life | Purpose |
| :--- | :---: | :--- |
| **`preference`** | **120 Days** | Stable operator preferences (e.g. "prefers dark mode", "always summarize in German"). |
| **`note`** | **60 Days** | General workflow notes regarding website behaviors and project milestones. |
| **`context`** | **14 Days** | Short-lived operational context (e.g. "Ticket #104 in progress, awaiting review"). |

* **Reinforcement on Access:** Every recall query (`nova.memory_recall`) updates the access timestamp, slowing the decay rate of actively used knowledge.
* **Privacy by Default:** Explicit deletion (`nova.memory_forget`) executes a permanent hard-delete.

---

## 3. The Knowledge Board (Multi-Agent Whiteboard)

For multi-agent workflows requiring collaborative reasoning:
* **Shared Bulletin Board:** Subagents post structured findings, discovered URLs, or intermediate data payloads using `nova.board_contribute`.
* **Consistent State Querying:** Peer agents query the board with `nova.board_get`, eliminating redundant API calls and repeated tab navigations.
* **Actor Provenance:** Every board entry records the contributing agent's ID (`actorId`), timestamp, and cryptographic evidence hashes.

---

## 4. Production Code References

| Component | Source File | Responsibility |
| :--- | :--- | :--- |
| **`BrowsingMemoryRepository`** | `NovaBrowser/Core/Knowledge/BrowsingMemoryRepository.cs` | SQLite persistence (`pks_browsing_memory`), deduplication, relevance scoring, and decay. |
| **`BrowsingMemoryService`** | `NovaBrowser/Core/Knowledge/BrowsingMemoryService.cs` | High-level memory service with caching and domain exclusion filtering. |
| **`KnowledgeBoardStore`** | `NovaBrowser/Core/KnowledgeBoard/KnowledgeBoardStore.cs` | Thread-safe in-memory and persisted storage for multi-agent contributions. |

---

## 5. MCP Tooling for Memory & Board

* **Personal Browser Memory:**
  * `nova.memory_note`: Saves an explicit note, preference, or context snippet for the target domain.
  * `nova.memory_recall`: Retrieves relevant memories for a domain or URL (ordered by relevance and decay).
  * `nova.memory_forget`: Purges specified notes or all memories associated with a domain.
  * `nova.memory_stats`: Returns storage telemetry, category distributions, and expiration schedules.
* **Collaborative Knowledge Board:**
  * `nova.board_contribute`: Posts a fresh hypothesis, finding, or dataset to the shared board.
  * `nova.board_get`: Reads active board topics with filters for tags, domains, and contributing actors.

---

## Related Documentation

* **[Episodic Task Memory (ETM)](etm-and-task-memory.md)** — Work unit tracking and task profile management.
* **[Operational Knowledge (OK)](operational-knowledge.md)** — Dynamic tab state and account capability tracking.
* **[Phenomenological Knowledge Store (PKS)](pks.md)** — Procedural UI memory and learned fast-paths.
