# Nova Demo Lab

Stand: 2026-09-20

Eine Seite zum Vorführen — gebaut für Videoaufnahmen und für den ersten Eindruck bei jemandem, der
Nova noch nicht kennt. Sie läuft **ohne Server**: `demos/lab.html` im Browser öffnen, fertig.

```
dist\NovaBrowser.exe          # Nova starten
# dann im Agenten:
nova.navigate url="file:///E:/-=Entwicklung=-/NovaBrowser/demos/lab.html"
```

## Wozu das Ganze

Ein Feature-Poster überzeugt niemanden. Was überzeugt, ist eine Aufgabe, an der übliche
Browser-Automatisierung sichtbar scheitert, gefolgt davon, dass Nova sie erledigt. Jede Sektion
hier ist genau so ein Fall — keine erfundene Schwierigkeit, sondern die, an denen echte Läufe
hängenbleiben.

Unten auf der Seite läuft ein **Aktivitätsstreifen** mit. Er macht im Video sichtbar, dass wirklich
etwas passiert ist, statt dass nur ein Cursor zuckt. Derselbe Verlauf liegt als
`window.novaDemoLog` bereit — aber nur mit `worldMode: "main"`:

```
nova.eval expression="JSON.stringify(window.novaDemoLog.map(e => e.what))" worldMode="main"
```

Ohne `worldMode` läuft `eval` in einer isolierten Welt und bekommt eine **leere Liste** zurück, ohne
zu meckern. Das ist beim Bauen dieser Seite passiert und wäre in einer Aufnahme peinlich.

## Die acht Fälle

Die Spalte rechts ist **nachgemessen**, nicht angenommen — jeder Weg wurde am 20.09.2026 gegen
diese Seite ausgeführt.

| Reiter | Was schwer daran ist | Der Weg, der funktioniert |
|---|---|---|
| **Session** | Ein frischer Lauf startet immer abgemeldet. | Einmal anmelden (`demo`/`nova`); die Sitzung übersteht Reload und Navigation. Zustand lesen mit `nova.storage_inspect(storageType='local')`. |
| **Deep list** | 10 000 Zeilen, ~12 im DOM. `#row-8472` existiert nicht, bis jemand dorthin scrollt. | `nova.scroll_element(selector='#vlist', deltaY=288000)` — der Container scrollt, nicht die Seite. Danach ist die Zeile da und `nova.wait_for_selector` greift. |
| **Hidden DOM** | Zwei verschachtelte Shadow Roots und ein Frame. | **`nova.click_selector` findet `#deepBtn` NICHT** — es durchdringt keine Shadow Roots und läuft in einen Timeout. Der Weg: `nova.eval(includeShadow=true)` liefert das Rechteck, dann `nova.input_click` auf dessen Mitte. Das Frame-Formular ist über `frameScope`/`frameId` erreichbar. |
| **Gestures** | Ziehen ist eine Folge echter Zeigerereignisse an echten Koordinaten. Ein `click` bewegt nichts. | Mittelpunkte per `eval` holen, dann `nova.input_drag(fromX, fromY, toX, toY)`. Hat die Karte zuverlässig nach DONE gelegt. |
| **Files** | Der Dateidialog gehört dem Betriebssystem, nicht der Seite. Ein Download muss irgendwo landen. | `nova.file_upload` umgeht den OS-Dialog; `nova.downloads_wait` + `nova.downloads_list` belegen die erzeugte CSV. |
| **Dialogs** | `alert`/`confirm`/`prompt` halten den Seitenthread an; Consent-Wall und Modal fressen jeden Klick. | **Nova beantwortet JS-Dialoge selbst** (sie werden abgewiesen) und läuft weiter — `nova.ui_inspect_native_dialog` findet hier nichts, das Tool ist für **OS- und Nova-eigene** Dialoge. Genau das ist der Punkt: ein Skript ohne Dialog-Handler bleibt hier stehen, Nova nicht. Consent-Wall und Modal sind normale Overlays: `nova.cmp_apply` bzw. `nova.dismiss_blockers`. |
| **Timing** | Die Wartezeit ist unbekannt, und ein Wert rendert zweimal. Ein fester Sleep ist entweder zu kurz oder verschenkt. | `nova.wait_for_selector` auf `#lateBtn`, `nova.wait_for_eval` für den zweiten Wert. |
| **Data** | Die Tabelle will strukturiert raus, und der Canvas-Code existiert nur als Pixel. | `nova.extract_table(selector='#dataTable')`. Für den Canvas: `nova.capture_screenshot(selector='#pixelCanvas')` — der Code **NV-4831** ist nur im Bild lesbar, kein Selektor gibt ihn je zurück. |

