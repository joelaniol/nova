# Troubleshooting

Choose the problem you can see. You do not need to know whether it belongs to the browser, the bridge or the agent.

## Start here

| What is happening? | Go to |
|---|---|
| Setup will not run, or Nova asks for activation | [Installation](#installation) |
| Your AI program cannot find or connect to Nova | [Connection](#connection) |
| It connects, but does not use Nova or cannot read its results | [Agent behavior](#agent-behavior) |
| A tab, login, sandbox or running agent needs attention | [Browser and sessions](#browser-and-sessions) |
| You need logs or details of a failure | [Diagnostics](#diagnostics) |
| The problem happens with one particular AI program | [Client-specific quirks](#client-specific-quirks) |

## Installation

Check the [installation requirements and setup notes](../getting-started/installation.md), including WebView2 and SmartScreen. For the current public alpha activation details, use [Alpha Trial License](../getting-started/trial-license.md).

If Nova does not start after setup, follow [Diagnostics](diagnostics.md). Do not reinstall or delete your browser profile as the first troubleshooting step.

## Connection

First, keep Nova open, use its connection wizard to check your AI program, and restart that program after connecting. Claude Desktop must be fully quit, including its tray icon.

If that does not help, follow [Agent connection issues](agent-connection-issues.md) for the local server, bridge and client entry checks. Manual configuration belongs in your [client's integration guide](../integration/README.md).

## Agent behavior

For a connected agent that avoids Nova, reports missing tools, sees only summary text or gets stuck on a page, follow [Agent behavior](agent-behavior.md).

## Browser and sessions

- To interrupt work or take over a tab, use [Staying in control](../user-guide/live-assist-and-spectator.md).
- For abandoned tabs, held claims, media streams or missing sandboxes, use [Sandbox and session recovery](sandbox-and-session-recovery.md).
- For everyday tabs, profiles, downloads and prompts, use the [User guide](../user-guide/README.md).

## Diagnostics

[Diagnostics and logs](diagnostics.md) explains where to find startup, browser and connection evidence. Note what you were doing and the visible error. Review logs and screenshots for personal data and secrets before sharing them; follow the [alpha reporting policy](../../ALPHA.md#what-to-report).

## Client-specific quirks

| Client | Setup and help |
|---|---|
| Claude Code | [Client guide](../integration/claude-code.md) |
| Claude Desktop | [Client guide](../integration/claude-desktop.md) · [Connection issues](agent-connection-issues.md#2-claude-desktop-shows-no-nova-tools) |
| OpenAI Codex CLI | [Client guide](../integration/openai-codex.md) |
| Google Antigravity / Gemini CLI | [Client guide](../integration/google-antigravity.md) · [Compatibility help](antigravity.md) |
| Another MCP client | [Custom agents](../integration/custom-agents.md) · [Missing result data](agent-behavior.md#the-agent-sees-only-summaries) |
