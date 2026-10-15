# EXP-028: Differential Pulse Survival & Signal Propagation Audit (C3 vs. C5)

**Status:** Completed & Empirically Verified (ADR-032)  
**Evidence Tier:** `[EMPIRICAL-SIGNAL-AUDIT]` / `[NUMERICAL-DETERMINISTIC]`  
**Wissenschaftliche Einordnung:** Deterministisches 5-Stufen-Signal-Audit zur lückenlosen Aufklärung des transienten Informationsverlusts aus EXP-027 (C3 Okklusions-Baseline vs. C5 gepulster Zwilling). Keine ungemessenen Spekulationen; alle Werte basieren auf exakten Pixel-Arrays der gerenderten Quelldaten.

---

## 1. Executive Summary & Kernergebnisse

In **EXP-027** wurde der $250\,\text{ms}$ dauernde Helligkeitspuls (Luminanz-Transiente, emissives Weiß, Sinus-Hüllkurve bei $t = 2{,}65\text{--}2{,}90\,\text{s}$) in Clip C5 von allen verblindeten Evaluatoren über alle experimentellen Formate hinweg vollständig übersehen (**Sensitivität = 0,0 %**).

Da bei 16 FPS die Abtastframes 43, 44, 45 und 46 direkt im Pulsfenster liegen (Frame 44 bei $t = 2{,}75\,\text{s}$ liegt nahe dem Hüllkurven-Maximum von $95{,}1\,\%$), war die Ursache kein zeitliches Abtastloch.

**EXP-028** trennt den physikalischen/numerischen Informationsverlust in der Signalverarbeitungskette von nachgelagerten Wahrnehmungs- und Aufmerksamkeitsgrenzen des Vision-Encoders.

### Die zwei Kernbefunde:

1. **Physischer Signal-Kollaps im E3-K12 Visual Carrier (Verlustursache identifiziert):**
   - **DC-Sättigungs-Kollaps:** Durch die statische Zentrierung um $-128$ bei sehr dunklem Hintergrund (`#0a0d14`, $Y \approx 11{,}5$) sinkt die unmodulierte Projektion $M_0$ auf $-984$ bis $-530$. Bei einer Skalierungsdivision durch $35{,}0$ wird $M_0 / 35{,}0$ über das gesamte Bild hinweg auf $-1{,}0$ hart geclippt (**100,0 % Sättigung bei Pixelwert 38 im Rotkanal von Quadrant T**). Die DC-Luminanzenergie des Pulses ($\Delta M_0 = +44{,}75$) wurde vollständig in der Klipping-Grenze vernichtet!
   - **Walsh-Energiedispersion:** Die verbleibende AC-Pulsenergie verteilte sich auf 11 orthogonale Moden ($k=1..11$), wodurch der maximale Pixeldeltabetrag im unkomprimierten Träger von $101{,}0$ auf $38{,}0$ gedämpft wurde.
   - **WebP-Quantisierungsvernichtung:** Die verlustbehaftete WebP-Kompression ($Q=80$) reduzierte die verbliebenen hochfrequenten Walsh-Muster von $38{,}0$ auf **$13{,}0$**, während sie zeitgleich Blockartefakte mit bis zu **$20{,}0$** Delta in benachbarten Quadranten erzeugte. Im komprimierten Carrier war das Signal **physikalisch unter den Rauschteppich versunken ($\text{SNR} < 0\,\text{dB}$)**.

