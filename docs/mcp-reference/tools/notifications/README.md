# Desktop Notifications & Alerts

Native OS notification dispatch, unread inbox management, and per-origin notification permissions.

* **Core Architecture Guide:** [Core Features: closed-loop-system.md](../../../core-features/closed-loop-system-cls/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (11 Tools)

Capability bundles of these tools: `notifications`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.notifications_clear`](nova-notifications-clear.md)** | Bulk-dismisses notifications matching source or age criteria. |
| **[`nova.notifications_dismiss`](nova-notifications-dismiss.md)** | Dismisses a notification, hiding it from the default inbox view. |
| **[`nova.notifications_get`](nova-notifications-get.md)** | Retrieves complete metadata and payload for a single notification by ID. |
| **[`nova.notifications_list`](nova-notifications-list.md)** | Queries the Nova notification inbox with filtering by source, website origin, and read status. |
| **[`nova.notifications_mark_read`](nova-notifications-mark-read.md)** | Marks a notification as read without dismissing it from the inbox. |
| **[`nova.notifications_open`](nova-notifications-open.md)** | Navigates to the originating tab, website, or resource referenced by a notification. |
| **[`nova.notifications_permission_default_set`](nova-notifications-permission-default-set.md)** | Sets the global website notification permission default (Ask, Allow, or Deny). |
| **[`nova.notifications_permission_set`](nova-notifications-permission-set.md)** | Configures notification permission (Ask, Allow, or Deny) for a specific website origin. |
| **[`nova.notifications_permissions_list`](nova-notifications-permissions-list.md)** | Lists website origin notification permissions and reports the effective global default. |
| **[`nova.notifications_send`](nova-notifications-send.md)** | Dispatches a host-authored Windows toast notification and persists it to the Nova notification inbox. |
| **[`nova.notifications_unread_count`](nova-notifications-unread-count.md)** | Returns the count of unread, non-dismissed notifications currently in the inbox. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
