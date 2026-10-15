# EXP-028: Differential Pulse Survival & Signal Propagation Audit (C3 vs. C5)

**Status:** Completed & Empirically Verified (ADR-032 & ADR-033)  
**Evidence Tier:** `[EMPIRICAL-SIGNAL-AUDIT]` / `[NUMERICAL-DETERMINISTIC]`  
**Wissenschaftliche Einordnung:** Zweistufiges deterministisches Signal-Audit (Phase A: Ursachenanalyse; Phase B: Experimenteller E4-Y0-Gegenversuch) zur lückenlosen Aufklärung des transienten Informationsverlusts aus EXP-027 (C3 Okklusions-Baseline vs. C5 gepulster Zwilling). Alle Messwerte basieren auf exakten Pixel-Arrays der gerenderten Quelldaten.

---

## 1. Executive Summary & Kernergebnisse

In **EXP-027** wurde der $250\,\text{ms}$ dauernde Helligkeitspuls (Luminanz-Transiente, emissives Weiß, Sinus-Hüllkurve bei $t = 2{,}65\text{--}2{,}90\,\text{s}$) in Clip C5 von allen verblindeten Evaluatoren über alle experimentellen Formate hinweg vollständig übersehen (**Sensitivität = 0,0 %**).

Da bei 16 FPS die Abtastframes 43, 44, 45 und 46 direkt im Pulsfenster liegen (Frame 44 bei $t = 2{,}75\,\text{s}$ liegt nahe dem Hüllkurven-Maximum von $95{,}1\,\%$), war die Ursache kein zeitliches Abtastloch.

**EXP-028** trennt den physikalischen/numerischen Informationsverlust in der Signalverarbeitungskette von nachgelagerten Wahrnehmungs- und Aufmerksamkeitsgrenzen des Vision-Encoders:

### Die drei Kernbefunde:

1. **Physischer Signal-Kollaps im E3-K12 Visual Carrier (Verlustursache identifiziert):**
   - **DC-Sättigungs-Kollaps:** Durch die statische Zentrierung um $-128$ bei sehr dunklem Hintergrund (`#0a0d14`, $Y \approx 11{,}5$) sinkt die unmodulierte Projektion $M_0$ auf $-984$ bis $-530$. Bei einer Skalierungsdivision durch $35{,}0$ wird $M_0 / 35{,}0$ über das gesamte Bild hinweg auf $-1{,}0$ hart geclippt (**100,0 % Sättigung bei Pixelwert 38 im Rotkanal von Quadrant T**). Die DC-Luminanzenergie des Pulses ($\Delta M_0 = +44{,}75$) wurde vollständig in der Klipping-Grenze vernichtet (Delta im Rotkanal des lossless Carriers = exakt 0,00).
   - **Kanalarchitektur & Walsh-Energiedispersion:** Es existieren 11 höhere zeitliche Modi ($P_1..P_{11}$), wovon $P_1$ (Trend) und $P_2$ (Krümmung) eigene Skalarkanäle besitzen, während die 9 höheren Modi ($P_3..P_{11}$) über räumliche Walsh-Subcarrier gemultiplext werden. Die AC-Pulsenergie verteilte sich auf diese Modi, wodurch der maximale Pixeldeltabetrag im unkomprimierten Träger von $101{,}0$ auf $38{,}0$ gedämpft wurde.
   - **WebP-Quantisierungsvernichtung:** Die verlustbehaftete WebP-Kompression ($Q=80$) reduzierte die verbliebenen hochfrequenten Walsh-Muster von $38{,}0$ auf **$13{,}0$**, während sie zeitgleich Blockartefakte mit bis zu **$20{,}0$** Delta in benachbarten Quadranten erzeugte. Auf identischen ROI-Pixeln gemessen liegt das Signal-zu-Fehler-Verhältnis bei **$\text{SNR}_{\text{diff}} = -0{,}41\,\text{dB}$** (Fehlerenergie $43{,}10$ übersteigt Signalenergie $39{,}19$).

