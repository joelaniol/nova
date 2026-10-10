# Limitations, Failure Modes & Boundary Analysis

**Project:** Dimensional Images  
**Document:** Boundary Analysis & Empirical Falsification Report (V1.1)  
**Date:** 2026-10-10  
**Lead:** Joel Aniol  
**Classification:** `[PROVED]` (Nullspace & Dimension Theorems) / `[EMPIRICAL-VLM]` (Observed Thresholds)  

---

## 1. Mathematical Nullspace Indeterminacy

### 1.1 Theorem on Orthogonal Information Loss
Let $\mathbf{s} \in \mathbb{R}^N$ represent a discrete pixel trajectory over $N$ frames, and let $P \in \mathbb{R}^{K \times N}$ be the orthonormal Gram polynomial projection matrix with $K < N$, satisfying $P P^T = I_K$.

The projection operator induces an exact orthogonal nullspace complement on $\mathbb{R}^N$:

$$\mathcal{N} = \ker(P) = \{ \mathbf{v} \in \mathbb{R}^N : P \mathbf{v} = \mathbf{0} \}$$

with dimension:

$$\dim(\mathcal{N}) = N - K$$

For an arbitrary temporal perturbation vector $\mathbf{u} \in \mathbb{R}^N$, the projection onto the nullspace is constructed via the orthogonal complement operator:

$$\Delta \mathbf{s} = (I_N - P^T P) \mathbf{u}, \quad \mathbf{u} \in \mathbb{R}^N$$

Applying the projection operator $P$ confirms:

$$P \Delta \mathbf{s} = P (I_N - P^T P) \mathbf{u} = (P - (P P^T) P) \mathbf{u} = (P - I_K P) \mathbf{u} = \mathbf{0}$$

For the standard E3-K12 configuration with $N = 64$ frames (8.0s @ 8 FPS) and $K = 12$ polynomial modes:

$$\dim(\mathcal{N}) = 64 - 12 = 52$$

### 1.2 Physical Consequences & Complete Carrier Nuance
1. **Unresolvable High-Frequency Modulations:** Any temporal variation $\Delta \mathbf{s} \in \mathcal{N}$ produces exactly zero projection response ($\mathbf{m}_{\Delta} = \mathbf{0}$).
2. **Carrier Bit-Identity Nuance:** The Gram projection coefficients govern dynamic Quadrants T and C. However, Quadrant G stores the spatial base frame $S(x, y, 0)$. Two distinct video sequences produce bit-identical complete carriers if and only if:
   $$\Delta \mathbf{s} \in \ker(P) \quad \text{AND} \quad \Delta \mathbf{s}(0) = \mathbf{0}$$
   If $\Delta \mathbf{s}(0) \neq \mathbf{0}$, Quadrants T and C remain identical, but Quadrant G will differ by the initial frame delta.
3. **Quantization Collapse:** In EXP-025 (F6), adversarial perturbations in raw video differed by $>30$ raw pixel values ($>11\%$ full scale), yet produced carrier differences of $\le 2$ LSB after 8-bit quantization and WebP compression.
4. **Requirement for Honest Uncertainty Calibration:** A multimodal system evaluating such carriers must recognize mathematical unresolvability. In blind evaluations (EXP-025 F6), blinded models correctly reported `0.0 confidence` and flagged `unresolvable_nullspace_collision: true`, preventing false hallucinations.

---

## 2. Empirical Temporal Resolution Boundaries

A central finding of EXP-025 and EXP-026 is that a fixed polynomial basis possesses a practical temporal resolution limit below which discrete events cannot be resolved as separate occurrences by a Vision-Language Model.

```
       0.0s          0.5s          1.0s          1.5s          2.0s          3.0s
Delta t: |-------------|-------------|-------------|-------------|-------------|
Status:  [    Fused Single Mode     ] [Phase Shift] [ Bimodal   ] [ Separated ]
         (Coherent Fusion)            (Desatur.)     (Bifurcation) (Fringe Grid)
```

### 2.1 Summary of Transition Phases (8.0s Window @ 8 FPS)
* **$\Delta t \le 0.50\text{s}$ (2–4 frames): Coherent Fusion (`fused_single`).** The two impulses collapse into a single coherent wavepacket in Quadrant C. Projection energy remains unimodal; individual event identification is physically impossible for the VLM.
* **$\Delta t = 1.00\text{s}$ (8 frames): Destructive Phase Interference.** At this spacing, the two pulses induce destructive phase cancellation, desaturating vibrant magenta/green tones into muted pastels. However, spatial topology remains unimodal without a distinct second peak (`fused_single`).
* **$\Delta t = 1.50\text{s}$ (12 frames): Bimodal Bifurcation (`separable_double`).** The empirical separation threshold is reached. Quadrant C exhibits a vertical midline dividing the carrier into two symmetric lobes with doubled fringe density. Blinded subagents detect two separable pulses with 0.92 confidence.
* **$\Delta t \ge 2.00\text{s}$ (16–24 frames): Fully Resolved Multimodal Fringe Grid.** The signal bifurcates into a 4-column interference grid with high perceptual salience.

