# Connect Claude Code to Nova

Use Nova's connection wizard or give Claude Code Nova's generated setup text. After connecting, ask Claude Code for a task and let it handle Nova's tools and results.

## Connect through Nova

Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Claude Code** in the program list. Click **Connect** if offered, then close the existing Claude Code session and start a new one.

If Claude Code is not listed, install it or make its installation available to Nova, then choose **Search again**.

## Have Claude Code configure the connection

Open Nova's wizard and choose **Set up manually → Let an AI program do it → Copy text for an AI program**. Paste the generated text into Claude Code and ask it to set up Nova for this Claude Code installation.

The text tells the agent which connection to add and supplies your current Nova details. Review the proposed changes, then start a new Claude Code session. See [the connection guide](README.md#ask-your-agent-to-set-it-up) for handling the setup text.

## Try a task

Use the [first research task](../getting-started/quickstart.md#4-give-it-a-task-and-watch), or describe your own goal. Your conversation and final answer stay in Claude Code; the browser work happens in Nova.

For recurring project work, optional [project onboarding](../getting-started/whats-next.md#recommended-optional-project-onboarding) helps later sessions find Nova's instructions.

## If it does not connect

Reopen the wizard and read the Claude Code row. It distinguishes a missing registration, an outdated entry, disabled automatic setup, a missing runner, and an unreadable configuration.

Use [Connection troubleshooting](../troubleshooting/agent-connection-issues.md). For a manually managed entry, use the current details supplied by Nova instead of copying a path from another machine.
