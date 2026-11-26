# Acceptable Use Policy / Nutzungsrichtlinie

*Last updated: November 25, 2026*

---

## English

This policy describes permitted use and misuse of Nova AI Workspace. Contractual consequences depend on the terms validly agreed with you; publication of this page does not by itself amend an existing contract. See the [EULA](EULA.md) for license rights, statutory warranty, liability, and suspension procedures.

### Authorized Testing

Authorized testing requires express permission from a person or organization entitled to grant it. Identify the systems, scope, permitted methods, and, where necessary, time limits before testing. Credentials, an existing session, or a technically available tool are not permission to act outside that scope.

### Permitted Use

- Personal browsing and productivity
- Authorized testing and automation of your own websites and services
- AI agent workflows on websites where you have explicit permission or where the site's terms of service allow automated access. Where a site asks agents to identify themselves, as Amazon does, let your agent do so with **Agent identification** (Settings → Privacy & Security, from version 1.0.0-alpha.21)
  - Agents can type, choose and click with real key and mouse input (`inputMode='keyboard'`, from version 1.0.0-alpha.21, not published yet), because some pages only react to that. This makes an agent's input work on such pages; it is not permission from the site. Whether automated use is allowed there is decided by the site's terms, and you check them. An account rule (`nova.account_rule`) keeps agents to a pace you choose and stops a second send; it protects your account, it does not make automated use allowed.
- Research and development within legal boundaries
- Connecting MCP-compatible tools and agents for legitimate purposes
- Inspecting, intercepting and replaying network traffic of your own sites and services — and of third-party services only within a scope their operator has authorized in writing
- Checking the TLS certificate and TLS configuration of a server (`nova.tls_inspect`) — what every server presents to every client that connects. The check covers one host per call, stays within a fixed handshake budget and does not attack the server
- Scanning networks you run (`nova.net_scan`, from version 1.0.0-alpha.21, not published yet) — your home or office network, your VPN, your own servers — to see which devices are there and which ports answer. Other networks only with the permission of whoever runs them
- Paying with your own payment cards, or cards you are allowed to use, through an agent (`nova.vault_card_fill`, from version 1.0.0-alpha.21, not published yet). You approve each fill with your Nova PIN, and the click on the pay button only when you tick it in the same dialog, which names the card, the shop and the payment provider. Whether automated purchases are allowed in a shop is decided by its terms
  - Within a purchase budget you set in Nova's settings and switch on (from version 1.0.0-alpha.21, not published yet), an agent's purchase that the remaining budget covers, in the budget's currency, goes ahead without the dialog and without your PIN. Anything the budget does not cover, and every purchase while it is off, asks you as before. Only you set and refill the budget. It is a limit Nova keeps, not a limit of your card or your bank

### Prohibited Use

**Rule #1: Don't do bad.**

You may **not** use Nova AI Workspace to:

- **Violate laws or regulations** — including but not limited to computer fraud, data protection (GDPR, CCPA), copyright, and telecommunications laws
- **Unauthorized access** — access systems, accounts, or data without explicit authorization, even if technically possible through Nova's tools
- **Circumvent security measures** — bypass authentication, CAPTCHAs, rate limits, or access controls of third-party services unless explicitly authorized by the service owner
  - Nova's setting "Let agents answer captchas" (off by default) lets an agent tick a verification checkbox itself. It is meant for your own services, testing, and services that allow it; it is not an authorization from the service. Check the service's terms first: many forbid automated access or answering their checks.
- **Scrape or harvest data** in violation of a website's terms of service, robots.txt, or applicable law
- **Distribute malware** — use Nova's automation, MCP server, or agent capabilities to create, distribute, or deploy malicious software
- **Spam or abuse** — send unsolicited messages, create fake accounts, manipulate reviews, or engage in any form of automated abuse
- **Getting around a block or suspension** — keep acting on a service through an account it has blocked or suspended, or open another account there to get around the block, through an agent or otherwise. Contacting the service about the block is of course allowed. When Nova locks an account because the site blocked it, only you can lift the lock; clear the matter with the service through its official way first
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
- **Scanning networks without permission** — scan a network or address range you neither run nor are authorized to test, for example at your workplace without the IT department's consent, in a hotel or on public Wi-Fi, or use a scan to prepare access to systems that are not yours. Approving the scan in Nova only confirms that it should run; it is not permission from the network's operator
- **Illegal commerce** — facilitate transactions involving illegal goods or services

