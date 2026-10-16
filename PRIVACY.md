# Privacy Policy / Datenschutzerklärung

*Last updated: October 16, 2026*

---

## English

### Controller and Contact

**Joel Aniol** is the controller for license-service data, reports you submit to Nova, and support correspondence. There is no separate data-protection contact: direct requests to Joel Aniol.

Postal address:

![Controller postal contact details](assets/legal/contact-identity.png)

Email contact:

![Email contact for privacy and support](assets/legal/contact-email.png)

The contact images reduce simple automated harvesting; they do not guarantee protection against scraping or OCR. An accessible text version of the contact details can be requested via the contact routes in the [legal notice](docs/legal-notice.md).

### Purposes and Legal Bases

Where the GDPR applies, the following bases are used for the specified purposes; sending a request is not consent to unrelated processing.

| Processing | Purpose and legal basis |
| --- | --- |
| License activation, renewal, device allocation and contract-related support | Providing and administering the license agreement: Article 6(1)(b) GDPR. Required fields are necessary to activate and administer the licensed service; without them activation cannot be completed. |
| License API security and event records | Preventing unauthorized activation, investigating errors, and defending the license service: Article 6(1)(f) GDPR, subject to the balancing of those legitimate interests and your rights. Records include event time, success/failure, license/activation identifiers, entered email where applicable, a hash of the IP address, request user agent, and the technical fields listed under License Activation. This is service-security logging, not browsing analytics. |
| Nova version and profile-layout state used to plan compatibility updates | Maintaining supported installations and avoiding data loss when retiring compatibility code: Article 6(1)(f) GDPR, subject to balancing your rights. |
| Optional crash reports | Your specific, voluntary consent to send the displayed report: Article 6(1)(a) GDPR. Declining does not prevent normal use of Nova. You may withdraw consent for further processing by contacting us; withdrawal does not invalidate earlier lawful processing. |
| Requests, objections, and privacy correspondence | Responding to a contract-related request: Article 6(1)(b); handling applicable legal duties or data-subject rights: Article 6(1)(c); other necessary correspondence: Article 6(1)(f), subject to balancing your rights. |

The absence of usage analytics does not mean that the license service has no technical records. The server receives connection data when contacted. Necessary hosting or service providers may process it on our behalf; disclosure to other recipients requires an applicable legal basis. Your websites and AI providers receive data directly under their own practices, as described below.

### Storage and Erasure Criteria

- **Local Nova data:** stays in the local profile until you delete it, a feature's configured retention removes it, or you choose removal during uninstall. Individual features may retain local history after an item disappears from the visible list; notification history is explained below.
- **License and activation records:** retained for administering the issued license and its device allocations, resolving related support or disputes, and meeting any applicable legal retention duties. Deactivation is not erasure. After those purposes end, deletion or anonymization is assessed against remaining legal obligations and claims.
- **License API/security records:** kept only for the security, error investigation, and dispute purposes above. Applicable incident investigation, legal claims, and statutory duties determine any continued retention; a device-deactivation action does not erase the event history.
- **Submitted crash reports:** retained for investigating the reported defect and related support; once that purpose ends, continued identifiable storage requires a separate applicable basis. Withdrawal or an erasure request is assessed accordingly.
- **Support and privacy correspondence:** retained while the request is handled and where necessary for related legal obligations or claims.

These are purpose-based criteria, not a promise of an implemented fixed-day purge. No fixed automatic deletion interval is currently specified here for server-side license, event, or crash-report records. Contact us to request erasure or information about the retention applicable to your records. Any statutory retention prevents deletion only to the extent it actually applies; it is not a blanket reason to keep all data indefinitely.

### Your Rights

