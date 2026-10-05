# Advanced Onboarding and Bootstrap

These steps are for project-based work and custom agent workflows. They are not prerequisites for the [first-task Quickstart](quickstart.md).

## Optional project reference files

For recurring development work, ask your agent to install Nova's onboarding reference in the project folder you choose. `nova.install_onboarding` requires an absolute `projectRoot`; a location Nova has not onboarded before also requires `confirmNewLocation: true`.

Nova writes its reference documents under `.nova/`, including `nova-mcp.quick.md` and `nova-mcp.md`, and marked instruction sections in the supported project agent files. These help later sessions find Nova's guidance. Nova does not write your agent client's permission configuration. Details and supported options: [install_onboarding](../mcp-reference/tools/app-shell-and-ui/nova-install-onboarding.md).

## Explicit session bootstrap

An agent should obtain Nova's current guidance and discover the tools it needs. For a custom workflow, start with these calls:

```text
nova.get_instructions(taskKeywords=["browser", "research"])
nova.tools_bundle(bundle="browser_automation")
```

For an unfamiliar capability, use `nova.tools_bundle(query="describe the task here")` instead of guessing a tool or bundle name. The [MCP reference](../mcp-reference/README.md) explains discovery and the tool catalog.

## Working with several agents

Agents can reserve tabs with a claim and release them when finished. This prevents competing work in the same tab. Your client guide explains coordination options; you do not need to issue claims manually for ordinary first tasks.

See [Agent integration](../integration/README.md), [Tab claims](../mcp-reference/tools/browser-automation/nova-tab-claim.md) and [Staying in control](../user-guide/live-assist-and-spectator.md).