### Your Responsibility

- **Your area of responsibility:** configure, authorize, and reasonably supervise connected agents to the extent these actions are within your control and legally attributable to you. This does not transfer responsibility for defects in Nova or failures in its permission checks to you
- **Review permissions carefully** — Nova's approval prompts exist for your protection. An authorization covers only its actual scope; it is not blanket consent to future actions
- **Monitor agent activity** — Use Nova's transcript, audit logs, and activity indicators to stay informed about what agents are doing
- **Third-party AI providers** — When using Claude, Codex, Gemini, or other providers through Nova, you must also comply with their respective terms of service and acceptable use policies
- **Emergency Stop exists for a reason** — If agent behavior is unexpected, use it
- **An armed interception rule stays your rule** — Nova shows it in the toolbar, binds it to one tab and a URL scope, and lets it expire by itself, but everything it does while armed is done on your behalf. Clear it when the task is over
- **Captured traffic can contain secrets** — headers and bodies may hold tokens, cookies and personal data, and they can reach an agent's transcript. Use `redact`, and treat a recording like the data it contains
- **An approved card payment is your purchase** — the approval covers exactly the card, shop, payment provider and agent shown in the dialog, and only for the time you chose. This does not transfer responsibility for defects in Nova's checks to you. Close the checkout tab when the purchase is done
- **A purchase budget is an approval in advance** — while it is on, agents may spend it without asking you, but only on what you asked them to buy. Nova lists every such purchase under Settings → Passwords → Purchase budget; set an amount you are comfortable with and switch it off when you do not need it. This does not transfer responsibility for defects in Nova's checks to you

### Alpha Risks and Mandatory Rights

Nova is alpha software; see the [technical risk notice](DISCLAIMER.md). Alpha status does not remove mandatory statutory warranty, update, consumer, or liability rights. The applicable license agreement governs contractual limitations; this policy creates no separate warranty or liability exclusion. See [EULA](EULA.md), sections 10 and 11.

---

## Deutsch

