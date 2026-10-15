"""Physical Scene Generator for EXP-028 Phase C2 Blind Benchmark.

Generates deterministic physical twin scene pairs (negative without pulse, positive with 250ms pulse).
Video format: 64 frames @ 64x64 RGB (uint8), representing a 4.0-second sequence.

Features:
- Parameterized 3D-shaded sphere with Lambertian diffuse + Blinn-Phong specular highlight.
- Soft floor contact shadow responding to sphere position and elevation.
- Background studio geometry with perspective floor plane, wall, and studio vignette.
- Obstacle geometry: static 3D block with front face, top bevel, and left highlight.
- 4 Trajectory classes:
    1. left_to_right_occluded: Sphere rolls L->R behind obstacle at z=-1.
    2. right_to_left_occluded: Sphere rolls R->L behind obstacle at z=-1.
    3. bounce_reversal: Sphere rolls towards obstacle at z=1, bounces at t_bounce, rolls back.
    4. diagonal_unobstructed: Sphere moves diagonally across scene with no occlusion.
- Systematically varied background luminance Y_bg in [18, 160] across 4 tiers:
    - Tier 1 (Dark Studio): Y_bg in [18, 30]
    - Tier 2 (Dim Ambient): Y_bg in [45, 65]
    - Tier 3 (Mid Gray): Y_bg in [80, 110]
    - Tier 4 (Bright Studio): Y_bg in [130, 160]
- 250ms Brightness Pulse:
    - Exactly 4 frames (frames 42..45 in default 64-frame sequence).
    - Smooth triangular/half-sine envelope peaking at Delta Y approx 100-120 LSB.
    - Negative twin is 100.0% bit-identical to positive twin outside pulse frames.
"""

import os
import math
import json
from typing import Dict, Any, Tuple, List, Optional
import numpy as np
from PIL import Image


