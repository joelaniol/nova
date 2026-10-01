# MCP troubleshooting

Status: 2026-10-01 · Deutsche Fassung weiter unten.

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

**Likely cause.** The client passes only the text part of an MCP answer (`content`) to the model and
drops the machine-readable result (`structuredContent`). For Google Antigravity see
[antigravity.md → The agent sees no data](antigravity.md#the-agent-sees-no-data). Public reports
describe the same behaviour for Cursor, Kiro, Goose and Continue; these have not been tested with Nova
yet. Claude Code and Codex are not affected.

Please do not let the agent bypass the MCP connection with `curl` or by reading Nova's files. Those
paths skip Nova's safety checks and break with every update.

## Nova is not running / connection refused

Keep Nova open while your agent works, and leave **Developer options** enabled — turning it off
disables the MCP server. On **Settings → AI & agents → Connection & setup**, **Sync now** rewrites the
client configurations and **Reinstall runner** repairs the connector after Nova was moved or
reinstalled. Restart the agent session afterwards; clients read their MCP configuration only at startup.

---

# MCP-Fehlerbehebung

Stand: 2026-10-01

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

**Wahrscheinliche Ursache.** Der Client gibt nur den Textteil einer MCP-Antwort (`content`) an das Modell
weiter und verwirft das maschinenlesbare Ergebnis (`structuredContent`). Für Google Antigravity siehe
[antigravity.md → Der Agent sieht keine Daten](antigravity.md#der-agent-sieht-keine-daten). Öffentliche
Berichte beschreiben dasselbe Verhalten bei Cursor, Kiro, Goose und Continue; mit Nova sind diese noch
nicht getestet. Claude Code und Codex sind nicht betroffen.

Bitte den Agenten nicht per `curl` oder über Novas Dateien an der MCP-Verbindung vorbeiarbeiten lassen:
Diese Wege umgehen Novas Schutzprüfungen und brechen mit jedem Update.

## Nova läuft nicht / Verbindung abgelehnt

Nova geöffnet lassen, solange der Agent arbeitet, und die **Entwickleroptionen** eingeschaltet lassen —
ausgeschaltet ist der MCP-Server aus. Unter **Einstellungen → KI & Agenten → Verbindung & Einrichtung**
schreibt **Jetzt synchronisieren** die Client-Konfigurationen neu, **Runner neu installieren** repariert
die Verbindung nach einem Umzug oder einer Neuinstallation. Danach die Agenten-Sitzung neu starten —
Clients lesen ihre MCP-Konfiguration nur beim Start.
