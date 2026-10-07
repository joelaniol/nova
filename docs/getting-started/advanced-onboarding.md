# Optional Project Onboarding

Once your agent is connected to Nova, project onboarding is recommended if you plan to use Nova regularly in a project. You can do it before your [first task](quickstart.md#recommended-before-your-first-task-optional-onboarding) or add it later. It is optional and gives later agent sessions a local reference to Nova's working instructions.

## Ask your agent to do the onboarding

Open your project in your AI program and ask the agent to do Nova's onboarding. By default, the agent uses the current project and installs Nova's reference files in its `.nova/` subfolder. You do not need to choose a separate installation folder.

Paste this into the agent's conversation:

> Please do Nova's onboarding for this project. Use Nova's current onboarding instructions, preserve my existing project instructions and permissions, and show me which files you added or updated.

The agent handles the tool calls and any required confirmation for a new location. If it cannot identify the current project, it should ask you which project you mean. You do not need to enter tool parameters yourself.

## Optional: use a different location

You can explicitly tell the agent to install the onboarding in another working folder instead:

> Please install Nova's onboarding in [full path to my other working folder] instead of the current project. Preserve existing instructions there and show me the files you added or updated.

The reference files go into that folder's `.nova/` subfolder, and the Nova marker sections go into the applicable instruction files there. This changes where onboarding is installed; it does not move your project or change the default location of Nova's application data.

## Check what changed

Nova writes its own reference files under `.nova/`, including `nova-mcp.quick.md` and `nova-mcp.md`, and marked Nova sections in the supported project instruction files. Existing instructions outside those sections are preserved.

Ask the agent to show you the changed paths. Onboarding should not create or edit your agent client's permission configuration. Tool approvals in Claude, Codex or another client remain a separate decision.

If the agent reports that self-onboarding is disabled, open **Menu → Settings → AI & agents → Confirmations & audit** and check **Agent self-onboarding (install/get_onboarding tools)**. Enable it if you want this feature, then ask the agent to retry. For a connection problem, follow [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).

## Use the project again

In a later session, ask your agent to use Nova for the task. The reference files help it find Nova's guidance; they do not replace a working MCP connection. Restart sessions that were open when the connection changed.

Project onboarding is separate from teaching Nova a website workflow. For recurring work on the same website, see [Learn Mode](whats-next.md#learn-recurring-website-workflows).

## For custom client developers

Client initialization, discovery and tool calls belong to your runner. Use [Custom integrations](../integration/custom-agents.md) and the [onboarding tool reference](../mcp-reference/tools/app-shell-and-ui/nova-install-onboarding.md) for the technical contracts.
