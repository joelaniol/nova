# EXP-028 Phase C1: Information & Decoder-Decomposition Summary

## 1. Vierstufiger Signalzerlegungs-Vergleich (Frame 44 Peak)

| Stufe | Repräsentationsform | ROI Max Delta | ROI MAE | Fehler vs GT | Signalverlust-Mechanismus |
|---|---|---|---|---|---|
| **Stage 1** | Ground Truth (64x64 BOX) | **100.17** | **23.8027** | 0.0000 | Physisches Eingangssignal |
| **Stage 2** | Ideale K12 Float-Projektion | **46.95** | **11.6001** | 12.4474 | -53,1 % Glättung (Gram-Filter) |
| **Stage 3a** | Unquantisierte Dedizierte Kanäle (P0..P2) | **10.16** | **2.5175** | 21.2852 | Nur 21,7 % der Peak-Amplitude in P0..P2 |
| **Stage 3b** | Carrier Quantisierte Kanäle (P0..P2) | **0.86** | **0.0647** | 23.7380 | 75 % Sättigung in Kugelbahn |
| **Stage 4** | Global Gemittelter Decoder (E4) | **0.87** | **0.0726** | 23.7445 | Globale Verdünnung (Faktor 1/64) |

## 2. Exakte Punkt-Modenzerlegung am Peak (x*=43, y*=33) & Räumliche L2-Energie

| Modus k | Basisfunktion | Delta M_k(x*, y*) | P_k(44) | Term am Peak (LSB) | Anteil am Peak | L2 ROI-Energie | L2-Anteil |
|---|---|---|---|---|---|---|---|
| k=00 | P0 (Mean) | +44.746 | +0.1250 | **+5.593** |  11.9 % | 20506.45 |  12.2 % |
| k=01 | P1 (Drift) | +31.313 | +0.0846 | **+2.649** |   5.6 % | 10124.45 |   6.0 % |
| k=02 | P2 (Curvature) | -25.366 | -0.0758 | **+1.923** |   4.1 % |  6512.16 |   3.9 % |
| k=03 | Walsh 1 | -51.863 | -0.1446 | **+7.501** |  16.0 % | 27609.35 |  16.4 % |
| k=04 | Walsh 2 | -16.177 | -0.0360 | **+0.582** |   1.2 % |  2878.05 |   1.7 % |
| k=05 | Walsh 3 | +38.457 | +0.1171 | **+4.505** |   9.6 % | 14949.60 |   8.9 % |
| k=06 | Walsh 4 | +46.855 | +0.1277 | **+5.984** |  12.8 % | 22767.12 |  13.6 % |
| k=07 | Walsh 5 |  -0.212 | -0.0173 | **+0.004** |   0.0 % |   198.55 |   0.1 % |
| k=08 | Walsh 6 | -46.170 | -0.1416 | **+6.539** |  13.9 % | 21596.29 |  12.9 % |
| k=09 | Walsh 7 | -36.965 | -0.0942 | **+3.483** |   7.4 % | 14579.41 |   8.7 % |
| k=10 | Walsh 8 | +15.280 | +0.0676 | **+1.033** |   2.2 % |  2454.91 |   1.5 % |
| k=11 | Walsh 9 | +48.312 | +0.1480 | **+7.152** |  15.2 % | 23808.72 |  14.2 % |

- **Summe aller 12 Terme am Peak:** **46.9461 LSB** (Exakter Match mit Peak: 46.9461 LSB)
- **Dedizierte Kanäle (P0..P2):** Peak-Beitrag: **10.165 LSB** (21,7 %), L2-Energie: **22.11 %**
- **Höhere Walsh-Modi (P3..P11):** Peak-Beitrag: **36.783 LSB** (78,3 %), L2-Energie: **77.89 %**

## 3. Synthetischer Stresstest: Lokalisierter Modus k=3 (8x8 Patch, Amp=25.0)

- **Physikalische Trägermodulation auf dem Patch:** **-26,50 LSB** (Hintergrund: **0,00 LSB**)
- **Globaler Decoder:** Demoduliert Mode k=03 zu **0.405 LSB** (Faktor 0.0162 = exakt 1/64 Flächenverdünnung!)
- **Lokaler Patch-Decoder:** Demoduliert Mode k=03 zu **25.92 LSB** (**103,7 % Wiederherstellungstreue**!)
- **Lokales Walsh-Aliasing:** Auf dem 8x8 Patch verliert die Walsh-Basis die lokale Orthogonalität, sodass Mode k=09 als Alias mit invertiertem Vorzeichen (-25.92) auftritt.
