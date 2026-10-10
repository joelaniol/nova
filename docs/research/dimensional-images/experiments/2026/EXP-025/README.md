# EXP-025: Long-Horizon Generalization, Stress-Testing & Falsification Suite

**Date:** 2026-10-09  
**Status:** Evaluated & Ratified (ADR-028)  
**Evidence Tier:** `[EMPIRICAL-VLM]` / `[PROVED]` (F6 Nullspace)  
**Container Geometry:** 512x512 Dimensional Video Mosaic (16 Slots, 128x128 each)  
**Timeline Duration:** 128.0 seconds (1,024 frames @ 8 FPS)  
**Sidecar Format:** `dimensional-mosaic-compact-v1` (230 bytes)  

---

## 1. Overview & Objective

EXP-025 evaluates the scalability, perceptual fidelity, and failure boundaries of the 512x512 Dimensional Video Mosaic across 128.0 seconds of continuous video. Rather than evaluating only cooperative scenarios, this experiment executes an adversarial 6-family falsification stress suite designed to systematically break the encoding.

### Primary Artifacts in this Directory:
* `protocol.json`: Full machine-readable experiment protocol, clip energies, WebP distortions, and per-event loss attributions.
* `model-responses.jsonl`: Complete, unedited responses from 6 independent blinded subagents evaluated on visual carrier stimuli.

---

## 2. The 6 Falsification Families

### F1: Event Density & Cognitive Attention Limits
* **Hypothesis:** Packing 10 discrete beacon transients across 128s causes token attention exhaustion or missed detections.
* **Result:** **Recall = 1.0 (10/10 events detected)**. 8 high salience, 1 medium, 1 low.
* **Loss Attribution:** Perceptual degradation is governed by VLM cognitive attention span, not carrier channel capacity.

### F2: Object Identity Swap under 36.0s Tunnel Occlusion
* **Hypothesis:** Long visual disappearance (>30s) causes identity loss and lane confusion when objects cross paths behind occluders.
* **Result:** **100% Identity Preservation & Swap Detection**. Gold disc (upper $\to$ lower) and Cyan square (lower $\to$ upper) tracked correctly without drift.

### F3: Temporal Mode Contention Boundary
* **Hypothesis:** Micro-transients with $\Delta t \le 1.0\text{s}$ in a single 8.0s slot collide within high-order Gram polynomial modes.
* **Result:** **Mode Contention Observed**. 4 rapid micro-bursts within 3.0s fuse into chromatic superposition in Quadrant C/T. Identified as an empirical resolution boundary for static 8.0s slots, establishing the necessity of Adaptive Temporal Windowing (ATW).

### F4: Format Isolation & Degradation Parity (L1 vs L2 vs L3)
* **Hypothesis:** Storing 16 slots in a single 512x512 mosaic (L3) degrades retrieval accuracy compared to 16 individual 128x128 tiles (L1) or 4 sub-mosaics (L2).
* **Result:** **$\Delta \text{F1} = 0.000$ (Zero Format Degradation)**. All 6 landmark events detected identically across all conditions, while L3 saves **22.8% container bytes** (5,464 B vs 7,076 B).

### F5: Non-Stationary Adaptive Temporal Windowing (ATW) Stress
* **Hypothesis:** Uniform 8.0s windows blur turbulent dynamic phases, whereas ATW dynamic budget allocation restores crisp edge resolution.
* **Result:** **ATW Advantage Confirmed (`preferred: adaptive`)**. High-velocity flurries resolved with sharp modal boundaries.

### F6: Adversarial Nullspace Calibration
* **Hypothesis:** Video modifications orthogonal to the 12-polynomial basis ($(I - P P^T)$) test model uncertainty honesty.
* **Result:** **0.0 Confidence / Unresolvability Acknowledged**. When raw video varies by >30 LSB but carrier difference is $\le 2$ LSB, the model correctly identifies mathematical indeterminacy rather than hallucinating false facts.

---

## 3. Quantitative Compression Metrics

| Metric | Raw Uncompressed Video | L1 Individual Tiles | L3 Mosaic + Compact Sidecar |
| :--- | :--- | :--- | :--- |
| **Payload Size** | 12,582,912 Bytes | 7,076 Bytes (WebP) | **5,464 Bytes (WebP) + 230 B Sidecar** |
| **Streaming Bitrate** | 98,304 B/s | 55.3 B/s | **42.5 B/s (mosaic payload) / 44.5 B/s (incl. sidecar)** |
| **Compression Ratio** | 1.0x | 1,778x | **2,210x** |
