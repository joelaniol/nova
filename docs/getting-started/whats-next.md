# What's Next?

After your [first task](quickstart.md), choose what you want to do next.

## Use Nova as a browser

The [User guide](../user-guide/README.md) covers everyday browsing. Start with the [workspace tour](../user-guide/workspace-layout.md), then explore [sandboxes and separate logins](../user-guide/sandboxes-and-profiles.md), [downloads](../user-guide/downloads-manager.md), or the [terminal dock](../user-guide/terminal-dock.md).

For agent-authored plugins and terminal connectors, check the [current alpha limitations](../../ALPHA.md#known-issues) before using them.

## Use Nova with agents regularly

### Recommended: optional project onboarding

If you plan to use Nova regularly in a project or workspace folder, tell your agent:

> Please do Nova's onboarding for this project. Preserve my existing instructions and permissions, and show me which files you added or updated.

This helps later sessions find Nova's working instructions. By default, the agent installs the references in the current project's `.nova/` subfolder and adds a marked section to the project's agent instruction files. You can optionally specify a different working folder. It requires agent self-onboarding to be enabled in Nova's settings; it does not grant tool permissions. Onboarding is optional and is separate from learning a website. See [Project onboarding and custom workflows](advanced-onboarding.md).

### Learn recurring website workflows

For your own rules on a website, use [Domain Notes](../user-guide/domain-notes.md). The guide shows how to require acknowledgement and ask your agent to explain the instructions before acting.

For tasks you repeat on the same website, ask your agent to use **Learn Mode**:

Read [Use Learn Mode](learn-mode.md) for the difference from normal tasks, useful scenarios, prompt examples and what to expect back.

> I will repeat this task on this website. Use Nova's Learn Mode to explore the relevant workflow, verify what works, and produce a reusable platform playbook. Ask me if the intended workflow is unclear.

Explain your goal and what you expect to repeat. The agent handles Nova's learning instructions and onboarding steps. Learn Mode builds evidence-backed website knowledge; it does not authorize purchases, sending messages, or other account changes. See [Website memory (PKS)](../core-features/pks.md) and [learning tools](../mcp-reference/tools/pks-and-learning/README.md).

For a guided local exercise, try the [interactive demo](../../demos/README.md).

## Understand how Nova works

- [How the connection works](mcp-setup.md) — why restarting the AI program matters and how Nova reconnects.
- [Architecture and processes](../components/README.md) — Nova and its helper processes.
- [Core features](../core-features/README.md) — memory, learning and verification.
- [MCP reference](../mcp-reference/README.md) — tools and custom integrations.

## Problems or feedback?

Start at [Troubleshooting](../troubleshooting/README.md). For an observed defect or work-session feedback, ask your agent for [Nova's reporting guide](../mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md). Security vulnerabilities use the [private reporting route](../../SECURITY.md).
