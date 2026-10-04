# Google Antigravity

Status: 2026-10-03 · Deutsche Fassung weiter unten.

Google Antigravity (and the Gemini CLI it builds on) handles two parts of MCP differently from Claude
Code or Codex. Nova adapts to them in a dedicated Antigravity mode of its MCP proxy.

## Setup

With **Auto-sync Nova entry to Antigravity** switched on (the default, under **Settings → AI & agents
→ Connection & setup**), Nova writes its entry into `~/.gemini/config/mcp_config.json` by itself when
Antigravity is installed, and keeps it up to date. To add the entry by hand, click **Set up** on the
same page, choose **Set up manually** and use **Copy entry for Google Antigravity**. The entry starts
the proxy with `--antigravity-tool-names`. Restart the Antigravity session after any change — it reads
its MCP configuration only at startup.

Antigravity mode arrives with the first Nova release after 1.0.0-alpha.17.

## Tool names with underscores

Antigravity does not accept dots in tool names, so `nova.tabs` appears as `nova_tabs` (very long names
are shortened and end in a short hash). Nova's own
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

**Fix.** In Antigravity mode the proxy also copies the structured result into an extra text block
that the model sees (`--antigravity-tool-names` includes `--mirror-structured-content`). If the agent
still sees only summaries, check that the `nova` entry in `~/.gemini/config/mcp_config.json` starts the
proxy with `--antigravity-tool-names` and that Nova is newer than 1.0.0-alpha.17, then restart the
Antigravity session.

Please do not let the agent bypass the MCP connection with `curl` or by reading Nova's files. Those
paths skip Nova's safety checks and break with every update.

---

# Google Antigravity (Deutsch)

Stand: 2026-10-03

Google Antigravity (und die Gemini CLI, auf der es aufbaut) behandelt zwei Teile von MCP anders als
Claude Code oder Codex. Nova passt sich in einem eigenen Antigravity-Modus seines MCP-Proxys daran an.

## Einrichtung

Ist **Nova-Eintrag automatisch mit Antigravity abgleichen** eingeschaltet (Standard, unter
**Einstellungen → KI & Agenten → Verbindung & Einrichtung**), schreibt Nova seinen Eintrag selbst in
`~/.gemini/config/mcp_config.json`, sobald Antigravity installiert ist, und hält ihn aktuell. Von Hand:
auf derselben Seite **Einrichten** klicken, **Selbst einrichten** wählen und **Eintrag für Google
Antigravity kopieren** verwenden. Der Eintrag startet den Proxy mit `--antigravity-tool-names`. Nach
jeder Änderung die Antigravity-Sitzung neu starten — die MCP-Konfiguration wird nur beim Start gelesen.

Den Antigravity-Modus gibt es ab dem ersten Nova-Release nach 1.0.0-alpha.17.

## Werkzeugnamen mit Unterstrich

Antigravity erlaubt keine Punkte in Werkzeugnamen, aus `nova.tabs` wird `nova_tabs` (sehr lange Namen
werden gekürzt und enden auf eine kurze Prüfsumme). Novas eigene
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

**Abhilfe.** Im Antigravity-Modus kopiert der Proxy das Ergebnis zusätzlich in einen Textblock, den
das Modell sieht (`--antigravity-tool-names` schließt `--mirror-structured-content` ein). Sieht der
Agent weiter nur Zusammenfassungen: prüfen, dass der Eintrag `nova` in
`~/.gemini/config/mcp_config.json` den Proxy mit `--antigravity-tool-names` startet und Nova neuer als
1.0.0-alpha.17 ist, dann die Antigravity-Sitzung neu starten.

Bitte den Agenten nicht per `curl` oder über Novas Dateien an der MCP-Verbindung vorbeiarbeiten lassen:
Diese Wege umgehen Novas Schutzprüfungen und brechen mit jedem Update.
