# Emergency Stop: Stop Work in Nova

Use **Menu → Emergency stop** when you want to interrupt agent work in Nova. You can activate it yourself without asking the agent or waiting for its next reply.

## Activate the stop

1. Open Nova's main menu.
2. Choose **Emergency stop**.
3. Nova shows **Emergency stop active**. The menu entry changes to **Release emergency stop**.

The stop blocks new agent/tool actions in Nova and interrupts running work. It stays active in the current Nova session until you release it. There is no keyboard shortcut for Emergency stop.

> [!IMPORTANT]
> **Your own Nova terminals are affected too.** Emergency stop terminates sessions managed by Nova's terminal service, including terminals you opened in the dock. Save work before deliberately trying it out.

## What it interrupts

| Work in Nova | Effect of Emergency stop |
|---|---|
| Agent requests and tool actions | Pending requests are cancelled; new actions are blocked while the stop is active. |
| Running crawls | Active crawls are cancelled. |
| Scheduled task runs | Running tasks are cancelled; scheduled work is blocked while the stop is active. |
| Nova terminal sessions and scripts | Sessions managed by Nova's terminal service are terminated, including your own dock terminals. |
| Connections from Nova to external MCP servers | Nova stops its external MCP sessions. |

Emergency stop acts on work managed through Nova. Your separate AI program can still be running or generating a reply; stop its task there too if you want the whole agent run to end. It does not terminate unrelated programs or shells outside Nova's terminal service.

Stopping is not undoing. A message already sent, a saved file or a change accepted by another service remains a completed action. Disconnecting from an external service does not guarantee that a job already accepted by that service stops there. Check the outcome before retrying a task.

## Continue after a stop

1. Check what happened in Nova and in your AI program. Decide whether to stop, change or continue the task.
2. When ready, open **Menu → Release emergency stop**. It becomes available after Nova finishes applying the stop.
3. Nova confirms **Emergency stop released**. Agent/tool actions can run again.
4. If needed, reopen your terminated Nova terminal sessions. Give your agent a clear instruction to inspect the current state before continuing.

For example, tell your agent:

> I interrupted the task with Nova's Emergency stop and have now released it. Check what was completed and what is still pending. Tell me before retrying anything that could duplicate a change.

Releasing the stop enables work again; it does not restore terminated shells or undo completed actions. Scheduled work can become eligible again, so review or disable unwanted schedules before releasing the stop.

## Take over one tab instead

Moving your mouse or typing does not pause the agent. To take over a single claimed tab, use the activity details to release its claim, or choose **Release agent** on its sandbox pill; confirm **Take over control** if prompted. This releases that claim and is distinct from the global Emergency stop.

See [AI visualization and staying in control](../user-guide/live-assist-and-spectator.md#3-staying-in-control) for activity markers and tab controls. Continue with [Your first five minutes](quickstart.md) or [What's next?](whats-next.md).
