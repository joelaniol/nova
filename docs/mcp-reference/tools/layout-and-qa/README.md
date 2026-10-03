# Layout Quality, Geometry & Web Vitals

Bounding box measurements, container width constraints, text clipping, WCAG accessibility audits, and Core Web Vitals.

* **Capability Bundle(s):** `page_read_debug`
* **Core Architecture Guide:** [Core Features: evm-and-visual-evidence.md](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (7 Tools)

| Tool | What it does |
| :--- | :--- |
| **[`nova.audit_accessibility`](nova-audit-accessibility.md)** | Runs an automated Accessibility (a11y) and UX compliance audit over the DOM, checking for WCAG color contrast failures, undersized tap targets, and missing accessible labels. |
| **[`nova.composer_state`](nova-composer-state.md)** | Inspects visual state, selection range, and placeholder text of rich text composers. |
| **[`nova.detect_overflow`](nova-detect-overflow.md)** | Scans the page or a scoped subtree for layout defects, clipped text, overflowing containers, and elements bleeding past the viewport edge. |
| **[`nova.force_pseudo_state`](nova-force-pseudo-state.md)** | Forces CSS pseudo-class states (:hover, :focus, :active, :visited) on an element. |
| **[`nova.get_computed_style`](nova-get-computed-style.md)** | Reads the fully resolved CSS computed style and box-model geometry of a specific DOM element, providing authoritative styling data without executing arbitrary JavaScript. |
| **[`nova.measure_elements`](nova-measure-elements.md)** | Measures geometric dimensions, client/scroll metrics, overflow flags, and constraining ancestor boundaries across multiple CSS selectors in a single round-trip. |
| **[`nova.measure_web_vitals`](nova-measure-web-vitals.md)** | Measures live Google Core Web Vitals (LCP, CLS, INP, FCP, TTFB) for the active page, providing categorized ratings (`good`, `needs-improvement`, or `poor`) for automated performance gating. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