def render_scene_frame(
    t: int,
    total_frames: int,
    ball_pos_start: Tuple[float, float, float],
    ball_pos_end: Tuple[float, float, float],
    ball_radius: float,
    ball_base_rgb: Tuple[float, float, float],
    bg_luminance: float,
    has_obstacle: bool = True,
    obstacle_rect: Optional[Tuple[float, float, float, float]] = None,
    pulse_frames: Optional[Tuple[int, int]] = None,
    pulse_intensity: float = 0.0,
    bounce: bool = False,
    bounce_t: float = 0.5,
) -> np.ndarray:
    """Render a single 64x64 RGB frame with full physical shading."""
    H, W = 64, 64
    frame = np.zeros((H, W, 3), dtype=np.float64)

    # 1. Background Floor (lower half) & Wall (upper half)
    floor_horizon = 26
    wall_y = np.arange(floor_horizon)[:, None]
    wall_lum = bg_luminance * (0.85 + 0.15 * (wall_y / floor_horizon))
    frame[:floor_horizon, :, 0] = wall_lum * 0.95
    frame[:floor_horizon, :, 1] = wall_lum * 1.00
    frame[:floor_horizon, :, 2] = wall_lum * 1.08  # cool tint

    floor_y = np.arange(H - floor_horizon)[:, None]
    floor_lum = bg_luminance * (1.05 + 0.25 * (floor_y / (H - floor_horizon)))
    frame[floor_horizon:, :, 0] = floor_lum * 1.02
    frame[floor_horizon:, :, 1] = floor_lum * 1.00
    frame[floor_horizon:, :, 2] = floor_lum * 0.96  # warm tint

    # Studio vignette
    yy, xx = np.mgrid[:H, :W]
    dist_center = np.sqrt((xx - 32.0)**2 + (yy - 32.0)**2) / 45.0
    vignette = np.clip(1.0 - 0.15 * dist_center**2, 0.70, 1.0)[:, :, None]
    frame *= vignette

    # 2. Sphere trajectory interpolation
    norm_t = t / (total_frames - 1)
    if bounce:
        if norm_t < bounce_t:
            sub_t = norm_t / bounce_t
            bx = ball_pos_start[0] + sub_t * (ball_pos_end[0] - ball_pos_start[0])
            by = ball_pos_start[1] + sub_t * (ball_pos_end[1] - ball_pos_start[1])
            bz = ball_pos_start[2] + sub_t * (ball_pos_end[2] - ball_pos_start[2])
        else:
            sub_t = (norm_t - bounce_t) / (1.0 - bounce_t)
            bx = ball_pos_end[0] + sub_t * (ball_pos_start[0] - ball_pos_end[0])
            by = ball_pos_end[1] + sub_t * (ball_pos_start[1] - ball_pos_end[1])
            bz = ball_pos_end[2] + sub_t * (ball_pos_start[2] - ball_pos_end[2])
    else:
        bx = ball_pos_start[0] + norm_t * (ball_pos_end[0] - ball_pos_start[0])
        by = ball_pos_start[1] + norm_t * (ball_pos_end[1] - ball_pos_start[1])
        bz = ball_pos_start[2] + norm_t * (ball_pos_end[2] - ball_pos_start[2])

    # 3. Soft Floor Contact Shadow
    shadow_cx = bx + 2.0
    shadow_cy = by + ball_radius * 0.85
    shadow_rx = ball_radius * 1.15
    shadow_ry = ball_radius * 0.45
    shadow_dist = ((xx - shadow_cx) / shadow_rx)**2 + ((yy - shadow_cy) / shadow_ry)**2
    shadow_mask = shadow_dist <= 2.5
    shadow_atten = np.clip(1.0 - 0.45 * np.exp(-0.5 * shadow_dist), 0.55, 1.0)
    frame[shadow_mask] *= shadow_atten[shadow_mask, None]

    # 4. Obstacle Geometry
    if obstacle_rect is None:
        obstacle_rect = (25.0, 39.0, 22.0, 48.0)
    ox_min, ox_max, oy_min, oy_max = obstacle_rect

    obs_behind = (has_obstacle and bz >= 0.0)
    obs_in_front = (has_obstacle and bz < 0.0)

    def draw_obstacle():
        obs_mask = (xx >= ox_min) & (xx <= ox_max) & (yy >= oy_min) & (yy <= oy_max)
        obs_base = np.array([95.0, 110.0, 130.0], dtype=np.float64)
        # Adapt obstacle slightly to ambient light
        obs_adj = obs_base * (0.6 + 0.4 * (bg_luminance / 100.0))
        frame[obs_mask] = obs_adj * 0.85
        top_mask = (xx >= ox_min) & (xx <= ox_max) & (yy >= oy_min) & (yy <= oy_min + 2)
        frame[top_mask] = obs_adj * 1.25
        left_mask = (xx >= ox_min) & (xx <= ox_min + 1) & (yy >= oy_min) & (yy <= oy_max)
        frame[left_mask] = obs_adj * 1.15

    if obs_behind:
        draw_obstacle()

    # 5. 3D Shaded Sphere
    ball_dist_sq = (xx - bx)**2 + (yy - by)**2
    ball_mask = ball_dist_sq <= ball_radius**2
    if np.any(ball_mask):
        dx = (xx[ball_mask] - bx) / ball_radius
        dy = (yy[ball_mask] - by) / ball_radius
        dz = np.sqrt(np.maximum(0.0, 1.0 - dx**2 - dy**2))

        # Directional light
        lx, ly, lz = -0.5, -0.6, 0.62
        l_len = math.sqrt(lx**2 + ly**2 + lz**2)
        lx, ly, lz = lx / l_len, ly / l_len, lz / l_len

        # Lambertian diffuse
        ndotl = np.maximum(0.0, -(dx * lx + dy * ly - dz * lz))
        diffuse = 0.25 + 0.75 * ndotl

        # Specular Blinn-Phong
        hx, hy, hz = lx, ly, lz + 1.0
        h_len = math.sqrt(hx**2 + hy**2 + hz**2)
        hx, hy, hz = hx / h_len, hy / h_len, hz / h_len
        ndoth = np.maximum(0.0, -(dx * hx + dy * hy - dz * hz))
        specular = 0.45 * (ndoth ** 16)

        # Pulse modulation (triangular envelope across pulse window)
        pulse_factor = 0.0
        if pulse_frames is not None and pulse_frames[0] <= t <= pulse_frames[1]:
            p_len = pulse_frames[1] - pulse_frames[0]
            p_mid = 0.5 * (pulse_frames[0] + pulse_frames[1])
            p_dist = abs(t - p_mid) / (0.5 * p_len + 0.1)
            pulse_factor = max(0.0, 1.0 - p_dist) * pulse_intensity

        base_col = np.array(ball_base_rgb, dtype=np.float64)
        ball_rgb = base_col * diffuse[:, None] + 255.0 * specular[:, None] + pulse_factor
        frame[ball_mask] = ball_rgb

    if obs_in_front:
        draw_obstacle()

    return np.clip(np.round(frame), 0, 255).astype(np.uint8)


