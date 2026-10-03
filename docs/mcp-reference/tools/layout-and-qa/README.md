# Layout Quality, Geometry & Web Vitals

Bounding box measurements, container width constraints, text clipping, WCAG accessibility audits, and Core Web Vitals.

* **Capability Bundle(s):** `page_read_debug`
* **Core Architecture Guide:** [Core Features: evm-and-visual-evidence.md](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (7 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.audit_accessibility`](nova-audit-accessibility.md)** | Documented | Audit a page (or a subtree) for accessibility/design issues and return a structured issue list — a lightweight in-house alterna... |
| **[`nova.composer_state`](nova-composer-state.md)** | Documented | Read what is currently sitting in a chat composer: its text, its attachments, and whether the send control is ready. |
| **[`nova.detect_overflow`](nova-detect-overflow.md)** | Documented | Scan a page (or a subtree) for layout-overflow issues — clipped text (text-overflow:ellipsis or hidden overflow cutting content... |
| **[`nova.force_pseudo_state`](nova-force-pseudo-state.md)** | Documented | Hold a CSS state on one element so it can be screenshotted or inspected: :hover, :active, :focus, :focus-visible, :focus-within... |
| **[`nova.get_computed_style`](nova-get-computed-style.md)** | Documented | Read the resolved getComputedStyle of one element plus its bounding box — the dedicated design-inspection tool (color, backgrou... |
| **[`nova.measure_elements`](nova-measure-elements.md)** | Documented | Measure many selectors in ONE call: bounding rect, client/scroll size, overflow flags, optional computed-style properties, and ... |
| **[`nova.measure_web_vitals`](nova-measure-web-vitals.md)** | Documented | Measure Core Web Vitals for the active page and return values with good/needs-improvement/poor ratings. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