2. **Perzeptiver / Attentionaler Verlust im Kontaktbogen (Signal intakt):**
   - Im hochauflösenden Kontaktbogen (**`GRID512_WEBP`**) überlebte der Puls in Kachel 11 (Frame 44) mit enormer physikalischer Amplitude: **$\text{ROI\_MAX\_DELTA} = 109{,}0$**, Peak-RGB stieg von $[76, 78, 82]$ auf $[185, 186, 190]$, und der Weber-Kontrast stieg um **$+40\,\%$** ($\Delta \text{Weber} = +0{,}40$).
   - Im pixel-gematchten Kontaktbogen (**`GRID128_WEBP`**) betrug das Delta in Kachel 11 noch immer **$98{,}0$**!
   - *Arbeitshypothese zur VLM-Kognition:* Im Kontaktbogen lag kein Signalverlust vor. Dass das Modell den Puls dennoch übersah, ist als kognitiver Aufmerksamkeitsfilter zu verstehen: Auf einem einzelnen Bild eines 16-teiligen Kontaktbogens wurde die isolierte Kugelaufhellung als normale 3D-Schattierung/Glanzlicht interpretiert, solange kein komparativer Differenz-Prompt vorlag.

3. **Phase B Durchbruch (E4-Y0 Adaptive Zentrierung):**
   - Durch die Substitution $Y_c'(t, x, y) = Y(t, x, y) - Y(0, x, y)$ bricht die DC-Sättigung über das gesamte Bild von **100,0 % auf 3,91 %** ein (Hintergrund-Sättigung = **0,0 %**).
   - **Mathematische Invarianz:** Die höheren Modi $P_1..P_{11}$ bleiben maschinengenau identisch ($\max |\Delta M_k| = 3{,}06 \times 10^{-13}$).
   - **Signalverstärkung im WebP-Carrier:** Das messbare maximale Pulsdelta in WebP Q80 steigt von **$13{,}0$ auf $24{,}0$** (nahezu Verdopplung).
   - **Multi-Clip Sicherheitskontrolle (C1..C5):** Bei allen 5 Clips wird die DC-Sättigung eliminiert, während die Richtungsumkehr in C4 und alle Kinematik-Trajektorien unberührt bleiben.

---

## 2. Automatisierter 64-Frame Synchronisationsnachweis (C3 vs. C5)

Zur formalen Absicherung des kontrafaktischen Zwillingspaares wurde eine lückenlose Pixelprüfung aller 64 Frames durchgeführt (`scripts/verify_exp028_sync.py`):
1. **Pre-Pulse (Frames 0 bis 42, $t = 0{,}0\text{--}2{,}625\,\text{s}$):**
   - Maximales Delta über alle $1080 \times 1080$ Pixel: **exakt 0** (**100,0 % bit-identisch**).
2. **Pulse-Window (Frames 43 bis 46, $t = 2{,}6875\text{--}2{,}875\,\text{s}$):**
   - Hintergrund außerhalb des Kugelbewegungspfads: **exakt 0** (**100,0 % bit-identisch**).
   - Kugel-ROI: Hochenergetischer Puls mit maximalen Delta-Werten von $117{,}0$ (F43), $118{,}0$ (F44), $120{,}0$ (F45), $110{,}0$ (F46).
3. **Post-Pulse (Frames 47 bis 63, $t = 2{,}9375\text{--}3{,}9375\,\text{s}$):**
   - Hintergrund außerhalb des Bewegungskorridors: **exakt 0** (**100,0 % bit-identisch**).
   - Kugel-Randpixel: Minor Decay / Tail-Differenz von max. $22\text{--}25$ LSB auf den Kanten der weiterlaufenden Kugel.

---

## 3. Die 5-Stufen Signalübertragungs-Tabelle (Phase A Baseline)

*Hinweis zur Interpretation:* Die Kontrastwerte in Stage 0 bis 2 basieren auf physikalischer Bildluminanz $Y$. Die Kontrastwerte in Stage 3 und 4 sind Koeffizienten-Kontraste im codierten Farbraum von Quadrant T und dienen als relative Signalstärken-Indikatoren.

