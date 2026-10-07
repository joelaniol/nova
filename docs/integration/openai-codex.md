# Connect Codex CLI to Nova

Connect Codex through Nova's wizard, then start a new Codex session. Codex handles the task, chooses tools and processes their results.

## Connect through Nova

Follow [Your first five minutes](../getting-started/quickstart.md), choosing **Codex** in the program list. Click **Connect** if offered.

Close the existing Codex session and start a new one so it loads the connection. Then try the [first research task](../getting-started/quickstart.md#4-give-it-a-task-and-watch).

## Have Codex configure the connection

In Nova's wizard, choose **Set up manually → Let an AI program do it → Copy text for an AI program**. Paste that text into Codex and ask it to configure Nova for this Codex installation.

Use the generated agent instructions for Codex: its configuration uses TOML, so the JSON entry intended for other clients is not a replacement. Review the changes and start a new Codex session afterwards. See [the connection guide](README.md#ask-your-agent-to-set-it-up) for handling the setup text.

## Regular work

Give Codex a goal and ask it to use Nova. You do not need to pick result sizes, write tool calls, or manage tab claims yourself.

If you want Nova's instructions available in later project sessions, ask for optional [project onboarding](../getting-started/whats-next.md#recommended-optional-project-onboarding). For repeated website tasks, see [Learn Mode](../getting-started/whats-next.md#learn-recurring-website-workflows).

## If it does not connect

Reopen Nova's wizard and read the Codex row. Check that you started a new session after the connection was saved. Continue with [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).
