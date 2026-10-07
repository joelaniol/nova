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

A held tab claim or the emergency stop may be blocking work. Check Nova's visible agent indicators and stop state. Use [Staying in control](../user-guide/live-assist-and-spectator.md) or [Session recovery](sandbox-and-session-recovery.md); do not impersonate another agent to bypass a claim.

## A page is stuck or asks for human verification

Repeated timeouts or `cdp.renderer_stalled` do not identify the cause on their own. Inspect the visible page. If it shows a CAPTCHA or other verification challenge, handle that step yourself and then ask the agent to continue. Avoid repeatedly dispatching the same action without checking whether it already happened.

For an unresponsive page without a clear challenge, use [Diagnostics](diagnostics.md). A timeout is not evidence that a site's anti-bot system deliberately froze its renderer.

## Deutsch: Der Agent ist verbunden, arbeitet aber nicht richtig

Prüfe zuerst, ob dein KI-Programm Nova nach einem Neustart tatsächlich als verbunden zeigt. Bitte den Agenten ausdrücklich, Nova für die Browser-Aufgabe zu verwenden. Fehlende Werkzeuge können auch ein Discovery- oder Client-Problem sein; nur sichtbarer Erfolg beweist den Aufgabenabschluss.

Sieht der Agent nur kurze Zusammenfassungen statt Daten, starte bestehende Sessions neu und bitte den Agenten, die Ergebnisverarbeitung seines Clients zu prüfen. Lass dir vorgeschlagene Konfigurationsänderungen vorher erklären. Für Antigravity reparierst du den Eintrag über Novas Verbindungsassistenten. Weitere Hilfe: [Antigravity](antigravity.md#google-antigravity-deutsch) und [Troubleshooting-Hub](README.md).
