"""EXP-027 Stimulus Builder & Cryptographic Blinding Pipeline.

Reads 5 source clips (C1..C5), resamples to canonical 64 frames (64x64 RGB),
and generates 3 randomized, blinded stimulus conditions per clip:
1. VLT_WEBP: 128x128 E3-K12 Carrier (Lossy WebP Q=80) + VLT_PNG.
2. GRID128_WEBP: 128x128 8x8 Contact Sheet (Lossy WebP Q=80) [Pixel-matched baseline].
3. GRID512_WEBP: 512x512 8x8 Contact Sheet (Lossy WebP Q=80) [Quality ceiling].
4. BASELINE_T0: 64x64 static frame at t=0.

Enforces:
- Cryptographic SHA-256 integrity hashing of all raw videos and stimuli.
- Neutral random UUID filenames (preventing semantic file-name leakage).
- Strict separation of public stimuli from internal ground truth manifest.
"""

import os
import io
import cv2
import json
import uuid
import hashlib
from typing import Dict, Any, List, Tuple
import numpy as np
from PIL import Image

try:
    from reference_carrier_codec import (
        encode_carrier_E3_hybrid_scaling,
    )
except ImportError:
    from scripts.reference_carrier_codec import (
        encode_carrier_E3_hybrid_scaling,
    )


def compute_sha256(file_path: str) -> str:
    """Compute SHA-256 hash of a file."""
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def load_and_resample_video(
    video_path: str,
    target_frames: int = 64,
    target_size: Tuple[int, int] = (64, 64),
    crop_corridor: bool = True,
) -> np.ndarray:
    """Decode video, resample temporally to target_frames, and crop/resize to target_size."""
    cap = cv2.VideoCapture(video_path)
    raw_frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        raw_frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cap.release()
    
    total = len(raw_frames)
    assert total >= target_frames, f"Video {video_path} has {total} frames, requires >= {target_frames}"
    
    indices = np.linspace(0, total - 1, target_frames, dtype=int)
    sampled = [raw_frames[i] for i in indices]
    
    processed = []
    for f in sampled:
        h, w, _ = f.shape
        if crop_corridor and w > h:
            # Crop motion corridor if horizontal widescreen
            roi_y1, roi_y2 = int(h * 0.25), int(h * 0.75)
            roi_x1, roi_x2 = 0, int(w * 0.65)
            crop = f[roi_y1:roi_y2, roi_x1:roi_x2]
            resized = cv2.resize(crop, target_size, interpolation=cv2.INTER_AREA)
        else:
            resized = cv2.resize(f, target_size, interpolation=cv2.INTER_AREA)
        processed.append(resized)
        
    return np.array(processed, dtype=np.uint8)


def create_contact_sheet(frames_64: np.ndarray, cell_size: int = 64) -> np.ndarray:
    """Create 8x8 contact sheet of 64 frames.
    
    cell_size=64 yields 512x512 grid.
    cell_size=16 yields 128x128 grid (pixel-matched to carrier).
    """
    rows = []
    for r in range(8):
        cols = []
        for c in range(8):
            f = frames_64[r * 8 + c]
            if cell_size != 64:
                f_cell = cv2.resize(f, (cell_size, cell_size), interpolation=cv2.INTER_AREA)
            else:
                f_cell = f
            cols.append(f_cell)
        rows.append(np.concatenate(cols, axis=1))
    return np.concatenate(rows, axis=0)


