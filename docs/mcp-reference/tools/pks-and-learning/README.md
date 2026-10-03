# Phenomenological Knowledge Store & Self-Learning

Cross-session procedural UI memory, learned interaction playbooks, fingerprint matching, and health telemetry.

* **Capability Bundle(s):** `pks_learning`
* **Core Architecture Guide:** [Core Features: pks.md](../../../core-features/pks.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (21 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.explain`](nova-explain.md)** | Documented | Explain why a PKS phenomenon is at its current learning level. |
| **[`nova.learn_feedback`](nova-learn-feedback.md)** | Documented | Return recent promotion/demotion/deprecation events as a learning feedback log. |
| **[`nova.learn_generate`](nova-learn-generate.md)** | Documented | Generate candidate phenomena/hints from accumulated observations. |
| **[`nova.learn_onboarding_confirm`](nova-learn-onboarding-confirm.md)** | Documented | Confirm the learn-mode onboarding for a domain. |
| **[`nova.learn_onboarding_recall`](nova-learn-onboarding-recall.md)** | Documented | Read-only: fetch the current learn-mode onboarding payload for a domain (or, when domain is omitted, for the session's active l... |
| **[`nova.learn_promote`](nova-learn-promote.md)** | Documented | Evaluate and execute staged promotions for PKS entries. |
| **[`nova.learn_resolve_opportunity`](nova-learn-resolve-opportunity.md)** | Documented | Resolve a semantic learning opportunity. |
| **[`nova.learn_suggest`](nova-learn-suggest.md)** | Documented | Return top learning opportunities from accumulated observations. |
| **[`nova.phenomenon_apply`](nova-phenomenon-apply.md)** | Documented | Execute a PKS phenomenon playbook server-side. |
| **[`nova.pks_deprecate`](nova-pks-deprecate.md)** | Documented | Mark a phenomenon as deprecated (soft-delete). |
| **[`nova.pks_get`](nova-pks-get.md)** | Documented | Get PKS (Phenomenological Knowledge Store) data for a domain scope. |
| **[`nova.pks_list`](nova-pks-list.md)** | Documented | List all known PKS domains with summary stats (active phenomenon counts plus per-domain health metrics). |
| **[`nova.pks_match`](nova-pks-match.md)** | Documented | Match an observation against known phenomena for a domain. |
| **[`nova.pks_patch`](nova-pks-patch.md)** | Documented | Partially update a phenomenon (merge fields without replacing the whole entry). |
| **[`nova.pks_platform_get`](nova-pks-platform-get.md)** | Documented | Get a platform's details including platform metadata, active-vs-total pattern counts, status/freshness hints, and all stored pa... |
| **[`nova.pks_platform_list`](nova-pks-platform-list.md)** | Documented | List all platforms with summary metadata including active-vs-total pattern counts plus status and freshness fields that explain... |
| **[`nova.pks_platform_seed`](nova-pks-platform-seed.md)** | Documented | Seed or update a platform with patterns and aliases. |
| **[`nova.pks_upsert`](nova-pks-upsert.md)** | Documented | Create or update a phenomenon entry in the PKS for a domain. |
| **[`nova.pks_upsert_hint`](nova-pks-upsert-hint.md)** | Documented | Create or update a declarative domain hint for CTA detection scoring. |
| **[`nova.revalidate`](nova-revalidate.md)** | Documented | Silent DOM-only revalidation of PKS phenomena. |
| **[`nova.telemetry_report`](nova-telemetry-report.md)** | Documented | Report success, failure, or not_applicable for an interaction with a phenomenon. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
