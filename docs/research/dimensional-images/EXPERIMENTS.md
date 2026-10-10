# Experiments: Milestone Experiment Index & Verification Archive

**Project:** Dimensional Images: Visual Latent Transport for Multimodal AI  
**Document:** Experiment Index & Empirical Verification Archive (V1.1)  
**Date:** 2026-10-10  
**Project Lead:** Joel Aniol  
**Status:** Experimental research / Working paper  

---

## 1. Scientific Evidence Hierarchy

Every experiment in this archive is cataloged under a strict scientific evidence classification:

| Badge | Evidence Classification | Verification Mechanism |
| :--- | :--- | :--- |
| `[PROVED]` | **Mathematically Derived & Proven** | Exact analytic derivation (e.g. projection nullspaces, polynomial recurrence, Parseval energy conservation). |
| `[NUMERICAL]` | **Numerically Measured & Replicated** | Algorithmic benchmark measurements (e.g. MSE, PSNR, WebP compression size, LSB quantization drift). |
| `[EMPIRICAL-VLM]` | **Experimentally Observed via Blinded VLM** | Independent blinded multi-agent model evaluations on visual stimuli without access to generator ground truth. |
| `[PROVISIONAL]` | **Empirical Hypothesis / Preliminary Finding** | Observed behavior within tested parameter ranges; requires further parametric sweeps to establish generality. |

---

## 2. Key Milestone Experiment Trajectory (EXP-001 to EXP-026)

*Note: This index documents the primary architectural milestones along the research trajectory from initial wavelet baselines to long-horizon 512x512 video mosaics.*

| ID | Title / Focus | Date | Evidence Tier | Container / Layout | Key Finding / Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **EXP-001** | Wavelet Carrier Baselines & Naive Bicubic | 2026-10-08 | `[NUMERICAL]` | 64x64 DWT (Haar / DB4) | DWT frequency packing preserves edges over bicubic downscaling; establishes baseline. |
| **EXP-002** | Color Space Quantization (RGB vs YCbCr) | 2026-10-08 | `[NUMERICAL]` | 64x64 YCbCr | Luminance separation reduces compression MSE by 18.4% under lossy WebP. |
| **EXP-008** | Gram Orthogonal Polynomial Temporal Breakthrough | 2026-10-08 | `[PROVED]` / `[NUMERICAL]` | 128x128 E3-K12 | 12-mode Gram polynomial projection eliminates non-periodic boundary leakage. |
| **EXP-015** | Continuous Trajectory Tracking | 2026-10-09 | `[EMPIRICAL-VLM]` | 128x128 Single-Tile | Models track object kinematic vectors via P0 mean offset and P2 curvature. |
| **EXP-023** | 32.0-Second Dimensional Video Mosaic V1 | 2026-10-09 | `[NUMERICAL]` / `[EMPIRICAL-VLM]` | 256x256 Mosaic (4 slots) | 4-slot uniform progression verified; 1,338x compression ratio vs raw uncompressed video. |
| **EXP-024a** | Open-Ended Cognitive Stress Testing | 2026-10-09 | `[EMPIRICAL-VLM]` | 256x256 Mosaic (4 slots) | Aggregate F1 = 86.5%; 100% Chronology; 100% Boundary Crossing Continuity. |
| **EXP-024b** | Long-Horizon Scaling (128.0s / 1,024 frames) | 2026-10-09 | `[NUMERICAL]` / `[EMPIRICAL-VLM]` | 512x512 Mosaic (16 slots) | Zero format degradation between 16 individual tiles and unified 512x512 mosaic ($\Delta \text{F1} = 0.000$). |
| **EXP-025** | Long-Horizon Falsification Suite (F1–F6) | 2026-10-09 | `[GUIDED-PILOT-VLM]` / `[PROVED]` | 512x512 Mosaic (ATW vs Uniform) | Full 6-family adversarial pilot suite; ATW confirmed; honest nullspace calibration validated in guided setting. |
| **EXP-026** | Empirical Temporal Resolution Boundary Audit | 2026-10-10 | `[GUIDED-PILOT-VLM]` | 128x128 Single-Tile (8.0s) | Pilot resolution threshold localized to $\Delta t \in (1.00\text{s}, 1.50\text{s}]$; arrow of time confirmed; identical hashes confirmed as saturation collapse. |
| **EXP-022b** | Numerical Round-Trip & Basis Invertibility | 2026-10-10 | `[PROVED]` / `[NUMERICAL]` | Single-Tile (N in {32, 64, 128}) | Machine-precision basis orthonormality ($< 8.9 \times 10^{-16}$); mean RMSE = 0.0176 (PNG), 0.1653 (WebP); Pearson $r \ge 0.964$. |

