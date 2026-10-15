"""Regression and Unit Tests for EXP-028 Phase C2 Evaluator and Scorer.

Verifies:
1. Lexical parser strictly maps words, rejecting substring false positives ("unknown" -> "unklar", not "nein").
2. Resolves phrases like "no change detected" properly.
3. Task 2 normalization correctly detects 'A', 'B', and 'kein_Unterschied'.
4. Catch trials in Task 2 are correctly evaluated and segregated.
5. Evaluator strictly raises on duplicate stimulus IDs, missing IDs, or unknown IDs.
6. Scene-level cluster bootstrap executes correctly and computes valid 95% CIs.
"""

import pytest
import numpy as np
from scripts.run_exp028_c2_evaluator import (
    normalize_task1_prediction,
    normalize_task2_prediction,
    score_task1_single_detection,
    score_task2_paired_discrimination,
    compute_scene_cluster_bootstrap,
)


def test_task1_lexical_normalization():
    # Exact cases
    assert normalize_task1_prediction("ja") == "ja"
    assert normalize_task1_prediction("yes") == "ja"
    assert normalize_task1_prediction("nein") == "nein"
    assert normalize_task1_prediction("no") == "nein"
    assert normalize_task1_prediction("unklar") == "unklar"
    
    # Substring trap: "unknown" must NOT map to "nein" (even though it contains "no")
    assert normalize_task1_prediction("unknown") == "unklar"
    assert normalize_task1_prediction("unclear") == "unklar"
    assert normalize_task1_prediction("unsicher") == "unklar"
    
    # Phrase handling
    assert normalize_task1_prediction("no change detected") == "nein"
    assert normalize_task1_prediction("yes, there is a pulse") == "ja"
    assert normalize_task1_prediction("Nein, keine Veränderung sichtbar.") == "nein"
    assert normalize_task1_prediction(None) == "unklar"
    assert normalize_task1_prediction("") == "unklar"


def test_task2_lexical_normalization():
    assert normalize_task2_prediction("A") == "A"
    assert normalize_task2_prediction("Bild A") == "A"
    assert normalize_task2_prediction("Image A") == "A"
    assert normalize_task2_prediction("B") == "B"
    assert normalize_task2_prediction("Bild B") == "B"
    assert normalize_task2_prediction("kein_Unterschied") == "kein_Unterschied"
    assert normalize_task2_prediction("kein Unterschied erkennbar") == "kein_Unterschied"
    assert normalize_task2_prediction("identisch") == "kein_Unterschied"
    assert normalize_task2_prediction("A", diff_detected=False) == "kein_Unterschied"


def test_evaluator_rejects_duplicates():
    blinding_key = {
        "stim_01": {"condition": "A", "has_pulse": True, "scene_id": "S01"},
    }
    duplicate_responses = [
        {"stimulus_id": "stim_01", "event_detected": "ja"},
        {"stimulus_id": "stim_01", "event_detected": "ja"},
    ]
    with pytest.raises(ValueError, match="Duplicate stimulus_id"):
        score_task1_single_detection(duplicate_responses, blinding_key)


def test_evaluator_rejects_missing_id():
    blinding_key = {
        "stim_01": {"condition": "A", "has_pulse": True, "scene_id": "S01"},
    }
    missing_id_responses = [
        {"event_detected": "ja"},
    ]
    with pytest.raises(ValueError, match="Response missing stimulus_id"):
        score_task1_single_detection(missing_id_responses, blinding_key)


def test_evaluator_rejects_unknown_id():
    blinding_key = {
        "stim_01": {"condition": "A", "has_pulse": True, "scene_id": "S01"},
    }
    unknown_id_responses = [
        {"stimulus_id": "stim_unknown_99", "event_detected": "ja"},
    ]
    with pytest.raises(KeyError, match="not found in blinding key"):
        score_task1_single_detection(unknown_id_responses, blinding_key)


def test_task2_catch_trial_scoring():
    paired_key = {
        "pair_diff_01": {
            "condition": "B",
            "is_catch_trial": False,
            "ground_truth_selected_image": "A",
        },
        "pair_catch_01": {
            "condition": "B",
            "is_catch_trial": True,
            "ground_truth_selected_image": "kein_Unterschied",
        },
    }
    
    # Model correctly identifies diff in pair 1, and correctly rejects diff in catch trial
    responses = [
        {"pair_id": "pair_diff_01", "selected_image": "A", "differential_detected": True},
        {"pair_id": "pair_catch_01", "selected_image": "kein_Unterschied", "differential_detected": False},
    ]
    result = score_task2_paired_discrimination(responses, paired_key)
    metrics_b = result["metrics_per_condition"]["B"]
    assert metrics_b["differential_pairs"]["HIT"] == 1
    assert metrics_b["catch_trials"]["CORRECT_REJECTION"] == 1
    assert metrics_b["catch_trials"]["FALSE_DIFF"] == 0
    assert metrics_b["catch_trials"]["specificity_pct"] == 100.0



def test_cluster_bootstrap():
    # Build synthetic scored items for 4 scenes with clear B superiority
    items = []
    for s_idx in range(10):
        scene_id = f"scene_{s_idx:02d}"
        # Condition A: 40% hit rate, 40% specificity
        items.append({"scene_id": scene_id, "condition": "A", "has_pulse": True, "outcome": "TP" if s_idx < 4 else "FN"})
        items.append({"scene_id": scene_id, "condition": "A", "has_pulse": False, "outcome": "TN" if s_idx < 4 else "FP"})
        # Condition B: 80% hit rate, 100% specificity
        items.append({"scene_id": scene_id, "condition": "B", "has_pulse": True, "outcome": "TP" if s_idx < 8 else "FN"})
        items.append({"scene_id": scene_id, "condition": "B", "has_pulse": False, "outcome": "TN"})

    boot = compute_scene_cluster_bootstrap(items, n_bootstrap=500, seed=42)
    assert boot["n_scene_clusters"] == 10
    assert boot["delta_balanced_accuracy"]["mean"] > 0
    assert len(boot["delta_balanced_accuracy"]["ci_95"]) == 2
    assert boot["delta_balanced_accuracy"]["ci_95"][0] <= boot["delta_balanced_accuracy"]["ci_95"][1]