2. **Perzeptiver / Attentionaler Verlust im Kontaktbogen (Signal intakt):**
   - Im hochauflösenden Kontaktbogen (**`GRID512_WEBP`**) überlebte der Puls in Kachel 11 (Frame 44) mit enormer physikalischer Amplitude: **$\text{ROI\_MAX\_DELTA} = 109{,}0$**, Peak-RGB stieg von $[76, 78, 82]$ auf $[185, 186, 190]$, und der Weber-Kontrast stieg um **$+40\,\%$** ($\Delta \text{Weber} = +0{,}40$).
   - Im pixel-gematchten Kontaktbogen (**`GRID128_WEBP`**) betrug das Delta in Kachel 11 noch immer **$98{,}0$**!
   - **Schlussfolgerung:** Im Kontaktbogen lag **kein Signalverlust** vor. Das Übersehen durch das VLM war ein rein kognitiver/attentionaler Filtereffekt: Auf einem einzelnen Bild eines 16-teiligen Kontaktbogens wurde die isolierte Kugelaufhellung als normale 3D-Schattierung/Glanzlicht interpretiert, anstatt als transientes Zeitereignis.

---

## 2. Die 5-Stufen Signalübertragungs-Tabelle

| Stufe / Format | Repräsentation & Auflösung | ROI MAE | ROI Max Delta | C3-C5 Equal (%) | Delta Weber Kontrast | Delta Michelson |
|---|---|---|---|---|---|---|
| **Stage 0: 1080p Ground Truth** | Unkomprimiert 1080p RGB (Frame 44) | **19,1150** | **118,0** | 55,6 % | **+1,66** | +0,070 |
| **Stage 1: 64x64 Resampled** | BOX (Area) Downsampling (Frame 44) | **23,6343** | **101,0** | 37,5 % | **+2,07** | +0,065 |
| **Stage 2: GRID512 Contact Sheet** | 4x4 Grid $512 \times 512$ WebP (Cell 11) | **5,1423** | **109,0** | 63,2 % | **+0,40** | +0,067 |
| **Stage 2: GRID128 Contact Sheet** | 4x4 Grid $128 \times 128$ WebP (Cell 11) | **6,6889** | **98,0** | 38,9 % | **+0,37** | +0,071 |
| **Stage 3: E3-K12 Visual Carrier** | $128 \times 128$ Lossless PNG (Quad T) | **1,9352** | **38,0** | 54,2 % | -0,01 | +0,008 |
| **Stage 4: E3-K12 Visual Carrier** | $128 \times 128$ Lossy WebP Q80 (Quad T) | **3,0556** | **13,0** | 8,3 % | -0,01 | +0,005 |

---

## 3. Zeitliche Detailanalyse der 4 Pulsframes (16 FPS)

Die KinetiCraft/SwiftClip Physik-Engine erzeugte den Puls mit einer theoretischen Sinushüllkurve über $250\,\text{ms}$ ($t \in [2{,}65, 2{,}90]\,\text{s}$):
$$\text{Envelope}(t) = \sin\left(\pi \frac{t - 2{,}65}{0{,}25}\right)$$

| Frame | Zeitstempel ($t$) | Theor. Hüllkurve | 1080p ROI Max Delta | 1080p ROI MAE | 1080p Delta Weber |
|---|---|---|---|---|---|
| **Frame 43** | $2{,}6875\,\text{s}$ | $0{,}4540$ | $117{,}0$ | $17{,}4375$ | $+1{,}51$ |
| **Frame 44** | $2{,}7500\,\text{s}$ (Peak) | **$0{,}9511$** | **$118{,}0$** | **$19{,}1150$** | **$+1{,}66$** |
| **Frame 45** | $2{,}8125\,\text{s}$ | $0{,}8910$ | $120{,}0$ | $19{,}0834$ | $+1{,}66$ |
| **Frame 46** | $2{,}8750\,\text{s}$ | $0{,}3090$ | $110{,}0$ | $16{,}3435$ | $+1{,}42$ |

Die Messung beweist: Alle vier Abtastzeitpunkte tragen hochenergetische Luminanzsignale mit Delta-Werten über 110 LSB.

---

## 4. Spektrale Gram-Moden-Zerlegung & Sättigungsanalyse

Die zeitliche Gram-Projektion $M_k = \sum_{t=0}^{63} (Y(t) - 128) \cdot P_k(t)$ verteilt die Energie über 12 orthogonale Basispolynome:

