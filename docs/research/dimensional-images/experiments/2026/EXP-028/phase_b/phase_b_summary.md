# EXP-028 Phase B: Adaptive Y0 Centering Evaluation Summary

## 1. Matrix der 4 Versuchsbedingungen (C5 vs. C3)

| Bedingung | Codec | Zentrierung | Format | Dateigröße (C5) | ROI Max Delta | ROI MAE | Quad T Red Max Delta |
|---|---|---|---|---|---|---|---|
| **Condition_A_E3_WebP** | E3-K12 | 128 (Statisch) | WebP Q80 | 560 B | 13.0 | 3.0556 | 9.0 |
| **Condition_B_E3_Lossless** | E3-K12 | 128 (Statisch) | Lossless PNG | 2564 B | 38.0 | 1.9352 | 0.0 |
| **Condition_C_E4_WebP** | E4-Y0 | Y0 (Adaptiv) | WebP Q80 | 528 B | 24.0 | 4.1528 | 13.0 |
| **Condition_D_E4_Lossless** | E4-Y0 | Y0 (Adaptiv) | Lossless PNG | 2724 B | 38.0 | 1.9722 | 3.0 |

## 2. Rigorose Signal-to-Noise / Fehler-Analyse (auf identischer ROI)

| Codec | ROI Signal Power | ROI WebP Error Power | Differential SNR (dB) | Differential PSNR (dB) |
|---|---|---|---|---|
| **E3-K12 (Statisch 128)** | 39.19 | 43.10 | **-0.41 dB** | 31.79 dB |
| **E4-Y0 (Adaptiv Y0)** | 39.26 | 42.69 | **-0.36 dB** | 31.83 dB |

## 3. P0 Sättigungsabbau über alle 5 Clips (Sicherheitskontrolle)

| Clip | E3-K12 Sättigung | E4-Y0 Sättigung (Gesamt) | E4 Positiv-Sättigung | E4 Negativ-Sättigung | E4 M0 Bereich | E4 Rekonstruktions-MAE |
|---|---|---|---|---|---|---|
| **C1** | 100.0% | **7.5%** | 6.3% | 1.2% | [-1345.9, 248.7] | 3.2485 |
| **C2** | 100.0% | **3.4%** | 2.7% | 0.7% | [-1192.4, 207.8] | 1.7895 |
| **C3** | 100.0% | **3.9%** | 3.1% | 0.8% | [-1246.3, 223.0] | 2.1070 |
| **C4** | 100.0% | **3.5%** | 2.5% | 1.0% | [-1235.4, 531.5] | 2.5273 |
| **C5** | 100.0% | **3.9%** | 3.1% | 0.8% | [-1246.3, 249.9] | 2.1319 |

## 4. Frame 44 Rekonstruktion & Puls-Wiederherstellung

- **Ground Truth (64x64 Box):** ROI Max Delta = 100.17, ROI MAE = 23.8027
- **E3-K12 Rekonstruktion:** ROI Max Delta = 0.87, ROI MAE = 0.0674 (Fehler vs GT: 23.7496)
- **E4-Y0 Rekonstruktion:**  ROI Max Delta = 0.87, ROI MAE = 0.0726 (Fehler vs GT: 23.7445)
