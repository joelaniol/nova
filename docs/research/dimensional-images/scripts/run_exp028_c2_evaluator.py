"""Evaluation Harness & Metric Scorer for EXP-028 Phase C2.

Amended per ChatGPT Peer-Review (Amendment 1):
1. Strict lexical validation of model predictions (no substring false positives, e.g. 'unknown' != 'no').
2. Strict duplicate rejection and stimulus completeness checks.
3. Explicit conservative abstention accounting (abstentions count as non-hits).
4. Task 2 Catch Trial evaluation: distinguishes differential pairs from identical twin catch trials.
5. Paired Scene-Level Cluster-Bootstrap (B=10,000) for empirical 95% Confidence Intervals.
6. Formal decision rule evaluation against pre-registered criteria.
"""

import os
import re
import json
from typing import Dict, Any, List, Tuple, Optional, Set
import numpy as np


def normalize_task1_prediction(raw_val: Any) -> str:
    """Strictly normalize Task 1 prediction to 'ja', 'nein', or 'unklar'.
    
    Guards against substring false matches (e.g. 'unknown' matching 'no')
    and handles structured phrasing cleanly.
    """
    if raw_val is None:
        return "unklar"
    s = str(raw_val).strip().lower()
    
    # 1. Exact string matches
    if s in {"ja", "yes", "true", "1"}:
        return "ja"
    if s in {"nein", "no", "false", "0"}:
        return "nein"
    if s in {"unklar", "unclear", "unsicher", "unknown", "inconclusive", "abstain"}:
        return "unklar"
        
    words = re.findall(r"\b\w+\b", s)
    if not words:
        return "unklar"
        
    # 2. Check first word (since prompt instructs: "Antworte mit 'ja', 'nein' oder 'unklar'")
    first_word = words[0]
    if first_word in {"ja", "yes"}:
        return "ja"
    if first_word in {"nein", "no"}:
        return "nein"
    if first_word in {"unklar", "unclear", "unsicher", "unknown"}:
        return "unklar"
        
    # 3. Keyword presence
    has_no = ("nein" in words) or ("no" in words) or ("nicht" in words) or ("kein" in words)
    has_yes = (("ja" in words) or ("yes" in words)) and not has_no
    has_unclear = ("unklar" in words) or ("unclear" in words) or ("unsicher" in words)
    
    if has_unclear:
        return "unklar"
    if has_yes:
        return "ja"
    if has_no:
        return "nein"
    return "unklar"


def normalize_task2_prediction(raw_val: Any, diff_detected: Optional[bool] = None) -> str:
    """Strictly normalize Task 2 prediction to 'A', 'B', or 'kein_Unterschied'."""
    if raw_val is None:
        return "kein_Unterschied"
    s = str(raw_val).strip().upper()
    
    if diff_detected is False:
        return "kein_Unterschied"
        
    no_diff_patterns = ["KEIN", "NONE", "NO_DIFFERENCE", "NEITHER", "GLEICH", "IDENTISCH", "KEIN_UNTERSCHIED"]
    if any(p in s for p in no_diff_patterns):
        return "kein_Unterschied"
        
    words = set(re.findall(r"\b[A-Za-z]+\b", s))
    has_a = "A" in words or "BILD_A" in s or "IMAGE_A" in s
    has_b = "B" in words or "BILD_B" in s or "IMAGE_B" in s
    
    if has_a and not has_b:
        return "A"
    if has_b and not has_a:
        return "B"
        
    return "kein_Unterschied"