| Modus ($k$) | Mathematische Basisfunktion | ROI Max Delta | Full Max Delta | $L_2$-Energie $||\Delta M_k||$ | Sättigung in C3 Baseline |
|---|---|---|---|---|---|
| **$k=00$** | **$P_0$ (DC-Mittelwert)** | **$44{,}75$** | **$44{,}75$** | **$143{,}30$** | **100,0 % (Vollständig geclippt)** |
| **$k=01$** | $P_1$ (Linearer Trend / Drift) | $31{,}31$ | $31{,}31$ | $100{,}72$ | $3{,}4\,\%$ |
| **$k=02$** | $P_2$ (Quadratische Krümmung / Bimodalität) | $25{,}37$ | $25{,}37$ | $80{,}74$ | $3{,}4\,\%$ |
| **$k=03$** | Walsh Subcarrier 1 ($k=3$, Odd) | $51{,}86$ | $51{,}86$ | $166{,}27$ | $3{,}2\,\%$ |
| **$k=04$** | Walsh Subcarrier 2 ($k=4$, Even) | $16{,}64$ | $16{,}64$ | $53{,}75$ | $3{,}4\,\%$ |
| **$k=05$** | Walsh Subcarrier 3 ($k=5$, Odd) | $38{,}46$ | $38{,}46$ | $122{,}32$ | $3{,}2\,\%$ |
| **$k=06$** | Walsh Subcarrier 4 ($k=6$, Even) | $46{,}85$ | $46{,}85$ | $151{,}01$ | $3{,}0\,\%$ |
| **$k=07$** | Walsh Subcarrier 5 ($k=7$, Odd) | $5{,}24$ | $5{,}24$ | $14{,}30$ | $2{,}6\,\%$ |
| **$k=08$** | Walsh Subcarrier 6 ($k=8$, Even) | $46{,}17$ | $46{,}17$ | $147{,}02$ | $2{,}4\,\%$ |
| **$k=09$** | Walsh Subcarrier 7 ($k=9$, Odd) | $37{,}22$ | $37{,}22$ | $120{,}89$ | $2{,}2\,\%$ |
| **$k=10$** | Walsh Subcarrier 8 ($k=10$, Even) | $16{,}74$ | $16{,}74$ | $49{,}57$ | $1{,}9\,\%$ |
| **$k=11$** | Walsh Subcarrier 9 ($k=11$, Odd) | $48{,}31$ | $48{,}31$ | $154{,}38$ | $1{,}6\,\%$ |

### Mathematische Diagnose des DC-Kollapses:
- Da der Hintergrund schwarz ist ($Y \approx 11{,}5$), ergibt $Y - 128 \approx -116{,}5$.
- Für $N=64$ ist $P_0(t) = 1/\sqrt{64} = 0{,}125$.
- Das zeitliche Integral für statischen Hintergrund ergibt: $M_0 = 64 \cdot (-116{,}5) \cdot 0{,}125 = -932{,}0$.
- Der Codec normalisiert mit: $m_0 = \text{clip}(M_0 / 35{,}0, -1{,}0, 1{,}0)$.
- $-932{,}0 / 35{,}0 = -26{,}63 \ll -1{,}0$.
- **Folge:** Der Kanalwert im Rotkanal von Quadrant T lautet: $128 + (-1{,}0) \cdot 90 = 38{,}0$ für jeden einzelnen Pixel des Hintergrunds und der Kugelbahn.
- Als der Puls in C5 die Helligkeit um $\Delta M_0 = +44{,}75$ erhöhte, stieg der Rohwert von $-932{,}0$ auf $-887{,}25$.
- Nach Division durch $35{,}0$ ergab dies $-25{,}35$, was **weiterhin hart auf $-1{,}0$ begrenzt** wurde!
- **Delta im Rotkanal des Carriers = exakt 0,00.**

---

## 5. WebP-Quantisierungs- & Artefakt-Analyse

