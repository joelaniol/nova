# Taking Over & Emergency Stop

Use these controls when you want to interrupt agent work or reclaim a tab. To follow its actions, see [Watching agent work](watching-agent-work.md).

## 3. Staying in Control

1. **Emergency stop:** **Menu → Emergency stop** interrupts agent work at once — pending MCP requests, running crawls, scheduled task runs, all sessions of Nova's terminal service (including your own terminals in the dock) and connections to external MCP servers. Nova confirms with *Emergency stop active. Agents, the agent interface (MCP), and running scripts were interrupted.*
2. **Releasing the stop:** the stop stays active until you choose **Menu → Release emergency stop**. After that, agents and the agent interface can run again.
3. **Your own input:** you can keep using the browser while an agent works — it is the same browser with the same sessions. When you type or use browser shortcuts, the visualization steps aside. This does not pause the agent; to interrupt all agent work, use the emergency stop. To take over one claimed tab, release its claim from the activity details or choose **Release agent** on the sandbox pill; confirm **Take over control** if prompted. Releasing a claim is distinct from the global emergency stop.

There is no keyboard shortcut for the emergency stop.

For a step-by-step guide to stopping and continuing, including the effect on your own terminals and completed actions, see [Emergency Stop](../../getting-started/emergency-stop.md).

[Back to this section](README.md) · [All user guides](../README.md)