def compute_scene_cluster_bootstrap(
    scored_items: List[Dict[str, Any]],
    n_bootstrap: int = 10000,
    seed: int = 20261028,
) -> Dict[str, Any]:
    """Compute paired cluster-bootstrap confidence intervals grouped by scene_id."""
    rng = np.random.default_rng(seed)
    
    scene_items: Dict[str, List[Dict[str, Any]]] = {}
    for it in scored_items:
        s_id = it["scene_id"]
        scene_items.setdefault(s_id, []).append(it)
        
    unique_scenes = sorted(scene_items.keys())
    n_scenes = len(unique_scenes)
    
    delta_ba_dist = []
    delta_spec_dist = []
    delta_sens_dist = []
    
    for _ in range(n_bootstrap):
        sampled_scenes = rng.choice(unique_scenes, size=n_scenes, replace=True)
        counts = {
            "A": {"TP": 0, "FP": 0, "TN": 0, "FN": 0, "POS": 0, "NEG": 0},
            "B": {"TP": 0, "FP": 0, "TN": 0, "FN": 0, "POS": 0, "NEG": 0},
        }
        for s in sampled_scenes:
            for it in scene_items[s]:
                c = it["condition"]
                if c in counts:
                    if it["has_pulse"]:
                        counts[c]["POS"] += 1
                        if it["outcome"] == "TP":
                            counts[c]["TP"] += 1
                        else:
                            counts[c]["FN"] += 1
                    else:
                        counts[c]["NEG"] += 1
                        if it["outcome"] == "TN":
                            counts[c]["TN"] += 1
                        else:
                            counts[c]["FP"] += 1
                            
        sens_a = (counts["A"]["TP"] / counts["A"]["POS"]) if counts["A"]["POS"] > 0 else 0.0
        spec_a = (counts["A"]["TN"] / counts["A"]["NEG"]) if counts["A"]["NEG"] > 0 else 0.0
        ba_a = 0.5 * (sens_a + spec_a)
        
        sens_b = (counts["B"]["TP"] / counts["B"]["POS"]) if counts["B"]["POS"] > 0 else 0.0
        spec_b = (counts["B"]["TN"] / counts["B"]["NEG"]) if counts["B"]["NEG"] > 0 else 0.0
        ba_b = 0.5 * (sens_b + spec_b)
        
        delta_ba_dist.append((ba_b - ba_a) * 100.0)
        delta_spec_dist.append((spec_b - spec_a) * 100.0)
        delta_sens_dist.append((sens_b - sens_a) * 100.0)
        
    delta_ba_arr = np.array(delta_ba_dist)
    delta_spec_arr = np.array(delta_spec_dist)
    delta_sens_arr = np.array(delta_sens_dist)
    
    ci_ba_low, ci_ba_high = np.percentile(delta_ba_arr, [2.5, 97.5])
    ci_spec_low, ci_spec_high = np.percentile(delta_spec_arr, [2.5, 97.5])
    ci_sens_low, ci_sens_high = np.percentile(delta_sens_arr, [2.5, 97.5])
    
    p_val_ba = float(np.mean(delta_ba_arr <= 0.0))
    p_val_spec = float(np.mean(delta_spec_arr <= 0.0))
    
    return {
        "n_bootstrap": n_bootstrap,
        "n_scene_clusters": n_scenes,
        "delta_balanced_accuracy": {
            "mean": round(float(np.mean(delta_ba_arr)), 2),
            "std": round(float(np.std(delta_ba_arr)), 2),
            "ci_95": [round(float(ci_ba_low), 2), round(float(ci_ba_high), 2)],
            "p_value_one_tailed": round(p_val_ba, 4),
            "statistically_significant": bool(ci_ba_low > 0.0),
        },
        "delta_specificity": {
            "mean": round(float(np.mean(delta_spec_arr)), 2),
            "std": round(float(np.std(delta_spec_arr)), 2),
            "ci_95": [round(float(ci_spec_low), 2), round(float(ci_spec_high), 2)],
            "p_value_one_tailed": round(p_val_spec, 4),
        },
        "delta_sensitivity": {
            "mean": round(float(np.mean(delta_sens_arr)), 2),
            "std": round(float(np.std(delta_sens_arr)), 2),
            "ci_95": [round(float(ci_sens_low), 2), round(float(ci_sens_high), 2)],
        },
    }


def score_task1_single_detection(
    model_responses: List[Dict[str, Any]],
    blinding_key: Dict[str, Dict[str, Any]],
    enforce_completeness: bool = False,
) -> Dict[str, Any]:
    """Score Task 1 single-image detection results across conditions."""
    conditions = ["A", "B", "C", "D", "E"]
    cond_counts = {c: {"TP": 0, "FP": 0, "TN": 0, "FN": 0, "ABSTAIN": 0, "TOTAL_POS": 0, "TOTAL_NEG": 0} for c in conditions}
    
    seen_ids: Set[str] = set()
    scored_items = []
    
    for resp in model_responses:
        stim_id = resp.get("stimulus_id")
        if not stim_id:
            raise ValueError("Response missing stimulus_id")
        if stim_id in seen_ids:
            raise ValueError(f"Duplicate stimulus_id encountered: {stim_id}")
        seen_ids.add(stim_id)
        
        gt = blinding_key.get(stim_id)
        if not gt:
            raise KeyError(f"Stimulus ID '{stim_id}' not found in blinding key!")
            
        c = gt["condition"]
        has_pulse = gt["has_pulse"]
        
        if has_pulse:
            cond_counts[c]["TOTAL_POS"] += 1
        else:
            cond_counts[c]["TOTAL_NEG"] += 1
            
        pred = normalize_task1_prediction(resp.get("event_detected"))
        conf = float(resp.get("confidence", 0.0))
        reasoning = resp.get("reasoning", "")
        
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
        else:  # pred == "nein"
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
            "grid512_sampling_covariate": gt.get("grid512_sampling_covariate"),
        })
        
    if enforce_completeness:
        expected_ids = set(blinding_key.keys())
        missing = expected_ids - seen_ids
        if missing:
            raise ValueError(f"Incomplete evaluation: {len(missing)} stimuli missing from responses: {list(missing)[:5]}")

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
        
    delta_bal_acc = metrics_per_condition["B"]["balanced_accuracy_pct"] - metrics_per_condition["A"]["balanced_accuracy_pct"]
    delta_spec = metrics_per_condition["B"]["specificity_pct"] - metrics_per_condition["A"]["specificity_pct"]
    
    # Statistical cluster bootstrap on scene level
    bootstrap_results = compute_scene_cluster_bootstrap(scored_items)
    ci_low = bootstrap_results["delta_balanced_accuracy"]["ci_95"][0]
    
    hypothesis_met_point = (delta_bal_acc >= 10.0) and (delta_spec >= -5.0)
    hypothesis_met_statistical = hypothesis_met_point and (ci_low > 0.0)
    
    return {
        "metrics_per_condition": metrics_per_condition,
        "delta_balanced_accuracy_B_vs_A": round(delta_bal_acc, 2),
        "delta_specificity_B_vs_A": round(delta_spec, 2),
        "hypothesis_threshold_met_point": hypothesis_met_point,
        "hypothesis_threshold_met_statistical": hypothesis_met_statistical,
        "bootstrap": bootstrap_results,
        "scored_items": scored_items,
    }