### 2.2 Critical Scientific Qualifications
> [!WARNING]
> The observed transition threshold at $\Delta t = 1.50\text{s}$ is an **empirical boundary specific to the evaluated E3-K12 configuration** ($N=64$, $K=12$, 8.0s duration, 8 FPS, evaluated via frontier VLMs).
>
> 1. **Mathematical Projection vs. VLM Perception:** The underlying Gram projection coefficients already exhibit subtle differences at $\Delta t = 0.50\text{s}$ (e.g. shifts in high-order mode energy ratios). The fusion into `fused_single` represents a limitation of VLM visual perception over the quantized carrier, not necessarily a total collapse of continuous projection mathematics.
> 2. **Descriptive Analogies:** The terms *"Sub-Rayleigh Coherence"* and *"Bimodal Bifurcation"* are descriptive qualitative analogies for the visual carrier pattern transitions; they do not represent formal analytic derivations of classical optical diffraction limits or dynamical system bifurcations.
> 3. **Non-Universal Constant:** Changing the frame rate $f_s$, increasing the mode count $K$, or adopting local wavelet subcarriers can shift this boundary.

---

## 3. High-Order Modal Contention

When more than two high-frequency micro-transients occur within a single 8.0s slot (e.g. 4 micro-bursts with $\Delta t \approx 1.0\text{s}$ in EXP-025 F3), the single high-order subcarrier channel (Quadrant T Blue channel, Quadrant C Blue channel) experiences **modal superposition contention**:

* The carrier remains structurally intact (no clipping or image corruption).
* However, individual micro-bursts blend into composite chromatic hues, preventing distinct enumeration of individual pulse counts.
* **Remedy:** Adaptive Temporal Windowing (ATW) partitions high-entropy dynamic phases into shorter slots (e.g., 4.0s or 2.0s), restoring distinct temporal modes.

---

## 4. Vision Transformer (ViT) Patch Alignment & Attention Smoothing

Multimodal foundation models process images by dividing them into uniform non-overlapping patches (typically $14 \times 14$ or $16 \times 16$ pixels):

1. **Quadrant Boundary Misalignment:** In a 128x128 carrier, 64x64 quadrants align cleanly with 16x16 patches ($4 \times 4$ patches per quadrant). However, for $14 \times 14$ patch tokenizers (e.g., standard ViT-L/14), patch boundaries straddle the quadrant seams ($64 / 14 \approx 4.57$), inducing spatial cross-attention bleeding between Quadrant G (geometry) and Quadrant T (kinematics).
2. **Self-Attention Smoothing:** Self-attention layers in early vision blocks can diffuse high-frequency carrier fringes, slightly attenuating weak subcarriers unless adequate contrast gain $\gamma_k$ is applied.

---

## 5. Model Dependency of Vision Token Costs

While Dimensional Images drastically reduces token overhead compared to raw video, exact token consumption depends entirely on the host model's proprietary vision ingestion pipeline:

* **OpenAI (GPT-4o):** Images are scaled and tiled into $512 \times 512$ patches. A single 512x512 mosaic consumes ~256 to 765 tokens depending on detail mode.
* **Anthropic (Claude 3.5 Sonnet):** Dynamic aspect-ratio tiling generates token counts proportional to pixel dimensions.
* **Google (Gemini 1.5/2.0):** Multiscale hierarchical patch tokenization produces model-specific token counts.

Consequently, statements of token savings must cite specific benchmark architectures rather than claiming universal token counts.

---

## 6. Summary of Empirical Boundaries

| Phenomenon | Boundary / Limit | Scientific Mechanism | Practical Mitigation |
| :--- | :--- | :--- | :--- |
| **High-Frequency Nullspace** | 52 dimensions ($N=64, K=12$) | Orthogonal projection complement $(I_N - P^T P) \mathbf{u} = \mathbf{0}$ | Explicit uncertainty calibration; EVM verification |
| **Temporal Bimodal Separation** | $\Delta t \in (1.00\text{s}, 1.50\text{s}]$ | Modal phase overlap in Gram basis | Adaptive Temporal Windowing (ATW) |
| **Dense Micro-Transient Contention** | $>3$ pulses per 8.0s slot | High-order subcarrier superposition | Energy-guided slot splitting |
| **Quantization Noise Floor** | $\Delta \le 2$ LSB | 8-bit dynamic range clipping | Calibrated mode gain vector $\gamma_k$ |
| **Vision Token Ingestion** | Model-dependent (~256 tokens) | Proprietary ViT patch architectures | Standardized 512x512 container dimension |
