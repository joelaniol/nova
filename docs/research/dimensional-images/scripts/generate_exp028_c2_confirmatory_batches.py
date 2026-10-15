"""Generate Orthogonal, Counterbalanced Batches for EXP-028 Phase C2 Confirmatory Run.

Guarantees:
1. Strict Scene Isolation: All 10 stimuli in a batch belong to 10 distinct scenes (0 scene overlap).
2. Prevalence Balancing: Exactly 5 positive twins and 5 negative twins per batch (50% prevalence).
3. Condition Orthogonality: Exactly 1 positive and 1 negative stimulus for each condition (A, B, C, D, E) per batch.
4. Zero Twin Overlap: Positive and negative twins of the same scene are never in the same batch.
5. Zero Semantic Leakage: Evaluators receive only blinded stimulus IDs, neutral prompts, and image paths.
"""

import os
import json
import numpy as np
from typing import Dict, Any, List

def generate_confirmatory_batches(
    phase_c2_dir: str = os.path.join("experiments", "2026", "EXP-028", "phase_c2"),
    random_seed: int = 20261028,
):
    gt_path = os.path.join(phase_c2_dir, "verified_ground_truth.json")
    with open(gt_path, "r", encoding="utf-8") as f:
        gt_data = json.load(f)
        
    blinding_key = gt_data["blinding_key"]
    conf_stimuli = [v for v in blinding_key.values() if v["subset"] == "confirmatory"]
    scenes = sorted(list(set(s["scene_id"] for s in conf_stimuli)))
    conds = ["A", "B", "C", "D", "E"]
    
    assert len(scenes) == 24, f"Expected 24 confirmatory scenes, got {len(scenes)}"
    assert len(conf_stimuli) == 240, f"Expected 240 confirmatory stimuli, got {len(conf_stimuli)}"
    
    # Map (scene_id, condition, twin_type) -> stimulus entry
    lookup = {}
    for st in conf_stimuli:
        lookup[(st["scene_id"], st["condition"], st["twin_type"])] = st
        
    batches_dir = os.path.join(phase_c2_dir, "batches", "confirmatory")
    os.makedirs(batches_dir, exist_ok=True)
    
    rng = np.random.default_rng(random_seed)
    
    manifest = {
        "experiment_id": "EXP-028",
        "phase": "Phase C2",
        "type": "Confirmatory Task 1 Batches",
        "random_seed": random_seed,
        "total_batches": 24,
        "items_per_batch": 10,
        "batches": [],
    }
    
    carrier_guidance = (
        "Das Bild ist ein 128x128 Visual Carrier mit 4 Quadranten (je 64x64):\n"
        "- Oben-Links: Basiszustand (Frame t=0)\n"
        "- Oben-Rechts: Temporale Kinematik (Rot=P0 Mittelwert, Grün=P2 Krümmung, Blau=höhere zeitliche Walsh-Moden)\n"
        "- Unten-Links: Chromatische Trägerschicht (Cb=P1 Trend, Cr=höhere zeitliche Walsh-Moden)\n"
        "- Unten-Rechts: Neutralgrau (128)"
    )
    grid_guidance = (
        "Das Bild ist ein 512x512 4x4 Kontaktbogen aus 16 zeitlich aufeinanderfolgenden Videobildern.\n"
        "Die Zeit verläuft zeilenweise von oben-links nach unten-rechts (Zeile 0 = Anfang, Zeile 3 = Ende)."
    )
    prompt_text = (
        "Untersuche für jedes Bild die dargestellte zeitliche Sequenz.\n"
        "Ist eine kurzzeitige Helligkeitsänderung eines Objekts erkennbar, die anschließend wieder verschwindet?\n"
        "Antworte für jedes Bild mit 'ja', 'nein' oder 'unklar' und beschreibe kurz die sichtbare Grundlage deiner Einschätzung."
    )
    
    all_assigned_ids = []
    
    for b in range(24):
        batch_id = f"conf_task1_batch_{b+1:02d}"
        batch_items = []
        batch_scenes = []
        
        for i, c in enumerate(conds):
            s_pos = scenes[(b + 2 * i) % 24]
            s_neg = scenes[(b + 2 * i + 1) % 24]
            batch_scenes.extend([s_pos, s_neg])
            
            item_pos = lookup[(s_pos, c, "pos")]
            item_neg = lookup[(s_neg, c, "neg")]
            
            batch_items.append({
                "stimulus_id": item_pos["stimulus_id"],
                "relative_path": item_pos["relative_path"],
                "condition": c,
                "format_guidance": grid_guidance if c == "E" else carrier_guidance,
                "format_type": "Kontaktbogen 512x512" if c == "E" else "Visual Carrier 128x128",
            })
            batch_items.append({
                "stimulus_id": item_neg["stimulus_id"],
                "relative_path": item_neg["relative_path"],
                "condition": c,
                "format_guidance": grid_guidance if c == "E" else carrier_guidance,
                "format_type": "Kontaktbogen 512x512" if c == "E" else "Visual Carrier 128x128",
            })
            
        assert len(set(batch_scenes)) == 10, f"Batch {batch_id} violated scene uniqueness!"
        assert len(batch_items) == 10, f"Batch {batch_id} does not have 10 items!"
        
        # Shuffle item presentation order deterministically within batch
        perm_idx = rng.permutation(10)
        shuffled_items = [batch_items[idx] for idx in perm_idx]
        
        batch_file_path = os.path.join(batches_dir, f"{batch_id}.json")
        batch_payload = {
            "batch_id": batch_id,
            "neutral_prompt": prompt_text,
            "items": shuffled_items,
        }
        with open(batch_file_path, "w", encoding="utf-8") as f:
            json.dump(batch_payload, f, indent=2)
            
        for it in shuffled_items:
            all_assigned_ids.append(it["stimulus_id"])
            
        manifest["batches"].append({
            "batch_id": batch_id,
            "batch_file": f"batches/confirmatory/{batch_id}.json",
            "item_count": 10,
        })
        
    assert len(all_assigned_ids) == 240, f"Total assigned {len(all_assigned_ids)} != 240"
    assert len(set(all_assigned_ids)) == 240, "Duplicates found across batches!"
    
    manifest_path = os.path.join(phase_c2_dir, "batches", "confirmatory_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
        
    print(f"[+] Successfully generated 24 orthogonal confirmatory batches in: {batches_dir}")
    print(f"[+] Saved confirmatory manifest to: {manifest_path}")

if __name__ == "__main__":
    generate_confirmatory_batches()
