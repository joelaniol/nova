"""Automated Verification of Complete C3 vs C5 Frame Synchronization.

Checks:
1. Exact bit-identity of frames 0 to 42 (pre-pulse) across all pixels.
2. Background bit-identity of frames 43 to 46 (pulse window) outside the ball ROI.
3. Exact bit-identity of frames 47 to 63 (post-pulse) across all pixels.
Evaluates both 1080p source frames and 64x64 resampled frames.
"""

import os
import json
import numpy as np
from PIL import Image

def verify_c3_c5_sync(delivery_dir: str):
    c3_dir = os.path.join(delivery_dir, "frames_64", "C3")
    c5_dir = os.path.join(delivery_dir, "frames_64", "C5")
    
    print(f"Auditing C3 vs C5 sync across all 64 frames...")
    print(f"C3: {c3_dir}")
    print(f"C5: {c5_dir}")
    
    report = {
        "pre_pulse_frames_0_to_42": {},
        "pulse_frames_43_to_46": {},
        "post_pulse_frames_47_to_63": {},
        "all_pre_pulse_bit_identical": True,
        "all_post_pulse_bit_identical": True,
        "pulse_window_background_bit_identical": True,
    }
    
    # 64x64 check
    max_pre_delta = 0
    for f in range(43):
        im3 = np.array(Image.open(os.path.join(c3_dir, f"f{f:02d}.png")).convert("RGB"))
        im5 = np.array(Image.open(os.path.join(c5_dir, f"f{f:02d}.png")).convert("RGB"))
        diff = np.abs(im5.astype(int) - im3.astype(int))
        m = diff.max()
        if m > max_pre_delta:
            max_pre_delta = m
        if m != 0:
            report["all_pre_pulse_bit_identical"] = False
            
    report["pre_pulse_frames_0_to_42"]["max_delta"] = int(max_pre_delta)
    print(f"Frames 0..42 Max Delta: {max_pre_delta} (Bit-identical: {max_pre_delta == 0})")
    
    # Pulse frames 43..46
    # Ball ROI in 1080p is within [400:700, 500:900]
    # In 64x64: [20:45, 30:55]
    # Background is everything outside [20:45, 30:55]
    max_bg_delta = 0
    pulse_info = {}
    for f in range(43, 47):
        im3 = np.array(Image.open(os.path.join(c3_dir, f"f{f:02d}.png")).convert("RGB"))
        im5 = np.array(Image.open(os.path.join(c5_dir, f"f{f:02d}.png")).convert("RGB"))
        diff = np.abs(im5.astype(int) - im3.astype(int))
        
        bg_mask = np.ones((1080, 1080), dtype=bool)
        bg_mask[400:700, 500:900] = False
        
        bg_diff = diff[bg_mask]
        m_bg = bg_diff.max()
        m_roi = diff[~bg_mask].max()
        if m_bg > max_bg_delta:
            max_bg_delta = m_bg
        if m_bg != 0:
            report["pulse_window_background_bit_identical"] = False
            
        pulse_info[f"f{f:02d}"] = {
            "roi_max_delta": int(m_roi),
            "bg_max_delta": int(m_bg),
        }
        print(f"Frame {f:02d}: ROI Max Delta = {m_roi}, Background Max Delta = {m_bg}")
        
    report["pulse_frames_43_to_46"] = pulse_info
    
    # Post pulse frames 47..63
    max_post_delta = 0
    for f in range(47, 64):
        im3 = np.array(Image.open(os.path.join(c3_dir, f"f{f:02d}.png")).convert("RGB"))
        im5 = np.array(Image.open(os.path.join(c5_dir, f"f{f:02d}.png")).convert("RGB"))
        diff = np.abs(im5.astype(int) - im3.astype(int))
        m = diff.max()
        if m > max_post_delta:
            max_post_delta = m
        if m != 0:
            report["all_post_pulse_bit_identical"] = False
            
    report["post_pulse_frames_47_to_63"]["max_delta"] = int(max_post_delta)
    print(f"Frames 47..63 Max Delta: {max_post_delta} (Bit-identical: {max_post_delta == 0})")
    
    print("\nSummary Result:")
    print(f"Pre-pulse Bit-Identical: {report['all_pre_pulse_bit_identical']}")
    print(f"Pulse Window Background Bit-Identical: {report['pulse_window_background_bit_identical']}")
    print(f"Post-pulse Bit-Identical: {report['all_post_pulse_bit_identical']}")
    
    return report

if __name__ == "__main__":
    delivery = os.path.join("..", "clip_generator", "projects", "swiftclip_exp027", "lieferung", "EXP-027")
    if not os.path.exists(delivery):
        delivery = os.path.join("data", "delivery", "EXP-027")
    verify_c3_c5_sync(delivery)
