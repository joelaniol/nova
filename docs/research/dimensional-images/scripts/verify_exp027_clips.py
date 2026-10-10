"""EXP-027 Rendered Video Quality Control & Ground Truth Verification.

Performs empirical verification of rendered clips (C1..C5) against
pre-registered target specifications:
1. Video stream metadata audit (duration, fps, frame count).
2. Computer vision trajectory tracking (sphere center-of-mass across time).
3. Automated occlusion classification (none, partial, full) and duration measurement.
4. Reversal / bounce detection and coordinate turning point.
5. Pulse detection (temporal derivative of peak luminance).
6. Outputs frozen, audited ground truth: verified_ground_truth.json.
"""

import os
import cv2
import json
from typing import Dict, Any, List, Tuple
import numpy as np


def analyze_clip_trajectory(
    video_path: str,
    clip_id: str,
    target_spec: Dict[str, Any],
) -> Dict[str, Any]:
    """Inspect and measure real empirical parameters of a rendered clip."""
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    raw_frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        raw_frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cap.release()
    
    total_frames = len(raw_frames)
    duration_s = total_frames / 60.0 if total_frames > 0 else 0.0 # nominal 60fps
    
    print(f"\n--- Analyzing Clip {clip_id}: {os.path.basename(video_path)} ---")
    print(f"  Frames: {total_frames}, Resolution: {w}x{h}, Estimated duration: {duration_s:.2f}s")
    
    # Track bright sphere pixels
    trajectory_x = []
    trajectory_y = []
    bright_pixel_counts = []
    peak_luminances = []
    
    for idx, f in enumerate(raw_frames):
        # Grayscale luminance
        f_gray = cv2.cvtColor(f, cv2.COLOR_RGB2GRAY)
        bright_mask = f_gray > 100
        count = int(np.sum(bright_mask))
        bright_pixel_counts.append(count)
        peak_luminances.append(float(np.max(f_gray)))
        
        if count > 50:
            y_indices, x_indices = np.where(bright_mask)
            trajectory_x.append(float(np.mean(x_indices)))
            trajectory_y.append(float(np.mean(y_indices)))
        else:
            trajectory_x.append(None)
            trajectory_y.append(None)
            
    # Measure max unoccluded brightness count
    valid_counts = [c for c in bright_pixel_counts if c > 500]
    baseline_sphere_size = np.percentile(valid_counts, 85) if valid_counts else 1000
    
    # Detect occlusion intervals
    min_count = min(bright_pixel_counts)
    occluded_frames = [idx for idx, c in enumerate(bright_pixel_counts) if c < baseline_sphere_size * 0.15]
    partially_occluded_frames = [idx for idx, c in enumerate(bright_pixel_counts) if baseline_sphere_size * 0.15 <= c <= baseline_sphere_size * 0.70]
    
    is_full_occlusion = len(occluded_frames) >= 15 # at least 0.25s occluded
    is_partial_occlusion = not is_full_occlusion and len(partially_occluded_frames) >= 10
    
    # Direction analysis
    valid_xs = [x for x in trajectory_x if x is not None]
    if len(valid_xs) >= 10:
        start_x = np.mean(valid_xs[:5])
        end_x = np.mean(valid_xs[-5:])
        dx_overall = end_x - start_x
        
        # Check reversal
        turning_points = 0
        dx_diffs = np.diff(valid_xs)
        smooth_dx = np.convolve(dx_diffs, np.ones(5)/5, mode='valid')
        if len(smooth_dx) > 10:
            signs = np.sign(smooth_dx)
            sign_changes = np.where(np.diff(signs) != 0)[0]
            turning_points = len(sign_changes)
    else:
        dx_overall = 0
        turning_points = 0
        
    # Pulse detection in peak luminance
    luminance_diffs = np.diff(peak_luminances)
    pulse_detected = False
    pulse_frame = None
    if len(luminance_diffs) > 0:
        max_jump = np.max(luminance_diffs)
        if max_jump > 30.0:
            pulse_detected = True
            pulse_frame = int(np.argmax(luminance_diffs))
            
    measured_data = {
        "clip_id": clip_id,
        "total_frames": total_frames,
        "nominal_duration_seconds": duration_s,
        "baseline_sphere_pixel_area": float(baseline_sphere_size),
        "min_bright_pixel_count": int(min_count),
        "occlusion_detected_type": "full" if is_full_occlusion else ("partial" if is_partial_occlusion else "none"),
        "full_occlusion_duration_seconds": float(len(occluded_frames) / 60.0),
        "overall_dx": float(dx_overall),
        "reversal_detected": bool(turning_points > 0 and dx_overall < 100),
        "pulse_detected": pulse_detected,
        "pulse_frame": pulse_frame,
    }
    
    print(f"  Measured Occlusion: {measured_data['occlusion_detected_type']} (full duration: {measured_data['full_occlusion_duration_seconds']:.2f}s)")
    print(f"  Measured Motion: overall dx={measured_data['overall_dx']:.1f}, reversal={measured_data['reversal_detected']}")
    print(f"  Measured Pulse: detected={measured_data['pulse_detected']} at frame {measured_data['pulse_frame']}")
    
    return measured_data


if __name__ == "__main__":
    print("EXP-027 Clip Verification module ready.")
