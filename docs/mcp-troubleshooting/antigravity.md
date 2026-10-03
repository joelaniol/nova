# Google Antigravity

Status: 2026-10-01 · Deutsche Fassung weiter unten.

Google Antigravity (and the Gemini CLI it builds on) handles two parts of MCP differently from Claude
Code or Codex. Nova adapts to them in a dedicated Antigravity mode of its MCP proxy.

## Setup

Open **Settings → AI & agents → Connection & setup** and use **Copy entry for Google Antigravity**.
With **Auto-sync Nova entry to Antigravity** switched on (the default), Nova keeps the entry in
`~/.gemini/config/mcp_config.json` up to date by itself. The entry starts the proxy with
`--antigravity-tool-names`. Restart the
Antigravity session after any change — it reads its MCP configuration only at startup.

## Tool names with underscores

Antigravity does not accept dots in tool names, so `nova.tabs` appears as `nova_tabs`. Nova's own
instructions, descriptions and answers keep writing `nova.tabs`; call the tool with the underscore.
The proxy tells the agent this when it connects.

## The agent sees no data

**Symptom.** Tool calls succeed, but the agent only sees short summaries such as
`Tab inventory resolved. Use structuredContent.tabs for the requested projection.` — none of the
actual tabs, notes or values. Agents in this state often try to work around it: they call Nova's HTTP
port with `curl`, or read Nova's files from disk.

**Cause.** Nova returns every answer in two parts: a short text (`content`) and the machine-readable
result (`structuredContent`). Antigravity passes only the text to the model and drops the rest
([antigravity-cli #953](https://github.com/google-antigravity/antigravity-cli/issues/953)).

**Fix.** Coming with the next Nova update: in Antigravity mode the proxy will also write the structured
result into the text the model sees. Your existing entry needs no change — update Nova and restart the
Antigravity session. This page will be updated when the update is out.

Please do not let the agent bypass the MCP connection with `curl` or by reading Nova's files. Those
paths skip Nova's safety checks and break with every update.

---

# Google Antigravity (Deutsch)

Stand: 2026-10-01

Google Antigravity (und die Gemini CLI, auf der es aufbaut) behandelt zwei Teile von MCP anders als
Claude Code oder Codex. Nova passt sich in einem eigenen Antigravity-Modus seines MCP-Proxys daran an.

## Einrichtung

**Einstellungen → KI & Agenten → Verbindung & Einrichtung** öffnen und **Eintrag für Google
Antigravity kopieren** verwenden. Ist **Nova-Eintrag automatisch mit Antigravity abgleichen** eingeschaltet
(Standard), hält Nova den Eintrag in `~/.gemini/config/mcp_config.json` selbst aktuell. Er startet den
Proxy mit `--antigravity-tool-names`. Nach jeder Änderung die Antigravity-Sitzung neu starten — die MCP-Konfiguration wird
nur beim Start gelesen.

## Werkzeugnamen mit Unterstrich

Antigravity erlaubt keine Punkte in Werkzeugnamen, aus `nova.tabs` wird `nova_tabs`. Novas eigene
Anweisungen, Beschreibungen und Antworten schreiben weiter `nova.tabs`; aufgerufen wird mit
Unterstrich. Das sagt der Proxy dem Agenten beim Verbinden.

## Der Agent sieht keine Daten

**Anzeichen.** Werkzeugaufrufe gelingen, der Agent sieht aber nur kurze Zusammenfassungen wie
`Tab inventory resolved. Use structuredContent.tabs …` und nichts von den eigentlichen Tabs, Notizen
oder Werten. Agenten versuchen dann oft auszuweichen: per `curl` auf Novas HTTP-Port oder über Novas
Dateien auf der Festplatte.

**Ursache.** Nova liefert jede Antwort in zwei Teilen: einen kurzen Text (`content`) und das
maschinenlesbare Ergebnis (`structuredContent`). Antigravity gibt nur den Text an das Modell weiter
([antigravity-cli #953](https://github.com/google-antigravity/antigravity-cli/issues/953)).

**Abhilfe.** Kommt mit dem nächsten Nova-Update: Im Antigravity-Modus schreibt der Proxy das Ergebnis
dann zusätzlich in den Text, den das Modell sieht. Der vorhandene Eintrag muss nicht geändert werden —
Nova aktualisieren und die Antigravity-Sitzung neu starten. Diese Seite wird mit dem Update aktualisiert.

Bitte den Agenten nicht per `curl` oder über Novas Dateien an der MCP-Verbindung vorbeiarbeiten lassen:
Diese Wege umgehen Novas Schutzprüfungen und brechen mit jedem Update.