def generate_scene_pair(
    scene_config: Dict[str, Any],
) -> Tuple[np.ndarray, np.ndarray, Dict[str, Any]]:
    """Render a matched negative and positive video twin pair.
    
    Returns:
        video_neg: Shape (64, 64, 64, 3) uint8
        video_pos: Shape (64, 64, 64, 3) uint8
        ground_truth: Dict with verified event parameters
    """
    total_frames = 64
    ball_radius = scene_config.get("ball_radius", 5.5)
    ball_base_rgb = scene_config.get("ball_base_rgb", (210.0, 215.0, 220.0))
    bg_luminance = scene_config["bg_luminance"]
    has_obstacle = scene_config.get("has_obstacle", True)
    obstacle_rect = scene_config.get("obstacle_rect", (25.0, 39.0, 22.0, 48.0))
    pulse_intensity = scene_config.get("pulse_intensity", 120.0)
    pulse_window = scene_config.get("pulse_window", (42, 45))
    trajectory = scene_config["trajectory"]
    bounce = (trajectory == "bounce_reversal")
    bounce_t = scene_config.get("bounce_t", 0.5)

    p_start = scene_config["ball_pos_start"]
    p_end = scene_config["ball_pos_end"]

    frames_neg = []
    frames_pos = []

    for t in range(total_frames):
        f_neg = render_scene_frame(
            t=t,
            total_frames=total_frames,
            ball_pos_start=p_start,
            ball_pos_end=p_end,
            ball_radius=ball_radius,
            ball_base_rgb=ball_base_rgb,
            bg_luminance=bg_luminance,
            has_obstacle=has_obstacle,
            obstacle_rect=obstacle_rect,
            pulse_frames=None,
            pulse_intensity=0.0,
            bounce=bounce,
            bounce_t=bounce_t,
        )
        frames_neg.append(f_neg)

        f_pos = render_scene_frame(
            t=t,
            total_frames=total_frames,
            ball_pos_start=p_start,
            ball_pos_end=p_end,
            ball_radius=ball_radius,
            ball_base_rgb=ball_base_rgb,
            bg_luminance=bg_luminance,
            has_obstacle=has_obstacle,
            obstacle_rect=obstacle_rect,
            pulse_frames=pulse_window,
            pulse_intensity=pulse_intensity,
            bounce=bounce,
            bounce_t=bounce_t,
        )
        frames_pos.append(f_pos)

    vid_neg = np.stack(frames_neg, axis=0)
    vid_pos = np.stack(frames_pos, axis=0)

    # Verification of bit-identity outside pulse window
    for t in range(total_frames):
        if not (pulse_window[0] <= t <= pulse_window[1]):
            delta = np.max(np.abs(vid_pos[t].astype(int) - vid_neg[t].astype(int)))
            assert delta == 0, f"Sync error: frame {t} differed outside pulse window (max delta={delta})!"

    max_pulse_delta = int(np.max(np.abs(vid_pos.astype(int) - vid_neg.astype(int))))
    assert max_pulse_delta > 50, f"Pulse intensity too low: max delta={max_pulse_delta}"

    ground_truth = {
        "scene_id": scene_config["scene_id"],
        "scene_set": scene_config["scene_set"],  # "pilot" or "confirmatory"
        "trajectory": trajectory,
        "bg_luminance": bg_luminance,
        "has_obstacle": has_obstacle,
        "pulse_window_frames": list(pulse_window),
        "pulse_window_seconds": [round(pulse_window[0] * 4.0 / 64.0, 3), round(pulse_window[1] * 4.0 / 64.0, 3)],
        "pulse_duration_frames": pulse_window[1] - pulse_window[0] + 1,
        "pulse_duration_seconds": 0.25,
        "max_rendered_pulse_delta": max_pulse_delta,
        "ball_radius": ball_radius,
    }

    return vid_neg, vid_pos, ground_truth