In Quadrant T (Temporal Kinematics) und Quadrant C (Chrominance) wird die AC-Energie auf 2D-Walsh-Muster aufmoduliert.
In der verlustfreien PNG-Datei erzeugt dies eine gut messbare Signatur mit maximalem Delta von **$38{,}0$**.

Bei der WebP-Kompression ($Q=80$) bricht diese Struktur ein:
- **Quadrant T (Temporale Kugelregion):** Maximales Delta fällt von $38{,}0$ auf **$13{,}0$**.
- **Quadrant G (Statischer Basiszustand t=0):** C3 und C5 sind bei $t=0$ bit-identisch. Trotzdem entstehen in WebP durch blockübergreifende Prädiktionsfehler Differenzen von bis zu **$20{,}0$** ($10{,}5\,\%$ verrauschte Pixel)!
- **Quadrant C (Chrominanz):** Differenzen von bis zu **$16{,}0$** ($16{,}4\,\%$ verrauschte Pixel).
- **Quadrant R (Neutralgrau 128):** Bleibt absolut rauschfrei ($0{,}0$ Delta).

**Ergebnis:** Das verbliebene Nutzkignal ($13{,}0$) ist kleiner als das durch WebP eingebrachte Kompressionsrauschen ($16\text{--}20$).

---

## 6. Wissenschaftliche Konsequenzen & Nächste Schritte

1. **E3-K12 Codec-Verbesserung (für Phase B):**
   - **Adaptive Hintergrund-Zentrierung:** Statt statischem $-128$ muss die Basiszustands-Luminanz $Y_0$ subtrahiert werden: $Y(t) - Y_0$. Dadurch wird $M_0$ für statischen Hintergrund exakt $0{,}0$ und Sättigung wird verhindert.
   - **Dynamische Skalierung:** Ein adaptiver Skalierungsfaktor oder ein erweiterter Dynamikbereich (z. B. $S = \max(35{,}0, \text{std}(M))$) schützt kontrastreiche Szenen vor dem Übersteuern.
   - **Lossless / High-Q Carrier:** WebP mit höherer Qualität ($Q \ge 95$) oder verlustfreies PNG verhindert die Zerstörung hochfrequenter Walsh-Subcarrier.

2. **Perzeptiver Versuchsaufbau für Kontaktbögen:**
   - Wenn ein Modell Helligkeitsblitze auf Kontaktbögen erkennen soll, benötigt es entweder einen expliziten Differenzkontrast-Kanal oder eine auf temporale Anomalien ausgerichtete Aufmerksamkeitsführung (Prompt-Design).

---

## 7. Archivierte Artefakte

Alle generierten Differenzkarten und Rohmetriken sind reproduzierbar hinterlegt:
- Metriken: [`pulse_survival_metrics.json`](pulse_survival_metrics.json)
- Zusammenfassung: [`summary_table.md`](summary_table.md)
- Heatmaps:
  - 1080p Frame 44: [`diff_maps/diff_stage0_1080p_f44.png`](diff_maps/diff_stage0_1080p_f44.png)
  - 64x64 Frame 44: [`diff_maps/diff_stage1_64x64_f44.png`](diff_maps/diff_stage1_64x64_f44.png)
  - Contact Sheet 128: [`diff_maps/diff_stage2_grid128.png`](diff_maps/diff_stage2_grid128.png)
  - Contact Sheet 512: [`diff_maps/diff_stage2_grid512.png`](diff_maps/diff_stage2_grid512.png)
  - Visual Carrier Raw: [`diff_maps/diff_stage3_carrier_raw.png`](diff_maps/diff_stage3_carrier_raw.png)
  - Visual Carrier PNG: [`diff_maps/diff_stage3_carrier_png.png`](diff_maps/diff_stage3_carrier_png.png)
  - Visual Carrier WebP: [`diff_maps/diff_stage4_carrier_webp.png`](diff_maps/diff_stage4_carrier_webp.png)
  - Gram-Moden-Spektrum: [`diff_maps/gram_modes_energy_spectrum.png`](diff_maps/gram_modes_energy_spectrum.png)
