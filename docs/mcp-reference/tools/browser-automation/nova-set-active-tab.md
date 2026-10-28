# `nova.set_active_tab`

Switches the active visual presentation and input focus in the Nova application shell to the specified sandbox surface or browser tab.

---

## 1. Overview

`nova.set_active_tab` brings a background tab or sandbox into active focus in the primary UI window. While agents can perform headless CDP operations on background tabs by passing `targetId`, visual screenshots, human inspection, and certain focus-dependent UI elements require foreground activation.

* **Target Resolution:** Accepts concrete browser tab IDs (e.g. `"tab-102"`) or sandbox identifiers (`"A"`, `"B"`).
* **Focus Presentation:** Updates WinUI tab strip selection and brings the associated WebView2 composition to the foreground.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Target ID to switch to (sandbox ID or browser tab ID). |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Call

```json
{
  "targetId": "tab-104"
}
```

---

## 4. Return Value Structure

```json
{
  "targetId": "tab-104",
  "ok": true,
  "webViewReady": true,
  "activated": true
}
```

If the target activates but its WebView does not finish initializing in time, the call returns `ok: false` with `status: "webview_not_ready"` and `reasonCode: "tab.webview_not_ready_after_activation"` — activation itself still happened, but tools that need a document (eval, navigate, read) will keep failing until the WebView comes up. A target that never becomes active within the internal timeout returns `ok: false` with `reasonCode: "tab.activate_timeout"`.

---

## 5. Operational Best Practices

* **Prefer Background Execution When Feasible:** Most Nova DOM and automation tools accept an explicit `targetId` parameter, enabling agents to inspect, evaluate scripts, and interact with background tabs without disturbing the operator's active window focus. Reserve `nova.set_active_tab` for workflows requiring visible presentation or focus-sensitive modal handling.
* **Verify Target Existence:** Always inspect open tab IDs via [`nova.tabs`](nova-tabs.md) before switching. Activating a non-existent or previously closed tab returns an error.
* **Check WebView Readiness:** Review the `webViewReady` property in the response. If `webViewReady: false` (status `webview_not_ready`), the UI switch succeeded, but the underlying rendering engine is still hydrating. Allow a brief settlement pause before issuing document-dependent tool calls.

---

## 6. Related Tools & Documentation

* [`nova.tabs`](nova-tabs.md) — Query open tabs and inspect their active state.
* [`nova.tab_new`](nova-tab-new.md) — Create and open a new tab.
* [`nova.tab_claim`](nova-tab-claim.md) — Lease exclusive write access to a tab.
