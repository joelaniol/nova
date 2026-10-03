# `nova.set_active_tab`

Switches the active visual presentation and input focus in the Nova application shell to the specified sandbox surface or browser tab.

---

## 1. Overview

`nova.set_active_tab` brings a background tab or sandbox into active focus in the primary UI window. While agents can perform headless CDP operations on background tabs by passing `targetId`, visual screenshots, human inspection, and certain focus-dependent UI elements require foreground activation.

* **Capability Bundle:** `browser_automation`, `app_shell_recovery`
* **Target Resolution:** Accepts concrete browser tab IDs (e.g. `"tab-102"`) or sandbox identifiers (`"A"`, `"B"`).
* **Focus Presentation:** Updates WinUI tab strip selection and brings the associated WebView2 composition to the foreground.

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | **Yes** | — | Target ID to switch to (sandbox ID or browser tab ID). |
| **`_meta.intent`**| `string` | No | — | Optional audit trail statement. |

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
  "success": true,
  "activeTargetId": "tab-104",
  "url": "https://example.com/checkout",
  "title": "Secure Checkout"
}
```

---

## 5. Related Tools & Documentation

* [`nova.tabs`](nova-tabs.md) — Query open tabs and inspect their active state.
* [`nova.tab_new`](nova-tab-new.md) — Create and open a new tab.
* [`nova.tab_claim`](nova-tab-claim.md) — Lease exclusive write access to a tab.
