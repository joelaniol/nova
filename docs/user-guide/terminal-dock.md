# Integrated Terminal Dock

> [!NOTE]
> Nova AI Workspace has a real terminal built in. It opens as a dock over the browser area, so you can run PowerShell, `claude`, `codex` or your build scripts next to the page you are working on.

---

## 1. Overview & Motivation

When an agent changes code, starts a local dev server or runs a deployment, checking the result usually means switching between a terminal window and the browser. The terminal dock keeps both in one window: the shell runs in the dock, the result shows in the tab behind it.

The terminal is a Windows pseudo console (ConPTY) session. It runs in a separate background service of Nova, so a terminal keeps running while the dock is collapsed or hidden.

* Turn it on or off under **Settings → AI & agents → Tasks & terminal → Terminal** with **Show the built-in terminal** (on by default).
* Open it with the **Terminal** button in the toolbar. On a fresh profile the dock stays closed until you open it; after that Nova remembers whether it was open.

---

## 2. Workspaces & Programs

The dock organises terminals as **workspaces**:

* **New Terminal** — start a new project or temporary environment, with a **Workspace name** and an optional project folder (**Choose project folder…**, otherwise the **Nova default folder**).
* **Join project** — open an existing project folder and start a terminal there.
* **Quick Terminal** — a temporary terminal that is not saved. **Clear Quick Terminal...** deletes the files in its temporary folder.
* **Recently used** and **Favorites** keep your workspaces at hand (**Pin as favorite**).

For each workspace you choose the **Program** that starts in it:

* Windows PowerShell or PowerShell 7 (`pwsh`) — Nova lists the installations it finds.
* **Claude Code** or **Codex**.
* **Custom…** — any command with optional arguments, for example `claude --model opus`.

---

## 3. Dock Modes

| Mode | How | Behavior |
| :--- | :--- | :--- |
| **Expanded** | **Terminal** button, or **Open the terminal again** | The full dock with the terminal. |
| **Collapsed** | **Collapse to the tab strip** | Only the dock's strip of terminal tabs stays visible. Double-click the move handle to expand it again. |
| **Hidden** | **Hide the terminal** | The dock disappears. |

Running sessions keep running in all three modes.

The dock lies over the page; it does not shrink the page. You can move it (**Move terminal**), resize its width, height or corner, and put it back with **Reset terminal layout**. The height is also available as **Terminal height (pixels)** in the terminal settings. **Open in a separate window** moves a terminal into its own **Nova Terminal** window.

---

## 4. Terminal Features

1. **Full terminal emulation:** colours, cursor control and full-screen interactive programs are supported. If you prefer plain output, **Colours in programs** in the terminal settings switches colours off for new sessions.
2. **Appearance:** **Theme** (**Standard Nova** or **Dark (VS Code)**) and **Font size** (Small to Very large) are set in the terminal settings. The font is Cascadia Mono, with Consolas as fallback.
3. **Stored credentials:** under **Credentials & keys** you can store API keys and tokens once and share them with chosen workspaces. Programs granted access in those workspaces receive them as environment variables. Those programs can read the values, so grant access only to workspaces and programs that should receive the credentials.
4. **Agent terminals:** agents open their own terminal sessions through Nova. These are separate from your terminals — an agent cannot type into yours. They appear in the dock under **Agent terminals** as read-only, so you can watch what they run.
5. **Agent dock control:** with **Allow agents to control the terminal dock** (on by default), agents may collapse, hide or show the dock through Nova. They cannot close your sessions this way.
6. **Activity at a glance:** the dot on a terminal tab pulses green while the program in it is producing output on its own, for example while Claude Code or Codex is working. This works for the terminal you are looking at as well as for terminals in the background. Your own typing does not count as activity.
7. **Links:** web addresses in the output are clickable. A click opens the address in a new Nova tab, a right-click copies it. A right-click on selected text copies the selection. Only `http` and `https` addresses are opened.

More on the architecture: [Terminal Workspaces](../core-features/terminal-workspaces.md).

## 5. Stopping work

Hiding or collapsing the dock does not stop a command. **Menu → Emergency stop** interrupts Nova's terminal sessions, including your own dock terminals, alongside agent work. It stays active until you release it. See [Staying in control](live-assist-and-spectator.md#3-staying-in-control).

Agent interfaces: [Terminal tools](../mcp-reference/tools/terminal-ops/README.md). Helper process: [Terminal runner](../components/terminal-runner.md).
