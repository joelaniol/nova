# Browser Memory & Knowledge Board (User Context & Agent Findings)

> [!NOTE]
> **Browser Memory** keeps notes, preferences and session context per domain across sessions, with relevance that decays over time. The **Agent Knowledge Board** is an opt-in shared board where agents record symptoms, refutations and reproductions of problems they hit with Nova's tools, so later agents can find them.

---

## 1. Start with context worth keeping

An agent helps a user review a pull request. The user prefers a compact view and there are unresolved discussion points to revisit. Browser Memory can keep the preference and a short note or context entry for `github.com`, optionally narrowed to a URL path pattern. A later agent can recall that context instead of asking the user to explain it again.

This preserves context, not the current truth of the page: a remembered discussion point may already be resolved, and a recalled preference is guidance rather than an instruction to act without permission.

Nova addresses this with two separate stores:
* **Browser Memory:** Domain-bound notes, preferences and context with a half-life per type.
* **Agent Knowledge Board:** Findings about tool problems, matched by a structured anchor.

### Which memory should hold it?

| What needs remembering? | Appropriate system |
| :--- | :--- |
| A site preference, note or short-lived context | **Browser Memory** |
| A recurring problem with a Nova tool, including attempted fixes and reproductions | **Agent Knowledge Board** |
| The currently reported login, plan or model state | [Operational Knowledge](operational-knowledge.md) |
| The remaining work and checks of an audit | [Task Memory (ETM)](etm-and-task-memory.md) |
| How to recognize and handle a recurring web situation | [PKS](pks.md) |

Sharing a database with PKS does not turn a browser note into a verified playbook. The note's relevance and the playbook's evidence-based trust serve different purposes.

---

## 2. The Agent Knowledge Board

For example, one agent encounters a tool failure and records the symptom and evidence. It tries a recovery path that does not help and records that refutation. The next agent can retrieve the topic and avoid repeating the same dead end, without inheriting the first agent's hypothesis as an established explanation.

The board is off by default and is enabled in the settings (**Enable shared agent knowledge board**).
* **Contributions:** `nova.board_contribute` opens a topic with an `observation` or appends a `refutation` (a report that a tried path did not help) or a `reproduction` (a report that the symptom recurred). Each contribution carries a structured anchor (component, capability, operation, symptom class, optional host), optional evidence references, and an idempotency key.
* **Hints on failures:** When a tool call fails with a symptom that matches an existing topic, Nova adds a `boardHint` to the result with the topic ID and a suggested `nova.board_get` call.
* **Reading:** `nova.board_get` reads a topic by ID or exact anchor. By default (`blind`), the original hypothesis is hidden while the symptom and refutations are shown, so the next agent is not steered by an earlier guess.
* **Provenance:** Each contribution records which agent client wrote it.

“Shared” here means shared between agents using the board in Nova's local profile context. Board contributions retain their authorship; storing a report does not independently establish its explanation. They are investigative records, not executable fixes or automatically promoted PKS knowledge. Recording a reproduction does not itself repair the tool.

---

## 3. The Decay Model

A preference can stay useful much longer than “this is the page we were just reviewing.” Decay reduces the relevance of unused context over time, while frequently recalled entries retain relevance longer. **Relevance is not a truth score:** recalling an old note does not verify its contents.

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

## 4. MCP Tooling for Memory & Board

* **Browser Memory:**
  * `nova.memory_note`: Saves a note, preference or context entry, bound to a domain (by default the active tab's domain) and optionally a URL path pattern.
  * `nova.memory_recall`: Retrieves memories for a domain or across all domains, sorted by decay-weighted relevance.
  * `nova.memory_forget`: Deletes memories by domain, ID, type, or all of them.
* **Agent Knowledge Board:**
  * `nova.board_contribute`: Opens a topic or appends a contribution.
  * `nova.board_get`: Reads one topic by topic ID or exact anchor.

`nova.memory_stats` and `nova.memory_add_candidate` belong to the Learning Candidate Journal, not to Browser Memory; see [Learning Pipeline (ALP)](learning-pipeline-alp.md).

---

## 5. Implementation notes

| Component | Responsibility |
| :--- | :--- |
| **`BrowsingMemoryRepository`** | SQLite persistence (`pks_browsing_memory` in `pks.db`), deduplication, relevance scoring, and decay. |
| **`BrowsingMemoryService`** | Memory service with domain exclusion, auto-capture and pruning. |
| **`KnowledgeBoardStore`** | SQLite persistence of board topics, contributions and hint deliveries (`agent-knowledge-board.db`). |

Browser notes are recalled through relevance scoring; board findings are retrieved by topic or structured anchor. Neither path applies a website action. Agents interpret the returned context and still use the appropriate task, knowledge and action tools.

---

## Related Documentation

* **[Episodic Task Memory (ETM)](etm-and-task-memory.md)** — Work unit tracking and task profile management.
* **[Operational Knowledge (OK)](operational-knowledge.md)** — Live tab state and account capabilities.
* **[Phenomenological Knowledge Store (PKS)](pks.md)** — Procedural UI memory and learned playbooks.
