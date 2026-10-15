"""Stimulus Generator & Cryptographic Blinding Pipeline for EXP-028 Phase C2.

Builds all stimuli for:
- 8 Technical Pilot Scene Pairs (16 videos -> 80 Task 1 stimuli + 40 Task 2 paired stimuli)
- 24 Confirmatory Scene Pairs (48 videos -> 240 Task 1 stimuli + 120 Task 2 paired stimuli)

Conditions:
- Condition A: E3-K12 WebP Q80 (128x128)
- Condition B: E4-Y0 WebP Q80 (128x128)
- Condition C: E3-K12 PNG lossless (128x128)
- Condition D: E4-Y0 PNG lossless (128x128)
- Condition E: GRID512 WebP Q80 (512x512 4x4 contact sheet)

Enforces:
- Neutral 12-char hex UUID filenames (zero semantic leakage).
- SHA-256 cryptographic hashing of all stimuli.
- Strict blinding separation: public pre-registration vs. internal ground truth.
- Zero absolute paths in public outputs.
"""

import os
import io
import json
import uuid
import hashlib
from typing import Dict, Any, List, Tuple
import numpy as np
from PIL import Image

try:
    from reference_carrier_codec import (
        encode_carrier_E3_hybrid_scaling,
        encode_carrier_E4_Y0_hybrid_scaling,
    )
    from generate_exp028_c2_scenes import (
        generate_scene_pair,
        build_scene_specifications,
    )
except ImportError:
    from scripts.reference_carrier_codec import (
        encode_carrier_E3_hybrid_scaling,
        encode_carrier_E4_Y0_hybrid_scaling,
    )
    from scripts.generate_exp028_c2_scenes import (
        generate_scene_pair,
        build_scene_specifications,
    )


def compute_sha256_bytes(data: bytes) -> str:
    """Compute SHA-256 hash of byte array."""
    return hashlib.sha256(data).hexdigest()


