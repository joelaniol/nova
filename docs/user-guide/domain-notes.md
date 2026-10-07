# Domain Notes: Give Your Agent Instructions for a Website

Use **Domain Notes** to leave instructions that your agent should see when working on a particular website. Nova's interface calls them **Site notes**. They can describe your preferred workflow, account-specific details or actions the agent must ask you about first.

## Add a note for the current website

1. Open the website in Nova, in the sandbox where you intend to use it.
2. Open **Site information** from the site icon beside the address bar.
3. Find **Notes for [domain]**, choose **Show**, then **+ Add note**.
4. Enter a short title and the instruction for your agent. An optional template can help you start.
5. Choose **Hint only**, **Warn the agent** or **MUST read (agent must acknowledge)**.
6. If a sandbox scope is offered, choose **For all sandboxes** or **Only for [sandbox]**.
7. Choose **Save** and check that the note appears for the intended site and scope.

To manage notes across websites, use **Settings → AI & agents → Access & rules → Site notes**, or **Manage all** from the site-information panel.

## Choose how strongly the note is delivered

| Level | What happens |
|---|---|
| **Hint only** | The note is available as context when the agent inspects the website. |
| **Warn the agent** | Nova adds a warning about the note to matching tool results. |
| **MUST read** | Nova blocks applicable tool calls on the matching site until the agent acknowledges the note. |

For Warn and MUST read, check **Site notes → Global override → On — per-note level wins (recommended)**. With the global switch off, even a MUST-read note becomes an inspection hint and does not block calls. The note editor also warns when this switch is off.

Site-note enforcement is part of Nova's **Agent Awareness Gates (AAG)**. You do not need to put every other awareness gate into Block mode to use a MUST-read note. See [AAG](../core-features/aag.md#site-notes-and-required-acknowledgement) for the technical context.

## Ask for a visible confirmation of understanding

For an important instruction, select **MUST read** and write the behavior you want explicitly. For example:

**Title:** `Before working in this portal`

> Before taking actions on this website, read the applicable Domain Notes. Summarize the rules in your own words and confirm that you understand them. If anything is unclear or conflicts with my task, ask me before continuing. Use filters and existing records first. Do not create, edit or delete records without my approval.

Then tell your agent in its conversation:

> Before working on [website], read the Domain Notes for the correct sandbox in Nova. Explain the instructions in your own words, confirm that you understand them, and acknowledge any MUST-read notes through Nova. Tell me about conflicts or unclear points before acting.

Review the reply. It should identify the actual rules, the site and any relevant sandbox, rather than merely say “understood.” For example:

> I will search and filter existing records first. I will ask before creating, editing or deleting anything. These instructions apply to this portal in the selected sandbox.

The agent handles Nova's acknowledgement mechanism. You do not need to type tool calls yourself. AAG records technical acknowledgement of delivered instructions; it does not assess whether the model interpreted every sentence correctly or require a chat explanation by itself. The explicit instruction and your review provide that visible check.

## Keep the right site and sandbox in scope

A note for all sandboxes applies on that domain across your Nova sandboxes. A sandbox-specific note is visible only in its matching sandbox, which is useful when work and personal accounts need different instructions.

For MUST-read enforcement, use the website's actual host. A note for `example.com` does not automatically block actions on `portal.example.com`; add a note for that host if you need required acknowledgement there. Nova treats a leading `www.` as the same domain. Parent-domain hints may be available during inspection, but those hints do not establish MUST-read enforcement on every subdomain.

Notes you create in Nova's interface are marked as **from you**. Notes the agent writes are its own observations. Review agent observations before relying on them as your instructions. Agent changes to your notes are subject to Nova's separate user-note override permission policy; the agent cannot mark its own notes as authored by you.

## Remind the agent during longer sessions

MUST-read acknowledgement is tracked per tab. A new tab, an edited note or a configured re-acknowledgement interval can require another acknowledgement.

Under **Site notes → Global default for re-acknowledge**, you can choose a time or tool-call interval. An individual note can override those defaults. A value of `0` disables that repeat trigger; closing the tab still re-arms acknowledgement. Use concise notes so repeated delivery stays useful.

If the agent seems to have lost the instructions, ask it to read the current notes again and restate them before continuing. Check the note's host, sandbox scope, enforcement level and the global switch if MUST read is not taking effect. The settings screen also shows note limits and expiration; review old instructions when the website or your workflow changes.

## How this differs from onboarding and Learn Mode

| Feature | Purpose |
|---|---|
| **Domain Notes** | Your instructions and context for a particular website. |
| [Project onboarding](../getting-started/advanced-onboarding.md) | Nova references in a project folder so later agent sessions can find its working instructions. |
| [Learn Mode](../getting-started/learn-mode.md) | Deliberate exploration and verification of a website's workflows. |

A note is guidance, not permission to perform a transaction. Nova's action permissions still apply. To interrupt running work, use [Emergency Stop](../getting-started/emergency-stop.md).
