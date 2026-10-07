# Optional Project Onboarding

Use this after your [first successful task](quickstart.md) if you plan to use Nova regularly in a project. Onboarding gives later agent sessions a local reference to Nova's working instructions.

## Choose the project folder

Open your project in your AI program. Tell the agent which folder should receive Nova's reference files; use the actual project folder rather than your whole user folder.

Paste this into the agent's conversation after choosing the project folder:

> Please set up Nova's onboarding in this project. Tell me the exact folder before writing. Use Nova's current onboarding instructions, preserve existing project instructions, and show me which files you added or updated.

The agent handles the tool calls and confirmation for a new location. You do not need to enter tool parameters yourself.

## Check what changed

Nova writes its own reference files under `.nova/`, including `nova-mcp.quick.md` and `nova-mcp.md`, and marked Nova sections in the supported project instruction files. Existing instructions outside those sections are preserved.

Ask the agent to show you the changed paths. Onboarding should not create or edit your agent client's permission configuration. Tool approvals in Claude, Codex or another client remain a separate decision.

If the agent reports that self-onboarding is disabled, open **Menu → Settings → AI & agents → Confirmations & audit** and check **Agent self-onboarding (install/get_onboarding tools)**. Enable it if you want this feature, then ask the agent to retry. For a connection problem, follow [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).

## Use the project again

In a later session, ask your agent to use Nova for the task. The reference files help it find Nova's guidance; they do not replace a working MCP connection. Restart sessions that were open when the connection changed.

Project onboarding is separate from teaching Nova a website workflow. For recurring work on the same website, see [Learn Mode](whats-next.md#learn-recurring-website-workflows).

## For custom client developers

Client initialization, discovery and tool calls belong to your runner. Use [Custom integrations](../integration/custom-agents.md) and the [onboarding tool reference](../mcp-reference/tools/app-shell-and-ui/nova-install-onboarding.md) for the technical contracts.
