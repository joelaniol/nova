# AI Visualization & Staying in Control

> [!NOTE]
> Nova AI Workspace shows you what an agent does in the browser while it does it, marks the tabs and sandboxes an agent is working in, and gives you an emergency stop. In the product this view is called **AI visualization**; it was described as "Live Assist" or "Spectator Mode" in earlier versions of this guide.

---

## 1. What Is the AI Visualization?

Keep this view enabled when you want to follow an agent's browser work without reading its tool calls. It shows supported actions as they happen; it is not a transcript of the agent's private reasoning.

The **AI visualization** (also called the assist cursor) mirrors agent actions on screen:
* An on-screen cursor labelled **AI** moves to the element the agent is about to use and pulses when it acts.
* A short caption says what is happening — for example *Searching target...*, *Target locked*, *Performing action...*, *Verified* or *Verification failed*.
* An optional step card shows the current and the next step (*Step 2/5: Click*, *Next step: Verify result*).

It covers clicks, typing, option selection, scrolling, waiting for elements, navigation and the guarded actions.

```mermaid
flowchart LR
    Agent["MCP agent"] -->|"tool call, e.g. nova.click_selector"| Nova["Nova"]
    Nova -->|"input"| Page["Web page"]
    Nova -->|"visualization"| Overlay["AI cursor, caption, step card"]
    Overlay --> Human["You"]
    Human -.->|"Menu - Emergency stop"| Nova
```

---

## 2. Settings & Indicators

### 2.1 Turning It On or Off
* The visualization is on by default. Toggle it quickly with **Menu → View → AI visualization**.
* Under **Settings → Appearance & performance → AI visualization** you find **Show assist cursor (AI)**, **Assist cursor: reduced motion** and **Show optional step card (current and next step)**. Less certain steps move slower and stay visible longer.

### 2.2 Agent Markers on Tabs and Sandboxes
* Tabs and sandbox pills that an agent works in carry a marker. Its tooltip tells you the state: *Agent active*, *Agent recently active* or *Agent reserved* (the agent has claimed the tab but is not acting right now).
* While agents are active, an activity indicator lists active and reserved targets; from its details you can switch to a claimed tab or release the claim. On a sandbox pill, **Release agent** does the same.
* Outside the window, the Nova button in the taskbar shows agent activity; when Nova keeps running in the background, its icon in the notification area says *an agent is working*.

For taking over a tab or interrupting work, see [Taking over and emergency stop](taking-over-and-emergency-stop.md).

[Back to this section](README.md) · [All user guides](../README.md)
