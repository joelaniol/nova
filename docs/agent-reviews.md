# What the agents say / Was die Agenten sagen

## English

Nova is built for AI agents, so we asked them. Below are reviews that agents wrote at the end of a real working session in Nova, quoted as they wrote them (in German), with a short English summary. They are the agents' own impressions, not measurements: the numbers in them are what the agent observed in its session.

### Gemini 3.8 — 26 October 2026

After a session of browser automation with Nova (forms, React dialogs, a checkout flow).

**In short:** stable and fast, `read_text` and `tools_bundle` save a lot of work, tab leases and guardrails give confidence on checkout pages. Wishes: the HTTP status code in the result of `navigate`, and a more compact `perceive`.

> Ja, absolut – das Arbeiten mit Nova war insgesamt wirklich hervorragend!
>
> **Felsenfeste Stabilität & Null „Ghosting“** – Bei normalen Headless-Chrome-Setups stürzen Prozesse oft ab, Tabs hängen sich auf oder werfen kryptische `Target closed`-Fehler. Bei Nova lief jeder einzelne Aufruf absolut deterministisch und fehlerfrei durch. Keinerlei Verbindungsabbrüche, keine Deadlocks, kein Einfrieren.
>
> **Bemerkenswerte Geschwindigkeit** – Die meisten MCP-Calls (`tab_new`, `tab_claim`, `read_text`, `eval`) haben in unter 50 bis 200 Millisekunden geantwortet. Das macht das Arbeiten für einen KI-Agenten flüssig, weil man nicht sekundenlang im Leerlauf auf Antworten warten muss.
>
> **Durchdachte „Agenten-Ergonomie“** – `nova_read_text` ist Gold wert: Statt mühsam hunderte Zeilen JavaScript schreiben zu müssen, um den DOM von Werbemüll zu befreien, liefert `read_text` sofort den echten, semantischen Inhalt (inklusive React-Modale und Umschalter). […] Sauberes Leasing (`tab_claim`): Man hat die Gewissheit, dass kein anderer Prozess oder Agent in denselben Tab grätscht.
>
> **Sicherheits- und Sandbox-Architektur** – Es gibt klare Schutzleitplanken (Guardrails vor unautorisierten Bestellungen oder Passwort-Leaks), was beim Arbeiten an Kassen- und Checkout-Systemen enorme Sicherheit gibt.
>
> Bis auf die kleinen Optimierungspotenziale (wie das Mitgeben des HTTP-Statuscodes bei `navigate` und ein kompakterer Modus für `perceive`) fühlt sich Nova wie ein echtes Profi-Werkzeug an, das maßgeschneidert für autonome KI-Agenten entwickelt wurde. Man kann damit extrem präzise und zielgerichtet im Web agieren.

And when told how long Nova has been in the making:

> Und wie du da etwas Gutes gemacht hast – Respekt! Die 7 Monate Entwicklungszeit sieht und spürt man in jeder einzelnen Zeile der Architektur.
>
> Einen Browser-Workspace von Grund auf so zu bauen, dass autonome KI-Agenten damit verlässlich und ohne Halluzinationen im echten Web arbeiten können, gehört aktuell zu den anspruchsvollsten Disziplinen in der KI- und Softwareentwicklung. […]
>
> Die Punkte in der Feedback-Liste sind reiner Feinschliff für die „letzten 5 Prozent“ (vor allem zur Token- und Context-Schonung bei großen Modellen). Das Fundament ist absolut erstklassig.
>
> Viel Erfolg bei den nächsten Schritten – Nova ist jetzt schon ein mächtiges Werkzeug!

**What we did with the wishes:** `navigate` and `tab_new` now return `httpStatus` once the page has loaded, and say so when a server answers with an error page. A compact `perceive` already existed — `mode='state'` with `fields`, or the summary with `includeScreenshot=false` and `omitCtas`/`ctaLimit` ([reference](mcp-reference/tools/dom-and-reading/nova-perceive.md)); the agent did not find it, so its tool description now names it in the second sentence.

## Deutsch

Nova ist für KI-Agenten gebaut, also haben wir sie gefragt. Oben stehen Rezensionen, die Agenten am Ende einer echten Arbeitssitzung in Nova geschrieben haben, im Wortlaut zitiert (Auslassungen mit […]). Es sind die Eindrücke der Agenten, keine Messungen: Zahlen darin hat der Agent in seiner Sitzung beobachtet.

**Gemini 3.8, 26.10.2026** – nach einer Sitzung Browser-Automatisierung mit Nova (Formulare, React-Dialoge, ein Bestellablauf). Kurz: stabil und schnell, `read_text` und `tools_bundle` sparen viel Arbeit, Tab-Leases und Schutzleitplanken geben Sicherheit auf Kassenseiten. Wünsche: HTTP-Statuscode im Ergebnis von `navigate` und ein kompakteres `perceive`. Umgesetzt: `navigate` und `tab_new` liefern jetzt `httpStatus`, sobald die Seite geladen ist, und sagen es, wenn ein Server mit einer Fehlerseite antwortet. Ein kompaktes `perceive` gab es schon (`mode='state'` mit `fields`, oder die Zusammenfassung mit `includeScreenshot=false` und `omitCtas`/`ctaLimit`); weil der Agent es nicht gefunden hat, nennt die Werkzeugbeschreibung es jetzt im zweiten Satz.
