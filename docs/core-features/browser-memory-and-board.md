# Browser Memory & Knowledge Board (User Context & Agent Findings)

> [!NOTE]
> **Browser Memory** keeps notes, preferences and session context per domain across sessions, with relevance that decays over time. The **Agent Knowledge Board** is an opt-in shared board where agents record symptoms, refutations and reproductions of problems they hit with Nova's tools, so later agents can find them.

---

## 1. Problem Statement & Motivation

Browser automation memory usually covers only site mechanics (PKS) and the current tab state (OK):
1. **Loss of Personal Context:** A user reviews pull request #42 on `github.com` and leaves open discussion points. In the next session, the agent no longer knows this, and the user has to explain the context again.
2. **Missing Time-Decay:** Notes that mattered months ago keep crowding the context if they never expire.
3. **Repeated Dead Ends:** When an agent hits a tool problem and works out what does not help, the next agent starts the same investigation from scratch.

Nova addresses this with two separate stores:
* **Browser Memory:** Domain-bound notes, preferences and context with a half-life per type.
* **Agent Knowledge Board:** Findings about tool problems, matched by a structured anchor.

---

## 2. The Decay Model

Browser Memory scores relevance with an exponential decay, calculated when memories are read:
$$\text{Relevance}(t) = \text{InitialWeight} \times e^{-\lambda \cdot \Delta t}$$

Each memory type has its own half-life:

| Memory Type | Half-Life | Purpose |
| :--- | :---: | :--- |
| **`preference`** | **120 days** | User preferences (e.g. "prefers the compact view on GitHub"). |
| **`note`** | **60 days** | Explicit notes from the agent or user. |
| **`context`** | **14 days** | Short-lived session context (e.g. "last visited: github.com/pulls/42"). |

* **Reinforcement on Access:** Every `nova.memory_recall` hit resets the access time and increases the access count, so memories that are used often stay relevant longer.
* **Limits:** A memory holds up to 2000 characters; there are at most 500 memories per domain. Memories whose relevance has fallen below 0.05 are deleted once the retention period (default 90 days) has passed.
* **Hard Delete:** `nova.memory_forget` deletes permanently; there is no recovery.
* **Optional Auto-Capture:** When enabled in the settings, Nova records a `context` memory with domain and path (no page content) on navigation, at most once per domain every 5 minutes. Excluded domains are never captured.

---

## 3. The Agent Knowledge Board

The board is off by default and is enabled in the settings (**Enable shared agent knowledge board**).
* **Contributions:** `nova.board_contribute` opens a topic with an `observation` or appends a `refutation` (a path that was tried and did not help) or a `reproduction` (the symptom confirmed with evidence). Each contribution carries a structured anchor (component, capability, operation, symptom class, optional host), optional evidence references, and an idempotency key.
* **Hints on failures:** When a tool call fails with a symptom that matches an existing topic, Nova adds a `boardHint` to the result with the topic ID and a suggested `nova.board_get` call.
* **Reading:** `nova.board_get` reads a topic by ID or exact anchor. By default (`blind`), the original hypothesis is hidden while the symptom and refutations are shown, so the next agent is not steered by an earlier guess.
* **Provenance:** Each contribution records which agent client wrote it.

---

## 4. Under the Hood

| Component | Responsibility |
| :--- | :--- |
| **`BrowsingMemoryRepository`** | SQLite persistence (`pks_browsing_memory` in `pks.db`), deduplication, relevance scoring, and decay. |
| **`BrowsingMemoryService`** | Memory service with domain exclusion, auto-capture and pruning. |
| **`KnowledgeBoardStore`** | SQLite persistence of board topics, contributions and hint deliveries (`agent-knowledge-board.db`). |

---

## 5. MCP Tooling for Memory & Board

* **Browser Memory:**
  * `nova.memory_note`: Saves a note, preference or context entry, bound to a domain (by default the active tab's domain) and optionally a URL path pattern.
  * `nova.memory_recall`: Retrieves memories for a domain or across all domains, sorted by decay-weighted relevance.
  * `nova.memory_forget`: Deletes memories by domain, ID, type, or all of them.
* **Agent Knowledge Board:**
  * `nova.board_contribute`: Opens a topic or appends a contribution.
  * `nova.board_get`: Reads one topic by topic ID or exact anchor.

`nova.memory_stats` and `nova.memory_add_candidate` belong to the Learning Candidate Journal, not to Browser Memory; see [Learning Pipeline (ALP)](learning-pipeline-alp.md).

---

## Related Documentation

* **[Episodic Task Memory (ETM)](etm-and-task-memory.md)** — Work unit tracking and task profile management.
* **[Operational Knowledge (OK)](operational-knowledge.md)** — Live tab state and account capabilities.
* **[Phenomenological Knowledge Store (PKS)](pks.md)** — Procedural UI memory and learned playbooks.
