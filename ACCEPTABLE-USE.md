# Acceptable Use Policy / Nutzungsrichtlinie

*Last updated: October 18, 2026*

---

## English

This policy describes permitted use and misuse of Nova AI Workspace. Contractual consequences depend on the terms validly agreed with you; publication of this page does not by itself amend an existing contract. See the [EULA](EULA.md) for license rights, statutory warranty, liability, and suspension procedures.

### Arms-Industry and Military-Use Restrictions

**No business licenses for arms companies.** Nova may not be acquired or used for professional or commercial purposes by or on behalf of a company that develops, manufactures, markets, or trades weapons, ammunition, military explosives, or components, systems, or services specifically designed for military combat. This also covers use through employees, contractors, or other intermediaries, and applies to paid, free, trial, and evaluation use.

**Military technology is included.** The company exclusion also covers providers of software, AI, data analysis, military intelligence, targeting, or combat command systems specifically designed or adapted for military combat. It applies even if the company also serves civilian customers.

**No use for weapons or military combat.** No user may use Nova to develop, manufacture, market, trade, or procure weapons, ammunition, or military explosives, or to plan, conduct, or directly support military combat operations. This includes technical, procurement, and logistical workflows serving those purposes.

Employment by such a company does not prevent genuinely private use unrelated to these prohibited purposes. Civilian explosives applications, such as mining or construction, are not prohibited solely because they involve explosives. Providing general-purpose civilian goods or services alone does not make a company an arms company under this definition. Journalism, historical research, humanitarian aid, and disarmament or explosive-ordnance disposal are not prohibited solely because they concern weapons or conflict; the business-customer exclusion above still applies.

These restrictions concern Nova-owned software. They do not restrict rights granted independently by third-party or open-source licenses. Publishing this revision does not by itself retroactively change existing contracts; applicable contractual terms and mandatory legal rights remain unaffected.

### Authorized Testing

Authorized testing requires express permission from a person or organization entitled to grant it. Identify the systems, scope, permitted methods, and, where necessary, time limits before testing. Credentials, an existing session, or a technically available tool are not permission to act outside that scope.

### Permitted Use

- Personal browsing and productivity
- Authorized testing and automation of your own websites and services
- AI agent workflows on websites where you have explicit permission or where the site's terms of service allow automated access
- Research and development within legal boundaries
- Connecting MCP-compatible tools and agents for legitimate purposes
- Inspecting, intercepting and replaying network traffic of your own sites and services — and of third-party services only within a scope their operator has authorized in writing
- Checking the TLS certificate and TLS configuration of a server (`nova.tls_inspect`) — what every server presents to every client that connects. The check covers one host per call, stays within a fixed handshake budget and does not attack the server

### Prohibited Use

**Rule #1: Don't do bad.**

You may **not** use Nova AI Workspace to:

- **Violate laws or regulations** — including but not limited to computer fraud, data protection (GDPR, CCPA), copyright, and telecommunications laws
- **Unauthorized access** — access systems, accounts, or data without explicit authorization, even if technically possible through Nova's tools
- **Circumvent security measures** — bypass authentication, CAPTCHAs, rate limits, or access controls of third-party services unless explicitly authorized by the service owner
- **Scrape or harvest data** in violation of a website's terms of service, robots.txt, or applicable law
- **Distribute malware** — use Nova's automation, MCP server, or agent capabilities to create, distribute, or deploy malicious software
- **Spam or abuse** — send unsolicited messages, create fake accounts, manipulate reviews, or engage in any form of automated abuse
- **Impersonation** — use browser identity features to impersonate other individuals or organizations for fraudulent purposes
- **Denial of service** — use crawling, automation, or agent features to overload or disrupt third-party services
- **Surveillance** — use Nova's capabilities to monitor, track, or surveil individuals without a valid legal basis or lawful authority
- **Harm or harassment** — use AI agent features to generate harmful, abusive, threatening, or harassing content
- **Credential abuse** — use Nova's vault or MCP tools to test stolen credentials or conduct credential stuffing attacks
- **Traffic manipulation against services you do not operate** — use request interception, modification or failure injection to bypass payment, licensing, quotas, client-side validation, consent dialogs or security controls of a service you neither operate nor are authorized to test
- **Replaying requests without authorization** — resend recorded requests, including under a session Nova can reuse, against a service that has not authorized it. That Nova is technically able to reuse your session is not permission from the service
- **Recording other people's data** — capture request or response bodies containing other people's personal data, credentials or tokens without a legal basis. If such data is captured, keeping it out of logs and agent transcripts and deleting it is your responsibility; Nova's `redact` option exists for this
- **Saving videos you have no right to keep** — use "Save video" to copy a video that is plainly an unlawful upload, or pass on or publish a saved video without the rights holder's permission. A private copy is allowed only as far as the copyright law where you live allows it. Nova refuses encrypted and copy-protected videos; do not use other tools to work around that protection
- **Recording people without a legal basis** — use screen recording to record video calls, meetings or other people shown on a page without their consent or another legal basis. Nova silences the sound while a page uses the microphone, but the picture of a call and its participants is still recorded
- **Illegal commerce** — facilitate transactions involving illegal goods or services