def score_task2_paired_discrimination(
    model_responses: List[Dict[str, Any]],
    paired_key: Dict[str, Dict[str, Any]],
    enforce_completeness: bool = False,
) -> Dict[str, Any]:
    """Score Task 2 paired discrimination results with catch trial segregation."""
    conditions = ["A", "B", "C", "D", "E"]
    
    cond_diff = {c: {"HIT": 0, "WRONG_SIDE": 0, "MISSED_DIFF": 0, "TOTAL": 0} for c in conditions}
    cond_catch = {c: {"CORRECT_REJECTION": 0, "FALSE_DIFF": 0, "TOTAL": 0} for c in conditions}
    
    seen_ids: Set[str] = set()
    scored_pairs = []
    
    for resp in model_responses:
        pair_id = resp.get("pair_id")
        if not pair_id:
            raise ValueError("Response missing pair_id")
        if pair_id in seen_ids:
            raise ValueError(f"Duplicate pair_id encountered: {pair_id}")
        seen_ids.add(pair_id)
        
        gt = paired_key.get(pair_id)
        if not gt:
            raise KeyError(f"Pair ID '{pair_id}' not found in paired ground truth!")
            
        c = gt["condition"]
        is_catch = gt.get("is_catch_trial", False)
        target_choice = gt["ground_truth_selected_image"]
        
        pred = normalize_task2_prediction(
            resp.get("selected_image"),
            diff_detected=resp.get("differential_detected"),
        )
        conf = float(resp.get("confidence", 0.0))
        reasoning = resp.get("reasoning", "")
        
        if is_catch:
            cond_catch[c]["TOTAL"] += 1
            if pred == "kein_Unterschied":
                outcome = "CORRECT_REJECTION"
                cond_catch[c]["CORRECT_REJECTION"] += 1
                is_correct = True
            else:
                outcome = "FALSE_DIFF"
                cond_catch[c]["FALSE_DIFF"] += 1
                is_correct = False
        else:
            cond_diff[c]["TOTAL"] += 1
            if pred == "kein_Unterschied":
                outcome = "MISSED_DIFF"
                cond_diff[c]["MISSED_DIFF"] += 1
                is_correct = False
            elif pred == target_choice:
                outcome = "HIT"
                cond_diff[c]["HIT"] += 1
                is_correct = True
            else:
                outcome = "WRONG_SIDE"
                cond_diff[c]["WRONG_SIDE"] += 1
                is_correct = False
                
        scored_pairs.append({
            "pair_id": pair_id,
            "scene_id": gt.get("scene_id", "unknown_scene"),
            "condition": c,
            "is_catch_trial": is_catch,
            "target_image": target_choice,
            "prediction": pred,
            "outcome": outcome,
            "is_correct": is_correct,
            "confidence": conf,
            "reasoning": reasoning,
        })
        
    if enforce_completeness:
        expected_ids = set(paired_key.keys())
        missing = expected_ids - seen_ids
        if missing:
            raise ValueError(f"Incomplete evaluation: {len(missing)} pairs missing from responses: {list(missing)[:5]}")

    metrics_per_condition = {}
    for c in conditions:
        diff_cnt = cond_diff[c]
        catch_cnt = cond_catch[c]
        
        d_tot = diff_cnt["TOTAL"]
        d_hit = diff_cnt["HIT"]
        d_acc = (d_hit / d_tot * 100.0) if d_tot > 0 else 0.0
        
        c_tot = catch_cnt["TOTAL"]
        c_cr = catch_cnt["CORRECT_REJECTION"]
        c_spec = (c_cr / c_tot * 100.0) if c_tot > 0 else 0.0
        
        metrics_per_condition[c] = {
            "differential_pairs": {
                "HIT": d_hit,
                "WRONG_SIDE": diff_cnt["WRONG_SIDE"],
                "MISSED_DIFF": diff_cnt["MISSED_DIFF"],
                "TOTAL": d_tot,
                "accuracy_pct": round(d_acc, 2),
            },
            "catch_trials": {
                "CORRECT_REJECTION": c_cr,
                "FALSE_DIFF": catch_cnt["FALSE_DIFF"],
                "TOTAL": c_tot,
                "specificity_pct": round(c_spec, 2),
            },
        }
        
    return {
        "metrics_per_condition": metrics_per_condition,
        "scored_pairs": scored_pairs,
    }


if __name__ == "__main__":
    print("EXP-028 Phase C2 Evaluator module loaded successfully.")
