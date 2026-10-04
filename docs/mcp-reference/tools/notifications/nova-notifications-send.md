# `nova.notifications_send`

Dispatches a host-authored Windows toast notification and persists it to the Nova notification inbox.

---

## 1. Overview

`nova.notifications_send` presents native Windows desktop toast notifications to the user and stores them in Nova's persistent notification drawer. It includes rate-limiting (10 requests per 30 seconds) and blocks website impersonation (`sourceKind: "website"` is rejected).


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sourceKind` | `string` | Yes | — | `nova`, `agent` | Source of the notification. Must be 'nova' or 'agent'. |
| `title` | `string` | Yes | — | — | Notification title (max 200 chars). |
| `body` | `string` | No | — | — | Notification body text (max 1000 chars). |
| `tag` | `string` | No | — | — | Optional tag for replacement semantics. A new notification with the same tag replaces the previous one. |
| `targetId` | `string` | No | — | — | Optional target ID for click routing. |
| `sandboxId` | `string` | No | — | — | Optional sandbox ID for click routing. |
| `urgent` | `boolean` | No | — | — | If true, mark the notification important (Windows 'Urgent' scenario) so it breaks through Focus Assist / Do-Not-Disturb and pops a banner even under 'priority only'. Reserve for genuinely important events; default false. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `notifications` (load it with `nova.tools_bundle(bundle='notifications')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_send",
  "arguments": {
    "sourceKind": "agent",
    "title": "Build Verification Complete",
    "body": "All 48 integration smoke tests passed successfully in 14.2s.",
    "urgent": false,
    "_meta": {
      "intent": "Notify operator of completed test suite run"
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Notification sent: notif-7b8c9d0e."
    }
  ],
  "structuredContent": {
    "status": "sent",
    "notificationId": "notif-7b8c9d0e"
  }
}
```

---

## 4. Operational Best Practices

* **Rate Limiting:** Guarded by a 10 requests / 30 seconds bucket. Exceeding this limit returns error `-32029` (Nova's rate-limit code) with `reasonCode` `notification.rate_limited` and `retryAfterMs`.
* **Urgent Scenarios:** Only set `urgent: true` for genuine emergencies or blocking operator interventions (e.g. required 2FA confirmation), to respect user focus.
* **Toast Replacement:** Use `tag` for progress updates (e.g. `tag: "batch-download-progress"`) to avoid flooding the user's desktop with dozens of individual toast popups.
* **`status: "sent"` Means Dispatched, Not Delivered:** The OS toast is shown asynchronously after this call returns, so `status: "sent"` only confirms the notification was queued and persisted to the inbox. Check `deliveryState` via [`nova.notifications_get`](nova-notifications-get.md) (`pending`/`delivered`/`failed`/`suppressed`) to confirm the toast actually reached the desktop.

---

## See Also

* [`nova.notifications_list`](nova-notifications-list.md) - List inbox notifications.
* [`nova.notifications_open`](nova-notifications-open.md) - Navigate to notification target.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
