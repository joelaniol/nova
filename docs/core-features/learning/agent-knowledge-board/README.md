# Agent Knowledge Board

> [!IMPORTANT]
> **Experimental feature:** The Agent Knowledge Board is currently not enabled for regular use. It is off by default; enabling it is an explicit opt-in for experimental testing, not a normal setup step.

The Agent Knowledge Board is an opt-in shared store of symptoms, refutations and reproductions of Nova tool problems. It is separate from [Browser Memory](../browser-memory/README.md), which holds per-site notes, preferences and context.

## Experimental activation and use

For example, one agent encounters a tool failure and records the symptom and evidence. It tries a recovery path that does not help and records that refutation. The next agent can retrieve the topic and avoid repeating the same dead end, without inheriting the first agent's hypothesis as an established explanation.

For explicit experimental testing, the opt-in controls are:

1. Open **Menu → Settings → AI & agents → Knowledge board**.
2. Enable **Enable shared agent knowledge board**. The agent interface must be active; if Nova reports that prerequisite, use **Connection & setup** to enable the interface first.
3. Ask your agent to record a concrete Nova tool problem with its evidence and any attempted recovery. Agents write the entries; enabling the board alone does not create one.
4. Return to **Knowledge board** to inspect the stored topics. A contribution is an observation, not proof that its proposed explanation is correct.

The board is off by default. Its technical interfaces are described below.
* **Contributions:** `nova.board_contribute` opens a topic with an `observation` or appends a `refutation` (a report that a tried path did not help) or a `reproduction` (a report that the symptom recurred). Each contribution carries a structured anchor (component, capability, operation, symptom class, optional host), optional evidence references, and an idempotency key.
* **Hints on failures:** When a tool call fails with a symptom that matches an existing topic, Nova adds a `boardHint` to the result with the topic ID and a suggested `nova.board_get` call.
* **Reading:** `nova.board_get` reads a topic by ID or exact anchor. By default (`blind`), the original hypothesis is hidden while the symptom and refutations are shown, so the next agent is not steered by an earlier guess.
* **Provenance:** Each contribution records which agent client wrote it.

“Shared” here means shared between agents using the board in Nova's local profile context. Board contributions retain their authorship; storing a report does not independently establish its explanation. They are investigative records, not executable fixes or automatically promoted PKS knowledge. Recording a reproduction does not itself repair the tool.

---

## Board tools

* **Agent Knowledge Board:**
  * `nova.board_contribute`: Opens a topic or appends a contribution.
  * `nova.board_get`: Reads one topic by topic ID or exact anchor.


## Storage and interpretation

Board topics, contributions and hint deliveries are stored in `agent-knowledge-board.db`. Findings are retrieved by topic or structured anchor. Agents interpret them; retrieving a finding does not apply a website action or repair a tool.

[Browser Memory](../browser-memory/README.md) · [Operational Knowledge (OK)](../operational-knowledge-ok/README.md)

[Learning overview](../README.md) · [All core features](../../README.md)