def compute_sha256_file(path: str) -> str:
    """Compute SHA-256 hash of a file on disk."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def build_contact_sheet_512(video_rgb: np.ndarray) -> np.ndarray:
    """Build 512x512 4x4 contact sheet from 16 equidistant frames (0, 4, ..., 60).
    
    Each frame is upscaled from 64x64 to 128x128 using Lanczos / Bicubic filter.
    """
    total_frames = video_rgb.shape[0]
    frame_indices = [int(i * 4) for i in range(16)]
    tiles = []
    for idx in frame_indices:
        f = video_rgb[idx]
        im_tile = Image.fromarray(f).resize((128, 128), Image.Resampling.LANCZOS)
        tiles.append(np.array(im_tile, dtype=np.uint8))
        
    rows = []
    for r in range(4):
        row = np.concatenate(tiles[r*4:(r+1)*4], axis=1)
        rows.append(row)
    grid_512 = np.concatenate(rows, axis=0)
    assert grid_512.shape == (512, 512, 3), f"Bad grid shape: {grid_512.shape}"
    return grid_512


def build_exp028_stimuli_dataset(
    output_dir: str,
    random_seed: int = 20261028,
) -> Dict[str, Any]:
    """Generate all pilot and confirmatory stimuli and blinding records."""
    rng = np.random.default_rng(random_seed)
    specs = build_scene_specifications()

    os.makedirs(output_dir, exist_ok=True)
    pilot_dir = os.path.join(output_dir, "pilot")
    conf_dir = os.path.join(output_dir, "confirmatory")
    
    for d in [pilot_dir, conf_dir]:
        os.makedirs(os.path.join(d, "single"), exist_ok=True)
        os.makedirs(os.path.join(d, "paired"), exist_ok=True)

    prereg_records = {
        "experiment_id": "EXP-028",
        "phase": "Phase C2",
        "title": "Blinded VLM Comparison Benchmark: E3-K12 vs. E4-Y0",
        "random_seed": random_seed,
        "conditions": {
            "A": {
                "name": "E3_K12_WEBP_Q80",
                "codec": "E3-K12",
                "format": "WebP",
                "quality": 80,
                "resolution": [128, 128],
                "role": "Frozen Baseline Reference",
            },
            "B": {
                "name": "E4_Y0_WEBP_Q80",
                "codec": "E4-Y0",
                "format": "WebP",
                "quality": 80,
                "resolution": [128, 128],
                "role": "Primary Candidate",
            },
            "C": {
                "name": "E3_K12_PNG_LOSSLESS",
                "codec": "E3-K12",
                "format": "PNG",
                "quality": "lossless",
                "resolution": [128, 128],
                "role": "WebP Degradation Control on Baseline",
            },
            "D": {
                "name": "E4_Y0_PNG_LOSSLESS",
                "codec": "E4-Y0",
                "format": "PNG",
                "quality": "lossless",
                "resolution": [128, 128],
                "role": "WebP Degradation Control on Candidate",
            },
            "E": {
                "name": "GRID512_WEBP_Q80",
                "codec": "Contact Sheet 4x4",
                "format": "WebP",
                "quality": 80,
                "resolution": [512, 512],
                "role": "Conventional Spatial Quality Ceiling",
            },
        },
        "tasks": {
            "task1_unpaired_detection": {
                "description": "Single-image blind pulse detection in fresh isolated context.",
                "neutral_prompt": "Untersuche die dargestellte zeitliche Sequenz. Ist eine kurzzeitige Helligkeitsänderung eines Objekts erkennbar, die anschließend wieder verschwindet? Antworte mit 'ja', 'nein' oder 'unklar' und beschreibe kurz die sichtbare Grundlage deiner Einschätzung.",
                "carrier_format_guidance": "Das Bild ist ein 128x128 Visual Carrier mit 4 Quadranten (je 64x64):\n- Oben-Links: Basiszustand (Frame t=0)\n- Oben-Rechts: Temporale Kinematik (Rot=P0 Mittelwert, Grün=P2 Krümmung, Blau=höhere zeitliche Walsh-Moden)\n- Unten-Links: Chromatische Trägerschicht (Cb=P1 Trend, Cr=höhere zeitliche Walsh-Moden)\n- Unten-Rechts: Neutralgrau (128)",
                "contact_sheet_format_guidance": "Das Bild ist ein 512x512 4x4 Kontaktbogen aus 16 zeitlich aufeinanderfolgenden Videobildern. Die Zeit verläuft zeilenweise von oben-links nach unten-rechts (Zeile 0 = Anfang, Zeile 3 = Ende).",
                "extraction_schema": {
                    "stimulus_id": "string",
                    "event_detected": "ja | nein | unklar",
                    "confidence": "float [0.0, 1.0]",
                    "reasoning": "string",
                },
                "success_criterion": "Delta Balanced Accuracy >= +10.0% points for Condition B vs. Condition A, with Specificity drop <= 5.0% points.",
            },
            "task2_paired_discrimination": {
                "description": "Side-by-side presentation of twin pair (with vs. without pulse) under identical condition with randomized left/right placement.",
                "neutral_prompt": "Untersuche die beiden Darstellungen derselben Szene (Bild A links, Bild B rechts). Ist eine zeitlich begrenzte Veränderung zwischen den beiden Darstellungen erkennbar und in welcher Darstellung tritt sie auf? Antworte mit 'A', 'B' oder 'kein_Unterschied' und begründe kurz.",
                "extraction_schema": {
                    "pair_id": "string",
                    "differential_detected": "boolean",
                    "selected_image": "A | B | kein_Unterschied",
                    "confidence": "float [0.0, 1.0]",
                    "reasoning": "string",
                },
                "reporting": "Reported in independent 4-quadrant contingency matrix (isolated salient, differential only, inaccessible, unstable).",
            },
        },
        "pilot_stimuli": [],
        "pilot_paired_stimuli": [],
        "confirmatory_stimuli": [],
        "confirmatory_paired_stimuli": [],
    }

    ground_truth_records = {
        "experiment_id": "EXP-028",
        "phase": "Phase C2",
        "blinding_key": {},
        "paired_key": {},
        "scenes": {},
    }

    # Process both subsets
    for subset_name, config_list in [("pilot", specs["pilot"]), ("confirmatory", specs["confirmatory"])]:
        print(f"\n=======================================================")
        print(f"Generating {subset_name.upper()} Dataset ({len(config_list)} scenes)...")
        print(f"=======================================================")
        
        target_sub_dir = pilot_dir if subset_name == "pilot" else conf_dir
        
        for scene_cfg in config_list:
            scene_id = scene_cfg["scene_id"]
            print(f"\n[+] Scene: {scene_id} ({scene_cfg['trajectory']}, Y_bg={scene_cfg['bg_luminance']})")
            
            vid_neg, vid_pos, gt_meta = generate_scene_pair(scene_cfg)
            ground_truth_records["scenes"][scene_id] = gt_meta
            
            # 1. Generate Encoded Arrays for both twins
            # Condition A & C: E3-K12
            c_e3_neg = encode_carrier_E3_hybrid_scaling(vid_neg, K=12)
            c_e3_pos = encode_carrier_E3_hybrid_scaling(vid_pos, K=12)
            
            # Condition B & D: E4-Y0
            c_e4_neg = encode_carrier_E4_Y0_hybrid_scaling(vid_neg, K=12)
            c_e4_pos = encode_carrier_E4_Y0_hybrid_scaling(vid_pos, K=12)
            
            # Condition E: Grid512
            grid_neg = build_contact_sheet_512(vid_neg)
            grid_pos = build_contact_sheet_512(vid_pos)
            
            # Dictionary of arrays per condition
            cond_arrays = {
                "A": {"neg": c_e3_neg, "pos": c_e3_pos, "ext": "webp", "fmt": "WEBP", "q": 80},
                "B": {"neg": c_e4_neg, "pos": c_e4_pos, "ext": "webp", "fmt": "WEBP", "q": 80},
                "C": {"neg": c_e3_neg, "pos": c_e3_pos, "ext": "png", "fmt": "PNG", "q": None},
                "D": {"neg": c_e4_neg, "pos": c_e4_pos, "ext": "png", "fmt": "PNG", "q": None},
                "E": {"neg": grid_neg, "pos": grid_pos, "ext": "webp", "fmt": "WEBP", "q": 80},
            }
            
            # Generate Task 1 Single Stimuli for both neg and pos
            for twin_type, has_pulse in [("neg", False), ("pos", True)]:
                for cond_key, c_info in cond_arrays.items():
                    arr = c_info[twin_type]
                    ext = c_info["ext"]
                    fmt = c_info["fmt"]
                    q = c_info["q"]
                    
                    # Generate neutral random UUID
                    stim_uuid = f"stimulus_{uuid.uuid4().hex[:12]}"
                    file_name = f"{stim_uuid}.{ext}"
                    rel_path = f"stimuli/{subset_name}/single/{file_name}"
                    abs_path = os.path.join(target_sub_dir, "single", file_name)
                    
                    im = Image.fromarray(arr)
                    if fmt == "WEBP":
                        im.save(abs_path, format="WEBP", quality=q)
                    else:
                        im.save(abs_path, format="PNG")
                        
                    file_bytes = os.path.getsize(abs_path)
                    sha256 = compute_sha256_file(abs_path)
                    
                    # Pre-registration record (strictly blinded, NO scene/twin/pulse info)
                    prereg_entry = {
                        "stimulus_id": stim_uuid,
                        "relative_path": rel_path,
                        "condition": cond_key,
                        "format": fmt,
                        "bytes": file_bytes,
                        "sha256": sha256,
                    }
                    if subset_name == "pilot":
                        prereg_records["pilot_stimuli"].append(prereg_entry)
                    else:
                        prereg_records["confirmatory_stimuli"].append(prereg_entry)
                        
                    # Ground truth record (unblinded)
                    gt_entry = {
                        "stimulus_id": stim_uuid,
                        "relative_path": rel_path,
                        "subset": subset_name,
                        "scene_id": scene_id,
                        "condition": cond_key,
                        "twin_type": twin_type,
                        "has_pulse": has_pulse,
                        "ground_truth_event": "ja" if has_pulse else "nein",
                        "pulse_window_frames": gt_meta["pulse_window_frames"] if has_pulse else None,
                        "pulse_duration_seconds": 0.25 if has_pulse else 0.0,
                        "bytes": file_bytes,
                        "sha256": sha256,
                    }
                    ground_truth_records["blinding_key"][stim_uuid] = gt_entry
                    
            # Generate Task 2 Paired Stimuli for each condition
            for cond_key, c_info in cond_arrays.items():
                ext = c_info["ext"]
                fmt = c_info["fmt"]
                q = c_info["q"]
                
                # Randomize left vs right placement
                left_is_pos = bool(rng.random() < 0.5)
                arr_left = c_info["pos"] if left_is_pos else c_info["neg"]
                arr_right = c_info["neg"] if left_is_pos else c_info["pos"]
                
                # Side-by-side composite
                composite_arr = np.concatenate([arr_left, arr_right], axis=1)
                pair_uuid = f"pair_{uuid.uuid4().hex[:12]}"
                pair_filename = f"{pair_uuid}.{ext}"
                pair_rel_path = f"stimuli/{subset_name}/paired/{pair_filename}"
                pair_abs_path = os.path.join(target_sub_dir, "paired", pair_filename)
                
                im_comp = Image.fromarray(composite_arr)
                if fmt == "WEBP":
                    im_comp.save(pair_abs_path, format="WEBP", quality=q)
                else:
                    im_comp.save(pair_abs_path, format="PNG")
                    
                pair_bytes = os.path.getsize(pair_abs_path)
                pair_sha = compute_sha256_file(pair_abs_path)
                
                # Pre-registration entry
                pair_prereg = {
                    "pair_id": pair_uuid,
                    "relative_path": pair_rel_path,
                    "condition": cond_key,
                    "format": fmt,
                    "bytes": pair_bytes,
                    "sha256": pair_sha,
                }
                if subset_name == "pilot":
                    prereg_records["pilot_paired_stimuli"].append(pair_prereg)
                else:
                    prereg_records["confirmatory_paired_stimuli"].append(pair_prereg)
                    
                # Ground truth entry
                pair_gt = {
                    "pair_id": pair_uuid,
                    "relative_path": pair_rel_path,
                    "subset": subset_name,
                    "scene_id": scene_id,
                    "condition": cond_key,
                    "differential_present": True,
                    "ground_truth_selected_image": "A" if left_is_pos else "B",
                    "left_twin": "pos" if left_is_pos else "neg",
                    "right_twin": "neg" if left_is_pos else "pos",
                    "sha256": pair_sha,
                }
                ground_truth_records["paired_key"][pair_uuid] = pair_gt

    # Save Pre-Registration JSON (strictly relative paths, zero secrets)
    prereg_path = os.path.join(output_dir, "phase_c2_preregistration.json")
    with open(prereg_path, "w", encoding="utf-8") as f:
        json.dump(prereg_records, f, indent=2)
    print(f"\n[+] Saved public frozen pre-registration to: {prereg_path}")

    # Save Ground Truth JSON (for verified evaluation scoring)
    gt_path = os.path.join(output_dir, "verified_ground_truth.json")
    with open(gt_path, "w", encoding="utf-8") as f:
        json.dump(ground_truth_records, f, indent=2)
    print(f"[+] Saved verified ground truth to: {gt_path}")

    print("\nSummary:")
    print(f"  Pilot Single Stimuli:        {len(prereg_records['pilot_stimuli'])} (expected 80)")
    print(f"  Pilot Paired Stimuli:        {len(prereg_records['pilot_paired_stimuli'])} (expected 40)")
    print(f"  Confirmatory Single Stimuli: {len(prereg_records['confirmatory_stimuli'])} (expected 240)")
    print(f"  Confirmatory Paired Stimuli: {len(prereg_records['confirmatory_paired_stimuli'])} (expected 120)")
    return prereg_records


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="EXP-028 Phase C2 Stimulus Generator")
    parser.add_argument(
        "--out",
        default=os.path.join("experiments", "2026", "EXP-028", "phase_c2"),
        help="Target directory for Phase C2 stimuli and protocol",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=20261028,
        help="Deterministic random seed",
    )
    args = parser.parse_args()
    build_exp028_stimuli_dataset(args.out, random_seed=args.seed)
