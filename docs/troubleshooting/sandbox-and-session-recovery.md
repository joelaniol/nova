# Sandbox & Session Recovery

Choose the problem below. To interrupt all agent work immediately, use **Menu → Emergency stop**; see [Staying in control](../user-guide/agents/taking-over-and-emergency-stop.md#3-staying-in-control) for its reach.

## 1. Cleaning Up Orphaned Agent Tabs

If an agent stopped and left tabs behind, you can close the tabs you recognize as no longer needed. To have your connected agent investigate first, ask:

> Check for abandoned agent-created tabs in Nova. Show me a cleanup preview before closing anything. Keep my own tabs and the tab I am viewing.

Nova's cleanup tool considers only agent-created tabs without a live claim that have been idle beyond its grace period. Cleanup runs when requested, not on a timer. Ask the agent to report which tabs were closed; a preview alone does not close them.

## 2. Resolving Tab Claims Held by Another Agent

A reservation can prevent another agent from changing a tab. If work is still running, let it finish or ask that agent to release the tab.

To take over yourself:

1. Open Nova's agent activity details and select the affected target. You can also right-click a claimed sandbox pill.
2. Choose **Release agent** for that target.
3. Review **Take over control** if Nova asks for confirmation.
4. Return to the tab and check its agent marker. Tell your agent whether to continue or leave that tab alone.

This releases a reservation; it is distinct from Emergency stop. Claims also expire, but an active agent can renew its reservation. Do not copy another agent's identity into a tool call to bypass ownership.

Developers implementing recovery can use the [claim](../mcp-reference/tools/browser-automation/nova-tab-claim.md) and [release](../mcp-reference/tools/browser-automation/nova-tab-release.md) contracts. Session ownership and Nova's reclaim setting apply.

## 3. Stopping Camera, Microphone and Screen Sharing (`nova.media_stop_all`)

First stop sharing or recording using the website's own control, or close the affected tab. To stop streams across Nova with help from your connected agent, ask:

> Stop the active camera, microphone and screen-sharing streams in Nova. Tell me which streams were stopped and whether any remain.

Stopping a stream does not revoke a saved permission; the site may request access again. Open **Settings → Site permissions** to review the site's stored decision. **Stop all temporary grants** also clears temporary media grants and stops their affected streams; it does not erase saved site choices.

For the technical interfaces, see [media stop](../mcp-reference/tools/media-and-transcription/nova-media-stop-all.md).

## 4. Sandbox Profile Recovery

### The Problem
A sandbox (for example `Sandbox B`) is missing after a crash or restart, or Nova shows the **Recover sandbox profiles** dialog on startup.

### How Sandbox Recovery Works
* Each sandbox keeps its browser data (cookies, logins, site storage) in its own folder in Nova's profile folder (see [Diagnostics → Local Filesystem Locations](diagnostics.md#1-local-filesystem-locations)):
  ```
  <profile folder>\UserData\Shared\EBWebView\WV2Profile_<id>\
  ```
  Next to the browser data, the folder holds a small marker file that records which sandbox it belongs to.
* On every start Nova compares the sandbox list in `settings.json` with these folders:
  * **Sandbox list empty or missing** (for example a damaged `settings.json`): Nova restores all sandboxes from their folders.
  * **A sandbox folder is missing from the list** but was not deleted: Nova adds it back automatically, as long as its letter is free and the sandbox limit is not reached.
  * **Otherwise** (its letter is now used by another sandbox, or no slot is free): Nova shows the **Recover sandbox profiles** dialog.
  * Nova never removes sandboxes from the list on its own.

### The Recover Sandbox Profiles Dialog
For each profile you can choose:
* **Restore** — the sandbox comes back with its cookies, sessions and logged-in accounts. Restore only profiles you recognize.
* **Delete permanently** — the folder is removed from disk on the next launch. This cannot be undone.
* **Leave for now** — the folder stays on disk and Nova does not ask again about this profile. Profiles from early Nova versions that have no marker file are offered again on the next start.

**Restore all**, **Delete all permanently** and **Close (leave for now)** apply one choice to every entry. If no sandbox slot is free, delete a sandbox you no longer need before restoring one.

### If the sandbox is still missing

Check **Settings → Sandboxes → Hidden sandboxes** first: a hidden sandbox retains its data and can be shown again. If it is missing there too, keep its profile folder and ask your agent to investigate using [Diagnostics](diagnostics.md). Describe the sandbox name and when it disappeared. Do not recreate it or edit `settings.json` as the first repair.

To intentionally remove a sandbox, use **Settings → Sandboxes → Delete...** and review the confirmation. This deletes its browser data permanently. At least one sandbox remains.

---

## Next Steps

* Return to the **[Troubleshooting Hub](README.md)**.
* Check [Agent Connection Issues](agent-connection-issues.md) for connectivity problems.
