# Methodology: Mathematical Foundations of Visual Latent Transport

**Project:** Dimensional Images  
**Document:** Methodology & Theoretical Specification (V1.0)  
**Date:** 2026-10-10  
**Lead:** Joel Aniol  
**Classification:** `[PROVED]` (Mathematical Derivations) / `[NUMERICAL]` (Quantization Bounds)  

---

## 1. Mathematical Formulation

Let continuous video be represented by a spatiotemporal color signal:

$$S(x, y, t) \in \mathbb{R}^{H \times W \times 3}, \quad t \in [0, T]$$

where $(x, y)$ denotes the spatial image coordinate, and $t$ denotes continuous time over duration $T$.

Under uniform discrete temporal sampling at frame rate $f_s$, the video sequence consists of $N = \lfloor T \cdot f_s \rfloor$ frames:

$$S_n(x, y) = S(x, y, n / f_s), \quad n \in \{0, 1, \dots, N-1\}$$

Standard multimodal Vision-Language Models (VLMs) cannot ingest continuous tensors or raw video streams without linear token scaling ($O(N)$ vision patches). **Visual Latent Transport (VLT)** projects the temporal dimension $n \in \{0, \dots, N-1\}$ onto a low-dimensional orthonormal functional basis, packing the projection coefficients into a compact, synthetic 2D visual carrier image $C(u, v) \in \{0, \dots, 255\}^{H_c \times W_c \times 3}$.

---

## 2. Discrete Gram Orthogonal Polynomial Basis

To eliminate spectral leakage associated with standard Fourier bases on short non-periodic finite intervals, VLT employs discrete orthogonal Gram polynomials (Chebyshev polynomials of a discrete variable).

### 2.1 Orthonormality Definition
A discrete polynomial basis $\{P_k(n)\}_{k=0}^{K-1}$ of degree $k$ over $N$ discrete sample points satisfies:

$$\sum_{n=0}^{N-1} P_j(n) P_k(n) = \delta_{jk} = \begin{cases} 1 & \text{if } j = k \\ 0 & \text{if } j \neq k \end{cases}$$

### 2.2 Discrete Recurrence Relation
The basis polynomials are constructed via the standard three-term recurrence:

$$P_0(n) = \frac{1}{\sqrt{N}}$$

$$P_1(n) = \sqrt{\frac{12}{N(N^2 - 1)}} \left(n - \frac{N - 1}{2}\right)$$

$$P_{k+1}(n) = \alpha_k \left(n - \frac{N - 1}{2}\right) P_k(n) - \beta_k P_{k-1}(n)$$

where normalization coefficients $\alpha_k$ and $\beta_k$ are chosen such that $\|P_k\|_2 = 1$.

### 2.3 Temporal Projection
For any spatial pixel channel $s(n) = S_n(x, y)$, the $k$-th temporal projection coefficient $m_k$ is defined by:

$$m_k(x, y) = \sum_{n=0}^{N-1} P_k(n) s(n), \quad k \in \{0, 1, \dots, K-1\}$$

In matrix notation, letting $P \in \mathbb{R}^{K \times N}$ denote the projection matrix with rows $P_k$:

$$\mathbf{m}(x, y) = P \mathbf{s}(x, y)$$

### 2.4 Energy Conservation & Parseval Identity
By orthonormality, the total energy captured by the $K$ coefficients satisfies Bessel's inequality:

$$\sum_{k=0}^{K-1} m_k(x, y)^2 \le \sum_{n=0}^{N-1} s(n)^2 = \|\mathbf{s}(x, y)\|_2^2$$

Equality holds if and only if the temporal signal $\mathbf{s}(x, y)$ lies entirely within the subspace spanned by $\{P_0, \dots, P_{K-1}\}$.

### 2.5 The Orthogonal Nullspace
Since $K < N$ (in E3-K12, $K=12$ modes for $N=64$ frames), the projection operator $P$ induces an exact $(N - K)$-dimensional nullspace $\mathcal{N}$:

$$\dim(\mathcal{N}) = N - K = 64 - 12 = 52$$

Any temporal perturbation $\Delta \mathbf{s} \in \mathcal{N}$ satisfies:

$$P \Delta \mathbf{s} = \mathbf{0}$$

Consequently, two distinct video signals $S_A(t)$ and $S_B(t)$ whose difference $\Delta \mathbf{s} = S_A - S_B$ lies within $\mathcal{N}$ produce mathematically identical projection coefficients:

$$\mathbf{m}_A(x, y) = \mathbf{m}_B(x, y)$$

This property is fundamental to the honest uncertainty calibration demonstrated in EXP-025 (F6).

---

## 3. The E3-K12 Carrier Architecture

The E3-K12 specification maps a continuous 8.0-second video block ($N=64$ frames @ 8 FPS) into a single 128x128 pixel visual carrier tile partitioned into four 64x64 quadrants:

```
+---------------------------+---------------------------+
|                           |                           |
|        Quadrant G         |        Quadrant T         |
|      (Geometric Base)     |    (Temporal Kinematics)  |
|          [64x64]          |          [64x64]          |
|                           |                           |
+---------------------------+---------------------------+
|                           |                           |
|        Quadrant C         |        Quadrant R         |
|    (Chromatic Dynamics)   |    (Calibration Floor)    |
|          [64x64]          |          [64x64]          |
|                           |                           |
+---------------------------+---------------------------+
```