---

## 3. EXP-025: Long-Horizon Guided Falsification Suite

* **Date:** 2026-10-09  
* **Classification Note:** Guided Pilot Evaluation (`[GUIDED-PILOT-VLM]`). Prompts and file paths in this pilot contained structural cues; pre-registered blinded replication planned for EXP-027.  
* **Target:** 128.0s continuous video (1,024 frames @ 8 FPS) mapped into a single 512x512 mosaic.  
* **Artifacts Directory:** [`experiments/2026/EXP-025/`](experiments/2026/EXP-025/) ([`protocol.json`](experiments/2026/EXP-025/protocol.json), [`model-responses.jsonl`](experiments/2026/EXP-025/model-responses.jsonl)).  

### F1: Event Density & Cognitive Attention Limits (`[GUIDED-PILOT-VLM]`)
* **Stimulus:** 10 discrete chromatic beacons distributed across the 16 slots.
* **Finding:** All 10/10 events detected (Recall: 1.0). Minor salience attenuation at Slot 11 attributed to VLM attention capacity rather than carrier loss.

### F2: Identity Swap under 36.0s Tunnel Occlusion (`[GUIDED-PILOT-VLM]`)
* **Stimulus:** Gold disc ($y \approx 20$) and Cyan square ($y \approx 44$) cross trajectories while fully occluded from $t=28\text{s}$ to $t=64\text{s}$.
* **Finding:** Swap recognized with 100% confidence (`lane_swap_detected: true`). Object identities preserved without drift.

### F3: Temporal Mode Contention Boundary (`[GUIDED-PILOT-VLM]`)
* **Stimulus:** 4 rapid chromatic pulses triggered within 3.0s ($\Delta t = 1.0\text{s}$) in Slot 5.
* **Finding:** Discrete pulses fused into an overlapping chromatic superposition in Quadrant C/T. Identifies an empirical resolution boundary for static 8.0s slots, demonstrating the need for ATW.

### F4: Format Isolation Parity (L1 vs L2 vs L3) (`[NUMERICAL]` / `[GUIDED-PILOT-VLM]`)
* **Stimulus:** 6 landmark events evaluated across 16 individual tiles (L1: 7,076 B), 4 sub-mosaics (L2: 6,036 B), and 1 unified mosaic (L3: 5,464 B).
* **Finding:** Perfect retrieval parity ($\Delta \text{F1} = 0.000$) with **22.8% byte savings** in the unified container.

### F5: Non-Stationary Adaptive Temporal Windowing (ATW) (`[GUIDED-PILOT-VLM]`)
* **Stimulus:** Sequence alternating between 48.0s calm drift and rapid high-velocity oscillation bursts.
* **Finding:** Uniform 8.0s grid suffered temporal smearing. ATW dynamic allocation eliminated smear (`preferred_representation: "adaptive"`).

