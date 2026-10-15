# EXP-028 Phase C2: Blinded VLM Comparison Benchmark (E3-K12 vs. E4-Y0)

## Executive Summary & Study Protocol

This document pre-registers and defines the confirmatory benchmark evaluating whether the mathematical dynamic range improvement achieved in **E4-Y0** (adaptive $Y_0$ centering, ADR-033/ADR-034) translates into a statistically significant improvement in semantic temporal event understanding by multimodal vision-language models (VLMs) compared to the frozen baseline **E3-K12**.

---

## 1. Experimental Conditions

The benchmark tests 5 rigorously controlled conditions across two stimulus presentations:

| Condition ID | Codec Scheme | Representation | File Format | Resolution | Experimental Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Condition A** | `E3-K12` | 2x2 Visual Carrier | WebP Q80 | 128x128 | Frozen Baseline Reference |
| **Condition B** | `E4-Y0` | 2x2 Visual Carrier ($Y_0$ Centering) | WebP Q80 | 128x128 | **Primary Candidate** |
| **Condition C** | `E3-K12` | 2x2 Visual Carrier | PNG lossless | 128x128 | WebP Lossy Degradation Control on E3 |
| **Condition D** | `E4-Y0` | 2x2 Visual Carrier ($Y_0$ Centering) | PNG lossless | 128x128 | WebP Lossy Degradation Control on E4 |
| **Condition E** | `GRID512` | 4x4 Temporal Contact Sheet (16 frames) | WebP Q80 | 512x512 | Spatial Resolution / Conventional Quality Ceiling |

---

## 2. Evaluation Tasks

### Task 1: Unpaired Single-Image Pulse Detection (Blind Primary Task)
- **Design:** Each stimulus is evaluated independently in a fresh, isolated model context. No paired positive and negative twins are co-presented.
- **Blinding:** Stimulus files use neutral random 12-character hex UUIDs (`stimulus_xxxxxxxxxxxx.webp` / `.png`).
- **Prompt:**
  > *"Untersuche die dargestellte zeitliche Sequenz. Ist eine kurzzeitige Helligkeitsänderung eines Objekts erkennbar, die anschließend wieder verschwindet? Antworte mit 'ja', 'nein' oder 'unklar' und beschreibe kurz die sichtbare Grundlage deiner Einschätzung."*
- **Format Information Provided:**
  - For Visual Carriers (Conditions A, B, C, D):
    > *"Das Bild ist ein 128x128 Visual Carrier mit 4 Quadranten (je 64x64):*
    > *- Oben-Links: Basiszustand (Frame t=0)*
    > *- Oben-Rechts: Temporale Kinematik (Rot=P0 Mittelwert, Grün=P2 Krümmung, Blau=höhere zeitliche Walsh-Moden)*
    > *- Unten-Links: Chromatische Trägerschicht (Cb=P1 Trend, Cr=höhere zeitliche Walsh-Moden)*
    > *- Unten-Rechts: Neutralgrau (128)"*
  - For Contact Sheets (Condition E):
    > *"Das Bild ist ein 512x512 4x4 Kontaktbogen aus 16 zeitlich aufeinanderfolgenden Videobildern. Die Zeit verläuft zeilenweise von oben-links nach unten-rechts (Zeile 0 = Anfang, Zeile 3 = Ende)."*
- **Strict Constraint:** Zero leading response examples. No default `event_detected: "nein"` or boolean placeholders.
- **JSON Schema:**
  ```json
  {
    "stimulus_id": "string",
    "event_detected": "ja | nein | unklar",
    "confidence": 0.0,
    "reasoning": "string"
  }
  ```

### Task 2: Paired Differential Discrimination Test (Secondary Task)
- **Design:** Side-by-side presentation of matched twin representations of the identical physical scene (negative twin without pulse vs. positive twin with pulse), rendered under the same condition.
- **Randomization:** Left/right presentation (`Image A` vs. `Image B`) is randomized per pair via seed.
- **Prompt:**
  > *"Untersuche die beiden Darstellungen derselben Szene (Bild A links, Bild B rechts). Ist eine zeitlich begrenzte Veränderung zwischen den beiden Darstellungen erkennbar und in welcher Darstellung tritt sie auf? Antworte mit 'A', 'B' oder 'kein_Unterschied' und begründe kurz."*
- **Reporting:** 4-Quadrant contingency matrix (Isolated Salient, Differential Only, Inaccessible, Unstable).

---

## 3. Sample Size & Dataset Partitioning

1. **Technical Pilot Run:**
   - 8 independent scene configurations (P01..P08).
   - 16 videos (8 negative twins, 8 positive twins).
   - 80 Task 1 evaluations (16 videos $\times$ 5 conditions).
   - 40 Task 2 evaluations (8 pairs $\times$ 5 conditions).
   - Purpose: Calibration of prompt adherence, JSON extraction robustness, and absence of format leakage. Codec parameters remain strictly frozen.

2. **Confirmatory Main Benchmark:**
   - 24 new independent scene configurations (S01..S24) varying trajectory (`left_to_right_occluded`, `right_to_left_occluded`, `bounce_reversal`, `diagonal_unobstructed`), luminance ($Y_{\text{bg}} \in [18, 160]$ LSB), sphere radius, obstacle geometry, and pulse timing.
   - 48 videos (24 negative twins, 24 positive twins).
   - 240 Task 1 evaluations (48 videos $\times$ 5 conditions).
   - 120 Task 2 evaluations (24 pairs $\times$ 5 conditions).

---

## 4. Formal Hypotheses & Pre-Registered Decision Gate

- **Primary Hypothesis $H_1$:**
  Multimodal understanding of the localized 250ms brightness transient in Condition B (`E4-Y0 WebP Q80`) exceeds Condition A (`E3-K12 WebP Q80`) by at least **+10.0 percentage points** in Balanced Accuracy:
  $$\Delta \text{Balanced Accuracy} = \text{BA}(\text{Condition B}) - \text{BA}(\text{Condition A}) \ge +10.0\%$$
- **Safety Gate (Anti-Hallucination):**
  The specificity (true negative rate on baseline clips without pulse) of Condition B must not degrade by more than 5.0 percentage points compared to Condition A:
  $$\Delta \text{Specificity} = \text{Spec}(\text{Condition B}) - \text{Spec}(\text{Condition A}) \ge -5.0\%$$
- **Pre-Registration Freeze & Amendment 1:**
  All stimulus hashes (SHA-256), blinded UUIDs, random seed (`20261028`), and prompt strings are frozen in `phase_c2_preregistration.json` prior to any confirmatory model evaluation.
  Following the pilot run and ChatGPT peer-review, [phase_c2_amendment_1.md](phase_c2_amendment_1.md) was ratified:
  1. Exact 12:12 counterbalanced Task 2 left/right positioning.
  2. Addition of 30 identical twin catch trials in Task 2 to measure false difference detection.
  3. Pre-registered paired scene-level cluster-bootstrap ($B=10,000$) 95% CI requirement ($\text{CI}_{2.5\%} > 0.0\%$).
  4. Numerical documentation of GRID512 pulse sampling attenuation as a formal covariate.

