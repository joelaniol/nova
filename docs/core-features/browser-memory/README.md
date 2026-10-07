# Browser Memory

> [!NOTE]
> **Browser Memory** keeps notes, preferences and session context per domain across sessions, with relevance that decays over time. For tool findings, see the separate [Agent Knowledge Board](../agent-knowledge-board/README.md).

---

## 1. Start with context worth keeping

An agent helps a user review a pull request. The user prefers a compact view and there are unresolved discussion points to revisit. Browser Memory can keep the preference and a short note or context entry for `github.com`, optionally narrowed to a URL path pattern. A later agent can recall that context instead of asking the user to explain it again.

This preserves context, not the current truth of the page: a remembered discussion point may already be resolved, and a recalled preference is guidance rather than an instruction to act without permission.

Browser Memory holds domain-bound notes, preferences and context with a half-life per type. Tool problem findings belong in the separate [Agent Knowledge Board](../agent-knowledge-board/README.md).

### Which memory should hold it?

| What needs remembering? | Appropriate system |
| :--- | :--- |
| A site preference, note or short-lived context | **Browser Memory** |
| A recurring problem with a Nova tool, including attempted fixes and reproductions | [Agent Knowledge Board](../agent-knowledge-board/README.md) |
| The currently reported login, plan or model state | [Operational Knowledge](../operational-knowledge-ok/README.md) |
| The remaining work and checks of an audit | [Task Memory (ETM)](../episodic-task-memory-etm/README.md) |
| How to recognize and handle a recurring web situation | [PKS](../phenomenological-knowledge-store-pks/README.md) |

Sharing a database with PKS does not turn a browser note into a verified playbook. The note's relevance and the playbook's evidence-based trust serve different purposes.

---

## 2. The Decay Model

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

## 3. MCP Tooling for Browser Memory

* **Browser Memory:**
  * `nova.memory_note`: Saves a note, preference or context entry, bound to a domain (by default the active tab's domain) and optionally a URL path pattern.
  * `nova.memory_recall`: Retrieves memories for a domain or across all domains, sorted by decay-weighted relevance.
  * `nova.memory_forget`: Deletes memories by domain, ID, type, or all of them.
`nova.memory_stats` and `nova.memory_add_candidate` belong to the Learning Candidate Journal, not to Browser Memory; see [Learning Candidate Journal (LCJ)](../learning-candidate-journal-lcj/README.md).

---

## 4. Implementation notes

| Component | Responsibility |
| :--- | :--- |
| **`BrowsingMemoryRepository`** | SQLite persistence (`pks_browsing_memory` in `pks.db`), deduplication, relevance scoring, and decay. |
| **`BrowsingMemoryService`** | Memory service with domain exclusion, auto-capture and pruning. |

Browser notes are recalled through relevance scoring. Recalling a note does not apply a website action. Agents interpret the returned context and still use the appropriate task, knowledge and action tools.

---

## Related Documentation

* **[Episodic Task Memory (ETM)](../episodic-task-memory-etm/README.md)** — Work unit tracking and task profile management.
* **[Operational Knowledge (OK)](../operational-knowledge-ok/README.md)** — Live tab state and account capabilities.
* **[Phenomenological Knowledge Store (PKS)](../phenomenological-knowledge-store-pks/README.md)** — Procedural UI memory and learned playbooks.

[All core features](../README.md)
