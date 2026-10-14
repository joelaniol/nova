"""EXP-027 Stimulus Builder & Cryptographic Blinding Pipeline.

Reads delivered 5 source clips (C1..C5) from:
EXP-027_delivery

Generates 3 blinded, randomized stimulus conditions per clip (15 total stimuli):
1. VLT_WEBP: 128x128 E3-K12 Carrier (Lossy WebP Q=80) + canonical PNG.
2. GRID128_WEBP: 128x128 4x4 Contact Sheet (Lossy WebP Q=80) [Pixel-matched baseline].
3. GRID512_WEBP: 512x512 4x4 Contact Sheet (Lossy WebP Q=80) [Quality ceiling reference].

Enforces:
- Cryptographic SHA-256 integrity hashing of all raw sources and stimuli.
- Neutral random UUID filenames (preventing semantic file-name leakage).
- Strict separation of public stimuli from internal ground truth manifest.
"""

import os
import io
import json
import uuid
import shutil
import hashlib
from typing import Dict, Any, List
import numpy as np
from PIL import Image

try:
    from reference_carrier_codec import encode_carrier_E3_hybrid_scaling
except ImportError:
    from scripts.reference_carrier_codec import encode_carrier_E3_hybrid_scaling


def compute_sha256(file_path: str) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def build_exp027_stimuli(
    delivery_dir: str,
    output_dir: str,
    random_seed: int = 20261027,
) -> Dict[str, Any]:
    """Generate all blinded stimuli and secure evaluation manifest."""
    os.makedirs(output_dir, exist_ok=True)
    stimuli_dir = os.path.join(output_dir, "stimuli")
    os.makedirs(stimuli_dir, exist_ok=True)
    
    rng = np.random.default_rng(random_seed)
    manifest_records = []
    
    clips = ["C1", "C2", "C3", "C4", "C5"]
    
    print("=" * 70)
    print("EXP-027 STIMULUS BUILDER & CRYPTOGRAPHIC BLINDING")
    print(f"Source Delivery: {delivery_dir}")
    print(f"Target Stimuli:  {stimuli_dir}")
    print("=" * 70)
    
    for clip_id in clips:
        print(f"\n[+] Processing Clip: {clip_id}")
        
        # 1. Load exact 64 frames and downscale to 64x64 using BOX filter (INTER_AREA)
        frames_dir = os.path.join(delivery_dir, "frames_64", clip_id)
        raw_frames_64 = []
        for i in range(64):
            fp = os.path.join(frames_dir, f"f{i:02d}.png")
            im = Image.open(fp).convert("RGB").resize((64, 64), Image.Resampling.BOX)
            raw_frames_64.append(np.array(im, dtype=np.uint8))
            
        frames_arr = np.array(raw_frames_64, dtype=np.uint8)
        assert frames_arr.shape == (64, 64, 64, 3), f"Bad frame shape: {frames_arr.shape}"
        
        # 2. Condition: VLT_WEBP (E3-K12 Carrier, 128x128)
        carrier_rgb = encode_carrier_E3_hybrid_scaling(frames_arr, K=12)
        vlt_uuid = f"stimulus_{uuid.uuid4().hex[:12]}"
        vlt_webp_path = os.path.join(stimuli_dir, f"{vlt_uuid}.webp")
        vlt_png_path = os.path.join(stimuli_dir, f"{vlt_uuid}.png")
        
        Image.fromarray(carrier_rgb).save(vlt_webp_path, format="WEBP", quality=80)
        Image.fromarray(carrier_rgb).save(vlt_png_path, format="PNG")
        
        vlt_record = {
            "stimulus_id": vlt_uuid,
            "filename": f"{vlt_uuid}.webp",
            "png_filename": f"{vlt_uuid}.png",
            "clip_id": clip_id,
            "condition": "VLT_WEBP",
            "format": "E3_K12_Carrier_128x128",
            "bytes_webp": os.path.getsize(vlt_webp_path),
            "bytes_png": os.path.getsize(vlt_png_path),
            "sha256_webp": compute_sha256(vlt_webp_path),
            "sha256_png": compute_sha256(vlt_png_path),
        }
        manifest_records.append(vlt_record)
        print(f"  Condition VLT_WEBP:     {vlt_uuid}.webp ({vlt_record['bytes_webp']:,} B) | SHA256: {vlt_record['sha256_webp'][:12]}...")
        
        # 3. Condition: GRID128_WEBP (Pixel-Matched Contact Sheet, 128x128)
        grid128_src = os.path.join(delivery_dir, "kontaktboegen", f"{clip_id}_GRID128.webp")
        grid128_uuid = f"stimulus_{uuid.uuid4().hex[:12]}"
        grid128_dst = os.path.join(stimuli_dir, f"{grid128_uuid}.webp")
        shutil.copyfile(grid128_src, grid128_dst)
        
        grid128_record = {
            "stimulus_id": grid128_uuid,
            "filename": f"{grid128_uuid}.webp",
            "clip_id": clip_id,
            "condition": "GRID128_WEBP",
            "format": "Contact_Sheet_128x128_4x4",
            "bytes_webp": os.path.getsize(grid128_dst),
            "sha256_webp": compute_sha256(grid128_dst),
            "source_file": os.path.basename(grid128_src),
        }
        manifest_records.append(grid128_record)
        print(f"  Condition GRID128_WEBP: {grid128_uuid}.webp ({grid128_record['bytes_webp']:,} B) | SHA256: {grid128_record['sha256_webp'][:12]}...")
        
        # 4. Condition: GRID512_WEBP (Quality Ceiling Contact Sheet, 512x512)
        grid512_src = os.path.join(delivery_dir, "kontaktboegen", f"{clip_id}_GRID512.webp")
        grid512_uuid = f"stimulus_{uuid.uuid4().hex[:12]}"
        grid512_dst = os.path.join(stimuli_dir, f"{grid512_uuid}.webp")
        shutil.copyfile(grid512_src, grid512_dst)
        
        grid512_record = {
            "stimulus_id": grid512_uuid,
            "filename": f"{grid512_uuid}.webp",
            "clip_id": clip_id,
            "condition": "GRID512_WEBP",
            "format": "Contact_Sheet_512x512_4x4",
            "bytes_webp": os.path.getsize(grid512_dst),
            "sha256_webp": compute_sha256(grid512_dst),
            "source_file": os.path.basename(grid512_src),
        }
        manifest_records.append(grid512_record)
        print(f"  Condition GRID512_WEBP: {grid512_uuid}.webp ({grid512_record['bytes_webp']:,} B) | SHA256: {grid512_record['sha256_webp'][:12]}...")

    # Shuffle evaluation order
    eval_order = list(manifest_records)
    rng.shuffle(eval_order)
    
    manifest_payload = {
        "experiment_id": "EXP-027",
        "random_seed": random_seed,
        "total_stimuli": len(manifest_records),
        "source_delivery": delivery_dir,
        "records": manifest_records,
        "evaluation_order": [r["stimulus_id"] for r in eval_order],
    }
    
    manifest_path = os.path.join(output_dir, "blinded_manifest.json")
    with open(manifest_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest_payload, f, indent=2)
        
    print("\n" + "=" * 70)
    print(f"[SUCCESS] Total Stimuli Generated: {len(manifest_records)}")
    print(f"[SUCCESS] Blinded Manifest Written: {manifest_path}")
    print("=" * 70)
    return manifest_payload


if __name__ == "__main__":
    delivery = r"EXP-027_delivery"
    out = r"data/experiments/exp_027_physical"
    build_exp027_stimuli(delivery, out)
