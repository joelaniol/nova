# `nova.tab_close`

Closes an open browser tab or background WebView, releasing its system resources and associated leases.

---

## 1. Overview

`nova.tab_close` terminates a specified browser tab inside Nova AI Workspace. It cleans up the underlying Microsoft WebView2 controller, releases network handles, unregisters any active tab leases, and restores focus to the nearest remaining tab.

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

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Browser tab ID or 'active' (must resolve to a browser tab). |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
  "requested": "tab-5",
  "targetId": "tab-5",
  "ok": true,
  "status": "ok",
  "reasonCode": null,
  "stage": "done",
  "retryable": false,
  "closed": true,
  "cancelledPendingRequests": 0,
  "finalizePersisted": true,
  "finalizeError": null
}
```

Closing an already-gone tab by an explicit `targetId` is not an error: the response comes back `ok: true, reasonCode: "tab.already_closed"` since the higher-level intent ("this tab is gone") is already satisfied. Closing with no `targetId` and no active tab is a hard error (`-32602`, `reasonCode: "tab.no_active_tab"`).

---

## 5. Best Practices & Common Traps

* **Verify Target ID Before Closing:** Always pass an explicit `targetId` when working with multiple tabs. Omitting `targetId` closes the currently focused tab, which might be a tab the human user is actively reading.
* **Cleaning Orphaned Tabs:** If an automated workflow crashed and left multiple hidden tabs open without known IDs, call [`nova.tab_cleanup_orphans`](nova-tab-cleanup-orphans.md) instead of closing tabs one by one.

---

## See Also

* [`nova.tab_new`](nova-tab-new.md) — Open a new tab.
* [`nova.tabs`](nova-tabs.md) — List open tabs.
* [`nova.tab_release`](nova-tab-release.md) — Release a claim lease without closing the tab.