## Vorschlag für den Videoablauf

Kurz halten. Ein Fall, den jeder kennt, dann zwei, die wehtun.

1. **Der Haken im Bild (20 s).** Adressleiste zeigt `lab.html`, Agentenpanel daneben. Eine Aufgabe
   stellen: *„Melde dich an, hol Build 8472 aus der Liste und zieh 'Deploy release' nach Done."*
2. **Zuschauen (40 s).** Der Aktivitätsstreifen schreibt mit. Nichts kommentieren — das Mitlaufen
   ist das Argument.
3. **Der Beweis (15 s).** Seite neu laden. Immer noch angemeldet. Das ist der Moment, den ein
   Headless-Lauf nicht hat.
4. **Die Zugabe (20 s).** Den Canvas-Code vorlesen lassen. Kein Selektor der Welt findet ihn.

Insgesamt unter zwei Minuten. Wer danach mehr will, klickt auf Releases.

## Grenzen

- **`file://` reicht für alles hier.** Der Frame nutzt `srcdoc`, damit er ohne Server funktioniert;
  eine echte fremde Herkunft (cross-origin) ist damit **nicht** abgedeckt. Dafür gibt es
  `tests/evil-pages/` mit zwei Ursprüngen und einem Server.
- **Die Wartezeiten sind zufällig** (2–6 s), damit man sie nicht auswendig lernen kann. Für eine
  Aufnahme, die exakt sitzen muss, ist das eher unbequem — dann lieber zweimal drehen als die
  Zufälligkeit rausnehmen, sonst beweist die Sektion nichts mehr.
- **Kein Netzwerkverkehr.** Die Seite lädt nichts nach. Wer `nova.network_read` oder
  `network_intercept` zeigen will, braucht eine Seite, die wirklich etwas anfragt.
- **Die Tabelle scrollt auf schmalen Fenstern seitwärts**, in ihrem eigenen Container. Das ist
  Absicht und die einzige Stelle, die breiter als der Inhaltsbereich wird; die Seite selbst hat bei
  390 px keinen horizontalen Scroll (`pageHorizontalScroll: false`, gemessen).

## Wenn etwas nicht klappt

- **Die Liste zeigt nur eine Handvoll Zeilen.** Sie rendert nach der sichtbaren Höhe. War der
  Reiter beim Laden versteckt, ist die Höhe 0 — ein `ResizeObserver` holt das nach, sobald der
  Reiter sichtbar wird. Wenn es doch einmal klemmt: Reiter wechseln oder neu laden.
- **`#deepBtn` wird nicht gefunden.** Richtig so, siehe Tabelle: erst `eval(includeShadow=true)`
  für das Rechteck, dann `input_click`.
- **`novaDemoLog` ist leer.** `worldMode: "main"` fehlt.
- **Der Aktivitätsstreifen bleibt stumm, obwohl etwas passiert ist.** Er protokolliert nur, was
  durch die Seite läuft. Ein `eval`, das einen Wert direkt setzt, umgeht ihn — und genau deshalb
  taugt er als Beweis: was dort steht, ist wirklich über die Oberfläche gegangen.