### Your Responsibility

- **Your area of responsibility:** configure, authorize, and reasonably supervise connected agents to the extent these actions are within your control and legally attributable to you. This does not transfer responsibility for defects in Nova or failures in its permission checks to you
- **Review permissions carefully** — Nova's approval prompts exist for your protection. An authorization covers only its actual scope; it is not blanket consent to future actions
- **Monitor agent activity** — Use Nova's transcript, audit logs, and activity indicators to stay informed about what agents are doing
- **Third-party AI providers** — When using Claude, Codex, Gemini, or other providers through Nova, you must also comply with their respective terms of service and acceptable use policies
- **Emergency Stop exists for a reason** — If agent behavior is unexpected, use it
- **An armed interception rule stays your rule** — Nova shows it in the toolbar, binds it to one tab and a URL scope, and lets it expire by itself, but everything it does while armed is done on your behalf. Clear it when the task is over
- **Captured traffic can contain secrets** — headers and bodies may hold tokens, cookies and personal data, and they can reach an agent's transcript. Use `redact`, and treat a recording like the data it contains

### Alpha Risks and Mandatory Rights

Nova is alpha software; see the [technical risk notice](DISCLAIMER.md). Alpha status does not remove mandatory statutory warranty, update, consumer, or liability rights. The applicable license agreement governs contractual limitations; this policy creates no separate warranty or liability exclusion. See [EULA](EULA.md), sections 10 and 11.

---

## Deutsch

