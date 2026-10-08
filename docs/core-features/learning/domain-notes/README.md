# Domain Notes

Domain Notes preserve instructions and context for a website across agent sessions. Nova's interface calls them **Site notes**. They belong to Learning as persistent guidance: a saved instruction is not automatically a learned or verified playbook.

To create and manage notes, follow the [Domain Notes user guide](../../../user-guide/agents/domain-notes.md). Start from **Site information → Notes for [domain]**, or manage existing notes under **Settings → AI & agents → Access & rules → Site notes**.

## Start with a website instruction

For example, save “Search existing records first; ask me before creating or deleting a record” for a work portal. Later agent sessions can retrieve the instruction for that website and the intended sandbox. Choose how strongly Nova should deliver it, then check the saved host, scope and level.

## Delivery and acknowledgement

| Level in Nova | Behavior |
| :--- | :--- |
| **Hint only** | Makes the note available as inspection context. |
| **Warn the agent** | Adds a warning to applicable tool results. |
| **MUST read** | Blocks applicable calls until the agent acknowledges the note. |

Warn and MUST-read enforcement require **Site notes → Global override → On — per-note level wins (recommended)**. When the global switch is off, those notes remain inspection hints. Enforcement uses [Agent Awareness Gates (AAG)](../../agent-awareness-gates-aag/README.md#site-notes-and-required-acknowledgement); it does not require putting every other awareness gate into Block mode.

Acknowledgement is tracked per tab. A new tab, an edited note or a configured time or tool-call interval can require another acknowledgement. An individual note can override the repeat defaults; `0` disables that repeat trigger, while closing the tab still re-arms acknowledgement.

Technical acknowledgement does not assess the model's understanding, prove task completion or grant permission for an action. For important instructions, ask the agent to explain the rules in its own words and review its answer. The user guide provides an example prompt.

## Host, sandbox and authorship

Notes can apply across sandboxes or only within a selected sandbox. Use sandbox-specific notes when different accounts need different instructions.

MUST-read enforcement matches the actual host, treating a leading `www.` as equivalent. A note for `example.com` does not automatically block actions on `portal.example.com`. Parent-domain hints may appear during inspection; create a note for the actual host when acknowledgement must be required there.

Notes created through Nova's interface are marked as authored by the user. Agent-written notes retain agent authorship. Agent changes to user-authored notes are subject to Nova's separate user-note override permission policy; an agent cannot label its own notes as written by the user.

## How Domain Notes differ from other Learning topics

| What you want to preserve | Topic |
| :--- | :--- |
| Website instructions, optionally with warnings or required acknowledgement | **Domain Notes** |
| Reported login, plan or active-model state for a target | [Operational Knowledge (OK)](../operational-knowledge-ok/README.md) |
| Recallable site preferences and context | [Browser Memory](../browser-memory/README.md) |
| Recognition, actions and verification for recurring website situations | [Phenomenological Knowledge Store (PKS)](../phenomenological-knowledge-store-pks/README.md) |

“Read the export instructions before downloading” is a Domain Note. “This tab is currently logged out” is an OK observation. A verified export workflow can become a PKS playbook. These records serve different purposes and do not replace one another.

## MCP tools

| Tool | Purpose |
| :--- | :--- |
| [`nova.domain_note`](../../../mcp-reference/tools/task-memory/nova-domain-note.md) | Creates or updates a note, including its scope, enforcement and repeat settings. |
| [`nova.domain_notes_list`](../../../mcp-reference/tools/task-memory/nova-domain-notes-list.md) | Retrieves stored notes for a domain and scope. |
| [`nova.domain_note_ack`](../../../mcp-reference/tools/task-memory/nova-domain-note-ack.md) | Acknowledges a MUST-read note for the applicable tab. |
| [`nova.domain_note_delete`](../../../mcp-reference/tools/task-memory/nova-domain-note-delete.md) | Deletes a note within the selected scope. |

Navigation can announce available notes; inspection or explicit retrieval supplies their content. Read the current notes for the correct sandbox before acknowledging them. Full parameters and examples remain in the linked tool references.

[Domain Notes user guide](../../../user-guide/agents/domain-notes.md) · [Learning overview](../README.md) · [All core features](../../README.md)
