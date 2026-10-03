# `nova.notifications_send`

Dispatches a host-authored Windows toast notification and persists it to the Nova notification inbox.

---

## 1. Overview

`nova.notifications_send` presents native Windows desktop toast notifications to the user and stores them in Nova's persistent notification drawer. It includes rate-limiting (10 requests per 30 seconds) and blocks website impersonation (`sourceKind: "website"` is rejected).

* **Capability Bundle:** `notifications`
* **Security Tier:** Tier 3 (High-Impact)
* **Core Architecture Guide:** [Closed-Loop System & Event Propagation](../../../core-features/closed-loop-system.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`sourceKind`** | `string` | Yes | `none` | Notification origin: `"nova"` or `"agent"`. Website impersonation is strictly forbidden. |
| **`title`** | `string` | Yes | `none` | Notification title (max 200 characters). |
| **`body`** | `string` | No | `null` | Notification message body text (max 1000 characters). |
| **`urgent`** | `boolean` | No | `false` | When `true`, sets Windows toast priority to Urgent, breaking through Focus Assist / Do-Not-Disturb modes. |
| **`tag`** | `string` | No | `null` | Replacement tag. A subsequent notification with the same tag replaces the previous toast. |
| **`targetId`** | `string` | No | `null` | Browser tab target ID for click navigation. |
| **`sandboxId`** | `string` | No | `null` | Sandbox ID for click activation. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | Yes | `none` | Execution intent metadata (`_meta.intent`) required for High-Impact auditing. |

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

* **Rate Limiting:** Guarded by a 10 requests / 30 seconds bucket. Exceeding this limit returns error `-32029` with `retryAfterMs`.
* **Urgent Scenarios:** Only set `urgent: true` for genuine emergencies or blocking operator interventions (e.g. required 2FA confirmation), to respect user focus.
* **Toast Replacement:** Use `tag` for progress updates (e.g. `tag: "batch-download-progress"`) to avoid flooding the user's desktop with dozens of individual toast popups.

---

## See Also

* [`nova.notifications_list`](nova-notifications-list.md) - List inbox notifications.
* [`nova.notifications_open`](nova-notifications-open.md) - Navigate to notification target.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
