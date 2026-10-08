# Surface Explorer

Surface Explorer helps an agent inspect content that is hidden behind interactive controls in the current visible tab: menus, dialogs, tab panels, accordions, popovers and hover content. It classifies candidate triggers before interaction and records what the interaction actually revealed.

## A Concrete Example: Read Content Behind a Panel

A documentation page contains several collapsed sections. The agent discovers their controls, checks which triggers are eligible and requests approval where required. Nova activates an eligible control under guards and returns evidence of the resulting state. The agent reads the revealed content and explicitly closes the exploration run when it is done.

The [crawler](../crawler/README.md) maps routes across a site. Surface Explorer examines states inside a page, including states that have no separate URL.

## Four Modes

| Mode | What it does | Important boundary |
| :--- | :--- | :--- |
| `discover` | Scans and classifies interactive triggers without activating them. | Discovery does not authorize every trigger it finds. Discovery policy can require approval or disable exploration. |
| `activate` | Activates an eligible trigger from a prior persisted, open run. | Requires the agent's tab claim, the recorded source state and applicable approval; Nova rechecks the trigger before acting. |
| `hover` | Peeks at hover content and compares before/after visual evidence. | Always requires user approval. Missing evidence produces an inconclusive result. |
| `close` | Ends the exploration run and releases its guards and caches. | Idempotent cleanup; ending a run does not undo website actions or promise to close every panel it opened. |

All modes use `nova.explore_surface` from the `surface_explorer` capability bundle. Its detailed parameters and JSON-RPC examples are in the [tool reference](../../../mcp-reference/tools/task-memory/nova-explore-surface.md).

## What Can Be Explored?

* **Explicit disclosure controls:** Supported controls for menus, dialogs, tabs, accordions and popovers.
* **Semantic or heuristic candidates:** Controls inferred from supported page and accessibility evidence. Their activation requires the relevant setting and explicit approval.
* **Read navigation:** Eligible pagination and load-more controls, with approval.
* **Supported route navigation:** Eligible same-origin or SPA route controls, subject to navigation policy, approval and checks for changed page state. Cross-origin and new-tab navigation are not automatically activated through this path.
* **Hover content:** Tooltips or other content revealed by hovering, with visual before/after evidence.

A denied trigger or one requiring more evidence is not a license to bypass the classification with another click. A scan also does not establish that every control on the page has been discovered.

## Guarded Interaction

Availability depends on MCP Remote Control and the Surface Explorer settings. The default activation policy asks before activation. Semantic, heuristic and read-navigation activation require explicit approval even when the general activation policy is less restrictive; hover always requires approval.

Before activation, Nova checks the run, trigger, tab ownership and current page context. A navigation trigger that has changed destination since discovery can be rejected. User interference, claim loss or other guard failures can stop the operation.

The guard session restricts unsupported navigation, network mutations, downloads, new windows, external URI schemes and permission or dialog requests. These controls contain supported exploration; they do not establish that an arbitrary website is harmless or that every page script has no side effects.

## Results, Persistence & Evidence

Discovery returns an inventory with classifications and optional safety evidence. Persisting discovery creates an exploration run; keeping it open lets a later activation refer to its recorded run, source state and trigger. The route can also be associated with the site URL index.

Activation reports the observed outcome rather than treating a dispatched click as proof that the intended panel opened. Depending on the operation, evidence can include state changes, text excerpts, screenshots and diagnostic artifacts. Discovery can also create a frozen baseline bundle containing a screenshot, trigger inventory and manifest.

Hover distinguishes revealed content, a completed comparison with no visual change and an inconclusive comparison when evidence could not be captured. An inconclusive result does not establish that no hover content exists.

## Limits & Coverage

* DOM stability is a readiness heuristic. A best-effort snapshot after a wait does not prove that all asynchronous content has loaded.
* Cross-origin iframes can be listed as opaque blocks; their contents are not discovered by this scan.
* Trigger limits, classification and website structure can leave controls or states unexplored.
* Coverage of a page's states and coverage of the site's URLs are separate questions. Use explicit task units and coverage evidence for exhaustive work.

## Related Documentation

* [Autonomous Crawler & URL Discovery](../crawler/README.md) — Traversal, persistent URLs and site-discovery files.
* [Agent Awareness Gates (AAG)](../../agent-awareness-gates-aag/README.md) — Preconditions and coordination before agent actions.
* [Task Memory (ETM)](../../learning/episodic-task-memory-etm/README.md) — Work units and task evidence.
* [Task URL Coverage (TUC)](../../learning/task-url-coverage-tuc/README.md) — Coverage observations and verification.
* [Surface Explorer Tool Reference](../../../mcp-reference/tools/task-memory/nova-explore-surface.md) — Current parameter contract and examples.

[Crawler & Discovery overview](../README.md) · [All core features](../../README.md)
