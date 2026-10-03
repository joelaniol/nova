# `nova.tab_close`

Closes an open browser tab or background WebView, releasing its system resources and associated leases.

---

## 1. Overview

`nova.tab_close` terminates a specified browser tab inside Nova AI Workspace. It cleans up the underlying Microsoft WebView2 controller, releases network handles, unregisters any active tab leases, and restores focus to the nearest remaining tab.

* **Capability Bundle:** `browser_automation`
* **Target Scope:** Tab-specific (defaults to the currently active tab).
* **Cleanup:** Frees DOM trees, GPU compositing memory, and temporary session state.

---

## 2. Key Capabilities & Features

### A. Controlled Teardown
When an agent completes a scraping or audit task on an ephemeral tab (`private: true`), calling `nova.tab_close` ensures:
* All in-memory private session tokens and cookie jars are scrubbed.
* Any active tab claims held by `agentId` are cleanly released without waiting for lease timeouts.

### B. Protection Against Host Window Shutdown
Closing a regular browser tab will not exit Nova AI Workspace even if it was the last visible tab. Nova automatically falls back to an empty new tab surface or home view unless `nova.app_quit` is explicitly called.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | No | `"active"` | The ID of the tab to close. Defaults to the active tab. |
| **`agentId`** | `string` | No | `"default"` | Identity of the calling agent for claim validation. |
| **`_meta`** | `object` | No | `null` | Optional intent metadata (`{ "intent": "Finished task" }`). |

---

## 4. Example Call

```json
{
  "name": "nova.tab_close",
  "arguments": {
    "targetId": "tab-5"
  }
}
```

### Sample Response
```json
{
  "ok": true,
  "closedTargetId": "tab-5",
  "activeTargetId": "tab-1",
  "remainingTabCount": 3
}
```

---

## 5. Best Practices & Common Traps

* **Verify Target ID Before Closing:** Always pass an explicit `targetId` when working with multiple tabs. Omitting `targetId` closes the currently focused tab, which might be a tab the human user is actively reading.
* **Cleaning Orphaned Tabs:** If an automated workflow crashed and left multiple hidden tabs open without known IDs, call [`nova.tab_cleanup_orphans`](nova-tabs.md) instead of closing tabs one by one.

---

## See Also

* [`nova.tab_new`](nova-tab-new.md) — Open a new tab.
* [`nova.tabs`](nova-tabs.md) — List open tabs.
* [`nova.tab_release`](nova-tab-release.md) — Release a claim lease without closing the tab.
