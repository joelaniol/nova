# Settings & Connecting an AI Program

Open **Menu → Settings** to change how Nova behaves. Use **Set up** in the settings navigation to check or add an AI connection.

## Connect an AI program

1. Open **Set up** and enable AI access if asked.
2. Choose **Easy setup (recommended)**.
3. Review **Your AI programs**, where Nova lists the programs it found.
4. Continue to **How the connection is saved**. Review the destinations and use **Connect** for the connection you want to add. A connection already managed by Nova does not need another Connect action.
5. Restart the AI program, then ask it to do a small browser task, such as finding cat pictures.

If a program is missing, install or start it and search again. **Connect another program** provides setup text for other clients. The [integration hub](../integration/README.md) has a guide for each supported client and for custom agents.

Nova adds or updates its own connection entry. It does not configure your agent client's permission allowlist. Approvals shown inside Claude, Codex or another client are controlled by that client.

## Find the right setting

| You want to change … | Start here |
|---|---|
| Download folder or automatic opening of file types | **General**; see [Downloads](downloads-manager.md) |
| Separate accounts, sandbox names or start pages | **Sandboxes**; see [Sandboxes and profiles](sandboxes-and-profiles.md) |
| Website access to devices or location | **Site permissions**; see [Permissions](permissions.md) |
| Agent access, autonomy or terminal behavior | **AI & agents**; see [Permissions](permissions.md) and [Terminal dock](terminal-dock.md) |
| The assist cursor, reduced motion or step card | **Appearance & performance → AI visualization** |

For a temporary interruption, use **Menu → Emergency stop**. To disable browser control more generally, switch off **Allow agents to control the browser** in settings. See [Staying in control](live-assist-and-spectator.md#3-staying-in-control) for the difference.

## Advanced connections

Most users can stay with the wizard. Custom scripts and clients can use Nova's stdio bridge or a direct authenticated connection; see [Custom agents](../integration/custom-agents.md) and [Protocol and transport](../mcp-reference/protocol-and-transport.md).

Access from other devices is off by default and requires **Allow access from other devices on the network**. Enable it only when you intend to make Nova available on that network. Connection keys authorize browser control; keep them private.

If setup fails, start with [Connection troubleshooting](../troubleshooting/agent-connection-issues.md).