Diese Richtlinie beschreibt erlaubte Nutzung und Missbrauch von Nova AI Workspace. Vertragliche Folgen richten sich nach den wirksam mit dir vereinbarten Bedingungen; die Veröffentlichung dieser Seite ändert für sich genommen keinen bestehenden Vertrag. Nutzungsrechte, Mängelrechte, Haftung und Sperrverfahren stehen in der [EULA](EULA.md#deutsch).

### Ausschluss der Rüstungswirtschaft und militärischer Nutzung

**Keine geschäftlichen Lizenzen für Rüstungsunternehmen.** Nova darf nicht für berufliche oder gewerbliche Zwecke durch oder im Auftrag eines Unternehmens erworben oder genutzt werden, das Waffen, Munition, militärische Sprengstoffe oder speziell für militärische Kampfhandlungen konzipierte Komponenten, Systeme oder Dienstleistungen entwickelt, herstellt, vermarktet oder damit handelt. Dies erfasst auch die Nutzung über Beschäftigte, Auftragnehmer oder andere Vermittler und gilt für bezahlte, kostenlose, Test- und Evaluierungsnutzung.

**Militärtechnologie ist eingeschlossen.** Der Unternehmensausschluss erfasst auch Anbieter von Software, KI, Datenanalyse, militärischen Aufklärungs-, Zielerfassungs- oder Gefechtsführungssystemen, die speziell für militärische Kampfhandlungen konzipiert oder angepasst sind. Er gilt auch dann, wenn das Unternehmen zusätzlich zivile Kunden bedient.

**Keine Nutzung für Waffen oder militärische Kampfhandlungen.** Niemand darf Nova zur Entwicklung, Herstellung, Vermarktung, zum Handel oder zur Beschaffung von Waffen, Munition oder militärischen Sprengstoffen oder zur Planung, Durchführung oder unmittelbaren Unterstützung militärischer Kampfhandlungen einsetzen. Dies umfasst technische, Beschaffungs- und Logistikabläufe, die diesen Zwecken dienen.

Die Beschäftigung bei einem solchen Unternehmen schließt eine tatsächlich private Nutzung ohne Bezug zu diesen verbotenen Zwecken nicht aus. Zivile Sprengstoffanwendungen, etwa im Bergbau oder Bauwesen, sind nicht allein wegen des Einsatzes von Sprengstoffen verboten. Das bloße Anbieten allgemeiner ziviler Waren oder Dienstleistungen macht ein Unternehmen nach dieser Definition nicht zum Rüstungsunternehmen. Journalismus, historische Forschung, humanitäre Hilfe sowie Abrüstung oder Kampfmittelbeseitigung sind nicht allein deshalb verboten, weil sie Waffen oder Konflikte betreffen; der oben geregelte Ausschluss als Geschäftskunde bleibt bestehen.

Diese Grenzen betreffen Nova-eigene Software. Sie beschränken keine Rechte, die Drittanbieter- oder Open-Source-Lizenzen unabhängig gewähren. Die Veröffentlichung dieser Überarbeitung ändert bestehende Verträge nicht für sich genommen rückwirkend; anwendbare Vertragsbedingungen und zwingende gesetzliche Rechte bleiben unberührt.

### Autorisierte Prüfungen

Autorisierte Prüfungen setzen die ausdrückliche Genehmigung einer dazu befugten Person oder Stelle voraus. Systeme, Umfang, zulässige Verfahren und erforderlichenfalls Zeitgrenzen sind vor der Prüfung festzulegen. Zugangsdaten, eine vorhandene Sitzung oder ein technisch verfügbares Werkzeug erlauben keine Aktionen außerhalb dieses Rahmens.

### Erlaubte Nutzung

- Persönliches Browsen und Produktivität
- Autorisiertes Testen und Automatisieren eigener Websites und Dienste
- KI-Agenten-Workflows auf Websites, für die du ausdrückliche Erlaubnis hast oder deren Nutzungsbedingungen automatisierten Zugriff erlauben
- Forschung und Entwicklung innerhalb gesetzlicher Grenzen
- Anbindung MCP-kompatibler Tools und Agenten für legitime Zwecke
- Beobachten, Abfangen und erneutes Senden von Netzwerkverkehr eigener Websites und Dienste — bei Drittanbieterdiensten nur in einem Rahmen, den deren Betreiber schriftlich genehmigt hat
- Prüfen des TLS-Zertifikats und der TLS-Konfiguration eines Servers (`nova.tls_inspect`) — das, was jeder Server jedem Client zeigt, der sich verbindet. Die Prüfung umfasst einen Host pro Aufruf, bleibt in einem festen Handshake-Budget und greift den Server nicht an

### Verbotene Nutzung

**Regel Nr. 1: Don't do bad.**

Du darfst Nova AI Workspace **nicht** verwenden für:

- **Gesetzes- oder Regelverstöße** — einschließlich Computerbetrug, Datenschutz (DSGVO, BDSG), Urheberrecht und Telekommunikationsrecht
- **Unbefugten Zugriff** — Zugang zu Systemen, Konten oder Daten ohne ausdrückliche Genehmigung, auch wenn technisch über Novas Werkzeuge möglich
- **Umgehung von Sicherheitsmaßnahmen** — Umgehen von Authentifizierung, CAPTCHAs, Rate Limits oder Zugangskontrollen von Drittanbietern, es sei denn, der Dienstanbieter hat dies ausdrücklich genehmigt
- **Daten-Scraping oder -Sammlung** unter Verstoß gegen Nutzungsbedingungen, robots.txt oder geltendes Recht einer Website
- **Verbreitung von Schadsoftware** — Nutzung von Novas Automation, MCP-Server oder Agentenfunktionen zur Erstellung, Verbreitung oder Bereitstellung von Malware
- **Spam oder Missbrauch** — Versand unerwünschter Nachrichten, Erstellung gefälschter Konten, Bewertungsmanipulation oder jede Form automatisierten Missbrauchs
- **Identitätstäuschung** — Nutzung der Browser-Identitätsfunktionen zur betrügerischen Nachahmung anderer Personen oder Organisationen
- **Dienstverweigerungsangriffe** — Nutzung von Crawling, Automation oder Agentenfunktionen zur Überlastung oder Störung von Drittanbieterdiensten
- **Überwachung** — Nutzung von Novas Fähigkeiten zur Beobachtung, Verfolgung oder Überwachung von Personen ohne gültige Rechtsgrundlage oder rechtmäßige Befugnis
- **Schädigung oder Belästigung** — Nutzung von KI-Agentenfunktionen zur Erzeugung schädlicher, missbräuchlicher, bedrohlicher oder belästigender Inhalte
- **Credential-Missbrauch** — Nutzung von Novas Vault oder MCP-Tools zum Testen gestohlener Zugangsdaten oder für Credential-Stuffing-Angriffe
- **Manipulation des Verkehrs fremder Dienste** — Nutzung von Abfangen, Verändern oder absichtlichem Scheiternlassen von Anfragen, um Bezahlung, Lizenzierung, Kontingente, clientseitige Prüfungen, Zustimmungsdialoge oder Sicherheitsmechanismen eines Dienstes zu umgehen, den du weder betreibst noch zu testen befugt bist
- **Erneutes Senden ohne Befugnis** — aufgezeichnete Anfragen erneut senden, auch unter einer Sitzung, die Nova wiederverwenden kann, gegen einen Dienst, der das nicht genehmigt hat. Dass Nova deine Sitzung technisch wiederverwenden kann, ist keine Erlaubnis des Dienstes
- **Speichern von Videos ohne Recht dazu** — mit „Video speichern" ein Video kopieren, das offensichtlich rechtswidrig hochgeladen wurde, oder ein gespeichertes Video ohne Erlaubnis des Rechteinhabers weitergeben oder veröffentlichen. Eine Privatkopie ist nur erlaubt, soweit das Urheberrecht an deinem Wohnort sie erlaubt. Nova lehnt verschlüsselte und kopiergeschützte Videos ab; umgehe diesen Schutz nicht mit anderen Werkzeugen
- **Aufnehmen von Personen ohne Rechtsgrundlage** — Bildschirmaufnahmen von Videoanrufen, Besprechungen oder anderen Personen auf einer Seite ohne deren Einwilligung oder eine andere Rechtsgrundlage. Nova schaltet den Ton stumm, solange eine Seite das Mikrofon nutzt; das Bild eines Gesprächs und seiner Teilnehmer wird trotzdem aufgenommen
- **Aufzeichnen fremder Daten** — Erfassen von Anfrage- oder Antwortinhalten mit personenbezogenen Daten, Zugangsdaten oder Tokens anderer Personen ohne Rechtsgrundlage. Werden solche Daten erfasst, liegt es bei dir, sie aus Protokollen und Agenten-Transcripts herauszuhalten und zu löschen; Novas `redact`-Option ist dafür da
- **Illegaler Handel** — Erleichterung von Transaktionen mit illegalen Gütern oder Dienstleistungen

### Deine Verantwortung

- **Dein Verantwortungsbereich:** Konfiguration, Autorisierung und angemessene Beaufsichtigung verbundener Agenten, soweit diese Handlungen in deinem Einflussbereich liegen und dir rechtlich zurechenbar sind. Fehler in Nova oder seiner Rechteprüfung werden dadurch nicht zu deiner Verantwortung
- **Prüfe Berechtigungen sorgfältig** — Novas Approval-Prompts existieren zu deinem Schutz. Eine Freigabe gilt nur in ihrem tatsächlichen Umfang und ist keine pauschale Zustimmung zu zukünftigen Aktionen
- **Überwache Agentenaktivität** — Nutze Novas Transcript, Audit-Logs und Aktivitätsindikatoren, um informiert zu bleiben
- **Drittanbieter-KI-Provider** — Bei Nutzung von Claude, Codex, Gemini oder anderen Anbietern über Nova müssen auch deren Nutzungsbedingungen eingehalten werden
- **Emergency Stop existiert aus gutem Grund** — Bei unerwartetem Agentenverhalten sofort nutzen
- **Eine scharfe Abfang-Regel bleibt deine Regel** — Nova zeigt sie in der Symbolleiste, bindet sie an einen Tab und einen URL-Bereich und lässt sie von selbst ablaufen; alles, was sie tut, solange sie scharf ist, geschieht in deinem Namen. Räume sie auf, wenn die Aufgabe erledigt ist
- **Aufgezeichneter Verkehr kann Geheimnisse enthalten** — Header und Inhalte können Tokens, Cookies und personenbezogene Daten tragen und in das Transcript eines Agenten gelangen. Nutze `redact` und behandle eine Aufzeichnung wie die Daten, die sie enthält

### Alpha-Risiken und zwingende Rechte

Nova ist Alpha-Software; siehe die [technischen Risikohinweise](DISCLAIMER.md). Der Alpha-Status beseitigt keine zwingenden gesetzlichen Mängel-, Aktualisierungs-, Verbraucher- oder Haftungsrechte. Vertragliche Grenzen richten sich nach der anwendbaren Lizenzvereinbarung; diese Richtlinie enthält keinen eigenständigen Gewährleistungs- oder Haftungsausschluss. Siehe [EULA](EULA.md#deutsch), Abschnitte 10 und 11.
