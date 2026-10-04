# Sandbox & Session Recovery

This guide covers what to do when agent tabs are left behind, a tab stays claimed by another agent, a page keeps the camera or microphone running, or a sandbox is missing after a restart.

---

## 1. Cleaning Up Orphaned Agent Tabs

### The Problem
An agent opened tabs with `nova.tab_new` and crashed or lost its context before closing them. The tabs stay open and use memory.

### Resolution
Preview first, then clean up:

```json
nova.tab_cleanup_orphans({ "dryRun": true })
nova.tab_cleanup_orphans({})
```

* **What counts as orphaned:** only tabs an agent created over MCP that have no live claim, are not the tab you are currently looking at, and have been idle longer than `graceMinutes` (default 15, range 1–720).
* **What stays:** tabs you opened yourself are never closed. Nova re-checks the active tab right before closing, so a tab you switch to in the meantime is kept.
* Nova never runs this cleanup on a timer; it happens only when the tool is called.

---

## 2. Resolving Tab Claims Held by Another Agent

### The Problem
An agent claimed a tab with `nova.tab_claim` and stopped before calling `nova.tab_release`. Other agents that try to act on the tab get error `-32040` with `reasonCode: "claim.owner_mismatch"` and a message such as:
```
Tab claimed by 'subagent-1' (lease 87s remaining). Your agentId is 'default'. …
```

### Resolution
1. **Wait for the lease to run out:** Every claim has a lease. `nova.tab_claim` uses 120 seconds unless `ttlMs` says otherwise (5 seconds to 30 minutes). When it runs out, the tab is free again.
2. **Resume as the owner:** If you are continuing that agent's work, retry with the owner's `agentId` from the message, or release the tab with it:
   ```json
   nova.tab_release({ "targetId": "<targetId>", "agentId": "subagent-1" })
   ```
3. **Take the tab over:** `nova.tab_claim` with a `reclaimReason` force-releases the existing claim; the previous owner is told the reason. Do this only when the user agrees.
   ```json
   nova.tab_claim({ "targetId": "<targetId>", "agentId": "coordinator", "reclaimReason": "previous agent crashed" })
   ```

---

## 3. Stopping Camera, Microphone and Screen Sharing (`nova.media_stop_all`)

### The Problem
A page or an automated session left a camera, microphone or screen-sharing stream running.

### Resolution
```json
nova.media_stop_all({})
```

* Stops every live camera, microphone and screen-sharing track in every tab and sandbox. With `"scope": "origin"` and an `origin`, only that site's tracks are stopped.
* It does **not** change saved permissions and does **not** forget temporary session grants, so the page may start the device again. To forget the session grants and stop their streams in one step, call `nova.media_permissions_clear_session_grants`.

---

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

### Best Practice Rules
* **Close Nova before editing or restoring `settings.json`.** Nova writes this file itself while it runs.
* **Do not delete sandbox folders by hand.** Delete a sandbox in **Settings → Sandboxes**, or have an agent call `nova.sandbox_delete` (with `"confirm": true`). Nova then closes the sandbox's browser view and removes its data. At least one sandbox always remains.

---

## Next Steps

* Return to the **[Troubleshooting Hub](README.md)**.
* Check [Agent Connection Issues](agent-connection-issues.md) for connectivity problems.
