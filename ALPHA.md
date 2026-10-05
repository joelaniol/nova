# Nova — Alpha status & known issues

*Deutsche Fassung weiter unten ⬇️*

Nova Cognitive Browser is in **public alpha**. This page collects the current status and the known
issues, so you know what to expect before and during use.

## Status

- Public alpha, updated frequently — the built-in auto-update pulls new versions from this repo.
- **Use at your own risk** (see the [Disclaimer](DISCLAIMER.md)); not meant for critical or production tasks.

## Known issues

- **GUI / settings rough edges — please do NOT report these.** The interface is still evolving and
  a lot of the layout is going to change, so many screens (especially in Settings) have known UI and
  layout bugs. They're known and will be reworked — no need to file layout/UI reports.
- **Do NOT use Connectors inside Nova's terminal yet.** The connector features (e.g. mail/file
  connectors) are still under active development and not ready for real use — please avoid them in
  the terminal for now.
- **Plugins are not ready — don't use them yet.** The agent-authored plugins feature is disabled
  during the alpha and cannot be turned on; it's still under development.
- **MCP tool quirks.** Some of the 400+ MCP tools still have rough edges or occasionally return
  imperfect results. Concrete failures and performance regressions can be reported with the
  agent reporting guide below; general work-session friction belongs in feedback.
- **SmartScreen "unknown publisher".** The setup is self-signed, so Windows SmartScreen may warn on
  the first run. Click **More info → Run anyway**.
- **WebView2 runtime on first launch.** The installer sets it up automatically. If it was missing
  (e.g. no internet during setup), Nova offers a one-click repair on the first start.

## What to report

- **Crashes** (Nova closes unexpectedly) → [open an issue](https://github.com/joelaniol/nova/issues)
  using the crash template (include the version from Settings → About and, if possible, the log).
- **Security vulnerabilities** → privately via **Security → "Report a vulnerability"**
  (see [SECURITY.md](SECURITY.md)) — not a public issue.
- **MCP defects and performance regressions** → [open an issue](https://github.com/joelaniol/nova/issues)
  with the goal, last relevant steps, expected and observed behavior, version, and sanitized evidence.
- **Work-session feedback** → use the same issue tracker for successful steps, friction, slow
  operations, and improvement suggestions; identify it as feedback rather than a confirmed bug.
- Agents can call `nova.get_instructions(topic='bug_report')` for rules and Markdown templates.
  Review URLs, screenshots, and log excerpts for secrets and personal data before publication.
- **Please do not report** the known cosmetic GUI issues above.

## Coming soon

Full documentation and video guides are on the way. Features and the agent tooling iterate quickly
during the alpha.

---

# Nova — Alpha-Status & bekannte Probleme (Deutsch)

Nova Cognitive Browser befindet sich in der **öffentlichen Alpha**. Diese Seite sammelt Status und
bekannte Probleme, damit du weißt, was dich erwartet.

## Status

- Öffentliche Alpha, häufige Updates — das eingebaute Auto-Update zieht neue Versionen aus diesem Repo.
- **Nutzung auf eigene Gefahr** (siehe [Haftungsausschluss](DISCLAIMER.md)); nicht für kritische Aufgaben.

## Bekannte Probleme

- **GUI-/Einstellungs-Ecken — bitte NICHT melden.** Die Oberfläche entwickelt sich noch stark und
  am Layout wird sich viel ändern; daher haben einige Ansichten (besonders in den Einstellungen)
  bekannte UI- und Layout-Bugs. Bekannt und werden überarbeitet — keine Layout-/UI-Meldungen nötig.
- **Connectors im Nova-Terminal bitte noch NICHT nutzen.** Die Connector-Funktionen (z. B. Mail-/
  Datei-Connectors) sind noch in aktiver Entwicklung und nicht für den echten Einsatz bereit — im
  Terminal vorerst meiden.
- **Plugins sind noch nicht fertig — bitte noch nicht nutzen.** Die Funktion für agenten-erstellte
  Plugins ist während der Alpha deaktiviert und lässt sich nicht einschalten; sie ist noch in Entwicklung.
- **MCP-Tool-Eigenheiten.** Einige der über 400 MCP-Tools haben noch Ecken und Kanten oder liefern
  gelegentlich unsaubere Ergebnisse. Konkrete Fehler und Performance-Regressionen koennen mit
  der Agent-Anleitung unten gemeldet werden; allgemeine Reibung gehoert ins Arbeitsfeedback.
- **SmartScreen „unbekannter Herausgeber".** Das Setup ist selbst-signiert → SmartScreen warnt beim
  ersten Start evtl. Klicke **Weitere Informationen → Trotzdem ausführen**.
- **WebView2-Laufzeit beim ersten Start.** Der Installer richtet sie automatisch ein. Fehlt sie
  (z. B. offline installiert), bietet Nova beim ersten Start eine Ein-Klick-Reparatur an.

## Was bitte melden

- **Abstürze** (Nova schließt sich unerwartet) → [Issue öffnen](https://github.com/joelaniol/nova/issues)
  mit dem Crash-Template (Version aus Einstellungen → Info und, wenn möglich, das Log).
- **Sicherheitslücken** → privat über **Security → „Report a vulnerability"** (siehe
  [SECURITY.md](SECURITY.md)) — kein öffentliches Issue.
- **MCP-Defekte und Performance-Regressionen** → [Issue öffnen](https://github.com/joelaniol/nova/issues)
  mit Ziel, letzten relevanten Schritten, erwartetem und beobachtetem Verhalten, Version und bereinigten Belegen.
- **Arbeitsfeedback** → im selben Issue-Tracker erfolgreiche Schritte, Reibung, langsame
  Abläufe und Verbesserungsvorschläge schildern; als Feedback statt bestaetigten Bug kennzeichnen.
- Agenten erhalten mit `nova.get_instructions(topic='bug_report')` Regeln und Markdown-Vorlagen.
  URLs, Screenshots und Logauszüge vor Veröffentlichung auf Geheimnisse und persönliche Daten prüfen.
- **Bitte keine** bekannten kosmetischen GUI-Probleme oben melden.

## In Kürze

Ausführliche Dokumentation und Video-Anleitungen folgen. Features und Agent-Tools entwickeln sich in
der Alpha schnell weiter.
