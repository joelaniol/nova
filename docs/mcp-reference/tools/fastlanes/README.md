# Fastlanes: Events, Conditions & Actions

> [!NOTE]
> **Upcoming.** Fastlanes arrive with a coming release, which is not published yet.

A fastlane is an automation an agent describes once and Nova then runs on its own: Nova waits for an event (no polling), checks a fixed condition and runs the actions without AI - for example a notification the moment a monitored server has been down for 30 seconds. The agent proposes; the user approves every fastlane, and every change to it, in Nova's agents panel.

* **Event source:** [Proxy Routing & Network Interception](../proxy-and-network/README.md) (`nova.net_monitor_*` long-term monitors)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (11 Tools)

Capability bundles of these tools: `fastlanes`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.fastlane_ack`](nova-fastlane-ack.md)** | Closes a claimed delivery with the agent's result. |
| **[`nova.fastlane_catalog`](nova-fastlane-catalog.md)** | Lists what a fastlane can react to and do: event sources with their conditions, the instances that exist, actions, defaults and limits. |
| **[`nova.fastlane_claim`](nova-fastlane-claim.md)** | Takes the events of a delivery, with an epoch for the acknowledgement. |
| **[`nova.fastlane_create`](nova-fastlane-create.md)** | Proposes a fastlane; it runs only after the user approves it. |
| **[`nova.fastlane_delete`](nova-fastlane-delete.md)** | Deletes a fastlane; it stops reacting at once. |
| **[`nova.fastlane_get`](nova-fastlane-get.md)** | Shows one fastlane: whether it runs, its revisions in plain words and what it did lately. |
| **[`nova.fastlane_list`](nova-fastlane-list.md)** | Lists the fastlanes of this Nova profile with their state. |
| **[`nova.fastlane_preview`](nova-fastlane-preview.md)** | Checks a fastlane contract without storing it and shows what the user will be asked to approve. |
| **[`nova.fastlane_set_state`](nova-fastlane-set-state.md)** | Pauses or resumes an approved fastlane. |
| **[`nova.fastlane_subscribe`](nova-fastlane-subscribe.md)** | Tells the agent session a fastlane wakes whether events wait for it. |
| **[`nova.fastlane_update`](nova-fastlane-update.md)** | Proposes a new revision of a fastlane; the approved one keeps running until the user approves the change. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
