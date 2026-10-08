# Operator Notes

Operator Notes preserve working guidance, preferences and environment context across agent sessions. They are searchable by keywords and tags, with an optional category and a global or sandbox-specific scope. Notes can record user-supplied guidance or an agent's observations; storing them does not verify their content.

## Start with guidance worth reusing

For example, you prefer CSV exports for recurring report work. Ask your agent:

> Save an Operator Note that I prefer CSV exports for report analysis. Use relevant report, CSV and workflow tags. Keep it in the sandbox we are using for this work, then show me the saved note ID, content and scope.

The agent stores the note through Nova, then retrieves it to check the result. In a later session, searching for the related task keywords can bring the guidance back into context. No website domain is required for an Operator Note.

## Store, find and maintain notes

1. Write concise content and meaningful tags. Add a category such as `workflow`, `preference` or `environment` when useful.
2. Choose global scope or an explicit sandbox binding. Check the returned note ID and sandbox reference.
3. Query by keywords for relevant notes, or list notes to review the stored collection. Listing is paginated; one page is not the whole collection.
4. Update an existing note by its ID when the guidance changes. If the supplied ID is missing, the store operation creates a new note and reports `created_id_not_found`; do not treat that as a successful update of the old record.
5. Delete an obsolete note by its ID when it should no longer be reused.

On an update, sandbox binding is supplied again. Omitting that binding makes the updated note global; preserve the intended sandbox explicitly rather than assuming the existing binding stays in place.

## Scope and sandbox identity

| Scope for query or list | What it returns |
| :--- | :--- |
| `current_sandbox` | Notes for the active or explicitly selected sandbox, plus global notes. This is the default. |
| `global` | Global notes only. |
| `all` | Notes across scopes. |
| `orphaned` | Notes still bound to sandbox identities that no longer resolve, for review and cleanup. |

Creating a sandbox-specific note or explicitly selecting a sandbox for retrieval requires both `sandboxId` and `sandboxRef`. The persistent reference protects against reusing a sandbox letter for a different identity. An orphaned note does not automatically become a global note.

## Retrieval and freshness

[`nova.operator_notes_query`](../../../mcp-reference/tools/task-memory/nova-operator-notes-query.md) returns relevance-ranked matches with note content, tags and scope information. A match score indicates relevance to the supplied keywords; it does not certify the note's truth or current validity.

The normal [`nova.get_instructions`](../../../mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md) response can also include matched Operator Notes when the agent supplies `taskKeywords`. This is a bounded contextual selection, not a complete inventory. For an explicitly scoped view, use query or list with the intended scope and sandbox, and inspect the returned records before relying on them.

Notes are snapshots from earlier sessions. Recheck environment facts and instructions that may have changed. Update or remove obsolete guidance. A saved preference is not permission to perform a purchase, send a message or change an account.

## How Operator Notes differ from other Learning topics

| What needs preserving? | Topic |
| :--- | :--- |
| Searchable working guidance, preferences or environment context, optionally scoped to a sandbox | **Operator Notes** |
| Instructions for a website with optional warnings or required acknowledgement | [Domain Notes](../domain-notes/README.md) |
| Domain-bound notes and recallable browsing context | [Browser Memory](../browser-memory/README.md) |
| Recurring tasks, work units and progress | [Episodic Task Memory (ETM)](../episodic-task-memory-etm/README.md) |
| Verified recognition and action recipes for recurring website situations | [Phenomenological Knowledge Store (PKS)](../phenomenological-knowledge-store-pks/README.md) |

Operator Notes do not establish a Domain Notes MUST-read gate, verify task completion or automatically become PKS playbooks. For research, [EVM](../../../research/evidence-verification-mode-evm/README.md) uses Operator Notes for reusable research context; the underlying claims still need appropriate evidence.

## MCP tools

| Tool | Purpose |
| :--- | :--- |
| [`nova.operator_notes_store`](../../../mcp-reference/tools/task-memory/nova-operator-notes-store.md) | Creates or updates content, tags, category, source metadata and sandbox binding. |
| [`nova.operator_notes_query`](../../../mcp-reference/tools/task-memory/nova-operator-notes-query.md) | Searches for relevant notes using task keywords and scope filters. |
| [`nova.operator_notes_list`](../../../mcp-reference/tools/task-memory/nova-operator-notes-list.md) | Lists notes with pagination and scope filters. |
| [`nova.operator_notes_delete`](../../../mcp-reference/tools/task-memory/nova-operator-notes-delete.md) | Removes a note by ID. |

[Learning overview](../README.md) · [All core features](../../README.md)
