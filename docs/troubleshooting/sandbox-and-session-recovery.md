# Sandbox & Session Recovery

This guide covers recovery procedures when tabs hang, subagents crash mid-execution, background processes leak resources, or browser sandboxes require restoration.

---

## 1. Cleaning Orphaned Background Tabs

### The Problem
During large-scale automated crawls, crawler verify runs, or parallel subagent jobs, hidden or detached tabs may linger in memory if an agent crashes unexpectedly before closing them.

### Resolution
Call the built-in orphan cleanup tool:

```json
nova.tab_cleanup_orphans({})
```

* **What it does:** Scans the active WebView2 controller registry for tabs that possess no parent window, no active agent lease, and no open user surface.
* **Result:** Closes all orphaned WebViews cleanly, flushes memory, and releases associated network handles.

---

## 2. Resolving Tab Lease Locks (`lease_conflict`)

### The Problem
An agent claimed exclusive access to a tab using `nova.tab_claim`, but the agent process terminated or encountered an unhandled exception before calling `nova.tab_release`. Subsequent agents attempting to interact with the tab receive:
```
-32002: Tab is locked by another agent lease
```

### Resolution
1. **Wait for Lease Expiration:** Every claim has a finite duration (default: 5 minutes / 300,000 ms). Once `leaseRemainingMs` reaches 0, the lock expires automatically.
2. **Explicit Release:** The parent coordinator agent or a new session can release the target:
   ```json
   nova.tab_release({
     "targetId": "tab-1"
   })
   ```

---

## 3. Emergency Media Stop (`nova.media_stop_all`)

### The Problem
A web page or automated meeting transcription session left an active microphone stream, camera capture, or WebAudio recording buffer running in the background.

### Resolution
Execute the global emergency stop tool:

```json
nova.media_stop_all({})
```

* **Instant Hardware Cut:** Immediately halts all audio capture, screen recording, and microphone streams across all tabs and sandboxes.
* **Revokes Session Grants:** Clears ephemeral media permission grants in the Permission Center.

---

## 4. Sandbox Profile Recovery & Integrity

### The Problem
A custom sandbox (e.g. `Sandbox B`) does not appear in the dropdown after an unexpected system restart.

### How Sandbox Recovery Works
Nova uses a robust **Disk-Anchor Architecture**:
* Every sandbox stores its persistent user data under:
  ```
  %LOCALAPPDATA%\NovaBrowser\Profiles\<SandboxId>\
  ```
* During startup, Nova reconciles the list in `settings.json` against the physical profile folders on disk.
* If `settings.json` is missing or corrupted, Nova automatically reconstructs the profile list from the disk anchors.

### Best Practice Rules:
* **Never edit `settings.json` while Nova is running:** The in-memory settings manager will overwrite external changes on shutdown.
* **Never delete disk profile directories directly:** Use `nova.sandbox_delete` to ensure WebView2 processes release all file locks first.

---

## Next Steps

* Return to the **[Troubleshooting Hub](README.md)**.
* Check [Agent Connection Issues](agent-connection-issues.md) for connectivity problems.
