# Evidence Verification Mode (EVM) & Visual Evidence

> [!NOTE]
> Evidence Verification Mode (EVM) is a set of research rules Nova hands to agents for factual tasks: split the task into claims, back each claim with sources, and say "unknown" instead of guessing. For visual checks, Nova's screenshot tools capture just the element or region in question, so small text stays readable and responses stay small.

---

## 1. Problem Statement

When agents research facts or check a UI, two failure modes are common:
1. **Unsupported claims:** The agent states facts (prices, security advisories, deadlines) from memory or from a single source.
2. **Oversized screenshots:** A full-viewport screenshot costs many image tokens, and once it is downscaled, small text can become unreadable.

---

## 2. The EVM Rules

`nova.get_instructions` in task mode returns the EVM rules as text and as `structuredContent.evm`. They are guidance for the agent; Nova does not check the agent's final answer against them. The rules apply to factual and research tasks, not to plain UI automation.

```mermaid
flowchart TD
    Claim["Task split into testable claims"] --> CheckDomain{"Critical domain?"}
    CheckDomain -- Yes --> Need2["At least 2 independent sources"]
    CheckDomain -- No --> Need1["At least 1 reliable source"]
    Need2 --> Verify["Check sources"]
    Need1 --> Verify
    Verify -- Verified --> Out["Results and Sources"]
    Verify -- Not verified --> Unknown["unknown plus exactly 1 concrete next step"]
```

1. **Claim test:** Break every factual task into testable claims.
2. **Evidence minimum:** Non-critical claims need at least 1 reliable source; critical claims need at least 2 independent sources.
3. **Unknown over guessing:** A claim that cannot be verified is marked `unknown`, with exactly one concrete next step.
4. **Stop early:** Stop researching once all claim tests pass.
5. **Compact output:** Answers use the sections `Results`, `Sources` and, if needed, `Unknowns`.

**Critical domains** (`structuredContent.evm.criticalDomains`): security, medical, legal, financial, political, pricing, deadlines and current-state claims ("latest", "today").

**Keeping results:** Claim results tied to a claimed tab can be stored with `nova.memory_add_candidate` (`component='evm'`, `status` `verified`, `unverified` or `disproven`); reusable research notes go to `nova.operator_notes_store` with the tag `evm`. `nova.memory_stats(componentFilter='evm')` shows the counts.

---

## 3. Visual Evidence: Crops Instead of Full Screenshots

`nova.capture_screenshot` can capture less than the whole viewport:
* **`selector`:** captures only the bounding box of one element (scrolled into view, ` >>> ` supported). Elements that are hidden or fully transparent are refused, because the crop would show something else.
* **`region`:** captures a rectangle in CSS pixels; the browser captures only that area.
* **`screenshotFormat: "auto"`** with a region: PNG for moderate text and UI crops (up to about 1 megapixel), JPEG for very large regions.
* **`highlightSelector`:** draws a marker (color, stroke, style and label configurable) around an element; on its own it captures a close-up of that element.
* **`includeContextImage`:** adds a small marked overview of the viewport for orientation.
* **`responseMode`:** `reference` returns only a `nova://screenshot/...` link that can be fetched later with `nova.read_screenshot_resource`; `thumbnail+reference` returns a small preview plus the link. These links are valid for the session, by default for one hour.
* **Budget:** Nova limits large inline captures per session; `force` overrides the soft limits but not the hard safety limits (50 MB encoded, 50 megapixels).

---

## 4. MCP Tooling for EVM & Evidence

| Tool | Purpose |
| :--- | :--- |
| `nova.get_instructions` | Returns the EVM rules in task mode. |
| `nova.capture_screenshot` | Viewport, full page, element or region capture with optional markers and reference delivery. |
| `nova.read_screenshot_resource` | Fetches a stored screenshot by its `nova://screenshot/...` URI. |
| `nova.screenshot_diff` | Pixel comparison of two PNG screenshots: changed-pixel share, changed regions and a diff overlay; supports masks and anti-aliasing filtering. |
| `nova.screenshot_baseline` | Saves named baselines and compares a new capture against them (`save`, `update`, `compare`, `list`, `delete`). |
| `nova.audit_accessibility` | Checks text contrast, tap-target size and missing labels or accessible names. |
| `nova.measure_web_vitals` | Measures LCP, CLS, INP, FCP and TTFB with ratings. |

---

## Related Documentation

* **[Tool Observation Bus (TOB)](tob.md)** — Server-side evidence ledger and visit windows.
* **[Agent Awareness Gates (AAG)](aag.md)** — Pre-execution safety and multi-agent lease locking.
* **[Input Dispatch & Shadow DOM Traversal](humanized-input-engine.md)** — How Nova delivers mouse and keyboard input.