Where applicable and subject to the statutory conditions, you may request access, rectification, erasure, restriction, and data portability. You may object to processing based on legitimate interests and withdraw consent at any time for consent-based processing. You may complain to a competent supervisory authority, including the [Bavarian State Office for Data Protection Supervision](https://www.lda.bayern.de/en/index.html). Contact [email contact](#controller-and-contact); proportionate identity verification may be needed to prevent disclosure to another person.

License-status decisions are technical checks against the issued license. They do not authorize behavioral profiling or automated evaluation of your suitability as a person. No sale of personal data or advertising use of license and crash-report data is permitted by this policy.

### Overview

Nova AI Workspace is designed to keep your data local. It does not collect usage analytics, does not track your browsing behavior, and does not build a behavioral profile of you. Nova only contacts its own server (`nova-cognitive.com`) for two purposes: **license activation and renewal** (required for the licensed app to run), and **optional, user-consented crash reports** after an unclean shutdown. A few features also connect directly to other services; they are listed under "Connections to Other Services". Nova keeps its browser profiles and stored workspace data locally. Data you send to websites, connected agents, or an optional crash report can leave your machine as described below.

### What Nova Does NOT Collect

- Nova does not upload your browsing-history database to its own server
- No usage analytics or telemetry during normal operation
- No behavioral tracking, browser/canvas fingerprinting, or usage profiling
- No automatic collection of your files, content, or activity
- No advertising identifiers

Note: license activation sends a small, defined set of data (including a hashed device identifier and your device name) so your license can be validated. This is described in full under "License Activation" below.

### License Activation

Nova is a licensed application. To activate your license and keep it valid, Nova contacts its own server at `nova-cognitive.com` over HTTPS. This happens when you activate a license and, afterwards, as an automatic background renewal while you use Nova (so your license lease stays current).

**What is sent during activation and renewal:**
- The **email address** and **license key** you entered
- A **Nova installation ID**, generated for the local installation; the same ID is used for crash-report correlation. It is pseudonymous, not anonymous, and an activation can associate it with license data.
- A **device fingerprint hash** (SHA-256) derived from that Nova installation ID, Windows user SID, and Windows MachineGuid. The Windows SID and MachineGuid are not sent in plaintext; the Nova installation ID is sent separately. The hash identifies and counts license seats and is not used for browsing tracking.
- Your **device name** (Windows hostname) in plain text, so you can recognize your own devices when managing activations
- Basic **environment info**: Windows edition and build, CPU architecture, and UI language
- The **Nova version** you are running
- Whether Nova's **data folder** has already been moved to its current location (one of two fixed words, `current` or `legacy` — never a path or user name)

**Why this data is used:** to validate the license, enforce the number of allowed devices per license, and let you manage your own activations and deactivations. The Nova version and the data-folder state are also used to **plan updates**: they tell us when compatibility code for older installations can be removed without leaving anyone's data behind. It is **not** used for advertising, cross-site tracking, or behavioral profiling.

**Where it is sent:**
- Endpoint: `nova-cognitive.com`
- Protocol: HTTPS (encrypted in transit)
- No third-party analytics services are involved

You can deactivate a device at any time. Deactivation marks the server-side activation record as deactivated; it does not automatically erase that record or the related license-event history.

### Optional Address-Bar Diagnostics

If you enable developer options and host performance timings, Nova records technical address-bar measurements in its local application log to investigate delays and flicker. These include elapsed times, suggestion counts, text lengths, cursor and selection positions, popup changes and navigation events. This diagnostic trace does not record the addresses or search phrases you type. It is off by default and stops collecting when host performance timings are disabled.

These measurements are not automatically transmitted. If you choose to send a crash report, its application-log excerpt may include them, as described below.

### Crash Reports (Opt-In Only)

If Nova did not shut down cleanly (crash, forced termination, system failure), it will show a dialog on the next launch offering to send a crash report.

**This is entirely opt-in:**
- You see the full report content as a JSON preview before deciding
- You choose "Send" or "Don't send"
- If you choose "Don't send", nothing is transmitted
- No data is sent automatically or in the background

**What a crash report contains:**
- Nova version and display version
- Operating system version, edition, and build number
- Pseudonymous installation ID (randomly generated to correlate reports from an installation)
- Application log tail (last 200 lines of the previous run's log)
- Crash exception type and stack trace
- Application uptime at the time of crash
- Open tab URLs, active tab index and tab count, and active sandbox names/identifiers
- Report timestamp, crashed-run identifier, and the crashed run's start time when available

**What a crash report does NOT contain:**
- The builder does not separately request real names, email addresses, or account details for the report
- No passwords, API keys, or authentication tokens
- No browsing history beyond the tabs open at crash time
- No file contents, downloads, or local documents
- No cookies or session data

Report excerpts and URLs can nevertheless contain personal or confidential context. Review the displayed report before sending it; automatic redaction is not a guarantee that every sensitive detail has been removed.

**Automatic PII redaction:**
Before the report is shown to you and before it could be sent, Nova automatically redacts:
- Local file paths → `<redacted-path>`
- Email addresses → `<redacted-email>`
- Bearer tokens → `Bearer <redacted>`
- Authorization headers → `<redacted>`
- Cookie values → `<redacted>`
- URL query parameters are stripped (only scheme, host, and path are kept)

**Where crash reports are sent:**
- Endpoint: `nova-cognitive.com`
- Protocol: HTTPS (encrypted in transit)
- No third-party analytics services are involved
- Reports are used solely to diagnose and fix bugs

### Connections to Other Services

Apart from the license and crash-report requests above, Nova itself contacts these services. Each receives your IP address and the request data described for that feature:

- **Update check — GitHub** (`api.github.com`). Nova asks GitHub for its newest release, at most about once a day and when you click **Check for updates**. If you install an update, the setup file is downloaded from GitHub. On by default; turn it off in Settings → About with **Check for new versions automatically**.
- **Search suggestions — your search engine.** While you type in the address bar, Nova sends the typed text to your default search engine (Google unless you changed it; Bing or DuckDuckGo otherwise) to show search suggestions. If that engine returns none, Nova asks DuckDuckGo. On by default; turn it off in Settings with **Show search suggestions from the internet**.
- **Speech models — Hugging Face** (`huggingface.co`). Only when you or an agent installs an additional transcription model is it downloaded from there. The basic model ships with Nova.
- **Proxy check — ipify** (`api.ipify.org`). Only if you use a proxy: while it is active, Nova asks this service about every 30 seconds, and whenever you or an agent tests a proxy, which public IP address the proxy shows. The request goes through the proxy, so ipify sees the proxy's address.
- **WebView2 runtime — Microsoft.** Only if the browser engine is missing or damaged does Nova download it from Microsoft.

The websites you open in Nova are contacted by the browser engine as in any browser; that traffic is not covered by this list.

### Third-Party AI Providers

When you use AI features in Nova (Claude, Codex, Gemini), your prompts and interactions are sent to the respective AI provider's API. Nova does not control how these providers handle your data. Please refer to their individual privacy policies:

- Claude: https://www.anthropic.com/privacy
- Codex/ChatGPT: https://openai.com/policies/privacy-policy
- Gemini: https://ai.google.dev/gemini-api/terms

Nova does not send your AI conversations to nova-cognitive.com or any other Nova server.

### MCP Server

Nova's local MCP server runs on localhost only by default. When enabled, it allows MCP-compatible tools on your machine to interact with Nova. This is a local communication channel — no data is sent to external servers through the MCP server unless you explicitly configure remote access.

On an agent's request, `read_text_structured` can return rendered page text as structured
messages, including declared roles, author labels and timestamps where available. The result
goes to the connected agent. If that agent uses a cloud service, it can transmit these contents
to its provider even when the MCP connection itself is local. This reading mode does not create
a separate conversation archive or load older messages automatically.

### Recorded Network Traffic

Nova can record the requests a page makes, including headers and bodies, and an agent can replay or
intercept them. This is off until you ask for it, and it changes nothing about where your data goes:

- **Nova does not store recorded traffic.** The recording lives in the page while the tab is open. No
  request, header or body is written to disk by this feature, and none of it is sent to
  `nova-cognitive.com`
- **The action log keeps metadata only** — which tool ran, on which host, whether it succeeded, how
  long it took and, if you switch that on, how many bytes the answer had. Never headers or bodies
- **What an agent receives, leaves your machine if that agent is a cloud service.** A recorded body
  handed to Claude, Codex or Gemini reaches that provider like any other part of the conversation —
  see "Third-Party AI Providers" above
- **`redact` masks credentials before an agent sees them** — tokens, cookies and credentials in URLs.
  Use it when the traffic is not yours to share
- **An interception rule is visible and temporary** — the toolbar shows it while it is armed, it is
  bound to one tab and a URL scope, and it expires on its own

### TLS Inspection

An agent can ask Nova to check a server's TLS certificate and configuration (`nova.tls_inspect`). This
runs only when an agent calls it:

- **Nova connects to the server the agent named**, over the same proxy route your browser uses, and
  reads what the server presents to every client. The result goes to that agent and is not stored
- **The optional subdomain lookup sends the domain name to crt.sh**, a public Certificate
  Transparency search operated by Sectigo. Only the domain is sent, nothing about you or your
  browsing. Nova asks crt.sh only when the agent requests this lookup explicitly
- **The action log keeps metadata only**, as for every other tool

### Local Data Storage

All application data is stored locally on your machine:

```
%LOCALAPPDATA%\nova-cognitive\Nova\
```

Installations up to version 1.0.0-alpha.17 used `%LOCALAPPDATA%\NovaBrowser\`. The setup of a newer version moves that folder to the new location; if the move is not possible, the data stays in the old folder.

This includes settings, browser profiles, history, favorites, vault entries, knowledge stores, conversation archives, logs, and task workspaces. You can delete this folder at any time to remove all Nova data. The uninstaller offers this option as well.

**Crash dumps:** If Nova or its terminal helper crashes, Windows stores a small memory snapshot of the crashed program (a minidump, at most five per program) in `%LOCALAPPDATA%\nova-cognitive\CrashDumps`. It can contain fragments of what the program held in memory at that moment, such as page addresses or text. The setup configures this so that a crash can be investigated at all. Nova never sends these files; they leave your computer only if you choose to share one with support. From version 1.0.0-alpha.21, if you do not want to keep them, turn off **Keep crash dumps** under Settings → Privacy & Security → Privacy; Nova then deletes them. You can also delete the folder at any time; the uninstaller's option to remove personal data deletes it as well.

**Notifications:** Nova keeps a local notification history containing message text, source website,
time, pictures when supplied, and the originating tab, sandbox, or browsing profile needed to open
the right source. This can include notifications received in private tabs: ending a private session
does not itself delete the notification history. Read or cleared notifications may remain in the
local history database until the configured retention period removes them. Windows also receives
the content of notifications shown through its notification system; Windows notification settings
control that separate copy. Nova does not upload notification history to its own server.

### Children

Nova AI Workspace is not directed at children under 13. We do not knowingly collect data from children.

### Contact

For privacy-related questions: [email contact](#controller-and-contact). See Controller and Contact above for postal details.

---

## Deutsch

### Verantwortlicher und Kontakt

**Joel Aniol** ist Verantwortlicher für Daten des Lizenzdienstes, an Nova übermittelte Berichte und Supportkorrespondenz. Es gibt keinen gesonderten Datenschutzkontakt; richte Anfragen direkt an Joel Aniol.

Postanschrift:

![Postalische Kontaktdaten des Verantwortlichen](assets/legal/contact-identity.png)

E-Mail-Kontakt:

![E-Mail-Kontakt für Datenschutz und Support](assets/legal/contact-email.png)

Die Kontaktbilder erschweren einfaches automatisiertes Auslesen; sie garantieren keinen Schutz vor Scraping oder OCR. Eine zugängliche Textfassung der Kontaktdaten kann über die Kontaktwege in den [rechtlichen Hinweisen](docs/legal-notice.md) angefragt werden.

### Zwecke und Rechtsgrundlagen

Soweit die DSGVO gilt, werden für die angegebenen Zwecke folgende Grundlagen verwendet. Eine Anfrage ist keine Einwilligung in sachfremde Verarbeitung.

| Verarbeitung | Zweck und Rechtsgrundlage |
| --- | --- |
| Lizenzaktivierung, Verlängerung, Gerätezuordnung und vertragsbezogener Support | Bereitstellung und Verwaltung der Lizenzvereinbarung: Art. 6 Abs. 1 lit. b DSGVO. Erforderliche Angaben sind für Aktivierung und Verwaltung des lizenzierten Dienstes notwendig; ohne sie ist die Aktivierung nicht möglich. |
| Sicherheit und Ereignisprotokolle der Lizenz-API | Verhinderung unbefugter Aktivierung, Fehlerklärung und Schutz des Lizenzdienstes: Art. 6 Abs. 1 lit. f DSGVO unter Abwägung dieser berechtigten Interessen und deiner Rechte. Protokolle enthalten Ereigniszeit, Erfolg/Fehler, Lizenz-/Aktivierungskennungen, gegebenenfalls eingegebene E-Mail, einen Hash der IP-Adresse, den User-Agent der Anfrage und die unter Lizenzaktivierung genannten technischen Angaben. Das ist Protokollierung zur Dienstsicherheit, keine Surfverhaltensanalyse. |
| Nova-Version und Profilpfadstatus für Kompatibilitätsplanung | Erhalt unterstützter Installationen und Vermeidung von Datenverlust beim Abbau von Kompatibilitätscode: Art. 6 Abs. 1 lit. f DSGVO unter Abwägung deiner Rechte. |
| Optionale Crashberichte | Deine konkrete, freiwillige Einwilligung in die Übermittlung des angezeigten Berichts: Art. 6 Abs. 1 lit. a DSGVO. Ablehnung verhindert nicht die normale Nutzung. Du kannst die Einwilligung für weitere Verarbeitung durch Kontaktaufnahme widerrufen; die Rechtmäßigkeit vorheriger Verarbeitung bleibt unberührt. |
| Anfragen, Einwände und Datenschutzkorrespondenz | Vertragsbezogene Anfragen: Art. 6 Abs. 1 lit. b; geltende Rechtspflichten oder Betroffenenrechte: Art. 6 Abs. 1 lit. c; sonstige erforderliche Korrespondenz: Art. 6 Abs. 1 lit. f jeweils unter Abwägung deiner Rechte. |

Keine Nutzungsanalysen bedeutet nicht, dass der Lizenzdienst keine technischen Protokolle führt. Bei Kontakt erhält der Server Verbindungsdaten. Erforderliche Hosting- oder Dienstleister können diese in unserem Auftrag verarbeiten; weitere Empfänger benötigen eine anwendbare Rechtsgrundlage. Websites und KI-Anbieter erhalten Daten direkt nach ihren eigenen Regeln, wie unten beschrieben.

### Aufbewahrungs- und Löschkriterien

- **Lokale Nova-Daten:** verbleiben im lokalen Profil, bis du sie löschst, eine eingestellte Aufbewahrungsdauer sie entfernt oder du beim Deinstallieren ihre Entfernung wählst. Einzelne Funktionen können lokale Historie nach dem Verschwinden eines sichtbaren Eintrags behalten; der Benachrichtigungsverlauf ist unten erläutert.
- **Lizenz- und Aktivierungsdaten:** werden für Verwaltung der erteilten Lizenz und ihrer Gerätezuordnung, zugehörigen Support oder Streitfälle sowie anwendbare gesetzliche Aufbewahrungspflichten gespeichert. Deaktivierung ist keine Löschung. Nach Wegfall dieser Zwecke wird Löschung oder Anonymisierung anhand verbleibender Pflichten und Ansprüche geprüft.
- **Lizenz-API-/Sicherheitsprotokolle:** werden nur für die oben genannten Sicherheits-, Fehlerklärungs- und Streitfallzwecke aufbewahrt. Laufende Vorfallklärung, Rechtsansprüche und gesetzliche Pflichten bestimmen eine weitere Aufbewahrung; Geräte-Deaktivierung löscht die Ereignishistorie nicht.
- **Übermittelte Crashberichte:** werden zur Untersuchung des gemeldeten Fehlers und für zugehörigen Support aufbewahrt. Nach Wegfall dieses Zwecks benötigt weitere personenbezogene Speicherung eine gesonderte anwendbare Grundlage. Widerrufs- und Löschanfragen werden entsprechend geprüft.
- **Support- und Datenschutzkorrespondenz:** wird während der Bearbeitung und soweit für zugehörige Pflichten oder Rechtsansprüche erforderlich gespeichert.

Dies sind zweckbezogene Kriterien, keine Zusage eines implementierten festen Löschintervalls. Für serverseitige Lizenz-, Ereignis- und Crashberichtsdaten ist hier derzeit keine feste automatische Tagesfrist angegeben. Kontaktiere uns für Löschung oder Auskunft über die Aufbewahrung deiner Daten. Gesetzliche Aufbewahrung verhindert Löschung nur in ihrem tatsächlichen Anwendungsbereich; sie rechtfertigt keine pauschale unbegrenzte Speicherung sämtlicher Daten.

### Deine Rechte

Soweit anwendbar und unter den gesetzlichen Voraussetzungen kannst du Auskunft, Berichtigung, Löschung, Einschränkung und Datenübertragbarkeit verlangen. Du kannst Verarbeitung auf Grundlage berechtigter Interessen widersprechen und Einwilligungen jederzeit für weitere Verarbeitung widerrufen. Du kannst dich bei einer zuständigen Aufsichtsbehörde beschweren, darunter dem [Bayerischen Landesamt für Datenschutzaufsicht](https://www.lda.bayern.de/de/index.html). Kontakt: [E-Mail-Kontakt](#verantwortlicher-und-kontakt). Eine verhältnismäßige Identitätsprüfung kann nötig sein, um Daten nicht an eine andere Person herauszugeben.

Lizenzstatusentscheidungen sind technische Prüfungen gegen die erteilte Lizenz. Sie erlauben keine Verhaltensprofile oder automatisierte Bewertung deiner Eignung als Person. Ein Verkauf personenbezogener Daten oder Werbenutzung von Lizenz- und Crashberichtsdaten ist durch diese Erklärung nicht gestattet.

### Überblick

Nova AI Workspace ist darauf ausgelegt, deine Daten lokal zu halten. Es werden keine Nutzungsanalysen gesammelt, dein Browserverhalten wird nicht getrackt und es wird kein Verhaltensprofil von dir erstellt. Nova kontaktiert seinen eigenen Server (`nova-cognitive.com`) nur für zwei Zwecke: **Lizenzaktivierung und -verlängerung** (erforderlich, damit die lizenzierte App läuft) und **optionale, von dir bestätigte Absturzberichte** nach einem unsauberen Beenden. Einige Funktionen verbinden sich außerdem direkt mit anderen Diensten; sie stehen unter „Verbindungen zu anderen Diensten“. Nova hält Browserprofile und gespeicherte Workspace-Daten lokal. Daten, die du an Websites, verbundene Agenten oder über einen optionalen Crashbericht sendest, können deinen Rechner wie unten beschrieben verlassen.

### Was Nova NICHT sammelt

- Nova lädt die Browserverlauf-Datenbank nicht auf seinen eigenen Server hoch
- Keine Nutzungsanalysen oder Telemetrie im Normalbetrieb
- Kein Verhaltens-Tracking, kein Browser-/Canvas-Fingerprinting, kein Nutzungsprofiling
- Keine automatische Erfassung deiner Dateien, Inhalte oder Aktivitäten
- Keine Werbe-Identifikatoren

Hinweis: Die Lizenzaktivierung sendet einen kleinen, klar definierten Datensatz (u.a. einen gehashten Geräte-Identifikator und deinen Gerätenamen), damit deine Lizenz validiert werden kann. Das ist unten unter „Lizenzaktivierung" vollständig beschrieben.

### Lizenzaktivierung

Nova ist eine lizenzierte Anwendung. Um deine Lizenz zu aktivieren und gültig zu halten, kontaktiert Nova seinen eigenen Server unter `nova-cognitive.com` über HTTPS. Das passiert bei der Aktivierung einer Lizenz und danach als automatische Hintergrund-Verlängerung, während du Nova nutzt (damit deine Lizenz-Lease aktuell bleibt).

**Was bei Aktivierung und Verlängerung gesendet wird:**
- Die von dir eingegebene **E-Mail-Adresse** und der **Lizenzschlüssel**
- Eine **Nova-Installations-ID**, die für die lokale Installation erzeugt wird; dieselbe ID dient der Zuordnung von Crashberichten. Sie ist pseudonym, nicht anonym, und kann bei der Aktivierung mit Lizenzdaten verknüpft werden.
- Ein **Geräte-Fingerprint-Hash** (SHA-256), abgeleitet aus dieser Nova-Installations-ID, der Windows-Benutzer-SID und der Windows-MachineGuid. Windows-SID und MachineGuid werden nicht im Klartext gesendet; die Nova-Installations-ID wird separat übertragen. Der Hash dient der Identifikation und Zählung von Lizenzplätzen und wird nicht für Surfverhaltens-Tracking verwendet.
- Dein **Gerätename** (Windows-Hostname) im Klartext, damit du deine eigenen Geräte bei der Verwaltung der Aktivierungen wiedererkennst
- Grundlegende **Umgebungsinfos**: Windows-Edition und -Build, CPU-Architektur und UI-Sprache
- Die **Nova-Version**, die du nutzt
- Ob Novas **Datenordner** schon an seinem aktuellen Ort liegt (eines von zwei festen Wörtern, `current` oder `legacy` — nie ein Pfad oder Benutzername)

**Wozu diese Daten dienen:** um die Lizenz zu validieren, die Anzahl erlaubter Geräte pro Lizenz durchzusetzen und dir die Verwaltung deiner eigenen Aktivierungen/Deaktivierungen zu ermöglichen. Nova-Version und Lage des Datenordners dienen außerdem der **Update-Planung**: Sie zeigen, wann Kompatibilitätscode für ältere Installationen entfernt werden kann, ohne dass jemandes Daten zurückbleiben. Sie werden **nicht** für Werbung, seitenübergreifendes Tracking oder Verhaltensprofiling verwendet.

**Wohin es gesendet wird:**
- Endpunkt: `nova-cognitive.com`
- Protokoll: HTTPS (verschlüsselt bei der Übertragung)
- Keine Drittanbieter-Analysedienste sind beteiligt

Du kannst ein Gerät jederzeit deaktivieren. Die Deaktivierung markiert den serverseitigen Aktivierungsdatensatz als deaktiviert; sie löscht diesen Datensatz oder die zugehörige Lizenz-Ereignishistorie nicht automatisch.

### Optionale Adresszeilen-Diagnose

Wenn du Entwickleroptionen und Host-Performance-Zeiten aktivierst, protokolliert Nova technische Messwerte der Adresszeile im lokalen Anwendungslog, um Verzögerungen und Flackern zu untersuchen. Dazu gehören verstrichene Zeiten, Vorschlagszahlen, Textlängen, Cursor- und Auswahlpositionen, Popup-Wechsel und Navigationsereignisse. Diese Diagnose zeichnet die eingegebenen Adressen oder Suchphrasen nicht auf. Sie ist standardmäßig aus und erfasst keine weiteren Messwerte, sobald Host-Performance-Zeiten deaktiviert sind.

Diese Messwerte werden nicht automatisch übertragen. Wenn du einen Absturzbericht sendest, kann dessen Anwendungslog-Auszug sie enthalten, wie unten beschrieben.

### Absturzberichte (nur auf Zustimmung)

Wenn Nova nicht sauber beendet wurde (Absturz, erzwungenes Beenden, Systemfehler), wird beim nächsten Start ein Dialog angezeigt, der das Senden eines Absturzberichts anbietet.

**Dies geschieht ausschließlich auf Zustimmung (Opt-in):**
- Du siehst den vollständigen Berichtsinhalt als JSON-Vorschau vor der Entscheidung
- Du wählst "Senden" oder "Nicht senden"
- Bei "Nicht senden" wird nichts übertragen
- Es werden keine Daten automatisch oder im Hintergrund gesendet

**Was ein Absturzbericht enthält:**
- Nova-Version und Anzeige-Version
- Betriebssystem-Version, Edition und Build-Nummer
- Pseudonyme Installations-ID (zufällig generiert, um Berichte einer Installation zuzuordnen)
- Anwendungs-Log-Ende (letzte 200 Zeilen des vorherigen Programmlaufs)
- Absturz-Ausnahmetyp und Stack-Trace
- Anwendungslaufzeit zum Zeitpunkt des Absturzes
- Geöffnete Tab-URLs, aktiver Tabindex und Tabanzahl sowie Namen/Kennungen aktiver Sandboxes
- Berichtszeitpunkt, Kennung des abgestürzten Laufs und dessen Startzeit, soweit verfügbar

**Was ein Absturzbericht NICHT enthält:**
- Der Builder fragt für den Bericht keine echten Namen, E-Mail-Adressen oder Kontodetails gesondert ab
- Keine Passwörter, API-Schlüssel oder Authentifizierungs-Tokens
- Keinen Browserverlauf über die zum Absturzzeitpunkt offenen Tabs hinaus
- Keine Dateiinhalte, Downloads oder lokale Dokumente
- Keine Cookies oder Sitzungsdaten

Berichtsauszüge und URLs können dennoch personenbezogenen oder vertraulichen Kontext enthalten. Prüfe den angezeigten Bericht vor dem Senden; automatische Maskierung garantiert nicht, dass jedes sensible Detail entfernt wurde.

**Automatische PII-Schwärzung:**
Bevor der Bericht dir angezeigt wird und bevor er gesendet werden könnte, schwärzt Nova automatisch:
- Lokale Dateipfade → `<redacted-path>`
- E-Mail-Adressen → `<redacted-email>`
- Bearer-Tokens → `Bearer <redacted>`
- Autorisierungs-Header → `<redacted>`
- Cookie-Werte → `<redacted>`
- URL-Query-Parameter werden entfernt (nur Schema, Host und Pfad bleiben erhalten)

**Wohin Absturzberichte gesendet werden:**
- Endpunkt: `nova-cognitive.com`
- Protokoll: HTTPS (verschlüsselt bei der Übertragung)
- Keine Drittanbieter-Analysedienste sind beteiligt
- Berichte werden ausschließlich zur Diagnose und Behebung von Fehlern verwendet

### Verbindungen zu anderen Diensten

Neben den oben beschriebenen Anfragen für Lizenz und Absturzberichte kontaktiert Nova selbst diese Dienste. Jeder erhält deine IP-Adresse und die bei der jeweiligen Funktion beschriebenen Anfragedaten:

- **Update-Prüfung — GitHub** (`api.github.com`). Nova fragt bei GitHub nach der neuesten Version, höchstens etwa einmal am Tag und wenn du auf **Nach Updates suchen** klickst. Installierst du ein Update, wird die Setup-Datei von GitHub geladen. Standardmäßig an; abschalten unter Einstellungen → Info mit **Automatisch nach neuen Versionen suchen**.
- **Suchvorschläge — deine Suchmaschine.** Während du in die Adressleiste tippst, sendet Nova den getippten Text an deine Standardsuchmaschine (Google, sofern du nichts anderes gewählt hast, sonst Bing oder DuckDuckGo), um Suchvorschläge anzuzeigen. Liefert diese keine, fragt Nova bei DuckDuckGo. Standardmäßig an; abschalten in den Einstellungen mit **Suchvorschläge aus dem Internet**.
- **Sprachmodelle — Hugging Face** (`huggingface.co`). Nur wenn du oder ein Agent ein zusätzliches Transkriptionsmodell installiert, wird es von dort geladen. Das Basismodell liefert Nova mit.
- **Proxy-Prüfung — ipify** (`api.ipify.org`). Nur wenn du einen Proxy nutzt: Solange er aktiv ist, fragt Nova diesen Dienst etwa alle 30 Sekunden, und bei jedem Test durch dich oder einen Agenten, welche öffentliche IP-Adresse der Proxy zeigt. Die Anfrage läuft über den Proxy, ipify sieht also dessen Adresse.
- **WebView2-Laufzeit — Microsoft.** Nur wenn die Browser-Engine fehlt oder beschädigt ist, lädt Nova sie von Microsoft.

Die Websites, die du in Nova öffnest, kontaktiert die Browser-Engine wie in jedem Browser; dieser Verkehr ist von dieser Liste nicht erfasst.

### Drittanbieter-KI-Provider

Bei Nutzung der KI-Funktionen in Nova (Claude, Codex, Gemini) werden deine Eingaben und Interaktionen an die API des jeweiligen KI-Anbieters gesendet. Nova hat keinen Einfluss darauf, wie diese Anbieter deine Daten verarbeiten. Bitte beachte deren individuelle Datenschutzerklärungen:

- Claude: https://www.anthropic.com/privacy
- Codex/ChatGPT: https://openai.com/policies/privacy-policy
- Gemini: https://ai.google.dev/gemini-api/terms

Nova sendet deine KI-Konversationen nicht an nova-cognitive.com oder andere Nova-Server.

### MCP-Server

Novas lokaler MCP-Server läuft standardmäßig nur auf localhost. Wenn aktiviert, ermöglicht er MCP-kompatiblen Werkzeugen auf deinem Rechner die Interaktion mit Nova. Dies ist ein lokaler Kommunikationskanal — es werden keine Daten über den MCP-Server an externe Server gesendet, es sei denn, du konfigurierst ausdrücklich den Remote-Zugriff.

Auf Anforderung eines Agenten kann `read_text_structured` gerenderten Seitentext als strukturierte
Nachrichten zurückgeben, einschließlich deklarierter Rollen, Autorenbezeichnungen und vorhandener
Zeitstempel. Das Ergebnis geht an den verbundenen Agenten. Nutzt dieser einen Cloud-Dienst, kann
er diese Inhalte an seinen Anbieter übertragen, auch wenn die MCP-Verbindung selbst lokal ist.
Dieser Lesemodus legt kein eigenes Gesprächsarchiv an und lädt ältere Nachrichten nicht automatisch.

### Aufgezeichneter Netzwerkverkehr

Nova kann die Anfragen einer Seite aufzeichnen, inklusive Header und Inhalte, und ein Agent kann sie
erneut senden oder abfangen. Das ist aus, bis du es verlangst, und es ändert nichts daran, wohin
deine Daten gehen:

- **Nova speichert aufgezeichneten Verkehr nicht.** Die Aufzeichnung lebt in der Seite, solange der
  Tab offen ist. Diese Funktion schreibt keine Anfrage, keinen Header und keinen Inhalt auf die
  Platte, und nichts davon geht an `nova-cognitive.com`
- **Das Aktionsprotokoll führt nur Metadaten** — welches Werkzeug lief, auf welchem Host, ob es
  erfolgreich war, wie lange es dauerte und, wenn du das einschaltest, wie viele Bytes die Antwort
  hatte. Niemals Header oder Inhalte
- **Was ein Agent bekommt, verlässt deinen Rechner, wenn dieser Agent ein Cloud-Dienst ist.** Ein
  aufgezeichneter Inhalt, den du Claude, Codex oder Gemini übergibst, erreicht diesen Anbieter wie
  jeder andere Teil des Gesprächs — siehe „Drittanbieter-KI-Provider" weiter oben
- **`redact` schwärzt Zugangsdaten, bevor ein Agent sie sieht** — Tokens, Cookies und Zugangsdaten in
  URLs. Nutze es, wenn der Verkehr nicht dir gehört
- **Eine Abfang-Regel ist sichtbar und vorübergehend** — die Symbolleiste zeigt sie, solange sie
  scharf ist, sie ist an einen Tab und einen URL-Bereich gebunden, und sie läuft von selbst ab

### TLS-Prüfung

Ein Agent kann Nova das TLS-Zertifikat und die TLS-Konfiguration eines Servers prüfen lassen
(`nova.tls_inspect`). Das läuft nur, wenn ein Agent es aufruft:

- **Nova verbindet sich mit dem Server, den der Agent nennt**, über denselben Proxy-Weg wie dein
  Browser, und liest, was der Server jedem Client zeigt. Das Ergebnis geht an diesen Agenten und
  wird nicht gespeichert
- **Die optionale Subdomain-Suche schickt den Domainnamen an crt.sh**, eine öffentliche Suche in den
  Certificate-Transparency-Logs, betrieben von Sectigo. Gesendet wird nur die Domain, nichts über
  dich oder dein Surfen. Nova fragt crt.sh nur, wenn der Agent diese Suche ausdrücklich anfordert
- **Das Aktionsprotokoll führt nur Metadaten**, wie bei jedem anderen Werkzeug

### Lokale Datenspeicherung

Alle Anwendungsdaten werden lokal auf deinem Rechner gespeichert:

```
%LOCALAPPDATA%\nova-cognitive\Nova\
```

Installationen bis Version 1.0.0-alpha.17 nutzten `%LOCALAPPDATA%\NovaBrowser\`. Das Setup einer neueren Version verschiebt diesen Ordner an den neuen Ort; ist das nicht möglich, bleiben die Daten im alten Ordner.

Dies umfasst Einstellungen, Browser-Profile, Verlauf, Favoriten, Vault-Einträge, Wissensspeicher, Gesprächsarchive, Logs und Task-Workspaces. Du kannst diesen Ordner jederzeit löschen, um alle Nova-Daten zu entfernen. Der Deinstaller bietet diese Option ebenfalls an.

**Absturzabbilder:** Stürzt Nova oder sein Terminal-Hilfsprogramm ab, legt Windows ein kleines Speicherabbild des abgestürzten Programms (Minidump, höchstens fünf je Programm) in `%LOCALAPPDATA%\nova-cognitive\CrashDumps` ab. Es kann Bruchstücke dessen enthalten, was das Programm in diesem Moment im Speicher hatte, etwa Seitenadressen oder Text. Das Setup richtet das ein, damit sich ein Absturz überhaupt untersuchen lässt. Nova sendet diese Dateien nie; sie verlassen deinen Rechner nur, wenn du eine davon selbst an den Support gibst. Ab Version 1.0.0-alpha.21 gilt: Willst du sie nicht behalten, schalte **Absturzabbilder behalten** unter Einstellungen → Datenschutz & Sicherheit → Datenschutz aus; Nova löscht sie dann. Du kannst den Ordner auch jederzeit löschen; die Deinstallations-Option zum Entfernen persönlicher Daten löscht ihn ebenfalls.

**Benachrichtigungen:** Nova führt einen lokalen Benachrichtigungsverlauf mit Meldungstext,
Website, Zeitpunkt, mitgelieferten Bildern sowie der Zuordnung zum ursprünglichen Tab, zur Sandbox
oder zum Browserprofil, damit die richtige Quelle geöffnet werden kann. Dazu können auch Meldungen
aus privaten Tabs gehören: Das Beenden einer privaten Sitzung löscht den Benachrichtigungsverlauf
nicht automatisch. Gelesene oder aus der Liste entfernte Meldungen können bis zum Ablauf der
eingestellten Aufbewahrungsdauer in der lokalen Datenbank verbleiben. Windows erhält außerdem die
Inhalte der über sein Benachrichtigungssystem angezeigten Meldungen; für diese separate Kopie gelten
die Windows-Benachrichtigungseinstellungen. Nova lädt den Verlauf nicht auf seinen eigenen Server hoch.

### Kinder

Nova AI Workspace richtet sich nicht an Kinder unter 13 Jahren. Es werden wissentlich keine Daten von Kindern erhoben.

### Kontakt

Für Datenschutzanfragen: [E-Mail-Kontakt](#verantwortlicher-und-kontakt). Postalische Angaben stehen oben unter Verantwortlicher und Kontakt.
