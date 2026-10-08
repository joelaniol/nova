# Learning

Nova preserves several kinds of experience: observations that may become learning candidates, verified website playbooks, task progress and site notes. This overview groups the core features and explains which kind of knowledge each one holds.

## How the Parts Relate

The Learning Candidate Journal (LCJ) holds observations and candidate evidence. The Agent Learning Pipeline (ALP) evaluates candidates and their trust. The Phenomenological Knowledge Store (PKS) keeps procedural entries and learned playbooks. Active knowledge can inform explicit actions or eligible Ambient Auto-Apply; permission to apply an action remains a separate decision.

Episodic Task Memory (ETM) preserves recurring tasks and their progress, while Task URL Coverage (TUC) tracks their URL work units and scan evidence. Operational Knowledge (OK) holds reported site-state signals. Domain Notes preserve website instructions, with optional warnings or required acknowledgement. Operator Notes keep searchable working guidance and environment context, globally or for a sandbox. Browser Memory keeps site notes and preferences. The experimental Agent Knowledge Board is currently not enabled for regular use; when explicitly enabled for testing, it records investigated Nova tool problems. Its contributions are observations, not established explanations.

## Learning Topics

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Phenomenological Knowledge Store (PKS)](phenomenological-knowledge-store-pks/README.md) | What Nova learns about how a site works | `nova.pks_get`, `nova.pks_match`, `nova.pks_upsert`, `nova.learn_promote` |
| [Operational Knowledge (OK)](operational-knowledge-ok/README.md) | Login state, plan and active model of a site, as signals agents report | `nova.ok_observe`, `nova.ok_signal_schema` |
| [Domain Notes](domain-notes/README.md) | Persistent website instructions, scope, warnings and required acknowledgement | `nova.domain_note`, `nova.domain_notes_list`, `nova.domain_note_ack`, `nova.domain_note_delete` |
| [Operator Notes](operator-notes/README.md) | Searchable working guidance, preferences and environment context with sandbox scope | `nova.operator_notes_store`, `nova.operator_notes_query`, `nova.operator_notes_list`, `nova.operator_notes_delete` |
| [Episodic Task Memory (ETM)](episodic-task-memory-etm/README.md) | Recurring tasks and their progress | `nova.task_match`, `nova.task_instance_create`, `nova.task_instance_complete` |
| [Task URL Coverage (TUC)](task-url-coverage-tuc/README.md) | URL work units, trusted scan evidence and coverage gates | `nova.coverage_scan`, `nova.task_instance_reconcile_coverage` |
| [Agent Learning Pipeline (ALP)](agent-learning-pipeline-alp/README.md) | How a lesson is checked before it is kept | `nova.learn_suggest`, `nova.learn_generate`, `nova.learn_promote` |
| [Learning Candidate Journal (LCJ)](learning-candidate-journal-lcj/README.md) | Observations and candidate evidence used by the learning pipeline | `nova.memory_stats`, `nova.memory_add_candidate` |
| [Browser Memory](browser-memory/README.md) | Notes and preferences per site | `nova.memory_note`, `nova.memory_recall`, `nova.memory_forget` |
| [Agent Knowledge Board](agent-knowledge-board/README.md) | Experimental; currently not enabled for regular use. Investigative records of Nova tool problems | `nova.board_get`, `nova.board_contribute` |
| [Ambient Auto-Apply](ambient-auto-apply/README.md) | Eligible automatic playbook application during agent work | `nova.perceive`, `nova.phenomenon_apply` |

## Related Documentation

* [Learn Mode user guide](../../getting-started/learn-mode.md) — A concrete website-learning task and its expected result.
* [Closed-Loop System (CLS)](../closed-loop-system-cls/README.md) — Actions checked against their expected outcome.
* [Tool Observation Bus (TOB)](../tool-observation-bus-tob/README.md) — Server-side evidence of agent actions.
* [Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md) — Required awareness before agent actions.

[All core features](../README.md)