| Stufe / Format | Repräsentation & Auflösung | ROI MAE | ROI Max Delta | C3-C5 Equal (%) | Delta Weber Kontrast | Delta Michelson |
|---|---|---|---|---|---|---|
| **Stage 0: 1080p Ground Truth** | Unkomprimiert 1080p RGB (Frame 44) | **19,1150** | **118,0** | 55,6 % | **+1,66** | +0,070 |
| **Stage 1: 64x64 Resampled** | BOX (Area) Downsampling (Frame 44) | **23,6343** | **101,0** | 37,5 % | **+2,07** | +0,065 |
| **Stage 2: GRID512 Contact Sheet** | 4x4 Grid $512 \times 512$ WebP (Cell 11) | **5,1423** | **109,0** | 63,2 % | **+0,40** | +0,067 |
| **Stage 2: GRID128 Contact Sheet** | 4x4 Grid $128 \times 128$ WebP (Cell 11) | **6,6889** | **98,0** | 38,9 % | **+0,37** | +0,071 |
| **Stage 3: E3-K12 Visual Carrier** | $128 \times 128$ Lossless PNG (Quad T) | **1,9352** | **38,0** | 54,2 % | -0,01 | +0,008 |
| **Stage 4: E3-K12 Visual Carrier** | $128 \times 128$ Lossy WebP Q80 (Quad T) | **3,0556** | **13,0** | 8,3 % | -0,01 | +0,005 |

---

## 4. Zeitliche Detailanalyse der 4 Pulsframes (16 FPS)

Die KinetiCraft/SwiftClip Physik-Engine erzeugte den Puls mit einer theoretischen Sinushüllkurve über $250\,\text{ms}$ ($t \in [2{,}65, 2{,}90]\,\text{s}$):
$$\text{Envelope}(t) = \sin\left(\pi \frac{t - 2{,}65}{0{,}25}\right)$$

| Frame | Zeitstempel ($t$) | Theor. Hüllkurve | 1080p ROI Max Delta | 1080p ROI MAE | 1080p Delta Weber |
|---|---|---|---|---|---|
| **Frame 43** | $2{,}6875\,\text{s}$ | $0{,}4540$ | $117{,}0$ | $17{,}4375$ | $+1{,}51$ |
| **Frame 44** | $2{,}7500\,\text{s}$ (Peak) | **$0{,}9511$** | **$118{,}0$** | **$19{,}1150$** | **$+1{,}66$** |
| **Frame 45** | $2{,}8125\,\text{s}$ | $0{,}8910$ | $120{,}0$ | $19{,}0834$ | $+1{,}66$ |
| **Frame 46** | $2{,}8750\,\text{s}$ | $0{,}3090$ | $110{,}0$ | $16{,}3435$ | $+1{,}42$ |

---

## 5. Spektrale Gram-Moden-Zerlegung (C5 minus C3)

Die zeitliche Gram-Projektion $M_k = \sum_{t=0}^{63} (Y(t) - 128) \cdot P_k(t)$ verteilt die Energie über 12 orthogonale Basispolynome:

