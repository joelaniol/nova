# Your First Five Minutes with Nova

Connect your AI program, give it a short research task, and watch the work happen in Nova.

## 1. Open Nova

[Install Nova](installation.md) if you have not done so, then open it from the Start menu. You also need an installed AI program such as Claude Code, Claude Desktop, Codex or Antigravity.

During the public alpha, the activation window is prefilled with shared trial details. If it appears, choose **Sign in**. No Nova registration is needed. If you entered your own license during setup, use that instead.

## 2. Connect your AI program

In Nova's connection wizard:

1. Choose **Easy setup (recommended)**. Nova shows the compatible programs it found.
2. Continue to **How the connection is saved**.
3. Click **Connect** beside your program if offered. An entry already listed as managed needs no new connection.

If the wizard is not open, use **Settings → AI & agents → Connection & setup → Set up**. If your program is missing, install it and choose **Search again**.

## 3. Restart your AI program

Close and reopen your AI program. Restart agent sessions and shells that were already running when the connection was saved; those sessions can still have the old configuration. For Claude Desktop, quit it completely, including its tray icon, before reopening it.

Check the AI program's MCP connection list before the first task. In clients that support it, enter **`/mcp`**; otherwise use their connection or tools view. **Nova should be listed as connected.** If it is missing or disconnected, return to Nova's connection wizard and check that program's entry.

> [!IMPORTANT]
> **Does the agent reach for `curl` to work with Nova?** In practice, this is an indicator that the MCP connection may be wrong or not loaded in the current session. Check the connection list and restart existing shells or agent sessions before continuing. For the first task, ask the agent to use Nova's registered MCP tools.

Once connected, supported AI programs can start Nova when needed and reconnect to it automatically.

## Recommended before your first task: optional onboarding

If you already have a project or working folder where you want to use Nova regularly, ask your agent:

> Please do the Nova project onboarding for this working folder. First explain which files you will create or update, and ask me if the target folder is unclear. Keep my existing instructions and permissions.

Tell the agent which folder you mean. Onboarding adds Nova's reference files under `.nova/` and a marked Nova section to the applicable project instruction file, such as `AGENTS.md` or `CLAUDE.md`. It does not change your agent client's permission settings.

This is recommended for regular project work, but **optional**. You can skip it and try the research task below without project files. See [Project onboarding](advanced-onboarding.md) for examples and the files involved.

## 4. Give it a task and watch

In your AI program, ask:

> Use Nova to research the current Microsoft Edge WebView2 release notes on Microsoft's official website. Open the relevant pages in Nova, summarize three recent changes, and give me the source links and release dates. No login or downloads needed.

Watch Nova's tabs as your agent browses. Agent activity is marked on tabs; with **AI visualization** enabled, a cursor and captions show supported browser actions. When the task finishes, you should have a short summary and source links you can open yourself.

If your AI program asks permission to use Nova, review and approve the requests needed for this task.

## Stay in control

**Menu → Emergency stop** interrupts agent work and remains active until you choose **Release emergency stop**. It also interrupts Nova's terminal sessions, including your own dock terminals. Moving your mouse or typing does not pause the agent.

Read [Emergency Stop](emergency-stop.md) for what it interrupts, what remains completed, and how to continue safely afterwards.

## What just happened?

- Your AI program provided the agent and kept your conversation.
- Nova provided the browser workspace and tools for the task.
- You could watch the work and interrupt it with Emergency stop.

**[What's next?](whats-next.md)** — explore browser features, set up optional project onboarding, or learn recurring website workflows.

If something did not work, start at [Troubleshooting](../troubleshooting/README.md). For taking over one tab and other controls, see [Staying in control](../user-guide/live-assist-and-spectator.md).
