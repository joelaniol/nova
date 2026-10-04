# MCP troubleshooting

Status: 2026-10-03 · Deutsche Fassung weiter unten.

Your AI agent is connected to Nova but does not work with it properly? Find the symptom below. Most
problems come from differences between MCP clients, not from Nova or the agent.

## Client guides

| Client | Page |
|---|---|
| Google Antigravity / Gemini CLI | [antigravity.md](antigravity.md) |

## The agent does not use Nova's tools

**Symptom.** Nova is connected, but the agent never calls its tools, says it has no browser tools, or
reports "tool not found" for names like `nova.tabs`.

**Likely cause.** The client does not accept dots in tool names. Nova's tools are called `nova.tabs`,
`nova.navigate` and so on; some clients reject or silently drop those names. Google Antigravity is one
of them — Nova has a dedicated mode for it: [antigravity.md → Tool names with underscores](antigravity.md#tool-names-with-underscores).

## The agent sees no data

**Symptom.** Tool calls succeed, but the agent only sees short summaries such as
`Tab inventory resolved. Use structuredContent.tabs for the requested projection.` — none of the
actual tabs, notes or values. The agent then often tries to work around it with `curl` or by reading
Nova's files from disk.

**Cause.** Nova returns every tool answer in two parts: a short text (`content`) and the
machine-readable result (`structuredContent`). Some clients pass only the text to the model and drop
the structured result. Public reports describe this for Cursor, Kiro, Goose and Continue; these have
not been tested with Nova yet. Claude Code and Codex read `structuredContent` and are not affected.

**Fix: add `--mirror-structured-content` to the Nova entry.** With this switch, Nova's bridge
(`NovaBrowser.McpProxy.exe`) copies the structured result into an extra text block, so the model sees
the data. Very large results are cut at 32,000 characters with a note saying how to ask for less.

1. Open your AI program's MCP configuration and find the `nova` entry. Its `command` points to
   `NovaBrowser.McpProxy.exe`.
2. Add the switch to its `args`:
   ```json
   {
     "mcpServers": {
       "nova": {
         "command": "C:\\Users\\<you>\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe",
         "args": ["--mirror-structured-content"]
       }
     }
   }
   ```
   Keep the `command` path your entry already has; on older installations it points into
   `%LOCALAPPDATA%\NovaBrowser\bin\`. In JSON files every backslash must be doubled.
3. Restart the AI program. Clients read their MCP configuration only at startup.

Nova keeps this switch when it updates its entry in a JSON configuration by itself. For Google
Antigravity you do not need it: the Antigravity entry already includes it, see
[antigravity.md → The agent sees no data](antigravity.md#the-agent-sees-no-data).

The bridge accepts only `--antigravity-tool-names` and `--mirror-structured-content`; with any other
switch (for example a mistyped one) it stops at once with exit code 2. Bridges from Nova
1.0.0-alpha.17 and older do not know the switch and ignore it — if nothing changes, update Nova.

Please do not let the agent bypass the MCP connection with `curl` or by reading Nova's files. Those
paths skip Nova's safety checks and break with every update.

## Nova is not running / connection refused

Keep Nova open while your agent works. On **Settings → AI & agents → Connection & setup**, check that
**Enable local agent control** and **Allow agents to control the browser** are ticked (both are on by
default). With **Allow agents to start Nova when it is closed** ticked (also the default), the bridge
starts Nova by itself when an agent needs it.

On the same page, **Sync now** writes Nova's entry into the AI programs Nova keeps in sync
automatically, **Reinstall runner** puts a fresh copy of the bridge into Nova's profile folder (for
example after Nova was moved or reinstalled), and **Set up** opens the connection wizard. Restart the
agent session afterwards; clients read their MCP configuration only at startup.

More diagnosis steps: [Agent & MCP connection issues](../troubleshooting/agent-connection-issues.md).

---

# MCP-Fehlerbehebung

Stand: 2026-10-03

Dein KI-Agent ist mit Nova verbunden, arbeitet aber nicht richtig damit? Such unten das passende
Anzeichen. Die meisten Probleme entstehen durch Unterschiede zwischen MCP-Clients, nicht durch Nova
oder den Agenten.

## Anleitungen je Client

| Client | Seite |
|---|---|
| Google Antigravity / Gemini CLI | [antigravity.md](antigravity.md) |

## Der Agent nutzt Novas Werkzeuge nicht

**Anzeichen.** Nova ist verbunden, aber der Agent ruft keine Werkzeuge auf, sagt, er habe keine
Browser-Werkzeuge, oder meldet „tool not found“ für Namen wie `nova.tabs`.

**Wahrscheinliche Ursache.** Der Client akzeptiert keine Punkte in Werkzeugnamen. Novas Werkzeuge heißen
`nova.tabs`, `nova.navigate` usw.; manche Clients lehnen solche Namen ab oder lassen sie stillschweigend
weg. Google Antigravity gehört dazu — Nova hat dafür einen eigenen Modus:
[antigravity.md → Werkzeugnamen mit Unterstrich](antigravity.md#werkzeugnamen-mit-unterstrich).

## Der Agent sieht keine Daten

**Anzeichen.** Werkzeugaufrufe gelingen, der Agent sieht aber nur kurze Zusammenfassungen wie
`Tab inventory resolved. Use structuredContent.tabs …` und nichts von den eigentlichen Tabs, Notizen
oder Werten. Er versucht dann oft, per `curl` oder über Novas Dateien auf der Festplatte auszuweichen.

**Ursache.** Nova liefert jede Werkzeugantwort in zwei Teilen: einen kurzen Text (`content`) und das
maschinenlesbare Ergebnis (`structuredContent`). Manche Clients geben nur den Text an das Modell weiter
und verwerfen das Ergebnis. Öffentliche Berichte beschreiben das bei Cursor, Kiro, Goose und Continue;
mit Nova sind diese noch nicht getestet. Claude Code und Codex lesen `structuredContent` und sind nicht
betroffen.

**Abhilfe: `--mirror-structured-content` in den Nova-Eintrag aufnehmen.** Mit diesem Schalter kopiert
Novas Brücke (`NovaBrowser.McpProxy.exe`) das Ergebnis zusätzlich in einen Textblock, den das Modell
sieht. Sehr große Ergebnisse werden bei 32.000 Zeichen abgeschnitten, mit einem Hinweis, wie man
weniger anfordert.

1. In der MCP-Konfiguration deines KI-Programms den Eintrag `nova` suchen. Sein `command` zeigt auf
   `NovaBrowser.McpProxy.exe`.
2. Den Schalter unter `args` eintragen:
   ```json
   {
     "mcpServers": {
       "nova": {
         "command": "C:\\Users\\<du>\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe",
         "args": ["--mirror-structured-content"]
       }
     }
   }
   ```
   Den `command`-Pfad aus deinem Eintrag beibehalten; bei älteren Installationen zeigt er nach
   `%LOCALAPPDATA%\NovaBrowser\bin\`. In JSON-Dateien muss jeder Backslash verdoppelt werden.
3. Das KI-Programm neu starten — Clients lesen ihre MCP-Konfiguration nur beim Start.

Nova behält den Schalter, wenn es seinen Eintrag in einer JSON-Konfiguration selbst aktualisiert. Für
Google Antigravity ist er nicht nötig: Der Antigravity-Eintrag enthält ihn bereits, siehe
[antigravity.md → Der Agent sieht keine Daten](antigravity.md#der-agent-sieht-keine-daten).

Die Brücke kennt nur `--antigravity-tool-names` und `--mirror-structured-content`; mit jedem anderen
Schalter (etwa einem vertippten) beendet sie sich sofort mit Exit-Code 2. Brücken aus Nova
1.0.0-alpha.17 und älter kennen den Schalter nicht und übergehen ihn — ändert sich nichts, Nova
aktualisieren.

Bitte den Agenten nicht per `curl` oder über Novas Dateien an der MCP-Verbindung vorbeiarbeiten lassen:
Diese Wege umgehen Novas Schutzprüfungen und brechen mit jedem Update.

## Nova läuft nicht / Verbindung abgelehnt

Nova geöffnet lassen, solange der Agent arbeitet. Unter **Einstellungen → KI & Agenten → Verbindung &
Einrichtung** prüfen, dass **Lokale Agentensteuerung aktivieren** und **Agenten dürfen den Browser
steuern** angehakt sind (beides ist Standard). Ist **Agenten dürfen Nova starten, wenn es geschlossen
ist** angehakt (ebenfalls Standard), startet die Brücke Nova selbst, wenn ein Agent es braucht.

Auf derselben Seite schreibt **Jetzt synchronisieren** Novas Eintrag in die KI-Programme, die Nova
automatisch abgleicht, **Runner neu installieren** legt eine frische Kopie der Brücke in Novas
Profilordner (etwa nach einem Umzug oder einer Neuinstallation), und **Einrichten** öffnet den
Verbindungsassistenten. Danach die Agenten-Sitzung neu starten — Clients lesen ihre MCP-Konfiguration
nur beim Start.

Weitere Diagnoseschritte: [Agent & MCP connection issues](../troubleshooting/agent-connection-issues.md).
