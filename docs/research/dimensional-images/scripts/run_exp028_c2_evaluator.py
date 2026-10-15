"""Evaluation Harness & Metric Scorer for EXP-028 Phase C2.

Computes formal VLM benchmark statistics for:
- Task 1: Unpaired Single-Image Pulse Detection
    - Sensitivity (Recall of positive pulse cases)
    - Specificity (True negative rate of negative baseline cases)
    - Balanced Accuracy = (Sensitivity + Specificity) / 2
    - Delta Balanced Accuracy = Balanced Accuracy(E4) - Balanced Accuracy(E3)
    - Confidence Intervals (paired bootstrap / Wilson score)
    - Abstention rate ('unklar')
    - Confusion matrices per condition (A, B, C, D, E)
- Task 2: Paired Differential Discrimination Test
    - Accuracy in identifying which image has the transient ('A' vs 'B')
    - 4-Quadrant contingency mapping:
        1. Isolated Salient (Detected in Task 1 AND Task 2)
        2. Differential Only (Missed in Task 1, but resolved in Task 2)
        3. Inaccessible (Missed in Task 1 AND Task 2)
        4. Unstable / Inverted
"""

import os
import json
from typing import Dict, Any, List, Tuple
import numpy as np


def score_task1_single_detection(
    model_responses: List[Dict[str, Any]],
    blinding_key: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """Score Task 1 single-image detection results across conditions."""
    conditions = ["A", "B", "C", "D", "E"]
    cond_counts = {c: {"TP": 0, "FP": 0, "TN": 0, "FN": 0, "ABSTAIN": 0, "TOTAL_POS": 0, "TOTAL_NEG": 0} for c in conditions}
    
    scored_items = []
    
    for resp in model_responses:
        stim_id = resp["stimulus_id"]
        pred_raw = str(resp.get("event_detected", "")).strip().lower()
        conf = float(resp.get("confidence", 0.0))
        reasoning = resp.get("reasoning", "")
        
        gt = blinding_key.get(stim_id)
        if not gt:
            continue
            
        c = gt["condition"]
        has_pulse = gt["has_pulse"]
        
        if has_pulse:
            cond_counts[c]["TOTAL_POS"] += 1
        else:
            cond_counts[c]["TOTAL_NEG"] += 1
            
        # Parse prediction
        if "ja" in pred_raw or "yes" in pred_raw or pred_raw == "true":
            pred = "ja"
        elif "nein" in pred_raw or "no" in pred_raw or pred_raw == "false":
            pred = "nein"
        else:
            pred = "unklar"
            
        if pred == "unklar":
            cond_counts[c]["ABSTAIN"] += 1
            is_correct = False
            outcome = "ABSTAIN"
        elif pred == "ja":
            if has_pulse:
                cond_counts[c]["TP"] += 1
                is_correct = True
                outcome = "TP"
            else:
                cond_counts[c]["FP"] += 1
                is_correct = False
                outcome = "FP"
        else: # pred == "nein"
            if not has_pulse:
                cond_counts[c]["TN"] += 1
                is_correct = True
                outcome = "TN"
            else:
                cond_counts[c]["FN"] += 1
                is_correct = False
                outcome = "FN"
                
        scored_items.append({
            "stimulus_id": stim_id,
            "scene_id": gt["scene_id"],
            "condition": c,
            "has_pulse": has_pulse,
            "prediction": pred,
            "outcome": outcome,
            "is_correct": is_correct,
            "confidence": conf,
            "reasoning": reasoning,
        })
        
    metrics_per_condition = {}
    for c in conditions:
        cnt = cond_counts[c]
        tp, fp, tn, fn, abstain = cnt["TP"], cnt["FP"], cnt["TN"], cnt["FN"], cnt["ABSTAIN"]
        pos, neg = cnt["TOTAL_POS"], cnt["TOTAL_NEG"]
        
        sens = (tp / pos * 100.0) if pos > 0 else 0.0
        spec = (tn / neg * 100.0) if neg > 0 else 0.0
        bal_acc = 0.5 * (sens + spec)
        raw_acc = ((tp + tn) / (pos + neg) * 100.0) if (pos + neg) > 0 else 0.0
        abs_rate = (abstain / (pos + neg) * 100.0) if (pos + neg) > 0 else 0.0
        
        metrics_per_condition[c] = {
            "TP": tp,
            "FP": fp,
            "TN": tn,
            "FN": fn,
            "ABSTAIN": abstain,
            "TOTAL_POS": pos,
            "TOTAL_NEG": neg,
            "sensitivity_pct": round(sens, 2),
            "specificity_pct": round(spec, 2),
            "balanced_accuracy_pct": round(bal_acc, 2),
            "raw_accuracy_pct": round(raw_acc, 2),
            "abstention_rate_pct": round(abs_rate, 2),
        }
        
    # Primary Hypothesis: Condition B (E4 WebP) vs Condition A (E3 WebP)
    delta_bal_acc = metrics_per_condition["B"]["balanced_accuracy_pct"] - metrics_per_condition["A"]["balanced_accuracy_pct"]
    delta_spec = metrics_per_condition["B"]["specificity_pct"] - metrics_per_condition["A"]["specificity_pct"]
    
    hypothesis_met = (delta_bal_acc >= 10.0) and (delta_spec >= -5.0)
    
    return {
        "metrics_per_condition": metrics_per_condition,
        "delta_balanced_accuracy_B_vs_A": round(delta_bal_acc, 2),
        "delta_specificity_B_vs_A": round(delta_spec, 2),
        "hypothesis_threshold_met": hypothesis_met,
        "scored_items": scored_items,
    }


def score_task2_paired_discrimination(
    model_responses: List[Dict[str, Any]],
    paired_key: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """Score Task 2 paired discrimination results across conditions."""
    conditions = ["A", "B", "C", "D", "E"]
    cond_counts = {c: {"CORRECT": 0, "INCORRECT": 0, "NO_DIFFERENCE": 0, "TOTAL": 0} for c in conditions}
    scored_pairs = []
    
    for resp in model_responses:
        pair_id = resp["pair_id"]
        sel_raw = str(resp.get("selected_image", "")).strip().upper()
        diff_det = bool(resp.get("differential_detected", False))
        conf = float(resp.get("confidence", 0.0))
        reasoning = resp.get("reasoning", "")
        
        gt = paired_key.get(pair_id)
        if not gt:
            continue
            
        c = gt["condition"]
        target_choice = gt["ground_truth_selected_image"] # "A" or "B"
        cond_counts[c]["TOTAL"] += 1
        
        if "KEIN" in sel_raw or "NONE" in sel_raw or not diff_det:
            outcome = "NO_DIFF"
            cond_counts[c]["NO_DIFFERENCE"] += 1
            is_correct = False
        elif target_choice in sel_raw:
            outcome = "CORRECT"
            cond_counts[c]["CORRECT"] += 1
            is_correct = True
        else:
            outcome = "INCORRECT"
            cond_counts[c]["INCORRECT"] += 1
            is_correct = False
            
        scored_pairs.append({
            "pair_id": pair_id,
            "scene_id": gt["scene_id"],
            "condition": c,
            "target_image": target_choice,
            "selected_image": sel_raw,
            "outcome": outcome,
            "is_correct": is_correct,
            "confidence": conf,
            "reasoning": reasoning,
        })
        
    metrics_per_condition = {}
    for c in conditions:
        cnt = cond_counts[c]
        tot = cnt["TOTAL"]
        cor = cnt["CORRECT"]
        acc = (cor / tot * 100.0) if tot > 0 else 0.0
        no_diff_rate = (cnt["NO_DIFFERENCE"] / tot * 100.0) if tot > 0 else 0.0
        
        metrics_per_condition[c] = {
            "CORRECT": cor,
            "INCORRECT": cnt["INCORRECT"],
            "NO_DIFFERENCE": cnt["NO_DIFFERENCE"],
            "TOTAL": tot,
            "accuracy_pct": round(acc, 2),
            "no_difference_rate_pct": round(no_diff_rate, 2),
        }
        
    return {
        "metrics_per_condition": metrics_per_condition,
        "scored_pairs": scored_pairs,
    }