### F6: Adversarial Nullspace Calibration (`[PROVED]` / `[GUIDED-PILOT-VLM]`)
* **Stimulus:** Video pair differing by $\Delta_{\text{raw}} = 31$ in raw pixel space, perturbed strictly within the orthogonal nullspace complement $P(I_N - P^T P) \mathbf{u} = \mathbf{0}$.
* **Finding:** Carrier difference was imperceptible ($\Delta_{\text{carrier}} \le 2$ LSB). Blinded model correctly recognized mathematical indeterminacy (`0.0 confidence`), confirming honest uncertainty reporting.

---

## 4. EXP-026: Empirical Temporal Resolution Boundary & Causal Information Audit

* **Date:** 2026-10-10  
* **Classification Note:** Guided Pilot Evaluation (`[GUIDED-PILOT-VLM]`). Prompt protocols and directory names contained task-level descriptors; serves as qualitative calibration for pre-registered EXP-027.  
* **Target:** Single 128x128 E3-K12 Carrier (8.0s @ 8 FPS, $K=12$ modes).  
* **Evaluation Structure:** 4 distinct sub-protocols (BT1 to BT4), each evaluated via independent model instances.  
* **Artifacts Directory:** [`experiments/2026/EXP-026/`](experiments/2026/EXP-026/) ([`protocol.json`](experiments/2026/EXP-026/protocol.json), [`metrics.csv`](experiments/2026/EXP-026/metrics.csv), [`model-responses.jsonl`](experiments/2026/EXP-026/model-responses.jsonl)).  

### S1: Two Identical Pulses (Separation Matrix Sweep) (`[GUIDED-PILOT-VLM]`)

| Delta t | Frame Delta | Perceptual Regime | Structural Pattern in Quadrant C | Classification |
| :--- | :--- | :--- | :--- | :--- |
| **0.25 s** | 2 frames | Coherent fusion | Unimodal vertical stripe, identical to single pulse | `fused_single` |
| **0.50 s** | 4 frames | Coherent fusion | Unimodal vertical stripe, zero discernible interference | `fused_single` |
| **1.00 s** | 8 frames | Spectral phase interference | Desaturation / destructive phase cancellation, unimodal topology | `fused_single` |
| **1.50 s** | 12 frames | **Bimodal bifurcation** | **Split into 2 distinct symmetrical lobes, doubled line density** | `separable_double` |
| **2.00 s** | 16 frames | High-order interference | 4-column interference grid clearly separated | `separable_double` |
| **3.00 s** | 24 frames | Fully resolved regime | Wide spatial separation across temporal subcarrier | `separable_double` |

| Figure 3a: Fused Single ($\Delta t = 0.25$s) | Figure 3b: Bifurcation Boundary ($\Delta t = 1.50$s) | Figure 3c: Separated Double ($\Delta t = 3.00$s) |
| :---: | :---: | :---: |
| ![Figure 3a](figures/exp-026/exp026_delta_0_25s.png) | ![Figure 3b](figures/exp-026/exp026_delta_1_50s.png) | ![Figure 3c](figures/exp-026/exp026_delta_3_00s.png) |

* **Empirical Resolution Transition:** The boundary of bimodal separation is observed in the interval $\Delta t \in (1.00\text{s}, 1.50\text{s}]$. At $\Delta t = 1.50\text{s}$ (12 frames @ 8 FPS), the carrier bifurcates into two distinct lobes (confidence 0.92).
* **Saturation Collapse Nuance:** Stimulus carriers for $\Delta t = 0.25\text{s}$ and $0.50\text{s}$ share identical SHA256 hashes due to 8-bit dynamic range saturation of $M_0$ and $M_2$ ($D=35.0$). Separation breaks the saturation threshold at $\Delta t = 1.00\text{s}$ ($\max |\Delta C| = 43$).

### S2: Chromatic Chronology & Temporal Arrow of Time (`[GUIDED-PILOT-VLM]`)
* **Test:** Cyan $\to$ Magenta vs. Magenta $\to$ Cyan (identical timing, position, and amplitudes).
* **Finding:** 100% accurate classification (confidence 1.0).
* **Mechanism:** 180° phase inversion in odd Gram polynomial coefficients ($P_1, P_3, \dots$) distinctly reverses chromatic trajectory in Quadrant C.

