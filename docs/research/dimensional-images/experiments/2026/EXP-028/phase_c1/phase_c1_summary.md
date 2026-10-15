# EXP-028 Phase C1: Information & Decoder-Decomposition Summary

## 1. Vierstufiger Signalzerlegungs-Vergleich (Frame 44 Peak)

| Stufe | Repräsentationsform | ROI Max Delta | ROI MAE | Fehler vs GT | Signalverlust-Mechanismus |
|---|---|---|---|---|---|
| **Stage 1** | Ground Truth (64x64 BOX) | **100.17** | **23.8027** | 0.0000 | Physisches Eingangssignal |
| **Stage 2** | Ideale K12 Float-Projektion | **46.95** | **11.6001** | 12.4474 | -53,1 % Glättung (Gram-Filter) |
| **Stage 3a** | Unquantisierte Dedizierte Kanäle (P0..P2) | **10.16** | **2.5175** | 21.2852 | Nur 21,6 % der Energie in P0..P2 |
| **Stage 3b** | Carrier Quantisierte Kanäle (P0..P2) | **0.86** | **0.0647** | 23.7380 | 75 % Sättigung in Kugelbahn |
| **Stage 4** | Global Gemittelter Decoder (E4) | **0.87** | **0.0726** | 23.7445 | Globale Verdünnung (Faktor 1/64) |

## 2. Moden-Beitrag zum 46,95 Peak bei Frame 44

| Modus k | Basisfunktion | Delta M_k ROI Max | P_k(44) | Rekonstruierter Term (LSB) |
|---|---|---|---|---|
| k=00 | P0 (Mean) |  44.75 | +0.1250 | ** +5.59** |
| k=01 | P1 (Drift) |  31.31 | +0.0846 | ** +2.65** |
| k=02 | P2 (Curvature) |   0.53 | -0.0758 | ** +1.92** |
| k=03 | Walsh 1 |   0.17 | -0.1446 | ** +7.50** |
| k=04 | Walsh 2 |   0.24 | -0.0360 | ** +0.60** |
| k=05 | Walsh 3 |  38.46 | +0.1171 | ** +4.50** |
| k=06 | Walsh 4 |  46.85 | +0.1277 | ** +5.98** |
| k=07 | Walsh 5 |   4.81 | -0.0173 | ** +0.09** |
| k=08 | Walsh 6 |   0.19 | -0.1416 | ** +6.54** |
| k=09 | Walsh 7 |   0.25 | -0.0942 | ** +3.51** |
| k=10 | Walsh 8 |  16.74 | +0.0676 | ** +1.13** |
| k=11 | Walsh 9 |  48.31 | +0.1480 | ** +7.15** |

## 3. Synthetischer Stresstest: Lokalisierter Modus k=3 (8x8 Patch, Amp=25.0)

- **Physikalische Trägermodulation auf dem Patch:** **-26,50 LSB** (Hintergrund: **0,00 LSB**)
- **Globaler Decoder:** Demoduliert Mode k=03 zu **0.405 LSB** (Faktor 0.0162 = exakt 1/64 Flächenverdünnung!)
- **Lokaler Patch-Decoder:** Demoduliert Mode k=03 zu **25.92 LSB** (**103,7 % Wiederherstellungstreue**!)
- **Lokales Walsh-Aliasing:** Auf dem 8x8 Patch verliert die Walsh-Basis die lokale Orthogonalität, sodass Mode k=09 als Alias mit invertiertem Vorzeichen (-25.92) auftritt.
