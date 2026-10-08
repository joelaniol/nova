# Layout Quality, Geometry & Web Vitals

Bounding box measurements, container width constraints, text clipping, WCAG accessibility audits, and Core Web Vitals.

* **Core Architecture Guide:** [Evidence Verification Mode (EVM) & Visual Evidence](../../../core-features/research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (7 Tools)

Capability bundles of these tools: `page_read_debug`, `visual_evidence`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.audit_accessibility`](nova-audit-accessibility.md)** | Runs an automated Accessibility (a11y) and UX compliance audit over the DOM, checking for WCAG color contrast failures, undersized tap targets, and missing accessible labels. |
| **[`nova.composer_state`](nova-composer-state.md)** | Reads what is currently sitting in a chat composer: its text, its attachments, and whether the send control looks ready. |
| **[`nova.detect_overflow`](nova-detect-overflow.md)** | Scans the page or a scoped subtree for layout defects, clipped text, overflowing containers, and elements bleeding past the viewport edge. |
| **[`nova.force_pseudo_state`](nova-force-pseudo-state.md)** | Forces CSS pseudo-class states (:hover, :focus, :active, :visited) on an element. |
| **[`nova.get_computed_style`](nova-get-computed-style.md)** | Reads the fully resolved CSS computed style and box-model geometry of a specific DOM element, providing authoritative styling data without executing arbitrary JavaScript. |
| **[`nova.measure_elements`](nova-measure-elements.md)** | Measures geometric dimensions, client/scroll metrics, overflow flags, and constraining ancestor boundaries across multiple CSS selectors in a single round-trip. |
| **[`nova.measure_web_vitals`](nova-measure-web-vitals.md)** | Measures Core Web Vitals (LCP, a simplified CLS, INP, FCP, plus TTFB and load timings) for the active page, rating LCP/CLS/INP/FCP as `good`, `needs-improvement`, or `poor` for automated performance gating. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
