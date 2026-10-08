# Nova — Alpha status & known issues

*Deutsche Fassung weiter unten ⬇️*

Nova AI Workspace is in **public alpha**. This page collects the current status and the known
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
- **MCP tool quirks.** Some MCP tools still have rough edges or occasionally return
  imperfect results. Concrete failures and performance regressions can be reported with the
  agent reporting guide below; general work-session friction belongs in feedback.
- **SmartScreen "unknown publisher".** The setup is self-signed, so Windows SmartScreen may warn on
  the first run. Click **More info → Run anyway**.
- **WebView2 runtime on first launch.** The installer sets it up automatically. If it was missing
  (e.g. no internet during setup), Nova offers a one-click repair on the first start.

## What to report

Report **crashes, concrete MCP defects and performance regressions**, or give **work-session feedback** about successful steps, friction, slow operations and improvement suggestions. Known cosmetic GUI/settings issues do not need a report during alpha.

### Report through your connected agent

**Your agent can handle the report using Nova's reporting instructions. You do not need to fill in a GitHub form yourself when the agent has GitHub submission access.** Give it this request:

> Please report this problem using Nova's bug-report instructions. Describe my goal, the last relevant steps, what I expected and what happened. Include the Nova version and only relevant, sanitized evidence. Show me the finished draft first. After I approve it, submit the report and give me its issue URL.

The agent retrieves the [reporting guide with `nova.get_instructions(topic='bug_report')`](docs/mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md#reporting-bugs-and-work-session-feedback), chooses a bug or feedback template, and shows you the draft. Review URLs, screenshots and log excerpts for secrets and personal data before approving publication.

Nova provides the instructions and templates; the guide itself does not collect logs or submit an issue. After approval, the agent can submit through the GitHub CLI when available and authenticated. Otherwise it gives you the prepared text and the matching form. A crash that interrupts the Nova connection can be described after reconnecting or through the manual route below.

### Without a connected agent or submission access

Use the [crash form](https://github.com/joelaniol/nova/issues/new?template=crash-report.yml), [bug report form](https://github.com/joelaniol/nova/issues/new?template=bug-report.yml), or [feedback form](https://github.com/joelaniol/nova/issues/new?template=feedback.yml). Include the version from **Settings → About**, the goal, relevant steps, expected and observed behavior, and reviewed evidence.

**Security vulnerabilities always use the [private security form](https://github.com/joelaniol/nova/security/advisories/new)** (see [SECURITY.md](SECURITY.md)). Do not publish vulnerabilities or secrets in an ordinary issue.

## Guides and release notes

Start with [Quickstart](docs/getting-started/quickstart.md), use the [User guide](docs/user-guide/README.md) for everyday browsing, and see [release notes](docs/changelog/README.md) for version-specific changes. Feature pages describe capabilities; the alpha limitations above still apply. [Feature videos](README.md#-cognitive-architecture-beyond-generic-memory) and the [interactive demo](demos/README.md) give examples.

---

# Nova — Alpha-Status & bekannte Probleme (Deutsch)

Nova AI Workspace befindet sich in der **öffentlichen Alpha**. Diese Seite sammelt Status und
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
- **MCP-Tool-Eigenheiten.** Einige MCP-Tools haben noch Ecken und Kanten oder liefern
  gelegentlich unsaubere Ergebnisse. Konkrete Fehler und Performance-Regressionen koennen mit
  der Agent-Anleitung unten gemeldet werden; allgemeine Reibung gehoert ins Arbeitsfeedback.
- **SmartScreen „unbekannter Herausgeber".** Das Setup ist selbst-signiert → SmartScreen warnt beim
  ersten Start evtl. Klicke **Weitere Informationen → Trotzdem ausführen**.
- **WebView2-Laufzeit beim ersten Start.** Der Installer richtet sie automatisch ein. Fehlt sie
  (z. B. weil das Nachladen im Setup fehlgeschlagen ist), bietet Nova beim ersten Start eine Ein-Klick-Reparatur an.

## Was bitte melden

Melde **Abstürze, konkrete MCP-Defekte und Performance-Regressionen**. **Arbeitsfeedback** zu erfolgreichen Schritten, Reibung, langsamen Abläufen und Verbesserungsvorschlägen ist ebenfalls willkommen. Bekannte kosmetische GUI-/Einstellungsprobleme brauchen während der Alpha keine Meldung.

### Über deinen verbundenen Agenten melden

**Dein Agent kann die Meldung anhand von Novas Meldeanleitung übernehmen. Du musst das GitHub-Formular nicht selbst ausfüllen, wenn der Agent Zugriff zum Absenden hat.** Gib ihm diesen Auftrag:

> Bitte melde dieses Problem anhand von Novas Bug-Report-Anleitung. Beschreibe mein Ziel, die letzten relevanten Schritte, das erwartete und das beobachtete Verhalten. Ergänze die Nova-Version und nur relevante, bereinigte Belege. Zeige mir zuerst den fertigen Entwurf. Sende die Meldung nach meiner Freigabe ab und gib mir den Link zum Issue.

Der Agent ruft die [Meldeanleitung mit `nova.get_instructions(topic='bug_report')`](docs/mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md#reporting-bugs-and-work-session-feedback) ab, wählt eine Fehler- oder Feedback-Vorlage und zeigt dir den Entwurf. Prüfe URLs, Screenshots und Logauszüge auf Geheimnisse und persönliche Daten, bevor du die Veröffentlichung freigibst.

Nova liefert Anleitung und Vorlagen; die Anleitung selbst sammelt keine Logs und sendet kein Issue. Nach deiner Freigabe kann der Agent über die GitHub CLI absenden, sofern sie verfügbar und angemeldet ist. Andernfalls gibt er dir den vorbereiteten Text und das passende Formular. Unterbricht ein Absturz die Nova-Verbindung, kann die Meldung nach dem erneuten Verbinden oder über den manuellen Weg unten erstellt werden.

### Ohne verbundenen Agenten oder Zugriff zum Absenden

Nutze das [Absturz-Formular](https://github.com/joelaniol/nova/issues/new?template=crash-report.yml), [Fehler-Formular](https://github.com/joelaniol/nova/issues/new?template=bug-report.yml) oder [Feedback-Formular](https://github.com/joelaniol/nova/issues/new?template=feedback.yml). Ergänze die Version aus **Einstellungen → Info**, Ziel, relevante Schritte, erwartetes und beobachtetes Verhalten sowie geprüfte Belege.

**Sicherheitslücken gehören immer ins [private Sicherheitsformular](https://github.com/joelaniol/nova/security/advisories/new)** (siehe [SECURITY.md](SECURITY.md)). Veröffentliche Sicherheitslücken oder Geheimnisse nicht als normales Issue.

## Anleitungen und Versionshinweise

Beginne mit der [Installation auf Deutsch](docs/getting-started/installation.md#nova-ai-workspace-installieren) oder der [Demo auf Deutsch](demos/README.de.md). Der [Quickstart](docs/getting-started/quickstart.md), das [Benutzerhandbuch](docs/user-guide/README.md) und die [Versionshinweise](docs/changelog/README.md) sind auf Englisch. Die Feature-Seiten beschreiben Fähigkeiten; die Alpha-Einschränkungen oben gelten weiterhin.