### 3.1 Quadrant Allocation Specification

| Quadrant | Coordinate Range | Channel | Mathematical Mapping | Physical Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| **G (Geometric)** | $u \in [0, 63], v \in [0, 63]$ | R, G, B | $S(x, y, 0)$ mapped to RGB | **Base Scene State:** High-resolution spatial snapshot at window onset ($t=0$). Anchors object geometry and background layout. |
| **T (Temporal)** | $u \in [64, 127], v \in [0, 63]$ | **R** | $m_0 = \sum P_0(n) Y(n)$ | **Mean Luminance (P0):** Time-averaged scene brightness. |
| | | **G** | $m_2 = \sum P_2(n) Y(n)$ | **Curvature / Acceleration (P2):** Detects velocity reversals, pulse counts, and bimodal bifurcations. |
| | | **B** | $\sum_{k=3}^{11} w_k m_k Y(n)$ | **High-Order Transient Subcarrier:** Weighted superposition of micro-transients and oscillations. |
| **C (Chromatic)** | $u \in [0, 63], v \in [64, 127]$ | **R** | $m_1^{Cb} = \sum P_1(n) Cb(n)$ | **Linear Color Trend (P1):** Determines temporal arrow of time (e.g. Cyan $\to$ Magenta vs Magenta $\to$ Cyan). |
| | | **G** | $m_0^{Cb} - Cb(0)$ | **Chromatic Drift:** Net color migration over duration. |
| | | **B** | $\sum_{k=2}^{11} w_k m_k^{Cr}$ | **Chrominance High-Order Subcarrier:** Cr-channel transients and beacon flares. |
| **R (Reference)** | $u \in [64, 127], v \in [64, 127]$ | R, G, B | Uniform constant 128 | **Calibration Floor:** Neutral reference floor enabling invariant contrast calibration across varying VLM backbones. |

### 3.2 Dynamic Range Mapping & Quantization
Raw projection coefficients $m_k \in \mathbb{R}$ are quantized to 8-bit unsigned integers $Q(m_k) \in [0, 255]$:

$$Q(m_k) = \text{clip}\left(\left\lfloor 128 + \gamma_k \cdot m_k \right\rceil, 0, 255\right)$$

where $\gamma_k$ is a calibrated mode-dependent gain vector preserving high-frequency transient fidelity without clipping low-order polynomials.

---

## 4. Dimensional Video Mosaic (128.0-Second Integration)

To represent multi-minute timelines, 16 individual 128x128 E3-K12 carriers are tiled into a unified **512x512 Mosaic**:

$$\text{Mosaic}(U, V) \in \{0, \dots, 255\}^{512 \times 512 \times 3}$$

### 4.1 Temporal Slot Indexing
The 16 slots are arranged in a 4x4 temporal raster grid:

$$\text{Slot } s = 4 \cdot \text{Row} + \text{Col}, \quad s \in \{0, 1, \dots, 15\}$$

$$\text{Time Interval: } t \in [s \cdot 8.0\text{s}, (s + 1) \cdot 8.0\text{s}]$$

### 4.2 Boundary Continuity Principle
Because Quadrant G of slot $s+1$ encodes $S(x, y, t = (s+1) \cdot 8.0\text{s})$, the terminal state of slot $s$ is directly adjacent to the initial state of slot $s+1$. In blind evaluations (EXP-024b, EXP-025), models reliably trace continuous trajectories across slot transitions without trajectory fragmentation.

---

## 5. Adaptive Temporal Windowing (ATW)

Uniform temporal allocation ($T = 8.0\text{s}$ per slot) suffers from temporal smearing when video contains rapid, non-stationary bursts. The **Adaptive Temporal Windowing (ATW)** engine computes the temporal activity entropy $\mathcal{E}(t)$:

$$\mathcal{E}(t) = \int_{\Omega} \left| \frac{\partial S(x, y, t)}{\partial t} \right|^2 dx dy$$

When dynamic bursts are detected ($\mathcal{E}(t) > \theta_{\text{dynamic}}$), the window allocator dynamically partitions the timeline:
* **High-activity burst:** $T_{\text{slot}} = 4.0\text{s}$ (allocates 2 slots to resolve sub-second transients).
* **Nominal activity:** $T_{\text{slot}} = 8.0\text{s}$ (standard E3-K12 configuration).
* **Quiescent / Static drift:** $T_{\text{slot}} = 16.0\text{s}$ (merges quiescent intervals to save token and container budget).

The total mosaic remains strictly 512x512, preserving deterministic spatial compatibility.

---

## 6. Compact Sidecar Protocol (`dimensional-mosaic-compact-v1`)

To guarantee zero-ambiguity model decoding without bloating token overhead, every mosaic is accompanied by a standardized, ultra-compact JSON sidecar (230 bytes):

```json
{
  "version": "dimensional-mosaic-compact-v1",
  "grid": [4, 4],
  "timeline_sec": [0.0, 128.0],
  "slots": 16,
  "slot_durations_sec": [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0],
  "quadrant_layout": {
    "G": [0, 0],
    "T": [0, 1],
    "C": [1, 0],
    "R": [1, 1]
  }
}
```

This sidecar specifies the exact duration and coordinate mapping for each slot, decoupling model inference from any hardcoded assumptions.
