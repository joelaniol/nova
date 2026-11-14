# Fastlanes: Events, Conditions & Actions

> [!NOTE]
> **Upcoming.** Fastlanes arrive with a coming release, which is not published yet.

A fastlane is an automation an agent describes once and Nova then runs on its own: Nova waits for an event (no polling), checks a fixed condition and runs the actions without AI - for example a notification the moment a monitored server has been down for 30 seconds, a run every weekday at 07:30, or a message when a new file lands in a folder. What only notifies or wakes the agent starts at once and the user is told; what starts a run on the user's account or calls the internet asks the user first. The user can pause or delete every fastlane in Nova's agents panel.

* **Event sources:** network monitors ([Proxy Routing & Network Interception](../proxy-and-network/README.md), `nova.net_monitor_*` long-term monitors); the clock (a schedule such as `weekdays 07:30` or `every 15m` in a time zone); a folder (new, changed, deleted or renamed files - Nova reads names, sizes and change times only, never the files)
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
| **[`nova.fastlane_create`](nova-fastlane-create.md)** | Sets up a fastlane; one that starts a run or calls the internet asks the user first. |
| **[`nova.fastlane_delete`](nova-fastlane-delete.md)** | Deletes a fastlane; it stops reacting at once. |
| **[`nova.fastlane_get`](nova-fastlane-get.md)** | Shows one fastlane: whether it runs, its revisions in plain words and what it did lately. |
| **[`nova.fastlane_list`](nova-fastlane-list.md)** | Lists the fastlanes of this Nova profile with their state. |
| **[`nova.fastlane_preview`](nova-fastlane-preview.md)** | Checks a fastlane contract without storing it and shows what the user will be asked to approve. |
| **[`nova.fastlane_set_state`](nova-fastlane-set-state.md)** | Pauses or resumes an approved fastlane. |
| **[`nova.fastlane_subscribe`](nova-fastlane-subscribe.md)** | Tells the agent session a fastlane wakes whether events wait for it. |
| **[`nova.fastlane_update`](nova-fastlane-update.md)** | Changes a fastlane by a new revision; one that needs the user's answer waits while the running one goes on. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