| Modus ($k$) | Basisfunktion & Kanalzuordnung | ROI Max Delta | Full Max Delta | $L_2$-Energie $||\Delta M_k||$ | Sättigung in C3 Baseline |
|---|---|---|---|---|---|
| **$k=00$** | **$P_0$ (DC-Mittelwert, Quad T Rot)** | **$44{,}75$** | **$44{,}75$** | **$143{,}30$** | **100,0 % (Vollständig geclippt)** |
| **$k=01$** | $P_1$ (Linearer Trend, Quad C Cb)** | $31{,}31$ | $31{,}31$ | $100{,}72$ | $3{,}4\,\%$ |
| **$k=02$** | $P_2$ (Krümmung / Bimodalität, Quad T Grün)** | $25{,}37$ | $25{,}37$ | $80{,}74$ | $3{,}4\,\%$ |
| **$k=03$** | Walsh Subcarrier 1 ($k=3$, Quad T Blau) | $51{,}86$ | $51{,}86$ | $166{,}27$ | $3{,}2\,\%$ |
| **$k=04$** | Walsh Subcarrier 2 ($k=4$, Quad C Cr) | $16{,}64$ | $16{,}64$ | $53{,}75$ | $3{,}4\,\%$ |
| **$k=05$** | Walsh Subcarrier 3 ($k=5$, Quad T Blau) | $38{,}46$ | $38{,}46$ | $122{,}32$ | $3{,}2\,\%$ |
| **$k=06$** | Walsh Subcarrier 4 ($k=6$, Quad C Cr) | $46{,}85$ | $46{,}85$ | $151{,}01$ | $3{,}0\,\%$ |
| **$k=07$** | Walsh Subcarrier 5 ($k=7$, Quad T Blau) | $5{,}24$ | $5{,}24$ | $14{,}30$ | $2{,}6\,\%$ |
| **$k=08$** | Walsh Subcarrier 6 ($k=8$, Quad C Cr) | $46{,}17$ | $46{,}17$ | $147{,}02$ | $2{,}4\,\%$ |
| **$k=09$** | Walsh Subcarrier 7 ($k=9$, Quad T Blau) | $37{,}22$ | $37{,}22$ | $120{,}89$ | $2{,}2\,\%$ |
| **$k=10$** | Walsh Subcarrier 8 ($k=10$, Quad C Cr) | $16{,}74$ | $16{,}74$ | $49{,}57$ | $1{,}9\,\%$ |
| **$k=11$** | Walsh Subcarrier 9 ($k=11$, Quad T Blau) | $48{,}31$ | $48{,}31$ | $154{,}38$ | $1{,}6\,\%$ |

---

## 6. Phase B: Experimenteller E4-Y0 Gegenversuch

Auf Empfehlung des wissenschaftlichen Peer-Reviews durch ChatGPT im Nova Tab A wurde der experimentelle Codec **`E4-Y0`** implementiert und in 4 orthogonalen Bedingungen evaluiert.

### 6.1 Die 4 Versuchsbedingungen im Vergleich

| Bedingung | Codec | Zentrierung | Format | Dateigröße (C5) | ROI Max Delta | ROI MAE | Quad T Red Max Delta |
|---|---|---|---|---|---|---|---|
| **Condition A** | E3-K12 | 128 (Statisch) | WebP Q80 | 560 Bytes | 13,0 | 3,0556 | 9,0 |
| **Condition B** | E3-K12 | 128 (Statisch) | Lossless PNG | 2.564 Bytes | 38,0 | 1,9352 | **0,0** |
| **Condition C** | **E4-Y0** | **Y0 (Adaptiv)** | **WebP Q80** | **528 Bytes** | **24,0** | **4,1528** | **13,0** |
| **Condition D** | **E4-Y0** | **Y0 (Adaptiv)** | **Lossless PNG** | 2.724 Bytes | 38,0 | 1,9722 | **3,0** |

### 6.2 Rigorose Signal-zu-Fehler-Definition (auf identischer Pixel-ROI)

Um ChatGPTs methodischer Forderung nach einem formal definierten Fehlermaß zu entsprechen, wurden Signal $S = \text{Carrier}_{\text{lossless}}(C5) - \text{Carrier}_{\text{lossless}}(C3)$ und Kompressionsfehler $E = S_{\text{webp}} - S$ auf denselben ROI-Pixeln gemessen:

$$\text{SNR}_{\text{diff}} = 10 \log_{10}\left(\frac{\sum_{\text{ROI}} \|S(x, y)\|^2}{\sum_{\text{ROI}} \|E(x, y)\|^2}\right)$$

| Codec | ROI Signal Power ($\|S\|^2$) | ROI Error Power ($\|E\|^2$) | Differential SNR | Differential PSNR |
|---|---|---|---|---|
| **E3-K12 (Statisch 128)** | 39,19 | 43,10 | **-0,41 dB** | 31,79 dB |
| **E4-Y0 (Adaptiv Y0)** | 39,26 | 42,69 | **-0,36 dB** | 31,83 dB |

