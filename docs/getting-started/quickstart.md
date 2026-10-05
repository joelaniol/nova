# Your First Task with Nova

Start Nova, connect your AI program, and ask for something you want. You do not need to learn tool names to begin.

## 1. Open Nova and connect

If you have not installed Nova yet, follow [Installation](installation.md). You also need a supported AI program, such as Claude Code, Claude Desktop, Codex or Antigravity, installed on this computer.

On first start, follow Nova's connection wizard:

1. Choose **Easy setup (recommended)**. Nova shows the compatible programs it found.
2. Continue to **How the connection is saved** and click **Connect** beside your program if offered. If Nova already lists its entry as managed, you can continue.
3. Restart your AI program, or start a new CLI session, so it loads the connection. For Claude Desktop, quit it completely, including its tray icon, before reopening it.

If the wizard is not open, use **Settings → AI & agents → Connection & setup → Set up**. If your program is not detected, use **Search again** after installing it, or choose its [integration guide](../integration/README.md).

## 2. Ask for your first task

In your AI program, ask:

> Use Nova to find cat pictures. Open the results in Nova and give me three source links.

Watch Nova's tabs as the agent browses. You should see a results page and receive links you can open yourself. If your AI program asks permission to use Nova's tools, review and approve the requests needed for your task.

The agent should handle Nova's working instructions and tool discovery. You do not need to paste a bootstrap sequence, install project files or manage tab claims for this first task.

Prefer a local exercise? Try the [interactive demo](../../demos/README.md).

## 3. See what is happening and stay in control

Agent activity is marked on tabs. With **AI visualization** enabled, an AI cursor and captions show supported browser actions.

**Menu → Emergency stop** interrupts agent work and remains active until you choose **Release emergency stop**. Typing or moving your mouse does not pause the agent. See [Staying in control](../user-guide/live-assist-and-spectator.md) for taking over a single tab and the scope of the stop.

## If the first task does not work

Start at [Troubleshooting](../troubleshooting/README.md). Choose **Connection** if Nova is missing or disconnected; choose **Agent behavior** if it is connected but the agent does not use it or cannot read its results.

## What Nova configured for you

Nova adds or updates its own connection entry in supported AI programs, subject to your connection settings. The entry starts Nova's bridge, which finds the browser and supplies its access token. You do not need to copy the token into client configuration.

Nova keeps its own entry current when automatic sync is enabled. Your AI program's tool approvals remain your decision; connecting Nova does not create a permission allowlist for it.

Details: [Agent integration](../integration/README.md).

## Advanced onboarding / bootstrap

Project reference files, explicit tool discovery and tab coordination are useful for development and custom agents. They are optional setup beyond this first task: [Advanced onboarding and bootstrap](advanced-onboarding.md).

Next: [First-run orientation](first-run.md) or the [User guide](../user-guide/README.md).
