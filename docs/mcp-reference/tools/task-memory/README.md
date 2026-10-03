# Episodic Task Memory & Guidance

Task instance tracking, guidance logs, coverage scans, surface exploration, and operator domain notes.

* **Core Architecture Guide:** [Core Features: etm-and-task-memory.md](../../../core-features/etm-and-task-memory.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (34 Tools)

Capability bundles of these tools: `pks_learning`, `surface_explorer`, `system_tools`, `task_memory`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.board_contribute`](nova-board-contribute.md)** | Opens a new Agent Knowledge Board topic or appends an evidence-bound research contribution. |
| **[`nova.board_get`](nova-board-get.md)** | Reads an Agent Knowledge Board laboratory topic by ID or exact structured anchor. |
| **[`nova.coverage_scan`](nova-coverage-scan.md)** | Runs a server-registered Coverage Scan script to discover and audit all interactive surfaces. |
| **[`nova.domain_note`](nova-domain-note.md)** | Stores or updates a domain-scoped operational note automatically surfaced during navigation. |
| **[`nova.domain_note_ack`](nova-domain-note-ack.md)** | Explicitly acknowledges a MUST-read domain note block to unblock subsequent tool calls. |
| **[`nova.domain_note_delete`](nova-domain-note-delete.md)** | Deletes a domain note by domain name and key. |
| **[`nova.domain_notes_list`](nova-domain-notes-list.md)** | Lists all stored procedural notes and operator instructions for a specific domain. |
| **[`nova.explore_surface`](nova-explore-surface.md)** | Discovers interactive UI triggers (buttons, tabs, accordions) and activates them to reveal hidden DOM. |
| **[`nova.goal_register`](nova-goal-register.md)** | Manages closed-loop task goals, verifying step advancement and milestone criteria. |
| **[`nova.memory_add_candidate`](nova-memory-add-candidate.md)** | Proposes a lightweight candidate memory claim for the currently claimed task and tab. |
| **[`nova.memory_forget`](nova-memory-forget.md)** | Deletes browsing memories matching domain, memoryType, or text query filters. |
| **[`nova.memory_note`](nova-memory-note.md)** | Saves a persistent browsing memory (user preference, workflow hint, domain context). |
| **[`nova.memory_recall`](nova-memory-recall.md)** | Recalls browsing memories and stored preferences for a domain or across all sites. |
| **[`nova.memory_stats`](nova-memory-stats.md)** | Reports memory engine metrics, commit rates, verification health, and outbox queues. |
| **[`nova.operator_notes_delete`](nova-operator-notes-delete.md)** | Deletes an operator note by unique ID. |
| **[`nova.operator_notes_list`](nova-operator-notes-list.md)** | Lists all persistent operator notes with tags and sandbox scopes. |
| **[`nova.operator_notes_query`](nova-operator-notes-query.md)** | Queries operator notes by keywords with tag-intersection and TF-IDF relevance scoring. |
| **[`nova.operator_notes_store`](nova-operator-notes-store.md)** | Stores or updates a persistent operator note with search tags and priority. |
| **[`nova.task_guidance_log_add`](nova-task-guidance-log-add.md)** | Logs a guidance observation or proposal without directly mutating task profiles. |
| **[`nova.task_guidance_logs`](nova-task-guidance-logs.md)** | Lists guidance log entries filtered by profile, domain, or guidance kind. |
| **[`nova.task_instance_abort`](nova-task-instance-abort.md)** | Ends a task instance without meeting completion conditions (site offline, unsolvable error). |
| **[`nova.task_instance_complete`](nova-task-instance-complete.md)** | Requests server evaluation and completion for an episodic task instance. |
| **[`nova.task_instance_create`](nova-task-instance-create.md)** | Creates a new episodic task instance from a profile or ad-hoc context with snapshot state. |
| **[`nova.task_instance_get`](nova-task-instance-get.md)** | Loads a task instance snapshot for session-crossing resume and progress inspection. |
| **[`nova.task_instance_progress`](nova-task-instance-progress.md)** | Commits progress deltas, completed work units, and observations to a task instance. |
| **[`nova.task_instance_reconcile_coverage`](nova-task-instance-reconcile-coverage.md)** | Replays an instance’s observation log against the unit table to propose discovered-to-checked upgrades. |
| **[`nova.task_instance_verify`](nova-task-instance-verify.md)** | Retrieves the verification contract steps, assertions, and checks required for task completion. |
| **[`nova.task_match`](nova-task-match.md)** | Finds the best matching task profiles for a task description with score breakdowns. |
| **[`nova.task_profile_get`](nova-task-profile-get.md)** | Retrieves full details of a task profile: guidance, mandatory checks, and completion conditions. |
| **[`nova.task_profile_upsert`](nova-task-profile-upsert.md)** | Creates or updates a task profile with semantic content revision tracking. |
| **[`nova.task_profiles`](nova-task-profiles.md)** | Lists known task profiles, optionally filtered by taskType, domain, or platform. |
| **[`nova.task_promote_guidance`](nova-task-promote-guidance.md)** | Explicitly promotes a guidance log entry into a profile’s stable guidance. |
| **[`nova.task_promotion_candidates`](nova-task-promotion-candidates.md)** | Lists guidance log entries and override patterns that are candidates for profile promotion. |
| **[`nova.task_search`](nova-task-search.md)** | Searches for matching task profiles by free-text query with keyword ranking. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
