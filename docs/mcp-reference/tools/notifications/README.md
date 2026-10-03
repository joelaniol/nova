# Desktop Notifications & Alerts

Native OS notification dispatch, unread inbox management, and per-origin notification permissions.

* **Capability Bundle(s):** `notifications`
* **Core Architecture Guide:** [Core Features: closed-loop-system.md](../../../core-features/closed-loop-system.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (11 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.notifications_clear`](nova-notifications-clear.md)** | Documented | Clear (dismiss) multiple notifications. |
| **[`nova.notifications_dismiss`](nova-notifications-dismiss.md)** | Documented | Dismiss a notification (hides it from the default list view). |
| **[`nova.notifications_get`](nova-notifications-get.md)** | Documented | Get a single notification by ID with full details. |
| **[`nova.notifications_list`](nova-notifications-list.md)** | Documented | List notifications from the Nova notification inbox. |
| **[`nova.notifications_mark_read`](nova-notifications-mark-read.md)** | Documented | Mark a notification as read. |
| **[`nova.notifications_open`](nova-notifications-open.md)** | Documented | Navigate to the target of a notification (e.g. originating tab or URL). |
| **[`nova.notifications_permission_default_set`](nova-notifications-permission-default-set.md)** | Documented | Set the global website notification permission default (Ask/Allow/Deny). |
| **[`nova.notifications_permission_set`](nova-notifications-permission-set.md)** | Documented | Set notification permission (Ask/Allow/Deny) for a website origin. |
| **[`nova.notifications_permissions_list`](nova-notifications-permissions-list.md)** | Documented | List known per-origin notification permission decisions (Ask/Allow/Deny) and global default. |
| **[`nova.notifications_send`](nova-notifications-send.md)** | Documented | Send a host-authored notification (toast + inbox entry). |
| **[`nova.notifications_unread_count`](nova-notifications-unread-count.md)** | Documented | Get the number of unread, non-dismissed notifications. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
