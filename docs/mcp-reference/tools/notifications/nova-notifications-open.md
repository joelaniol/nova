# `nova.notifications_open`

Navigates to the originating tab, website, or resource referenced by a notification.

---

## 1. Overview

`nova.notifications_open` activates the target surface associated with a notification (focusing an open tab or opening the URL in its origin sandbox). If the notification is missing, dismissed, or targetless, returns a structured no-op status.


---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `notificationId` | `string` | Yes | — | — | The notification ID whose target to open. |

Capability bundle: `notifications` (load it with `nova.tools_bundle(bundle='notifications')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.notifications_open",
  "arguments": {
    "notificationId": "notif-7b8c9d0e"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Opened: notif-7b8c9d0e."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "notificationId": "notif-7b8c9d0e"
  }
}
```

---

## 4. Operational Best Practices

* **Structured No-Op Handling:** If a notification has no target URL or tab, returns `ok: false` with `status: "no_target"` and `reasonCode: "notification.no_target"` rather than throwing an exception.
* **Dismissed Safety:** Opening an already dismissed notification returns `status: "already_dismissed"`.

---

## See Also

* [`nova.notifications_get`](nova-notifications-get.md) - Inspect notification target before opening.
* [Desktop Notifications Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
