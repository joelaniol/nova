# Episodic Task Memory & Guidance

Task instance tracking, guidance logs, coverage scans, surface exploration, and operator domain notes.

* **Capability Bundle(s):** `task_memory`
* **Core Architecture Guide:** [Core Features: etm-and-task-memory.md](../../../core-features/etm-and-task-memory.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (34 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.board_contribute`](nova-board-contribute.md)** | Documented | Open a new Agent Knowledge Board laboratory topic or append an evidence-bound contribution. |
| **[`nova.board_get`](nova-board-get.md)** | Documented | Read one Agent Knowledge Board laboratory topic by topicId or exact structured anchor. |
| **[`nova.coverage_scan`](nova-coverage-scan.md)** | Documented | Run a server-registered Coverage Scan script on the resolved tab. |
| **[`nova.domain_note`](nova-domain-note.md)** | Documented | Store or update a domain-scoped note. |
| **[`nova.domain_note_ack`](nova-domain-note-ack.md)** | Documented | Explicitly acknowledge a MUST-read site-note block. |
| **[`nova.domain_note_delete`](nova-domain-note-delete.md)** | Documented | Delete a single domain note by domain and key. |
| **[`nova.domain_notes_list`](nova-domain-notes-list.md)** | Documented | List all notes for a specific domain. |
| **[`nova.explore_surface`](nova-explore-surface.md)** | Documented | Discover interactive UI triggers (buttons, tabs, modals, accordions) on the current page surface, activate them to reveal hidde... |
| **[`nova.goal_register`](nova-goal-register.md)** | Documented | Create/query/close/annotate closed-loop goals. |
| **[`nova.memory_add_candidate`](nova-memory-add-candidate.md)** | Documented | Add or update a lightweight LCJ candidate for the currently claimed task/tab. |
| **[`nova.memory_forget`](nova-memory-forget.md)** | Documented | Delete browsing memories. |
| **[`nova.memory_note`](nova-memory-note.md)** | Documented | Save a browsing memory — a note, preference, or session context for a domain. |
| **[`nova.memory_recall`](nova-memory-recall.md)** | Documented | Recall browsing memories for a domain or across all domains. |
| **[`nova.memory_stats`](nova-memory-stats.md)** | Documented | Read LCJ/finalize/outbox memory metrics with derived rates (commit/verification/curation/outbox health).. |
| **[`nova.operator_notes_delete`](nova-operator-notes-delete.md)** | Documented | Delete an operator note by ID.. |
| **[`nova.operator_notes_list`](nova-operator-notes-list.md)** | Documented | List all operator notes (paginated). |
| **[`nova.operator_notes_query`](nova-operator-notes-query.md)** | Documented | Query operator notes by keywords. |
| **[`nova.operator_notes_store`](nova-operator-notes-store.md)** | Documented | Store or update an operator note. |
| **[`nova.task_guidance_log_add`](nova-task-guidance-log-add.md)** | Documented | Log a guidance observation or proposal. |
| **[`nova.task_guidance_logs`](nova-task-guidance-logs.md)** | Documented | List guidance log entries with optional filters. |
| **[`nova.task_instance_abort`](nova-task-instance-abort.md)** | Documented | End a task instance WITHOUT meeting its completion condition — use when the task cannot be finished (site offline, unsolvable c... |
| **[`nova.task_instance_complete`](nova-task-instance-complete.md)** | Documented | Request task completion. |
| **[`nova.task_instance_create`](nova-task-instance-create.md)** | Documented | Create a new task instance from a profile or ad-hoc context. |
| **[`nova.task_instance_get`](nova-task-instance-get.md)** | Documented | Load a task instance snapshot for session-crossing resume. |
| **[`nova.task_instance_progress`](nova-task-instance-progress.md)** | Documented | Commit delta/append progress to a task instance. |
| **[`nova.task_instance_reconcile_coverage`](nova-task-instance-reconcile-coverage.md)** | Documented | Replay an instance's observation log against the current unit table and propose discovered -> checked upgrades. |
| **[`nova.task_instance_verify`](nova-task-instance-verify.md)** | Documented | Retrieve verification contract steps for a task instance. |
| **[`nova.task_match`](nova-task-match.md)** | Documented | Find the best matching task profiles for a task description. |
| **[`nova.task_profile_get`](nova-task-profile-get.md)** | Documented | Get a single task profile with full guidance, mandatory checks, completion condition, and known exceptions.. |
| **[`nova.task_profile_upsert`](nova-task-profile-upsert.md)** | Documented | Create or update a task profile. |
| **[`nova.task_profiles`](nova-task-profiles.md)** | Documented | List known task profiles, optionally filtered by taskType, domain, or platform.. |
| **[`nova.task_promote_guidance`](nova-task-promote-guidance.md)** | Documented | Explicitly promote a guidance log entry into a profile's stableGuidance. |
| **[`nova.task_promotion_candidates`](nova-task-promotion-candidates.md)** | Documented | List guidance log entries and override patterns that are candidates for promotion into a profile. |
| **[`nova.task_search`](nova-task-search.md)** | Documented | Search for matching task profiles by free-text query. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
