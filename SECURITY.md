# Security Policy · Sicherheitsrichtlinie

## Reporting a vulnerability (EN)

Report **security vulnerabilities privately** using GitHub's
[Report a vulnerability form](https://github.com/joelaniol/nova/security/advisories/new).
Private vulnerability reporting is enabled for this repository.

Please do not publish vulnerabilities, exploit details, or secrets in a public issue.
Include what you found, how to reproduce it, the affected Nova version (Settings → About),
and the potential impact. During the alpha there is no fixed response-time commitment.

### Bugs, crashes, and work-session feedback

For ordinary defects and feedback, ask your agent to call
`nova.get_instructions(topic='bug_report')`. [Nova's reporting guide](docs/mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md)
provides rules and draft templates. It does not collect logs or submit a report automatically:
the agent shows you the draft and submits it only with your approval.

Without an agent, use the [bug report](https://github.com/joelaniol/nova/issues/new?template=bug-report.yml),
[crash report](https://github.com/joelaniol/nova/issues/new?template=crash-report.yml), or
[work-session feedback](https://github.com/joelaniol/nova/issues/new?template=feedback.yml) form.
These issues are public: review URLs, screenshots, and log excerpts for secrets and personal data.
See [what to report during alpha](ALPHA.md#what-to-report), including known GUI limitations.
Security vulnerabilities always belong in the private form above.

## Sicherheitslücke melden (DE)

Melde **Sicherheitslücken privat** über GitHubs
[„Report a vulnerability“-Formular](https://github.com/joelaniol/nova/security/advisories/new).
Privates Vulnerability-Reporting ist für dieses Repository aktiviert.

Veröffentliche Sicherheitslücken, Exploit-Details oder Geheimnisse bitte nicht als öffentliches Issue.
Beschreibe Fund, Reproduktion, betroffene Nova-Version (Einstellungen → Info) und mögliche Auswirkungen.
Während der Alpha gibt es keine feste Reaktionszeit-Zusage.

### Bugs, Abstürze und Arbeitsfeedback

Bitte deinen Agenten, `nova.get_instructions(topic='bug_report')` aufzurufen.
[Novas Meldeanleitung](docs/mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md) liefert Regeln und Entwurfsvorlagen.
Sie sammelt keine Logs und sendet keine Meldung automatisch: Der Agent zeigt dir den Entwurf
und sendet ihn nur mit deiner Zustimmung.

Ohne Agenten nutze das [Fehler-Formular](https://github.com/joelaniol/nova/issues/new?template=bug-report.yml),
[Absturz-Formular](https://github.com/joelaniol/nova/issues/new?template=crash-report.yml) oder
[Feedback-Formular](https://github.com/joelaniol/nova/issues/new?template=feedback.yml).
Diese Issues sind öffentlich: Prüfe URLs, Screenshots und Logauszüge auf Geheimnisse und persönliche Daten.
Siehe [was während der Alpha gemeldet werden soll](ALPHA.md#was-bitte-melden), einschließlich bekannter GUI-Einschränkungen.
Sicherheitslücken gehören immer ins private Formular oben.