**Ergebnis:** Bei beiden Codecs übersteigt das WebP Q80 Quantisierungsrauschen auf der Puls-ROI knapp die differentielle Signalenergie ($\text{SNR} < 0\,\text{dB}$). Allerdings führt E4-Y0 in WebP zu einem messbaren Max-Delta von **24,0** (gegenüber 13,0 bei E3), da der Rotkanal aktiv zur Differenz beiträgt.

### 6.3 Multi-Clip Sicherheitskontrolle (C1 bis C5)

Die adaptive Subtraktion von $Y_0$ birgt theoretisch das Risiko negativer Koeffizienten an Positionen, an denen das Objekt in Frame 0 hell war und danach den Ort verlässt. Zur Absicherung wurden alle 5 Physik-Clips auditiert:

| Clip | Szenario | E3 Sättigung | E4 Sättigung (Gesamt) | E4 Positiv-Sättigung | E4 Negativ-Sättigung (Origin) | E4 Rekonstruktions-MAE |
|---|---|---|---|---|---|---|
| **C1** | Freier linearer Durchlauf | 100,0 % | **7,5 %** | 6,3 % | 1,2 % | 3,2485 |
| **C2** | Partielle Verdeckung | 100,0 % | **3,4 %** | 2,7 % | 0,7 % | 1,7895 |
| **C3** | Vollständige Okklusion (Baseline) | 100,0 % | **3,9 %** | 3,1 % | 0,8 % | 2,1070 |
| **C4** | **Richtungsumkehr / Abprallen** | 100,0 % | **3,5 %** | 2,5 % | 1,0 % | **2,5273** |
| **C5** | Okklusion mit Luminanzpuls | 100,0 % | **3,9 %** | 3,1 % | 0,8 % | 2,1319 |

**Befund:** Der statische Hintergrund ist in allen 5 Clips zu **100 % ungesättigt** ($0{,}0\,\%$ Sättigung). Die minimale Negativ-Sättigung von $0{,}7\text{--}1{,}2\,\%$ ist lokal strikt auf die Startposition der Kugel in Frame 0 begrenzt. Die Richtungsumkehr in C4 wird fehlerfrei und unbeeinträchtigt übertragen.

---

## 7. Archivierte Artefakte

Alle generierten Differenzkarten, Rohmetriken und Zusammenfassungen sind reproduzierbar hinterlegt:

- **Phase A Rohdaten:**
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

- **Phase B Rohdaten:**
  - JSON-Metriken: [`phase_b/phase_b_results.json`](phase_b/phase_b_results.json)
  - Markdown-Tabelle: [`phase_b/phase_b_summary.md`](phase_b/phase_b_summary.md)
  - Differenzkarten der 4 Bedingungen:
    - Condition A (E3 WebP): [`phase_b/phase_b_plots/diff_Condition_A_E3_WebP.png`](phase_b/phase_b_plots/diff_Condition_A_E3_WebP.png)
    - Condition B (E3 Lossless): [`phase_b/phase_b_plots/diff_Condition_B_E3_Lossless.png`](phase_b/phase_b_plots/diff_Condition_B_E3_Lossless.png)
    - Condition C (E4 WebP): [`phase_b/phase_b_plots/diff_Condition_C_E4_WebP.png`](phase_b/phase_b_plots/diff_Condition_C_E4_WebP.png)
    - Condition D (E4 Lossless): [`phase_b/phase_b_plots/diff_Condition_D_E4_Lossless.png`](phase_b/phase_b_plots/diff_Condition_D_E4_Lossless.png)
  - Rekonstruktionskarten:
    - Ground Truth F44 Diff: [`phase_b/phase_b_plots/ground_truth_f44_diff.png`](phase_b/phase_b_plots/ground_truth_f44_diff.png)
    - E3 Reconstructed Diff: [`phase_b/phase_b_plots/recon_f44_diff_e3.png`](phase_b/phase_b_plots/recon_f44_diff_e3.png)
    - E4 Reconstructed Diff: [`phase_b/phase_b_plots/recon_f44_diff_e4.png`](phase_b/phase_b_plots/recon_f44_diff_e4.png)
