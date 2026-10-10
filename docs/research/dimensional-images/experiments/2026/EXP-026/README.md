# EXP-026: Empirical Temporal Resolution Boundary & Causal Information Audit

**Date:** 2026-10-10  
**Status:** Evaluated & Ratified (ADR-030)  
**Evidence Tier:** `[EMPIRICAL-VLM]` / `[NUMERICAL]` / `[PROVISIONAL]` (Resolution Threshold)  
**Carrier Geometry:** 128x128 E3-K12 Single-Carrier Tile  
**Window Duration:** 8.0 seconds (64 frames @ 8 FPS)  
**Encoding:** E3-K12 (12 Discrete Gram Orthogonal Polynomials)  

---

## 1. Overview & Objective

EXP-026 addresses the scientific boundary question identified during peer review: What is the empirical minimum temporal separation $\Delta t$ required for two discrete impulse events to be reliably separated by a Vision-Language Model reading an E3-K12 carrier?

Additionally, this experiment evaluates:
1. Preservation of the temporal arrow of time (chronological ordering) via odd Gram polynomial phase flips.
2. The Energy Equivalence Fallacy (discriminating a single broad pulse from two discrete pulses having mathematically identical total energy $\int I^2 dt$).
3. Temporal window position invariance (checking for boundary attenuation at $t = 1.5\text{s}, 4.0\text{s}, 6.5\text{s}$).

### Primary Artifacts in this Directory:
* `protocol.json`: Full machine-readable generator parameters, per-mode Gram energies, and WebP compression metrics.
* `metrics.csv`: Tabulated sweep data comparing $\Delta t$, WebP byte size, MSE, PSNR, high-order spectral energy ratio, and VLM separation verdicts.
* `model-responses.jsonl`: Complete, unedited responses from 4 independent blinded subagents.

---

## 2. Experimental Stimuli & Results

### S1: Temporal Resolution Matrix Sweep
Sweep over $\Delta t \in \{0.25\text{s}, 0.50\text{s}, 1.00\text{s}, 1.50\text{s}, 2.00\text{s}, 3.00\text{s}\}$ using two identical Amber pulses (frames $N=64$, duration $8.0\text{s}$):

| Condition | $\Delta t$ (sec) | Frames | WebP (Bytes) | MSE | PSNR (dB) | High-Order Energy Ratio | VLM Perceptual Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Control** | 0.00s (Single) | 0 | 468 | 22.42 | 34.62 | 0.6812 | Unimodal baseline |
| **Delta 0.25s** | 0.25s | 2 | 476 | 22.63 | 34.58 | 0.6792 | `fused_single` (sub-Rayleigh coherence) |
| **Delta 0.50s** | 0.50s | 4 | 478 | 22.56 | 34.60 | 0.6402 | `fused_single` (sub-Rayleigh coherence) |
| **Delta 1.00s** | 1.00s | 8 | 496 | 22.18 | 34.67 | 0.5369 | `fused_single` (spectral phase desaturation) |
| **Delta 1.50s** | 1.50s | 12 | 510 | 22.09 | 34.69 | 0.5284 | **`separable_double` (bimodal bifurcation)** |
| **Delta 2.00s** | 2.00s | 16 | 506 | 21.84 | 34.74 | 0.6706 | `separable_double` (4-column fringe grid) |
| **Delta 3.00s** | 3.00s | 24 | 504 | 21.90 | 34.73 | 0.8145 | `separable_double` (wide spatial separation) |

* **Empirical Resolution Transition:** The transition from unimodal fusion to bimodal separability occurs in the interval $\Delta t \in (1.00\text{s}, 1.50\text{s}]$. At $\Delta t = 1.50\text{s}$ (12 frames), the vertical midline bifurcates into two distinct lobes with doubled fringe density (confidence 0.92).
* **Scientific Note:** This resolution threshold is specific to the evaluated E3-K12 configuration (8.0s window, 64 frames @ 8 FPS). It represents an empirical VLM perception boundary rather than an unalterable mathematical constant.

### S2: Chromatic Causal Order (Temporal Arrow of Time)
* **Design:** Visual stimulus with Cyan followed by Magenta vs. Magenta followed by Cyan (identical timing, spatial coordinate, and amplitudes).
* **Finding:** **100% Accuracy (Confidence 1.0)**. A 180° phase inversion in the odd Gram polynomial coefficients ($P_1, P_3, \dots$) distinctly inverts the chromatic trajectory in Quadrant C, preserving temporal event ordering.

### S3: Energy Equivalence Integral Fallacy
* **Design:** Single broad pulse vs. two discrete pulses calibrated to have mathematically identical total signal energy $\int I^2 dt$.
* **Finding:** **Distinguishable (Confidence 0.98)**. While an integrating sensor (standard camera) cannot separate equal energy bursts, the E3-K12 carrier discriminates them via Quadrant T curvature ($P_2$) and high-order modal cross-gratings.

### S4: Window Position Invariance
* **Design:** Identical pulse pair placed at Early ($t=1.5\text{s}$), Mid ($t=4.0\text{s}$), and Late ($t=6.5\text{s}$) positions in the 8.0s carrier.
* **Finding:** **Uniform High Salience (Confidence 0.99)**. Odd polynomial zero-crossings shift the modal chromatic continuum smoothly from warm orange/lime to violet/cyan without boundary attenuation or edge artifacts.
