# Learning

Nova preserves several kinds of experience: observations that may become learning candidates, verified website playbooks, task progress and site notes. This overview groups the core features and explains which kind of knowledge each one holds.

## How the Parts Relate

The Learning Candidate Journal (LCJ) holds observations and candidate evidence. The Agent Learning Pipeline (ALP) evaluates candidates and their trust. The Phenomenological Knowledge Store (PKS) keeps procedural entries and learned playbooks. Active knowledge can inform explicit actions or eligible Ambient Auto-Apply; permission to apply an action remains a separate decision.

Episodic Task Memory (ETM) preserves recurring tasks and their progress, while Task URL Coverage (TUC) tracks their URL work units and scan evidence. Operational Knowledge (OK) holds reported site-state signals and domain notes. Browser Memory keeps site notes and preferences. The opt-in Agent Knowledge Board records investigated Nova tool problems; its contributions are observations, not established explanations.

## Learning Topics

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Phenomenological Knowledge Store (PKS)](phenomenological-knowledge-store-pks/README.md) | What Nova learns about how a site works | `nova.pks_get`, `nova.pks_match`, `nova.pks_upsert`, `nova.learn_promote` |
| [Operational Knowledge (OK)](operational-knowledge-ok/README.md) | Login state, plan and active model of a site, as signals agents report; domain notes | `nova.ok_observe`, `nova.ok_signal_schema`, `nova.domain_note` |
| [Episodic Task Memory (ETM)](episodic-task-memory-etm/README.md) | Recurring tasks and their progress | `nova.task_match`, `nova.task_instance_create`, `nova.task_instance_complete` |
| [Task URL Coverage (TUC)](task-url-coverage-tuc/README.md) | URL work units, trusted scan evidence and coverage gates | `nova.coverage_scan`, `nova.task_instance_reconcile_coverage` |
| [Agent Learning Pipeline (ALP)](agent-learning-pipeline-alp/README.md) | How a lesson is checked before it is kept | `nova.learn_suggest`, `nova.learn_generate`, `nova.learn_promote` |
| [Learning Candidate Journal (LCJ)](learning-candidate-journal-lcj/README.md) | Observations and candidate evidence used by the learning pipeline | `nova.memory_stats`, `nova.memory_add_candidate` |
| [Browser Memory](browser-memory/README.md) | Notes and preferences per site | `nova.memory_note`, `nova.memory_recall`, `nova.memory_forget` |
| [Agent Knowledge Board](agent-knowledge-board/README.md) | Opt-in investigative records of Nova tool problems | `nova.board_get`, `nova.board_contribute` |
| [Ambient Auto-Apply](ambient-auto-apply/README.md) | Eligible automatic playbook application during agent work | `nova.perceive`, `nova.phenomenon_apply` |

## Related Documentation

* [Learn Mode user guide](../../getting-started/learn-mode.md) — A concrete website-learning task and its expected result.
* [Closed-Loop System (CLS)](../closed-loop-system-cls/README.md) — Actions checked against their expected outcome.
* [Tool Observation Bus (TOB)](../tool-observation-bus-tob/README.md) — Server-side evidence of agent actions.
* [Agent Awareness Gates (AAG)](../agent-awareness-gates-aag/README.md) — Required awareness before agent actions.

[All core features](../README.md)
