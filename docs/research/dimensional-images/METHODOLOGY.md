# Methodology: Mathematical Foundations of Visual Latent Transport

**Project:** Dimensional Images  
**Document:** Methodology & Theoretical Specification (V1.2)  
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

In matrix notation, letting $P \in \mathbb{R}^{K \times N}$ denote the projection matrix with rows $P_k$:

$$P P^T = I_K$$

### 2.2 Discrete Recurrence & Normalization
The basis polynomials are constructed via the standard three-term recurrence:

$$P_0(n) = \frac{1}{\sqrt{N}}$$

$$P_1(n) = \sqrt{\frac{12}{N(N^2 - 1)}} \left(n - \frac{N - 1}{2}\right)$$

$$P_{k+1}(n) = \alpha_k \left(n - \frac{N - 1}{2}\right) P_k(n) - \beta_k P_{k-1}(n)$$

where normalization coefficients $\alpha_k$ and $\beta_k$ are chosen such that $\|P_k\|_2 = 1$. The sign convention is anchored such that $P_1(N-1) > 0$, $P_2(0) > 0$ (convex parabola), and $P_k(N-1) > 0$ for $k \ge 3$.

### 2.3 Temporal Projection
For centered pixel luminance $y(n) = Y_n(x, y) - 128.0$, the $k$-th temporal projection coefficient $M_k$ is computed by:

$$M_k(x, y) = \sum_{n=0}^{N-1} P_k(n) \cdot y(n), \quad k \in \{0, 1, \dots, K-1\}$$

In vector notation:

$$\mathbf{M}(x, y) = P \mathbf{y}(x, y)$$

### 2.4 Energy Conservation & Bessel Inequality
By orthonormality, the energy captured by the $K$ coefficients satisfies:

$$\sum_{k=0}^{K-1} M_k(x, y)^2 \le \sum_{n=0}^{N-1} y(n)^2 = \|\mathbf{y}(x, y)\|_2^2$$

### 2.5 The Orthogonal Nullspace Complement
Since $K < N$ ($K=12$ modes for $N=64$ frames in E3-K12), the projection operator $P \in \mathbb{R}^{K \times N}$ induces an exact $(N - K)$-dimensional nullspace $\mathcal{N} = \ker(P)$ on $\mathbb{R}^N$:

$$\dim(\mathcal{N}) = N - K = 64 - 12 = 52$$

For an arbitrary temporal sequence $\mathbf{u} \in \mathbb{R}^N$, its projection onto the nullspace is formed by the orthogonal complement operator:

$$\Delta \mathbf{s} = (I_N - P^T P) \mathbf{u}$$

Because $P P^T = I_K$:

$$P \Delta \mathbf{s} = P(I_N - P^T P)\mathbf{u} = (P - P P^T P)\mathbf{u} = (P - I_K P)\mathbf{u} = \mathbf{0}$$

Consequently, two distinct video signals $S_A(t)$ and $S_B(t)$ whose difference lies in $\mathcal{N}$ produce mathematically identical Gram projection coefficients.

---

## 3. The E3-K12 Spatial Carrier Specification

The E3-K12 specification maps a continuous 8.0-second video block ($N=64$ frames @ 8 FPS, $H=64, W=64$) into a single 128x128 pixel visual carrier tile partitioned into four 64x64 quadrants:

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

### 3.1 Mode Normalization & Dynamic Range Mapping
To avoid clipping while preserving faint transients, projection coefficients $M_k \in \mathbb{R}$ are normalized using a calibrated saturation divisor ($D = 35.0$):

$$m_k^{\text{norm}}(x, y) = \text{clip}\left(\frac{M_k(x, y)}{35.0}, -1.0, 1.0\right)$$

### 3.2 Exact Quadrant Encoding Equations

#### 1. Quadrant G (Geometric Base State, $[0:64, 0:64]$)
Anchors initial scene geometry at $t=0$:
$$Q_G(x, y, c) = \text{clip}(Y_0(x, y), 0, 255), \quad c \in \{R, G, B\}$$

#### 2. Quadrant T (Temporal Kinematics, $[0:64, 64:128]$)
Encodes luminance mean, curvature, and odd high-order subcarriers:
* **Channel 0 (Red):** Mean intensity offset ($P_0$):
  $$T_R(x, y) = \text{clip}\left(128.0 + 90.0 \cdot m_0^{\text{norm}}(x, y), 0, 255\right)$$
* **Channel 1 (Green):** Temporal curvature / acceleration ($P_2$):
  $$T_G(x, y) = \text{clip}\left(128.0 + 90.0 \cdot m_2^{\text{norm}}(x, y), 0, 255\right)$$
* **Channel 2 (Blue):** Odd high-order subcarrier modulation ($k \in \{3, 5, 7, 9, 11\}$):
  $$T_B(x, y) = \text{clip}\left(128.0 + \sum_{j=0}^{|\text{odd}|-1} m_{k_j}^{\text{norm}}(x, y) \cdot \frac{80.0}{\sqrt{|\text{odd}|}} \cdot W_{j+1}(x, y), 0, 255\right)$$
  where $W_j(x, y) \in \{-1, +1\}$ are 2D Walsh orthogonal block bases over the $64 \times 64$ grid.

