# Dimensional Images: Experiment Log & Falsification Suite

> [!NOTE]
> This document compiles the empirical experiment logs, stimulus parameters, evaluation protocols, and raw blind-test responses for the **Dimensional Images (Visual Latent Transport)** project. It provides reproducible evidence for the claims summarized in the [Research Overview](README.md).

---

## 1. Experiment Overview Index

| Experiment | Focus Area | Container Layout | Key Metric / Result |
| :--- | :--- | :--- | :--- |
| **EXP-023** | 32s Dimensional Video Mosaic V1 | 256x256 Mosaic (4x 128x128 tiles) | 4-slot uniform progression verified; 1,338x compression vs raw. |
| **EXP-024a** | Open-Ended Cognitive Stress Testing | 256x256 Mosaic (4x 128x128 tiles) | Aggregate F1 = 86.5%; 100% Chronology; 100% Object Binding. |
| **EXP-024b** | Long-Horizon Scaling (128.0s / 1,024 frames) | 512x512 Mosaic (16x 128x128 tiles) | Format Parity Delta F1 = 0.000 (L1 vs L3); 22.8% byte savings in L3. |
| **EXP-025** | Long-Horizon Falsification Suite (128s / 512x512) | 512x512 Mosaic (ATW vs Uniform) | Full F1-F6 stress suite; mode contention boundary; honest nullspace calibration. |
| **EXP-026** | Temporal Resolution Boundary & Causal Audit | Single 128x128 Carrier (8.0s, K=12) | Empirical resolution boundary localized at Delta t = 1.50s; 100% causal arrow; energy equivalence distinguished. |

---

## 2. Mathematical Carrier Formalization (E3-K12)

The temporal projection maps a temporal pixel intensity sequence $s(t)$ of length $N = 64$ frames (8.0 seconds at 8 FPS) onto an orthogonal Gram discrete polynomial basis $P_k(t)$:

$$m_k = \sum_{t=0}^{N-1} P_k(t) \cdot s(t), \quad k = 0, \ldots, 11$$

The resulting coefficients $m_k$ are allocated to the carrier sub-quadrants:

1. **Quadrant G ($64 \times 64$):** Baseline spatial frame at slot onset $t = 0$.
2. **Quadrant T ($64 \times 64$):** 
   - Channel R: $P_0$ (Temporal Mean / DC Offset).
   - Channel G: $P_2$ (Curvature / Acceleration / Reversals).
   - Channel B: High-frequency subcarrier modulation.
3. **Quadrant C ($64 \times 64$):**
   - Channel R: $P_1$ (Linear Velocity / Trend).
   - Channel G: Cb chromatic drift.
   - Channel B: Cr chromatic subcarrier.
4. **Quadrant R ($64 \times 64$):** Neutral reference floor (constant intensity 128).

---

## 3. EXP-025: Long-Horizon Falsification Suite (Detailed Protocols)

EXP-025 evaluated 6 stress hypotheses using independent blinded model evaluators.

### F1: Event Density & Salience Thresholds
* **Stimulus:** 128-second timeline containing 10 discrete chromatic beacons distributed across the 16 slots.
* **Empirical Finding:**
  - Evaluator detected all 10 out of 10 events (Recall: 1.0).
  - Minor salience attenuation observed at Slot 11, successfully localized to Stage 3 (cognitive attention threshold) rather than Stage 1 (projection loss) or Stage 2 (compression loss).

### F2: Identity Swap under Occlusion Gap
* **Stimulus:** Two objects (Gold Disc on upper lane $y \approx 20$, Cyan Square on lower lane $y \approx 44$). Both enter a complete visual tunnel occlusion from $t = 28$s to $t = 64$s (36.0s gap). During occlusion, trajectories cross.
* **Empirical Finding:**
  - Objects re-emerged in Slot 8 with swapped lanes.
  - Blind evaluation confirmed lane swap detection (`lane_swap_detected: true`, confidence: 1.0).
  - Object identity preserved without re-identification drift (`identity_maintained_despite_swap: true`).

### F3: Temporal Mode Contention
* **Stimulus:** In Slot 5 (40.0s - 48.0s), 4 rapid chromatic pulses were triggered within 3.0 seconds ($\Delta t = 1.0$s spacing).
* **Empirical Finding:**
  - Carrier container remained structurally intact.
  - Discrete pulses fused into an overlapping Cyan/Magenta superposition (`mode_contention_observed: true`, `distinguishable_burst_count: 0`).
  - **Empirical Boundary:** Within an 8.0s window, micro-events spaced at $\Delta t \le 1.0$s exceed the resolving capacity of the fixed 12-polynomial basis, demonstrating the practical necessity of Adaptive Temporal Windowing (ATW).

### F4: Format Isolation Parity (L1 vs L2 vs L3)
* **Stimulus:** 6 landmark events distributed across the 128-second timeline, evaluated across three formats:
  - **L1:** 16 individual $128 \times 128$ PNG images (Total: 7,076 Bytes).
  - **L2:** 4 sub-mosaics of $256 \times 256$ (Total: 6,036 Bytes).
  - **L3:** 1 unified $512 \times 512$ mosaic (Total: 5,464 Bytes).
* **Empirical Finding:**
  - Retrieval Parity: All 6 landmark events detected identically in L1 and L3 ($\Delta F1 = 0.000$).
  - Container Efficiency: L3 achieved **22.8% byte savings** over L1 while maintaining crisp perceptual boundaries (`sharp_uncompromised`).