Diese Richtlinie beschreibt erlaubte Nutzung und Missbrauch von Nova AI Workspace. Vertragliche Folgen richten sich nach den wirksam mit dir vereinbarten Bedingungen; die Veröffentlichung dieser Seite ändert für sich genommen keinen bestehenden Vertrag. Nutzungsrechte, Mängelrechte, Haftung und Sperrverfahren stehen in der [EULA](EULA.md#deutsch).

### Autorisierte Prüfungen

Autorisierte Prüfungen setzen die ausdrückliche Genehmigung einer dazu befugten Person oder Stelle voraus. Systeme, Umfang, zulässige Verfahren und erforderlichenfalls Zeitgrenzen sind vor der Prüfung festzulegen. Zugangsdaten, eine vorhandene Sitzung oder ein technisch verfügbares Werkzeug erlauben keine Aktionen außerhalb dieses Rahmens.

### Erlaubte Nutzung

- Persönliches Browsen und Produktivität
- Autorisiertes Testen und Automatisieren eigener Websites und Dienste
- KI-Agenten-Workflows auf Websites, für die du ausdrückliche Erlaubnis hast oder deren Nutzungsbedingungen automatisierten Zugriff erlauben. Verlangt eine Seite wie Amazon, dass sich Agenten zu erkennen geben, lass deinen Agenten das mit der **Kennung für Agenten** tun (Einstellungen → Datenschutz & Sicherheit, ab Version 1.0.0-alpha.21)
  - Agenten können mit echten Tastatur- und Mauseingaben tippen, auswählen und klicken (`inputMode='keyboard'`, ab Version 1.0.0-alpha.21, noch nicht veröffentlicht), weil manche Seiten nur darauf reagieren. Damit funktioniert die Eingabe eines Agenten auf solchen Seiten; eine Erlaubnis der Seite ist das nicht. Ob automatisierte Nutzung dort erlaubt ist, entscheiden die Nutzungsbedingungen der Seite, und die prüfst du. Eine Kontoregel (`nova.account_rule`) hält Agenten in einem Tempo, das du wählst, und verhindert eine zweite Absendung; sie schützt dein Konto, sie macht automatisierte Nutzung nicht erlaubt.
- Forschung und Entwicklung innerhalb gesetzlicher Grenzen
- Anbindung MCP-kompatibler Tools und Agenten für legitime Zwecke
- Beobachten, Abfangen und erneutes Senden von Netzwerkverkehr eigener Websites und Dienste — bei Drittanbieterdiensten nur in einem Rahmen, den deren Betreiber schriftlich genehmigt hat
- Prüfen des TLS-Zertifikats und der TLS-Konfiguration eines Servers (`nova.tls_inspect`) — das, was jeder Server jedem Client zeigt, der sich verbindet. Die Prüfung umfasst einen Host pro Aufruf, bleibt in einem festen Handshake-Budget und greift den Server nicht an
- Scannen eigener Netze (`nova.net_scan`, ab Version 1.0.0-alpha.21, noch nicht veröffentlicht) — Heim- oder Büronetz, eigenes VPN, eigene Server —, um zu sehen, welche Geräte dort sind und welche Ports antworten. Fremde Netze nur mit Erlaubnis dessen, der sie betreibt
- Bezahlen mit deinen eigenen Zahlungskarten oder Karten, die du nutzen darfst, über einen Agenten (`nova.vault_card_fill`, ab Version 1.0.0-alpha.21, noch nicht veröffentlicht). Du gibst jede Füllung mit deiner Nova-PIN frei und den Klick auf den Bezahlknopf nur, wenn du ihn im selben Dialog ankreuzt; der Dialog nennt Karte, Shop und Zahlungsanbieter. Ob automatisierte Käufe in einem Shop erlaubt sind, entscheiden dessen Bedingungen
  - Innerhalb eines Einkaufsbudgets, das du in Novas Einstellungen festlegst und einschaltest (ab Version 1.0.0-alpha.21, noch nicht veröffentlicht), läuft ein Kauf eines Agenten, den das verbleibende Budget in seiner Währung deckt, ohne Dialog und ohne deine PIN. Was das Budget nicht deckt, und jeder Kauf, solange es aus ist, fragt dich wie bisher. Festlegen und auffüllen kannst nur du. Es ist eine Grenze, die Nova einhält, kein Limit deiner Karte oder deiner Bank

### Verbotene Nutzung

**Regel Nr. 1: Don't do bad.**

Du darfst Nova AI Workspace **nicht** verwenden für:

- **Gesetzes- oder Regelverstöße** — einschließlich Computerbetrug, Datenschutz (DSGVO, BDSG), Urheberrecht und Telekommunikationsrecht
- **Unbefugten Zugriff** — Zugang zu Systemen, Konten oder Daten ohne ausdrückliche Genehmigung, auch wenn technisch über Novas Werkzeuge möglich
- **Umgehung von Sicherheitsmaßnahmen** — Umgehen von Authentifizierung, CAPTCHAs, Rate Limits oder Zugangskontrollen von Drittanbietern, es sei denn, der Dienstanbieter hat dies ausdrücklich genehmigt
  - Novas Einstellung „Agenten dürfen Captchas beantworten“ (standardmäßig aus) erlaubt einem Agenten, ein Prüfkästchen selbst anzuklicken. Sie ist für eigene Dienste, Tests und Dienste gedacht, die das erlauben; sie ist keine Genehmigung des Dienstes. Prüfe vorher die Nutzungsbedingungen des Dienstes: viele verbieten automatisierte Zugriffe oder das Beantworten ihrer Prüfungen.
- **Daten-Scraping oder -Sammlung** unter Verstoß gegen Nutzungsbedingungen, robots.txt oder geltendes Recht einer Website
- **Verbreitung von Schadsoftware** — Nutzung von Novas Automation, MCP-Server oder Agentenfunktionen zur Erstellung, Verbreitung oder Bereitstellung von Malware
- **Spam oder Missbrauch** — Versand unerwünschter Nachrichten, Erstellung gefälschter Konten, Bewertungsmanipulation oder jede Form automatisierten Missbrauchs
- **Umgehen einer Sperre** — über ein Konto weiter handeln, das der Dienst gesperrt oder stillgelegt hat, oder dort ein weiteres Konto anlegen, um die Sperre zu umgehen, mit einem Agenten oder anders. Den Dienst wegen der Sperre zu kontaktieren ist selbstverständlich erlaubt. Sperrt Nova ein Konto, weil die Seite es gesperrt hat, kannst nur du die Sperre aufheben; kläre die Sache vorher mit dem Dienst über dessen offiziellen Weg
- **Identitätstäuschung** — Nutzung der Browser-Identitätsfunktionen zur betrügerischen Nachahmung anderer Personen oder Organisationen
- **Dienstverweigerungsangriffe** — Nutzung von Crawling, Automation oder Agentenfunktionen zur Überlastung oder Störung von Drittanbieterdiensten
- **Überwachung** — Nutzung von Novas Fähigkeiten zur Beobachtung, Verfolgung oder Überwachung von Personen ohne gültige Rechtsgrundlage oder rechtmäßige Befugnis
- **Schädigung oder Belästigung** — Nutzung von KI-Agentenfunktionen zur Erzeugung schädlicher, missbräuchlicher, bedrohlicher oder belästigender Inhalte
- **Credential-Missbrauch** — Nutzung von Novas Vault oder MCP-Tools zum Testen gestohlener Zugangsdaten oder für Credential-Stuffing-Angriffe
- **Manipulation des Verkehrs fremder Dienste** — Nutzung von Abfangen, Verändern oder absichtlichem Scheiternlassen von Anfragen, um Bezahlung, Lizenzierung, Kontingente, clientseitige Prüfungen, Zustimmungsdialoge oder Sicherheitsmechanismen eines Dienstes zu umgehen, den du weder betreibst noch zu testen befugt bist
- **Erneutes Senden ohne Befugnis** — aufgezeichnete Anfragen erneut senden, auch unter einer Sitzung, die Nova wiederverwenden kann, gegen einen Dienst, der das nicht genehmigt hat. Dass Nova deine Sitzung technisch wiederverwenden kann, ist keine Erlaubnis des Dienstes
- **Speichern von Videos ohne Recht dazu** — mit „Video speichern" ein Video kopieren, das offensichtlich rechtswidrig hochgeladen wurde, oder ein gespeichertes Video ohne Erlaubnis des Rechteinhabers weitergeben oder veröffentlichen. Eine Privatkopie ist nur erlaubt, soweit das Urheberrecht an deinem Wohnort sie erlaubt. Nova lehnt verschlüsselte und kopiergeschützte Videos ab; umgehe diesen Schutz nicht mit anderen Werkzeugen
- **Aufnehmen von Personen ohne Rechtsgrundlage** — Bildschirmaufnahmen von Videoanrufen, Besprechungen oder anderen Personen auf einer Seite ohne deren Einwilligung oder eine andere Rechtsgrundlage. Nova schaltet den Ton stumm, solange eine Seite das Mikrofon nutzt; das Bild eines Gesprächs und seiner Teilnehmer wird trotzdem aufgenommen
- **Scannen fremder Netze ohne Erlaubnis** — ein Netz oder einen Adressbereich scannen, den du weder betreibst noch prüfen darfst, etwa am Arbeitsplatz ohne Zustimmung der IT, im Hotel oder in einem öffentlichen WLAN, oder einen Scan nutzen, um den Zugriff auf fremde Systeme vorzubereiten. Die Freigabe in Nova bestätigt nur, dass der Scan laufen soll; sie ist keine Erlaubnis des Netzbetreibers
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
- **Eine freigegebene Kartenzahlung ist dein Kauf** — die Freigabe gilt genau für Karte, Shop, Zahlungsanbieter und Agent aus dem Dialog und nur für die Zeit, die du gewählt hast. Die Verantwortung für Fehler in Novas Prüfungen geht dadurch nicht auf dich über. Schließe den Checkout-Tab, wenn der Kauf erledigt ist
- **Ein Einkaufsbudget ist eine Freigabe im Voraus** — solange es an ist, dürfen Agenten es ohne Rückfrage ausgeben, aber nur für das, was du ihnen zu kaufen aufgetragen hast. Nova führt jeden solchen Kauf unter Einstellungen → Passwörter → Einkaufsbudget auf; wähle einen Betrag, mit dem du gut leben kannst, und schalte es aus, wenn du es nicht brauchst. Die Verantwortung für Fehler in Novas Prüfungen geht dadurch nicht auf dich über

### Alpha-Risiken und zwingende Rechte

Nova ist Alpha-Software; siehe die [technischen Risikohinweise](DISCLAIMER.md). Der Alpha-Status beseitigt keine zwingenden gesetzlichen Mängel-, Aktualisierungs-, Verbraucher- oder Haftungsrechte. Vertragliche Grenzen richten sich nach der anwendbaren Lizenzvereinbarung; diese Richtlinie enthält keinen eigenständigen Gewährleistungs- oder Haftungsausschluss. Siehe [EULA](EULA.md#deutsch), Abschnitte 10 und 11.
