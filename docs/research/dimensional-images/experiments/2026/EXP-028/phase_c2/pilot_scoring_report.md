# EXP-028 Phase C2: Technical Pilot Evaluation Report

## 1. Task 1 Single-Image Detection Results (8 Scene Pairs, 80 Stimuli)

| Condition | Codec / Format | Total Pos | Total Neg | TP | FP | TN | FN | Abstain | Sensitivity | Specificity | Balanced Accuracy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Condition A** | E3-K12 WebP Q80 (Baseline) | 8 | 8 | 3 | 4 | 4 | 3 | 2 | 37.5% | 50.0% | **43.8%** |
| **Condition B** | E4-Y0 WebP Q80 (Candidate) | 8 | 8 | 3 | 0 | 8 | 3 | 2 | 37.5% | 100.0% | **68.8%** |
| **Condition C** | E3-K12 PNG (Lossless) | 8 | 8 | 3 | 4 | 4 | 3 | 2 | 37.5% | 50.0% | **43.8%** |
| **Condition D** | E4-Y0 PNG (Lossless) | 8 | 8 | 3 | 0 | 8 | 3 | 2 | 37.5% | 100.0% | **68.8%** |
| **Condition E** | GRID512 WebP Q80 (Ceiling) | 8 | 8 | 4 | 0 | 8 | 4 | 0 | 50.0% | 100.0% | **75.0%** |

## 2. Decision Gate Evaluation

- **Delta Balanced Accuracy (Condition B vs. Condition A):** `+25.00%` points
- **Delta Specificity (Condition B vs. Condition A):** `+50.00%` points
- **Threshold Met (Delta BA >= +10.0%, Delta Spec >= -5.0%):** `YES`
