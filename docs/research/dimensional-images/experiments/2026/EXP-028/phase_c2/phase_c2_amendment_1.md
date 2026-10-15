# EXP-028 Phase C2: Pre-Registration Amendment 1

**Date:** 2026-10-15  
**Experiment ID:** EXP-028  
**Phase:** Phase C2 (Blinded VLM Comparison Benchmark)  
**Authors:** Joel Aniol & Antigravity (Agy)  
**Peer-Reviewer:** ChatGPT (via Nova Browser)  
**Status:** RATIFIED & FROZEN PRIOR TO CONFIRMATORY RUN  

---

## 1. Context & Motivation

Following the successful execution of the EXP-028 Phase C2 Technical Pilot (8 scenes = 80 Task 1 evaluations), which demonstrated that E4-Y0 achieved 0 false alarms (100.0% specificity) compared to 4 false alarms in E3-K12 (50.0% specificity), ChatGPT conducted a rigorous peer review.

The review ratified the pilot as technically successful, but established five mandatory methodological hardening requirements that must be frozen before launching the 24-scene confirmatory benchmark:
1. Counterbalanced Left/Right positioning in Task 2.
2. Introduction of identical negative/negative catch trials in Task 2.
3. Explicit numerical documentation of GRID512 pulse sampling attenuation as a covariate.
4. Fully deterministic UUID generation tied to random seed.
5. Strict lexical parsing, duplicate prevention, and cluster-bootstrap confidence intervals on scene level.

---

## 2. Formal Amendments to Protocol

### Amendment 1.1: Exact 12:12 Left/Right Counterbalancing (Task 2)
- **Previous state:** Independent random coin flip per scene (`rng.random() < 0.5`), which introduced unequal left/right distribution across conditions.
- **Amended rule:** Deterministic orthogonal schedule guaranteeing exactly:
  - Confirmatory: 12 positive-on-left (Choice A) and 12 positive-on-right (Choice B) per condition.
  - Pilot: 4 positive-on-left and 4 positive-on-right per condition.
  - Balanced across the 4 trajectory classes (3 A, 3 B per trajectory class).

### Amendment 1.2: Identical Twin Catch Trials (Task 2)
- **Previous state:** All Task 2 pairs contained an objective differential (`has_pulse: True` on one side), making "kein_Unterschied" an objectively incorrect choice in every pair.
- **Amended rule:** Inclusion of identical negative/negative twin pairs (`arr_neg` on both sides):
  - Confirmatory: 6 catch trials per condition (30 catch pairs total).
  - Pilot: 2 catch trials per condition (10 catch pairs total).
  - Ground truth: `differential_present: False`, `ground_truth_selected_image: "kein_Unterschied"`.
  - Serves as an unforced false-difference detection baseline.

### Amendment 1.3: GRID512 Pulse Sampling Phase Covariate
- **Rationale:** The 4-frame pulse (e.g. frames 40..43 or 42..45) is subsampled by the 16 contact sheet frames (multiples of 4: 0, 4, ..., 60).
- **Formal Covariate:** Each scene's ground truth now includes `grid512_sampling_covariate`:
  - `grid_captured_pulse_frames`: List of pulse frames captured in the contact sheet.
  - `grid_best_pulse_envelope_fraction`: Maximum triangular envelope fraction captured (e.g., 6.25% at frame 40 vs 68.75% at frame 44, an 11x difference).
  - `is_pulse_sampled_near_peak`: Boolean indicating if best envelope $\ge 0.5$.

### Amendment 1.4: Cryptographic Determinism of Identifiers
- **Previous state:** `uuid.uuid4()` was non-deterministic across Python runs.
- **Amended rule:** `make_deterministic_uuid(prefix, key_str)` generates SHA-256 derived hex UUIDs from `(subset, scene_id, condition, twin_type, seed)`. Running `build_exp028_c2_stimuli.py` with seed `20261028` reproduces bit-identical files, hashes, and UUIDs deterministically across any machine.

### Amendment 1.5: Strict Lexical Parsing & Cluster-Bootstrap CIs
- **Strict Parsing:** Word boundary matching prevents substring false positives (e.g. "unknown" will no longer match "no").
- **Completeness & Duplicates:** Explicit assertions reject duplicate evaluations and verify that all expected stimuli are evaluated.
- **Abstention Rule:** Abstentions ("unklar") count conservatively as non-hits in the denominator.
- **Statistical Decision Criterion:** Confirmatory hypothesis testing requires:
  1. Point estimate: $\Delta \text{Balanced Accuracy} \ge +10.0\%$ points for Condition B vs. Condition A.
  2. Point estimate: $\Delta \text{Specificity} \ge -5.0\%$ points.
  3. Statistical validation: Lower bound of 95% paired cluster-bootstrap confidence interval (grouped by 24 independent scenes, $B=10,000$) must satisfy $\text{CI}_{2.5\%} > 0.0\%$.

---

## 3. Dataset Dimensions (Post-Amendment)

| Dataset Subset | Scenes | Task 1 Stimuli (Single) | Task 2 Differential Pairs | Task 2 Catch Trials | Total Task 2 Pairs |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Technical Pilot** | 8 | 80 | 40 | 10 | 50 |
| **Confirmatory Main** | 24 | 240 | 120 | 30 | 150 |
| **Total** | **32** | **320** | **160** | **40** | **200** |

All stimuli files remain Git-ignored per Joel's Git hygiene directive and are 100% deterministically reproducible via seed `20261028`.
