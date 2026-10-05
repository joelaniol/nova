# Google Antigravity Compatibility

Updated: 2026-10-05 · [Deutsch](#google-antigravity-deutsch)

Use Nova's [Antigravity / Gemini integration guide](../integration/google-antigravity.md) for setup. This page covers the compatibility behavior of Nova's bridge when that mode is enabled.

## Setup

Use Nova's connection wizard and restart the client afterwards. The generated entry selects `--antigravity-tool-names`. If you manage your entry manually, preserve the bridge path and use the [client guide](../integration/google-antigravity.md).

## Tool names with underscores

In Antigravity mode, Nova exposes client-compatible tool names using underscores and converts calls back to its canonical names. Use the names actually provided by discovery. Do not apply this mode to other clients just because a tool call failed.

## The agent sees no data

Antigravity mode also mirrors structured results into text. If the agent sees only summaries, check that the configured entry starts Nova's current bridge with `--antigravity-tool-names`, then restart the client. You do not need to add `--mirror-structured-content` separately in this mode.

For other causes, use [Agent behavior](agent-behavior.md) or [Connection issues](agent-connection-issues.md).

# Google Antigravity (Deutsch)

Stand: 2026-10-05

## Einrichtung

Nutze Novas Verbindungsassistenten und starte das KI-Programm danach neu. Der erzeugte Eintrag verwendet `--antigravity-tool-names`. Manuelle Einrichtung: [Client-Anleitung](../integration/google-antigravity.md).

## Werkzeugnamen mit Unterstrich

Im Antigravity-Modus bietet Nova kompatible Werkzeugnamen mit Unterstrichen an und übersetzt Aufrufe zurück. Nutze die Namen aus der tatsächlichen Tool-Discovery. Andere Clients brauchen diesen Modus nicht automatisch.

## Der Agent sieht keine Daten

Der Modus gibt strukturierte Ergebnisse zusätzlich als Text aus. Prüfe bei fehlenden Daten den verwendeten Bridge-Eintrag und starte den Client neu. `--mirror-structured-content` musst du in diesem Modus nicht zusätzlich angeben. Weitere Hilfe: [Agent behavior](agent-behavior.md) und [Troubleshooting](README.md).
