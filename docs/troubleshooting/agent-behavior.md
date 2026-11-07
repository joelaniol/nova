# A Connected Agent Is Not Working as Expected

Start with the symptom. A working connection does not by itself show that the agent discovered the tools, received the result data or completed the requested action.

## The agent does not use Nova's tools

Ask explicitly: **“Use Nova for this browser task.”** If it still says it has no browser tools, check that your AI program actually lists Nova as connected after a restart.

If Nova is connected, ask the agent to obtain Nova's instructions and discover capabilities for the task. Tool names and available schemas can differ by client; use the entry Nova's wizard generated rather than renaming tools by hand. For later project sessions, see [Optional project onboarding](../getting-started/advanced-onboarding.md). For an Antigravity-specific problem, see [Antigravity compatibility](antigravity.md).

If the client lists no Nova connection, return to [Connection issues](agent-connection-issues.md).

## The agent sees only summaries

If the agent reports that it received only a summary rather than the actual tabs or values:

1. Check Nova is connected in your AI program (`/mcp` where supported).
2. Restart sessions that were open when you connected or updated Nova.
3. Paste this into your agent's conversation:

> Nova is connected, but you appear to receive only summary text. Check whether your client receives the structured tool results. Explain the problem and any proposed connection change before editing configuration. Preserve other MCP servers and settings.

Antigravity's Nova entry already includes result compatibility. Repair that entry through **Menu → Settings → AI & agents → Connection & setup → Set up** rather than adding options at random.

For developers maintaining a different client, Nova's bridge supports mirroring structured results into text. See [Custom integrations](../integration/custom-agents.md) and [Protocol and transport](../mcp-reference/protocol-and-transport.md).

## The agent claims success, but the page did not change

Ask it to check the visible outcome and show the relevant verification evidence. An accepted click or request is not necessarily a completed task. The [Experience loop demo](../../demos/README.md) makes this distinction concrete.

## The agent cannot act on a tab

A held tab claim or the emergency stop may be blocking work. Check Nova's visible agent indicators and stop state. Use [Staying in control](../user-guide/agents/taking-over-and-emergency-stop.md) or [Session recovery](sandbox-and-session-recovery.md); do not impersonate another agent to bypass a claim.

## A page is stuck or asks for human verification

Repeated timeouts or `cdp.renderer_stalled` do not identify the cause on their own. Inspect the visible page. If it shows a CAPTCHA or other verification challenge, handle that step yourself and then ask the agent to continue. Avoid repeatedly dispatching the same action without checking whether it already happened.

For an unresponsive page without a clear challenge, use [Diagnostics](diagnostics.md). A timeout is not evidence that a site's anti-bot system deliberately froze its renderer.

## Cookie Banners, Consent & Blocker Clearance

Modern websites frequently present modals, cookie banners, or overlays that block agent interactions.

### 1. `accept_all_blocked` (-32035 Error)
* **Symptom:** The agent calls `nova.cmp_apply` with `intent: { mode: "AcceptAll" }` and receives error `-32035` (`accept_all_blocked`).
* **Root Cause:** By design, autonomous agents are **unconditionally prohibited** from granting commercial tracking consent on behalf of the user.
* **Resolution:** The agent must request `intent: { mode: "RejectOptional" }` (or `PreserveExisting`). If commercial tracking is genuinely desired by the human user, the user must click *"Accept All"* directly in the visible browser window.

### 2. `no_adapter` from `nova.cmp_apply`
* **Symptom:** `nova.cmp_apply` returns `{ ok: false, failureCode: "no_adapter", nextAction: "fallback_dismiss_blockers" }`.
* **Root Cause:** The website uses a custom cookie wall or an unadapted CMP lacking a direct JavaScript runtime API (such as Didomi, Klaro, or in-house dialogs).
* **Resolution:** The agent should not halt. It must immediately escalate to heuristic dismissal:
  ```json
  {
    "mode": "conservative"
  }
  ```
  Nova's heuristic scanner uses its built-in vendor selector lists and evaluates candidate buttons with the Stage 1 Consent Guard.

### 3. `DENY_LABEL_MISMATCH` or `DENY_CONSENT_CLOSE`
* **Symptom:** An automated click via `nova.dismiss_blockers` is refused with `DENY_LABEL_MISMATCH` or `DENY_CONSENT_CLOSE`.
* **Root Cause:**
  * `DENY_LABEL_MISMATCH`: The button's visible text (e.g. *"Reject"*) conflicts with its ARIA accessible name (e.g. *"Accept all cookies"*), exposing an active dark-pattern hijack.
  * `DENY_CONSENT_CLOSE`: The agent tried to click an *✕*, *"Close"*, or *"Later"* button inside a consent area. On many European websites, closing without choosing counts legally as continued tracking.
* **Resolution:** These blocks are intentional safety features. If conservative clicking cannot find an unproven reject button, escalate to `mode: "aggressive"` to inject `display: none` overrides and restore body scroll without consenting.

### 4. Cross-Origin Iframe Cookie Banners
* **Symptom:** Cookie modals embedded in third-party iframes (e.g. Sourcepoint TCF v2 frames like `notice.sp-prod.net`) are not dismissed, and `nova.cmp_apply` reports forbidden.
* **Root Cause:** Running banner scripts inside frames from another site is off by default, so a page cannot use it to get scripts run in foreign frames.
* **Resolution:** Ask the user to turn on the Settings checkbox *Also reach into cookie-banner iframes (advanced)* for sites where the banner does not respond otherwise; agents cannot change it. Otherwise fall back to `nova.dismiss_blockers`. Learn more in [Cross-Origin CMP Boundaries](../core-features/consent-management/hijack-protection/cross-origin-and-privilege-boundaries/README.md).