#### 3. Quadrant C (Chromatic Dynamics & False-Color Multiplexing, $[64:128, 0:64]$)
Quadrant C encodes the luminance linear temporal trend mode ($P_1$) and even high-order luminance subcarriers ($k \in \{4, 6, 8, 10\}$) by mapping them onto the chrominance channels (Cb and Cr) via **false-color carrier multiplexing**:
* **Cb Channel:** Linear trend ($P_1$):
  $$Cb(x, y) = \text{clip}\left(128.0 + 90.0 \cdot m_1^{\text{norm}}(x, y), 0, 255\right)$$
* **Cr Channel:** Even high-order subcarriers ($k \in \{4, 6, 8, 10\}$):
  $$Cr(x, y) = \text{clip}\left(128.0 + \sum_{j=0}^{|\text{even}|-1} m_{k_j}^{\text{norm}}(x, y) \cdot \frac{80.0}{\sqrt{|\text{even}|}} \cdot W_{j+1}(x, y), 0, 255\right)$$
* **Luminance Floor:** $Y_C(x, y) = 128.0$.
* The composite $(Y_C, Cb, Cr)$ layer is mapped to RGB via standard BT.601 conversion.
* *Implementation Note:* In the current E3-K12 reference architecture, Quadrant C functions as a false-color carrier to visually represent temporal gradients and even-mode activity for the VLM. Full spatiotemporal chrominance projection (projecting native Cb and Cr channels across time) is defined as a planned architectural extension.

#### 4. Quadrant R (Reference Floor, $[64:128, 64:128]$)
Invariant neutral baseline:
$$Q_R(x, y, c) = 128, \quad c \in \{R, G, B\}$$

### 3.3 Model Attribution & Evaluation Transparency

The Vision-Language Models GPT-4o, Claude, and Gemini are referenced in this working paper as illustrative examples of multimodal model architectures and potential deployment target platforms. Their citation does not imply that they participated directly in the reported experiments.

The visual evaluations in EXP-025 and EXP-026 were performed by independently invoked AI evaluation subagents operating within the Antigravity agentic runtime with direct multimodal image inspection capabilities. Their exact underlying model configurations, prompts, and execution transcripts are permanently preserved in the repository experiment archives (`experiments/2026/`).

ChatGPT contributed methodological review, mathematical criticism, adversarial stress-testing, and examination of published experimental documentation and results. This review constitutes independent theoretical and editorial critique, not an independent visual blind-test replication.

Future experiment records (EXP-027+) will explicitly document the model provider, exact model identifier, API snapshot/version where available, evaluation timestamp, blind-test prompts, input image checksums, and decoding configuration.

---

## 4. Dimensional Video Mosaic (128.0-Second Integration)

To encode multi-minute timelines, 16 individual 128x128 E3-K12 carriers are tiled into a unified **512x512 Mosaic**:

$$\text{Mosaic}(U, V) \in \{0, \dots, 255\}^{512 \times 512 \times 3}$$

### 4.1 Temporal Slot Indexing
The 16 slots are arranged in a 4x4 temporal raster grid:

$$\text{Slot } s = 4 \cdot \text{Row} + \text{Col}, \quad s \in \{0, 1, \dots, 15\}$$

$$\text{Time Interval: } t \in [t_{\text{start}}(s), t_{\text{end}}(s)]$$

### 4.2 Boundary Continuity Principle
Because Quadrant G of slot $s+1$ encodes $S(x, y, t = t_{\text{start}}(s+1))$, the terminal state of slot $s$ is directly adjacent to the initial state of slot $s+1$. In blind evaluations (EXP-024b, EXP-025), models reliably trace continuous trajectories across slot transitions without trajectory fragmentation.

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

To guarantee zero-ambiguity model decoding without bloating token overhead, every mosaic is accompanied by a standardized, ultra-compact JSON sidecar (215–230 bytes minified):

### 6.1 Exact Transmitted Minified JSON (215 Bytes)
```json
{"format":"dimensional-mosaic-compact-v1","fps":8,"total_duration_sec":128.0,"layout":[4,4],"carrier_size":[128,128],"mosaic_size":[512,512],"encoding":"E3-K12","partition_code":"16,16,16,8,8,8,8,8,8,4,4,4,4,8,4,4"}
```

### 6.2 Schema Definition
* `format` (string): Protocol version identifier (`"dimensional-mosaic-compact-v1"`).
* `fps` (int): Sampling frame rate of original video.
* `total_duration_sec` (float): Total temporal coverage across all slots.
* `layout` ([int, int]): Grid dimensions $[rows, cols]$ ($[4, 4]$ for 16 slots).
* `carrier_size` ([int, int]): Single tile resolution ($[128, 128]$).
* `mosaic_size` ([int, int]): Composite container resolution ($[512, 512]$).
* `encoding` (string): Basis specification (`"E3-K12"`).
* `partition_code` (string): Comma-separated list of individual slot durations in seconds.
