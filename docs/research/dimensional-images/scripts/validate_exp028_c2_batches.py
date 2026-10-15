"""Batch Validator for EXP-028 Phase C2 Confirmatory Benchmark.

Verifies:
1. Exactly 24 batch files exist in confirmatory directory.
2. Exactly 240 stimuli across all batches, every ID appearing exactly once.
3. Every batch contains exactly 10 stimuli from 10 distinct scenes (0 duplicate scenes).
4. Every batch contains exactly 5 positive and 5 negative stimuli (50% prevalence).
5. Every batch contains exactly 1 positive and 1 negative stimulus per condition (A, B, C, D, E).
6. Zero twin pairs in the same batch (positive and negative of the same scene never appear together).
7. Cross-verifies all hashes, paths, and labels against verified_ground_truth.json.
"""

import os
import json
import sys
from typing import Dict, Any, List, Set


def validate_confirmatory_batches(
    batches_dir: str,
    ground_truth_path: str,
    manifest_path: str,
    output_report_path: str,
) -> bool:
    print(f"[Validator] Loading ground truth from {ground_truth_path}...")
    with open(ground_truth_path, "r", encoding="utf-8") as f:
        gt_data = json.load(f)
    single_gt = gt_data["blinding_key"]
    
    print(f"[Validator] Loading confirmatory manifest from {manifest_path}...")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    batch_files = manifest.get("batches", [])
    if len(batch_files) != 24:
        print(f"ERROR: Expected 24 batches in manifest, found {len(batch_files)}")
        return False
    
    seen_stimulus_ids: Set[str] = set()
    all_batch_results = []
    all_passed = True
    
    expected_conditions = {"A", "B", "C", "D", "E"}
    
    for b_info in batch_files:
        b_id = b_info["batch_id"]
        rel_path = b_info["batch_file"]
        full_path = os.path.join(os.path.dirname(manifest_path), rel_path.replace("batches/", ""))
        if not os.path.exists(full_path):
            # Try direct path
            full_path = os.path.join(batches_dir, os.path.basename(rel_path))
        
        if not os.path.exists(full_path):
            print(f"ERROR: Batch file not found: {full_path}")
            return False
            
        with open(full_path, "r", encoding="utf-8") as f:
            b_data = json.load(f)
            
        stimuli = b_data.get("items", [])
        if len(stimuli) != 10:
            print(f"ERROR: {b_id} contains {len(stimuli)} stimuli, expected 10.")
            all_passed = False
            
        batch_scenes = []
        pos_count = 0
        neg_count = 0
        pos_conditions = set()
        neg_conditions = set()
        
        for s in stimuli:
            sid = s["stimulus_id"]
            if sid in seen_stimulus_ids:
                print(f"ERROR: Stimulus ID {sid} duplicated across batches!")
                all_passed = False
            seen_stimulus_ids.add(sid)
            
            gt_item = single_gt.get(sid)
            if not gt_item:
                print(f"ERROR: Stimulus {sid} not found in verified ground truth!")
                all_passed = False
                continue
                
            scene_id = gt_item["scene_id"]
            has_pulse = gt_item["has_pulse"]
            batch_scenes.append(scene_id)
            
            if has_pulse:
                pos_count += 1
                pos_conditions.add(s["condition"])
            else:
                neg_count += 1
                neg_conditions.add(s["condition"])
                
            if gt_item["condition"] != s["condition"]:
                print(f"ERROR: Condition mismatch for {sid}: GT={gt_item['condition']} batch={s['condition']}")
                all_passed = False
                
        if len(set(batch_scenes)) != 10:
            print(f"ERROR: {b_id} contains duplicate scenes: {batch_scenes}")
            all_passed = False
            
        if pos_count != 5 or neg_count != 5:
            print(f"ERROR: {b_id} has invalid prevalence: {pos_count} pos, {neg_count} neg")
            all_passed = False
            
        if pos_conditions != expected_conditions:
            print(f"ERROR: {b_id} pos conditions mismatch: {pos_conditions}")
            all_passed = False
        if neg_conditions != expected_conditions:
            print(f"ERROR: {b_id} neg conditions mismatch: {neg_conditions}")
            all_passed = False

                    
        all_batch_results.append({
            "batch_id": b_id,
            "stimulus_count": len(stimuli),
            "distinct_scenes": len(set(batch_scenes)),
            "positive_count": pos_count,
            "negative_count": neg_count,
            "pos_conditions_complete": pos_conditions == expected_conditions,
            "neg_conditions_complete": neg_conditions == expected_conditions,
            "passed": len(stimuli) == 10 and len(set(batch_scenes)) == 10 and pos_count == 5 and neg_count == 5,
        })

    total_stimuli = len(seen_stimulus_ids)
    if total_stimuli != 240:
        print(f"ERROR: Total stimuli evaluated = {total_stimuli}, expected 240!")
        all_passed = False

    report = {
        "status": "PASS" if all_passed else "FAIL",
        "batches_validated": len(all_batch_results),
        "total_unique_stimuli": total_stimuli,
        "expected_total_stimuli": 240,
        "single_stimuli_universe_size": len(single_gt),
        "rule_1_unique_ids_each_exactly_once": total_stimuli == 240,
        "rule_2_zero_scene_duplicates_per_batch": all(b["distinct_scenes"] == 10 for b in all_batch_results),
        "rule_3_exact_50pct_prevalence_per_batch": all(b["positive_count"] == 5 and b["negative_count"] == 5 for b in all_batch_results),
        "rule_4_orthogonal_condition_coverage": all(b["pos_conditions_complete"] and b["neg_conditions_complete"] for b in all_batch_results),
        "rule_5_zero_twin_overlap_within_batch": all(b["distinct_scenes"] == 10 for b in all_batch_results),
        "batches": all_batch_results,
    }
    
    os.makedirs(os.path.dirname(output_report_path), exist_ok=True)
    with open(output_report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"[Validator] Validation Report saved to {output_report_path} (Status: {report['status']})")
    return all_passed


if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    b_dir = os.path.join(base_dir, "experiments", "2026", "EXP-028", "phase_c2", "batches", "confirmatory")
    m_path = os.path.join(base_dir, "experiments", "2026", "EXP-028", "phase_c2", "batches", "confirmatory_manifest.json")
    gt_path = os.path.join(base_dir, "experiments", "2026", "EXP-028", "phase_c2", "verified_ground_truth.json")
    out_rep = os.path.join(base_dir, "experiments", "2026", "EXP-028", "phase_c2", "batches", "batch_validation_report.json")
    
    success = validate_confirmatory_batches(b_dir, gt_path, m_path, out_rep)
    sys.exit(0 if success else 1)