### F5: Non-Stationary Adaptive Temporal Windowing (ATW)
* **Stimulus:** Non-stationary video alternating between 48.0s calm drift and rapid high-velocity oscillation bursts.
* **Empirical Finding:**
  - Uniform 8.0s grid suffered significant temporal smearing during dynamic phases (`uniform_temporal_smear_observed: true`).
  - Adaptive partition (`16,16,16,8,8,8,8,8,8,4,4,4,4,8,4,4`) allocated 4.0s slots to bursts, eliminating smearing (`preferred_representation: "adaptive"`).

### F6: Adversarial Nullspace Calibration
* **Stimulus:** Two video sequences differing by $\Delta_{\text{raw}} = 31$ in raw pixel space, perturbed strictly within the orthogonal nullspace complement $(I - P^T P)$ of the Gram polynomial basis.
* **Empirical Finding:**
  - Carrier difference was below perceptual discrimination ($\Delta_{\text{carrier}} \le 2$ LSB, mean absolute difference 0.0004).
  - Blind evaluator correctly recognized mathematical unresolvability (`is_unresolvable_nullspace_collision: true`, `uncertainty_honestly_calibrated: true`, confidence: 0.0). No false hallucinations were generated.

---

## 4. EXP-026: Empirical Temporal Resolution Boundary Audit

To resolve the peer-review question raised by ChatGPT regarding whether temporal event separation possesses a hard boundary or a continuous transition, EXP-026 isolated the fundamental 2-pulse discrimination problem in a single $128 \times 128$ carrier (8.0s @ 8 FPS, $K=12$ modes).

### S1: Two Identical Pulses (Separation Matrix Sweep)
Evaluated across 6 discrete time deltas:

| Delta t | Frame Delta | Perceptual Regime | Structural Pattern in Quadrant C | Classification |
| :--- | :--- | :--- | :--- | :--- |
| **0.25 s** | 2 frames | Sub-Rayleigh coherence | Unimodal vertical stripe, identical to single pulse | `fused_single` |
| **0.50 s** | 4 frames | Sub-Rayleigh coherence | Unimodal vertical stripe, zero discernible interference | `fused_single` |
| **1.00 s** | 8 frames | Spectral phase interference | Desaturation / destructive phase cancellation, unimodal topology | `fused_single` |
| **1.50 s** | 12 frames | **Bimodal bifurcation** | **Split into 2 distinct symmetrical lobes, doubled line density** | `separable_double` |
| **2.00 s** | 16 frames | High-order interference | 4-column interference grid clearly separated | `separable_double` |
| **3.00 s** | 24 frames | Fully resolved regime | Wide spatial separation across temporal subcarrier | `separable_double` |

* **Empirical Resolution Limit:** Exactly **$\Delta t = 1.50$ seconds** (12 frames at 8 FPS) under the standard E3-K12 configuration.
* **Spectral Interference Onset:** Phase interference is detectable as destructive desaturation starting at $\Delta t = 1.00$s.

| Fused Single ($\Delta t = 0.25$s) | Bifurcation Boundary ($\Delta t = 1.50$s) | Separated Double ($\Delta t = 3.00$s) |
| :---: | :---: | :---: |
| ![Delta 0.25s](exp026_delta_0_25s.png) | ![Delta 1.50s](exp026_delta_1_50s.png) | ![Delta 3.00s](exp026_delta_3_00s.png) |

### S2: Causal Chronology & Arrow of Time
* **Test:** Pulse 1 (Cyan) $\to$ Pulse 2 (Magenta) vs Pulse 1 (Magenta) $\to$ Pulse 2 (Cyan).
* **Empirical Finding:** Evaluator correctly identified temporal order in both directions with **100% accuracy** (`causal_arrow_of_time_preserved: true`, confidence: 1.0).
* **Mechanism:** Quadrant C exhibits a strict 180° phase inversion in the odd Gram polynomial coefficients ($P_1$, $P_3$), preserving causal chronology unambiguously.

### S3: Integral Energy Equivalence Discrimination
* **Test:** 1 broad continuous pulse vs 2 discrete pulses with **mathematically identical integrated energy** ($\int I^2 dt$).
* **Empirical Finding:** Evaluator distinguished both conditions with **98% confidence** (`distinguishable_from_integral: true`).
* **Mechanism:** Single pulse yields smooth, unimodal $P_2$ response; double pulse generates strong bimodal curvature in Quadrant T (Green channel) and high-frequency Gram subcarrier modulation (Blue channel).

### S4: Window Position Invariance
* **Test:** Identical pulse pair ($\Delta t = 1.0$s) positioned early ($t = 1.5$s), mid ($t = 4.0$s), and late ($t = 6.5$s) in the 8-second window.
* **Empirical Finding:** All three positions achieved `high` salience with **zero boundary attenuation** (`position_invariance_confirmed: true`, confidence: 0.99).
* **Mechanism:** Temporal position is encoded continuously as a smooth chromatic phase shift (warm orange/lime $\to$ magenta/teal $\to$ cool violet/cyan) across the polynomial basis.

---

## 5. Transmission & Bitrate Metrics

$$\text{Continuous Streaming Rate} = \frac{\text{Container Payload (Bytes)} + \text{Sidecar Metadata (Bytes)}}{\text{Timeline Duration (Seconds)}}$$

$$\text{EXP-025 Rate} = \frac{5,464 \text{ B} + 230 \text{ B}}{128.0 \text{ s}} \approx 44.5 \text{ Bytes / second}$$

$$\text{Raw Video Frame Baseline (1,024 frames @ 64x64 RGB)} = 12,582,912 \text{ Bytes} \implies 98,304 \text{ Bytes / second}$$

$$\text{Effective Bandwidth Reduction Factor} = \frac{12,582,912 \text{ B}}{5,694 \text{ B}} \approx 2,210\times$$

---

[Back to Research Overview](README.md) · [Evidence Verification Mode (EVM)](../evidence-verification-mode-evm/README.md)