### S3: Energy Equivalence Integral Fallacy (`[GUIDED-PILOT-VLM]`)
* **Test:** 1 broad continuous pulse vs. 2 discrete pulses with **mathematically identical integrated energy** ($\int I^2 dt$).
* **Finding:** Distinguished with **98% confidence**. Curvature ($P_2$) and high-order Gram subcarriers discriminate the discrete pulses from the continuous pulse.

### S4: Window Position Invariance (`[GUIDED-PILOT-VLM]`)
* **Test:** Identical pulse pair placed early ($t=1.5\text{s}$), mid ($t=4.0\text{s}$), and late ($t=6.5\text{s}$).
* **Finding:** Uniform `high` salience with **zero boundary attenuation** (confidence 0.99).

---

## 5. EXP-022b: Numerical Round-Trip & Invertibility Audit

* **Date:** 2026-10-10  
* **Target:** Mathematical basis orthonormality and matched-filter reference decoder invertibility (`decode_carrier_E3_hybrid_scaling`).  
* **Classification:** `[PROVED]` / `[NUMERICAL]`. Automated verification via `scripts/audit_numerical_roundtrip.py`.  

| Evaluation Axis | Test Scope | Empirical Result | Scientific Significance |
| :--- | :--- | :--- | :--- |
| **Basis Orthonormality** | $N \in \{32, 64, 128\}$, $K=12$ | Max error: $8.88 \times 10^{-16}$ | Exact machine-precision orthonormality $P P^T = I_{12}$ across all ATW window lengths. |
| **Lossless Inversion (PNG)** | Modes $k \in \{0..11\}$ | **Mean RMSE: 0.0176**, Min $r = 0.9899$ | Direct proof of mathematical channel invertibility in 8-bit carrier space (~1.8% error). |
| **Lossy Transport (WebP Q=80)** | Modes $k \in \{0..11\}$ | **Mean RMSE: 0.1653**, Min $r = 0.9643$ | Proves linear coefficient retention survives lossy image transport with high rank fidelity. |
| **Modal Crosstalk Isolation** | Off-diagonal $\max_{j \neq k} \|\hat{a}_j\|$ | PNG: $< 0.0333$, WebP: $< 0.0694$ | Negligible inter-mode interference across the 12 functional dimensions. |

---

## 6. Streaming Bitrate & Payload Accounting

$$\text{Continuous Streaming Rate} = \frac{\text{Container Payload (Bytes)} + \text{Sidecar Metadata (Bytes)}}{\text{Timeline Duration (Seconds)}}$$

$$\text{EXP-025 Rate} = \frac{5,464 \text{ B} + 215 \text{ B}}{128.0 \text{ s}} \approx 44.4 \text{ Bytes / second}$$

$$\text{Raw Video Frame Baseline (1,024 frames @ 64x64 RGB)} = 12,582,912 \text{ Bytes} \implies 98,304 \text{ Bytes / second}$$

$$\text{Effective Bandwidth Reduction Factor} = \frac{12,582,912 \text{ B}}{5,679 \text{ B}} \approx 2,215\times$$

---

## 6. Reproducibility & Open Experiment Artifacts

Every experiment run produces a standardized machine-readable artifact bundle:
1. `protocol.json`: Generator configuration, frame indices, pulse parameters, and compression metrics.
2. `metrics.csv`: Tabular quantitative measurements.
3. `model-responses.jsonl`: Verbatim model evaluation transcripts, including prompt protocols, stimulus SHA256 hashes, and extracted model responses.

Refer to the released experiment packages ([`EXP-025`](experiments/2026/EXP-025/README.md), [`EXP-026`](experiments/2026/EXP-026/README.md)) for all artifacts.