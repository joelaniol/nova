# EXP-028: Differential Signal Survival Summary Table

| Stufe / Format | Representation | ROI MAE | ROI Max Delta | C3-C5 Equal (%) | Delta Weber Contrast | Delta Michelson |
|---|---|---|---|---|---|---|
| **Stage 0: 1080p Ground Truth (F44)** | Uncompressed 1080p RGB | 19.1150 | 118.0 | 55.6% | +1.66 | +0.070 |
| **Stage 1: 64x64 Resampled (F44)** | BOX (Area) Downsampling | 23.6343 | 101.0 | 37.5% | +2.07 | +0.065 |
| **Stage 2: GRID512 Contact Sheet** | 4x4 Grid 512x512 WebP (Cell 11) | 5.1423 | 109.0 | 63.2% | +0.40 | +0.067 |
| **Stage 2: GRID128 Contact Sheet** | 4x4 Grid 128x128 WebP (Cell 11) | 6.6889 | 98.0 | 38.9% | +0.37 | +0.071 |
| **Stage 3: E3-K12 Visual Carrier** | 128x128 Lossless PNG | 1.9352 | 38.0 | 54.2% | -0.01 | +0.008 |
| **Stage 4: E3-K12 Visual Carrier** | 128x128 Lossy WebP (Q=80) | 3.0556 | 13.0 | 8.3% | -0.01 | +0.005 |

### Gram Mode Energy Distribution (C5 - C3)

| Mode k | Basis Function | ROI Max Delta | Full Max Delta | L2 Energy | Saturation (C3) |
|---|---|---|---|---|---|
| k=00 | P0 (Mean DC offset) | 44.75 | 44.75 | 143.30 | 100.0% |
| k=01 | P1 (Linear drift) | 31.31 | 31.31 | 100.72 | 3.4% |
| k=02 | P2 (Curvature / Bimodal) | 25.37 | 25.37 |  80.74 | 3.4% |
| k=03 | Walsh Subcarrier 1 (k=3) | 51.86 | 51.86 | 166.27 | 3.2% |
| k=04 | Walsh Subcarrier 2 (k=4) | 16.64 | 16.64 |  53.75 | 3.4% |
| k=05 | Walsh Subcarrier 3 (k=5) | 38.46 | 38.46 | 122.32 | 3.2% |
| k=06 | Walsh Subcarrier 4 (k=6) | 46.85 | 46.85 | 151.01 | 3.0% |
| k=07 | Walsh Subcarrier 5 (k=7) |  5.24 |  5.24 |  14.30 | 2.6% |
| k=08 | Walsh Subcarrier 6 (k=8) | 46.17 | 46.17 | 147.02 | 2.4% |
| k=09 | Walsh Subcarrier 7 (k=9) | 37.22 | 37.22 | 120.89 | 2.2% |
| k=10 | Walsh Subcarrier 8 (k=10) | 16.74 | 16.74 |  49.57 | 1.9% |
| k=11 | Walsh Subcarrier 9 (k=11) | 48.31 | 48.31 | 154.38 | 1.6% |
