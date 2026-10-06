# MCP Setup

How Nova connects to your AI program, and the one step people most often miss.

---

## What the setup does

Nova's setup guide finds the AI programs on your computer (Claude Code, Codex, Antigravity, Claude Desktop) and adds a single entry named `nova` to each program's own MCP configuration. Other entries in those files stay untouched, and no password or access key is written into them. The last page of the guide lists every program, its status and the file Nova updated.

## Restart your AI program

An AI program reads its MCP configuration **when it starts**. A Claude Code, Codex or Antigravity window that was already open during the setup keeps running without Nova, even though the setup reports success.

Close every open window or terminal session of the program and start it again. The setup guide names the programs it found running; a session started some other way (for example Claude Code through npm) may not be detected, so restart it as well.

## Check the connection

Ask your AI program: **“Can you use Nova?”** If it finds Nova, give it a first task, for example: **“Use Nova to find cat pictures and give me three source links.”**

## Still not connected?

- Make sure Nova is running and AI access is switched on in Nova's settings.
- Open the setup guide again from Nova's settings and check the status of each program.
- See [Troubleshooting](../troubleshooting/README.md) and [Agent integration](../integration/README.md) for client-specific details.