def build_exp027_stimuli(
    video_manifest: Dict[str, str],
    output_dir: str,
    random_seed: int = 20261027,
) -> Dict[str, Any]:
    """Generate all blinded stimuli and secure evaluation manifest."""
    os.makedirs(output_dir, exist_ok=True)
    stimuli_dir = os.path.join(output_dir, "stimuli")
    os.makedirs(stimuli_dir, exist_ok=True)
    
    rng = np.random.default_rng(random_seed)
    manifest_records = []
    
    for clip_id, video_path in sorted(video_manifest.items()):
        print(f"\nProcessing Clip: {clip_id} -> {video_path}")
        video_hash = compute_sha256(video_path)
        video_bytes = os.path.getsize(video_path)
        
        # Resample to canonical 64 frames
        frames_64 = load_and_resample_video(video_path, target_frames=64, target_size=(64, 64))
        
        # 1. Condition: VLT_CARRIER
        carrier_rgb = encode_carrier_E3_hybrid_scaling(frames_64, K=12)
        
        # VLT WebP
        vlt_webp_id = f"stimulus_{uuid.uuid4().hex[:12]}"
        vlt_webp_path = os.path.join(stimuli_dir, f"{vlt_webp_id}.webp")
        Image.fromarray(carrier_rgb).save(vlt_webp_path, format="WEBP", quality=80)
        vlt_webp_bytes = os.path.getsize(vlt_webp_path)
        vlt_webp_hash = compute_sha256(vlt_webp_path)
        
        # VLT PNG
        vlt_png_path = os.path.join(stimuli_dir, f"{vlt_webp_id}.png")
        Image.fromarray(carrier_rgb).save(vlt_png_path, format="PNG")
        vlt_png_bytes = os.path.getsize(vlt_png_path)
        vlt_png_hash = compute_sha256(vlt_png_path)
        
        manifest_records.append({
            "stimulus_id": vlt_webp_id,
            "filename": f"{vlt_webp_id}.webp",
            "png_filename": f"{vlt_webp_id}.png",
            "clip_id": clip_id,
            "condition": "VLT_WEBP",
            "format": "E3_K12_Carrier_128x128",
            "bytes_webp": vlt_webp_bytes,
            "bytes_png": vlt_png_bytes,
            "sha256_webp": vlt_webp_hash,
            "sha256_png": vlt_png_hash,
            "raw_video_sha256": video_hash,
        })
        
        # 2. Condition: GRID128_WEBP (Pixel-Matched Contact Sheet, 128x128)
        grid128_rgb = create_contact_sheet(frames_64, cell_size=16)
        grid128_id = f"stimulus_{uuid.uuid4().hex[:12]}"
        grid128_webp_path = os.path.join(stimuli_dir, f"{grid128_id}.webp")
        Image.fromarray(grid128_rgb).save(grid128_webp_path, format="WEBP", quality=80)
        grid128_bytes = os.path.getsize(grid128_webp_path)
        grid128_hash = compute_sha256(grid128_webp_path)
        
        manifest_records.append({
            "stimulus_id": grid128_id,
            "filename": f"{grid128_id}.webp",
            "clip_id": clip_id,
            "condition": "GRID128_WEBP",
            "format": "Contact_Sheet_128x128",
            "bytes_webp": grid128_bytes,
            "sha256_webp": grid128_hash,
            "raw_video_sha256": video_hash,
        })
        
        # 3. Condition: GRID512_WEBP (Quality Ceiling Contact Sheet, 512x512)
        grid512_rgb = create_contact_sheet(frames_64, cell_size=64)
        grid512_id = f"stimulus_{uuid.uuid4().hex[:12]}"
        grid512_webp_path = os.path.join(stimuli_dir, f"{grid512_id}.webp")
        Image.fromarray(grid512_rgb).save(grid512_webp_path, format="WEBP", quality=80)
        grid512_bytes = os.path.getsize(grid512_webp_path)
        grid512_hash = compute_sha256(grid512_webp_path)
        
        manifest_records.append({
            "stimulus_id": grid512_id,
            "filename": f"{grid512_id}.webp",
            "clip_id": clip_id,
            "condition": "GRID512_WEBP",
            "format": "Contact_Sheet_512x512",
            "bytes_webp": grid512_bytes,
            "sha256_webp": grid512_hash,
            "raw_video_sha256": video_hash,
        })
        
        # 4. Baseline: Single Frame t=0 (64x64)
        t0_id = f"stimulus_{uuid.uuid4().hex[:12]}"
        t0_path = os.path.join(stimuli_dir, f"{t0_id}.png")
        Image.fromarray(frames_64[0]).save(t0_path, format="PNG")
        t0_bytes = os.path.getsize(t0_path)
        t0_hash = compute_sha256(t0_path)
        
        manifest_records.append({
            "stimulus_id": t0_id,
            "filename": f"{t0_id}.png",
            "clip_id": clip_id,
            "condition": "BASELINE_T0",
            "format": "Single_Frame_64x64",
            "bytes_png": t0_bytes,
            "sha256_png": t0_hash,
            "raw_video_sha256": video_hash,
        })
        
        print(f"  VLT WebP:     {vlt_webp_bytes:,} B | Hash: {vlt_webp_hash[:8]}...")
        print(f"  Grid 128:     {grid128_bytes:,} B | Hash: {grid128_hash[:8]}...")
        print(f"  Grid 512:     {grid512_bytes:,} B | Hash: {grid512_hash[:8]}...")
        print(f"  Baseline t0:  {t0_bytes:,} B | Hash: {t0_hash[:8]}...")
        
    # Shuffle manifest records for evaluation order
    eval_order = list(manifest_records)
    rng.shuffle(eval_order)
    
    manifest_payload = {
        "experiment_id": "EXP-027",
        "random_seed": random_seed,
        "total_stimuli": len(manifest_records),
        "records": manifest_records,
        "evaluation_order": [r["stimulus_id"] for r in eval_order],
    }
    
    manifest_path = os.path.join(output_dir, "blinded_manifest.json")
    with open(manifest_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(manifest_payload, f, indent=2)
    print(f"\n[SUCCESS] Blinded manifest generated: {manifest_path}")
    return manifest_payload


if __name__ == "__main__":
    print("EXP-027 Stimulus Builder module ready.")