def build_scene_specifications() -> Dict[str, List[Dict[str, Any]]]:
    """Build exact parameter configurations for 8 Pilot and 24 Confirmatory scenes."""
    
    # -------------------------------------------------------------------------
    # 8 TECHNICAL PILOT SCENES (P01..P08)
    # -------------------------------------------------------------------------
    pilot_configs = [
        # P01: Dark studio, L->R occluded
        {
            "scene_id": "P01_dark_lr_occluded",
            "scene_set": "pilot",
            "trajectory": "left_to_right_occluded",
            "bg_luminance": 25.0,
            "ball_pos_start": (8.0, 38.0, -1.0),
            "ball_pos_end": (56.0, 38.0, -1.0),
            "ball_radius": 5.5,
            "has_obstacle": True,
            "obstacle_rect": (25.0, 39.0, 22.0, 48.0),
            "pulse_window": (42, 45),
            "pulse_intensity": 120.0,
        },
        # P02: Dim ambient, R->L occluded
        {
            "scene_id": "P02_dim_rl_occluded",
            "scene_set": "pilot",
            "trajectory": "right_to_left_occluded",
            "bg_luminance": 55.0,
            "ball_pos_start": (56.0, 38.0, -1.0),
            "ball_pos_end": (8.0, 38.0, -1.0),
            "ball_radius": 5.5,
            "has_obstacle": True,
            "obstacle_rect": (25.0, 39.0, 22.0, 48.0),
            "pulse_window": (42, 45),
            "pulse_intensity": 115.0,
        },
        # P03: Mid gray, Bounce reversal
        {
            "scene_id": "P03_mid_bounce_reversal",
            "scene_set": "pilot",
            "trajectory": "bounce_reversal",
            "bg_luminance": 90.0,
            "ball_pos_start": (8.0, 38.0, 1.0),
            "ball_pos_end": (25.0, 38.0, 1.0),
            "ball_radius": 5.5,
            "has_obstacle": True,
            "obstacle_rect": (27.0, 41.0, 22.0, 48.0),
            "pulse_window": (40, 43),
            "pulse_intensity": 120.0,
            "bounce_t": 0.5,
        },
        # P04: Bright studio, Diagonal unobstructed
        {
            "scene_id": "P04_bright_diagonal_unobstructed",
            "scene_set": "pilot",
            "trajectory": "diagonal_unobstructed",
            "bg_luminance": 140.0,
            "ball_pos_start": (8.0, 30.0, 1.0),
            "ball_pos_end": (56.0, 46.0, 1.0),
            "ball_radius": 5.5,
            "has_obstacle": False,
            "pulse_window": (42, 45),
            "pulse_intensity": 110.0,
        },
        # P05: Dark studio, Bounce reversal
        {
            "scene_id": "P05_dark_bounce_reversal",
            "scene_set": "pilot",
            "trajectory": "bounce_reversal",
            "bg_luminance": 22.0,
            "ball_pos_start": (10.0, 36.0, 1.0),
            "ball_pos_end": (26.0, 36.0, 1.0),
            "ball_radius": 6.0,
            "has_obstacle": True,
            "obstacle_rect": (28.0, 42.0, 20.0, 46.0),
            "pulse_window": (42, 45),
            "pulse_intensity": 125.0,
            "bounce_t": 0.5,
        },
        # P06: Dim ambient, Diagonal unobstructed
        {
            "scene_id": "P06_dim_diagonal_unobstructed",
            "scene_set": "pilot",
            "trajectory": "diagonal_unobstructed",
            "bg_luminance": 60.0,
            "ball_pos_start": (56.0, 46.0, 1.0),
            "ball_pos_end": (8.0, 30.0, 1.0),
            "ball_radius": 5.0,
            "has_obstacle": False,
            "pulse_window": (42, 45),
            "pulse_intensity": 115.0,
        },
        # P07: Mid gray, L->R occluded
        {
            "scene_id": "P07_mid_lr_occluded",
            "scene_set": "pilot",
            "trajectory": "left_to_right_occluded",
            "bg_luminance": 85.0,
            "ball_pos_start": (8.0, 38.0, -1.0),
            "ball_pos_end": (56.0, 38.0, -1.0),
            "ball_radius": 5.5,
            "has_obstacle": True,
            "obstacle_rect": (24.0, 40.0, 22.0, 48.0),
            "pulse_window": (44, 47),
            "pulse_intensity": 120.0,
        },
        # P08: Bright studio, R->L occluded
        {
            "scene_id": "P08_bright_rl_occluded",
            "scene_set": "pilot",
            "trajectory": "right_to_left_occluded",
            "bg_luminance": 145.0,
            "ball_pos_start": (56.0, 38.0, -1.0),
            "ball_pos_end": (8.0, 38.0, -1.0),
            "ball_radius": 5.5,
            "has_obstacle": True,
            "obstacle_rect": (25.0, 39.0, 22.0, 48.0),
            "pulse_window": (42, 45),
            "pulse_intensity": 110.0,
        },
    ]

    # -------------------------------------------------------------------------
    # 24 CONFIRMATORY SCENES (S01..S24)
    # Balanced 4x4 matrix: 4 trajectory classes x 4 luminance tiers + variations
    # -------------------------------------------------------------------------
    traj_classes = [
        "left_to_right_occluded",
        "right_to_left_occluded",
        "bounce_reversal",
        "diagonal_unobstructed",
    ]
    lum_tiers = [
        ("dark", 24.0),
        ("dim", 55.0),
        ("mid", 95.0),
        ("bright", 145.0),
    ]

    confirmatory_configs = []
    idx = 1
    # 4 trajectories x 4 luminance tiers = 16 base grid scenes
    for traj in traj_classes:
        for lum_name, lum_val in lum_tiers:
            # Trajectory specific coordinates
            if traj == "left_to_right_occluded":
                p_start = (8.0, 38.0, -1.0)
                p_end = (56.0, 38.0, -1.0)
                has_obs = True
                obs_rect = (25.0, 39.0, 22.0, 48.0)
                pulse_win = (42, 45)
            elif traj == "right_to_left_occluded":
                p_start = (56.0, 38.0, -1.0)
                p_end = (8.0, 38.0, -1.0)
                has_obs = True
                obs_rect = (25.0, 39.0, 22.0, 48.0)
                pulse_win = (42, 45)
            elif traj == "bounce_reversal":
                p_start = (8.0, 38.0, 1.0)
                p_end = (25.0, 38.0, 1.0)
                has_obs = True
                obs_rect = (27.0, 41.0, 22.0, 48.0)
                pulse_win = (40, 43)
            elif traj == "diagonal_unobstructed":
                p_start = (8.0, 32.0, 1.0)
                p_end = (56.0, 44.0, 1.0)
                has_obs = False
                obs_rect = None
                pulse_win = (42, 45)

            cfg = {
                "scene_id": f"S{idx:02d}_{traj[:6]}_{lum_name}",
                "scene_set": "confirmatory",
                "trajectory": traj,
                "bg_luminance": lum_val,
                "ball_pos_start": p_start,
                "ball_pos_end": p_end,
                "ball_radius": 5.5,
                "has_obstacle": has_obs,
                "obstacle_rect": obs_rect,
                "pulse_window": pulse_win,
                "pulse_intensity": 115.0 if lum_val > 100 else 120.0,
            }
            confirmatory_configs.append(cfg)
            idx += 1

    # 8 additional scenes to complete 24: variation in radius, elevation, pulse window
    extras = [
        # S17: Dark, High elevation L->R
        {
            "trajectory": "left_to_right_occluded",
            "bg_luminance": 28.0,
            "ball_pos_start": (8.0, 32.0, -1.0),
            "ball_pos_end": (56.0, 32.0, -1.0),
            "ball_radius": 4.8,
            "has_obstacle": True,
            "obstacle_rect": (25.0, 39.0, 18.0, 44.0),
            "pulse_window": (44, 47),
            "name": "dark_lr_high",
        },
        # S18: Dim, Low elevation R->L
        {
            "trajectory": "right_to_left_occluded",
            "bg_luminance": 50.0,
            "ball_pos_start": (56.0, 44.0, -1.0),
            "ball_pos_end": (8.0, 44.0, -1.0),
            "ball_radius": 6.2,
            "has_obstacle": True,
            "obstacle_rect": (25.0, 39.0, 26.0, 52.0),
            "pulse_window": (40, 43),
            "name": "dim_rl_low",
        },
        # S19: Mid, Large sphere Bounce
        {
            "trajectory": "bounce_reversal",
            "bg_luminance": 88.0,
            "ball_pos_start": (6.0, 38.0, 1.0),
            "ball_pos_end": (23.0, 38.0, 1.0),
            "ball_radius": 6.8,
            "has_obstacle": True,
            "obstacle_rect": (25.0, 39.0, 22.0, 48.0),
            "pulse_window": (42, 45),
            "name": "mid_bounce_large",
        },
        # S20: Bright, Steep diagonal
        {
            "trajectory": "diagonal_unobstructed",
            "bg_luminance": 135.0,
            "ball_pos_start": (12.0, 48.0, 1.0),
            "ball_pos_end": (52.0, 28.0, 1.0),
            "ball_radius": 5.0,
            "has_obstacle": False,
            "obstacle_rect": None,
            "pulse_window": (42, 45),
            "name": "bright_diag_steep",
        },
        # S21: Dark, Wide obstacle L->R
        {
            "trajectory": "left_to_right_occluded",
            "bg_luminance": 18.0,
            "ball_pos_start": (8.0, 38.0, -1.0),
            "ball_pos_end": (56.0, 38.0, -1.0),
            "ball_radius": 5.5,
            "has_obstacle": True,
            "obstacle_rect": (22.0, 42.0, 22.0, 48.0),
            "pulse_window": (45, 48),
            "name": "dark_lr_wideblock",
        },
        # S22: Dim, Narrow obstacle R->L
        {
            "trajectory": "right_to_left_occluded",
            "bg_luminance": 62.0,
            "ball_pos_start": (56.0, 38.0, -1.0),
            "ball_pos_end": (8.0, 38.0, -1.0),
            "ball_radius": 5.5,
            "has_obstacle": True,
            "obstacle_rect": (28.0, 36.0, 22.0, 48.0),
            "pulse_window": (40, 43),
            "name": "dim_rl_narrowblock",
        },
        # S23: Mid, Early pulse Bounce
        {
            "trajectory": "bounce_reversal",
            "bg_luminance": 105.0,
            "ball_pos_start": (8.0, 38.0, 1.0),
            "ball_pos_end": (25.0, 38.0, 1.0),
            "ball_radius": 5.2,
            "has_obstacle": True,
            "obstacle_rect": (27.0, 41.0, 22.0, 48.0),
            "pulse_window": (38, 41),
            "name": "mid_bounce_earlypulse",
        },
        # S24: Bright, Small sphere L->R
        {
            "trajectory": "left_to_right_occluded",
            "bg_luminance": 155.0,
            "ball_pos_start": (8.0, 38.0, -1.0),
            "ball_pos_end": (56.0, 38.0, -1.0),
            "ball_radius": 4.5,
            "has_obstacle": True,
            "obstacle_rect": (25.0, 39.0, 22.0, 48.0),
            "pulse_window": (42, 45),
            "name": "bright_lr_smallball",
        },
    ]

    for ex in extras:
        cfg = {
            "scene_id": f"S{idx:02d}_{ex['name']}",
            "scene_set": "confirmatory",
            "trajectory": ex["trajectory"],
            "bg_luminance": ex["bg_luminance"],
            "ball_pos_start": ex["ball_pos_start"],
            "ball_pos_end": ex["ball_pos_end"],
            "ball_radius": ex["ball_radius"],
            "has_obstacle": ex["has_obstacle"],
            "obstacle_rect": ex["obstacle_rect"],
            "pulse_window": ex["pulse_window"],
            "pulse_intensity": 115.0 if ex["bg_luminance"] > 100 else 120.0,
        }
        confirmatory_configs.append(cfg)
        idx += 1

    return {
        "pilot": pilot_configs,
        "confirmatory": confirmatory_configs,
    }


if __name__ == "__main__":
    specs = build_scene_specifications()
    print(f"Generated {len(specs['pilot'])} pilot configurations and {len(specs['confirmatory'])} confirmatory configurations.")
    assert len(specs["pilot"]) == 8, f"Expected 8 pilot scenes, got {len(specs['pilot'])}"
    assert len(specs["confirmatory"]) == 24, f"Expected 24 confirmatory scenes, got {len(specs['confirmatory'])}"
    print("All scene configurations validated successfully!")