---

## Deep Web-Exploration, Crawling & Scope Reset

### 1. `challengeHold` During Background Crawl
* **Symptom:** `nova.crawl_status` reports `status: "paused"` with an active `challengeHold` object.
* **Root Cause:** A worker encountered a bot challenge wall (Cloudflare Turnstile, 1020 challenge, or reCAPTCHA). Nova automatically pauses all workers to prevent IP banning.
* **Resolution:**
  1. Inspect the visible browser or navigate to the URL reported in `challengeHold.url`.
  2. Complete the human verification challenge in the browser.
  3. Resume the crawl by calling `nova.crawl_update` with `crawlId` and `paused: false`.

### 2. `crawl.persistence_unavailable` on Start
* **Symptom:** `nova.crawl_start` fails immediately with `reasonCode: "crawl.persistence_unavailable"`.
* **Root Cause:** Nova could not bootstrap or lock the local SQLite database (`crawl.db`) in application data (e.g. disk full, file permissions, or external file lock).
* **Resolution:** Check local disk space, inspect file locks on `%LOCALAPPDATA%\NovaBrowser\crawl.db`, and restart Nova if another process locked SQLite.

### 3. `discovery_reset.active_jobs` on Scope Eviction
* **Symptom:** `nova.discovery_reset_scope` returns `status: "blocked"` with `reasonCode: "discovery_reset.active_jobs"`.
* **Root Cause:** A background crawl job or an interactive surface exploration run is currently active, pausing, or draining within that domain scope.
* **Resolution:** Stop active crawls via `nova.crawl_stop` and close open surface exploration sessions via `nova.explore_surface(mode="close", targetId="active", executionSurface="live_tab", guardProfile="phase1_default", close={"runId": "..."})` before requesting scope deletion.

### 4. `CLAIM_LOST` or `TAB_BECAME_HIDDEN` in Surface Explorer
* **Symptom:** `nova.explore_surface(mode="activate", ...)` reports reason code `CLAIM_LOST` or `TAB_BECAME_HIDDEN`.
* **Root Cause:**
  * `CLAIM_LOST`: The agent's lease on the tab expired, was released, or was claimed by another agent.
  * `TAB_BECAME_HIDDEN`: The human user switched away to another browser tab or sandbox profile during in-flight trigger activation.
* **Resolution:** Re-acquire the tab lease using `nova.tab_claim` before resuming exploration. Nova strictly refuses to click on background or hidden user tabs to protect user workspaces from invisible clicks.

### 5. `networkMutationGuard` Tripped in Surface Explorer
* **Symptom:** Trigger activation ends with `status: "blocked"`, reason code `NON_GET_REQUEST_BLOCKED` and a `networkMutationGuard` entry in `guardIncidents`.
* **Root Cause:** The clicked trigger initiated a mutating HTTP request (`POST`, `PUT`, `DELETE`, `PATCH`).
* **Resolution:** Surface Explorer is designed strictly for read-only interface disclosure (tabs, accordions, menus). Mutating actions are safely blocked to prevent unintended database changes or form submissions.

---

## Deutsch: Der Agent ist verbunden, arbeitet aber nicht richtig

Prüfe zuerst, ob dein KI-Programm Nova nach einem Neustart tatsächlich als verbunden zeigt. Bitte den Agenten ausdrücklich, Nova für die Browser-Aufgabe zu verwenden. Fehlende Werkzeuge können auch ein Discovery- oder Client-Problem sein; nur sichtbarer Erfolg beweist den Aufgabenabschluss.

Sieht der Agent nur kurze Zusammenfassungen statt Daten, starte bestehende Sessions neu und bitte den Agenten, die Ergebnisverarbeitung seines Clients zu prüfen. Lass dir vorgeschlagene Konfigurationsänderungen vorher erklären. Für Antigravity reparierst du den Eintrag über Novas Verbindungsassistenten.

### Cookie-Banner & Blocker-Probleme
* **Fehler `-32035` (`accept_all_blocked`):** Autonome Agenten dürfen niemals eigenmächtig kommerzielles Werbe-Tracking akzeptieren. Der Agent muss `RejectOptional` nutzen; will der Nutzer zustimmen, klickt er selbst im Fenster.
* **`no_adapter`:** Bei unbekannten CMPs (z. B. Didomi, Klaro) eskaliert der Agent sofort auf `nova.dismiss_blockers(mode="conservative")`.
* **`DENY_LABEL_MISMATCH` / `DENY_CONSENT_CLOSE`:** Nova verhindert Dark-Pattern-Hijacks (wenn der sichtbare Text vom Screenreader-Namen abweicht) sowie das Schließen von Cookie-Bannern via *✕* oder Escape, da Schließen oft als stillschweigende Einwilligung gewertet wird.

### Crawler- & Surface-Explorer-Probleme
* **`challengeHold`:** Ein Bot-Schutz (Cloudflare/CAPTCHA) hat den Crawler pausiert. Der Nutzer löst die Prüfung im Browser, danach setzt der Agent den Lauf mit `nova.crawl_update(paused=false)` fort.
* **`discovery_reset.active_jobs`:** Vor dem Löschen eines Site-Index (`nova.discovery_reset_scope`) müssen alle aktiven Crawls und Explorer-Sessions dieser Domain beendet werden.
* **`TAB_BECAME_HIDDEN` / `CLAIM_LOST`:** Klicks im Surface Explorer werden sofort abgebrochen, wenn der Tab gewechselt wird oder der Tab-Claim abläuft, um versehentliche Klicks im Hintergrund zu verhindern.

Weitere Hilfe: [Antigravity](antigravity.md#google-antigravity-deutsch) und [Troubleshooting-Hub](README.md).
