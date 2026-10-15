"""EXP-028: Differential Pulse Survival & Signal Propagation Audit (C3 vs. C5).

Standalone empirical audit pipeline measuring signal survival across 5 processing stages:
Stage 0: 1080p Ground Truth (Raw Video Frames)
Stage 1: 64x64 Spatial Resampling (Box / Area Downsampling)
Stage 2: Temporal Grid / Contact Sheets (GRID128 and GRID512)
Stage 3: Visual Carrier Encoding (E3-K12 Gram Projection & 2D Walsh Multiplexing)
Stage 4: Codec Quantization & Compression (Lossless PNG vs. Lossy WebP Q80)

Generates:
- metrics.json with all numerical measurements (ROI_MAE, ROI_MAX_DELTA, C3_C5_PIXEL_EQUAL, Contrast, SNR)
- difference heatmaps and visualizations for all stages
- markdown summary table for peer-review
"""

import os
import io
import json
from typing import Dict, Any, Tuple, List
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Import reference codec
try:
    from reference_carrier_codec import (
        encode_carrier_E3_hybrid_scaling,
        compute_gram_polynomials_N_K,
        rgb_to_ycbcr,
        ycbcr_to_rgb,
    )
except ImportError:
    from scripts.reference_carrier_codec import (
        encode_carrier_E3_hybrid_scaling,
        compute_gram_polynomials_N_K,
        rgb_to_ycbcr,
        ycbcr_to_rgb,
    )


def compute_metrics(
    arr_c3: np.ndarray,
    arr_c5: np.ndarray,
    roi_mask: np.ndarray,
) -> Dict[str, float]:
    """Calculate standard differential metrics between C3 and C5 arrays."""
    diff = np.abs(arr_c5.astype(np.float64) - arr_c3.astype(np.float64))
    if diff.ndim == 3:
        diff_max_ch = diff.max(axis=-1)
        diff_mean_ch = diff.mean(axis=-1)
    else:
        diff_max_ch = diff
        diff_mean_ch = diff

    full_mae = float(diff.mean())
    full_max = float(diff.max())
    
    # Pixel equality
    full_equal_pct = float((diff_max_ch == 0).sum() / diff_max_ch.size * 100.0)

    # ROI metrics
    if roi_mask is not None and roi_mask.sum() > 0:
        roi_diff = diff[roi_mask]
        roi_diff_max_ch = diff_max_ch[roi_mask]
        roi_mae = float(roi_diff.mean())
        roi_max = float(roi_diff.max())
        roi_equal_pct = float((roi_diff_max_ch == 0).sum() / roi_mask.sum() * 100.0)
    else:
        roi_mae = 0.0
        roi_max = 0.0
        roi_equal_pct = 100.0

    return {
        "full_mae": round(full_mae, 4),
        "full_max_delta": round(full_max, 2),
        "full_pixel_equal_pct": round(full_equal_pct, 2),
        "roi_mae": round(roi_mae, 4),
        "roi_max_delta": round(roi_max, 2),
        "roi_pixel_equal_pct": round(roi_equal_pct, 2),
    }


def compute_contrast(
    arr_c3: np.ndarray,
    arr_c5: np.ndarray,
    roi_mask: np.ndarray,
    bg_mask: np.ndarray,
) -> Dict[str, float]:
    """Compute local Weber and Michelson contrast in C3 and C5."""
    y3, _, _ = rgb_to_ycbcr(arr_c3)
    y5, _, _ = rgb_to_ycbcr(arr_c5)

    y3_ball = float(y3[roi_mask].mean()) if roi_mask.sum() > 0 else 0.0
    y5_ball = float(y5[roi_mask].mean()) if roi_mask.sum() > 0 else 0.0
    y3_bg = float(y3[bg_mask].mean()) if bg_mask.sum() > 0 else 1.0
    y5_bg = float(y5[bg_mask].mean()) if bg_mask.sum() > 0 else 1.0

    eps = 1e-6
    # Weber contrast: (I_obj - I_bg) / I_bg
    weber_c3 = (y3_ball - y3_bg) / max(y3_bg, eps)
    weber_c5 = (y5_ball - y5_bg) / max(y5_bg, eps)

    # Michelson contrast: (I_obj - I_bg) / (I_obj + I_bg)
    michelson_c3 = abs(y3_ball - y3_bg) / max(y3_ball + y3_bg, eps)
    michelson_c5 = abs(y5_ball - y5_bg) / max(y5_ball + y5_bg, eps)

    return {
        "y_ball_c3": round(y3_ball, 2),
        "y_ball_c5": round(y5_ball, 2),
        "y_bg_c3": round(y3_bg, 2),
        "y_bg_c5": round(y5_bg, 2),
        "delta_y_ball": round(y5_ball - y3_ball, 2),
        "weber_contrast_c3": round(weber_c3, 3),
        "weber_contrast_c5": round(weber_c5, 3),
        "delta_weber_contrast": round(weber_c5 - weber_c3, 3),
        "michelson_contrast_c3": round(michelson_c3, 3),
        "michelson_contrast_c5": round(michelson_c5, 3),
        "delta_michelson_contrast": round(michelson_c5 - michelson_c3, 3),
    }


def save_diff_heatmap(diff_map: np.ndarray, out_path: str, title: str, vmin: float = 0.0, vmax: float = None):
    """Save normalized difference map as a false-color heatmap image."""
    plt.figure(figsize=(6, 5))
    if diff_map.ndim == 3:
        d = diff_map.max(axis=-1)
    else:
        d = diff_map
    if vmax is None:
        vmax = max(1.0, float(d.max()))
    im = plt.imshow(d, cmap="magma", vmin=vmin, vmax=vmax)
    plt.colorbar(im, fraction=0.046, pad=0.04, label="Delta |C5 - C3|")
    plt.title(title, fontsize=10)
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def run_exp028_audit(
    delivery_dir: str,
    output_dir: str,
) -> Dict[str, Any]:
    """Execute complete 5-stage differential signal survival audit."""
    os.makedirs(output_dir, exist_ok=True)
    diff_dir = os.path.join(output_dir, "diff_maps")
    os.makedirs(diff_dir, exist_ok=True)

    print("=" * 75)
    print("EXP-028: DIFFERENTIAL PULSE SURVIVAL & SIGNAL PROPAGATION AUDIT")
    print(f"Source Data: {delivery_dir}")
    print(f"Output Dir:  {output_dir}")
    print("=" * 75)

    c3_frames_dir = os.path.join(delivery_dir, "frames_64", "C3")
    c5_frames_dir = os.path.join(delivery_dir, "frames_64", "C5")
    kontakt_dir = os.path.join(delivery_dir, "kontaktboegen")

    results = {
        "experiment_id": "EXP-028",
        "description": "Differential Signal Survival Audit (C3 baseline vs. C5 pulsed twin)",
        "stages": {},
        "gram_modes": {},
        "temporal_frames": {},
        "summary_table": [],
    }

    # =========================================================================
    # STAGE 0: 1080p Ground Truth
    # =========================================================================
    print("\n--- [STAGE 0] 1080p Ground Truth Frame Audit ---")
    # Load Frame 44 at 1080p
    im3_1080_f44 = Image.open(os.path.join(c3_frames_dir, "f44.png")).convert("RGB")
    im5_1080_f44 = Image.open(os.path.join(c5_frames_dir, "f44.png")).convert("RGB")
    arr3_1080_f44 = np.array(im3_1080_f44)
    arr5_1080_f44 = np.array(im5_1080_f44)

    # Define Ball ROI: [460:610, 630:800]
    roi_mask_1080 = np.zeros((1080, 1080), dtype=bool)
    roi_mask_1080[460:610, 630:800] = True
    bg_mask_1080 = np.zeros((1080, 1080), dtype=bool)
    bg_mask_1080[100:300, 100:300] = True

    m_stage0 = compute_metrics(arr3_1080_f44, arr5_1080_f44, roi_mask_1080)
    c_stage0 = compute_contrast(arr3_1080_f44, arr5_1080_f44, roi_mask_1080, bg_mask_1080)
    
    results["stages"]["stage0_1080p"] = {
        **m_stage0,
        **c_stage0,
        "resolution": [1080, 1080],
        "frame_index": 44,
        "timestamp_seconds": 2.75,
    }
    print(f"Stage 0 (1080p F44): ROI_MAX_DELTA={m_stage0['roi_max_delta']}, ROI_MAE={m_stage0['roi_mae']:.4f}, Delta Weber={c_stage0['delta_weber_contrast']:.2f}")

    diff_1080 = np.abs(arr5_1080_f44.astype(float) - arr3_1080_f44.astype(float))
    save_diff_heatmap(diff_1080, os.path.join(diff_dir, "diff_stage0_1080p_f44.png"), "Stage 0: 1080p Frame 44 Delta |C5 - C3|")

    # Audit the 4 pulse frames (43, 44, 45, 46) at 1080p
    pulse_frames_info = {}
    for f_idx in [43, 44, 45, 46]:
        f3 = np.array(Image.open(os.path.join(c3_frames_dir, f"f{f_idx:02d}.png")).convert("RGB"))
        f5 = np.array(Image.open(os.path.join(c5_frames_dir, f"f{f_idx:02d}.png")).convert("RGB"))
        t_sec = f_idx / 16.0
        # Theoretical sinusoidal pulse envelope
        env = np.sin(np.pi * (t_sec - 2.65) / 0.25)
        # Shift ROI slightly with ball motion (ball moves ~13 px per frame at 1080p)
        x_start = 630 + (f_idx - 44) * 13
        x_end = 800 + (f_idx - 44) * 13
        rm = np.zeros((1080, 1080), dtype=bool)
        rm[460:610, max(0, x_start):min(1080, x_end)] = True
        fm = compute_metrics(f3, f5, rm)
        fc = compute_contrast(f3, f5, rm, bg_mask_1080)
        pulse_frames_info[f"frame_{f_idx}"] = {
            "frame": f_idx,
            "timestamp_seconds": t_sec,
            "theoretical_envelope": round(float(env), 4),
            **fm,
            **fc,
        }
        print(f"  Frame {f_idx:02d} (t={t_sec:.3f}s, env={env:.3f}): ROI_MAX={fm['roi_max_delta']}, ROI_MAE={fm['roi_mae']:.4f}")
    results["temporal_frames"] = pulse_frames_info

    # =========================================================================
    # STAGE 1: 64x64 Spatial Resampling
    # =========================================================================
    print("\n--- [STAGE 1] 64x64 Spatial Resampling Audit ---")
    im3_64_f44 = im3_1080_f44.resize((64, 64), Image.Resampling.BOX)
    im5_64_f44 = im5_1080_f44.resize((64, 64), Image.Resampling.BOX)
    arr3_64_f44 = np.array(im3_64_f44)
    arr5_64_f44 = np.array(im5_64_f44)

    # Ball ROI at 64x64: [27:35, 38:47]
    roi_mask_64 = np.zeros((64, 64), dtype=bool)
    roi_mask_64[27:35, 38:47] = True
    bg_mask_64 = np.zeros((64, 64), dtype=bool)
    bg_mask_64[5:20, 5:20] = True

    m_stage1 = compute_metrics(arr3_64_f44, arr5_64_f44, roi_mask_64)
    c_stage1 = compute_contrast(arr3_64_f44, arr5_64_f44, roi_mask_64, bg_mask_64)
    
    # Also evaluate Lanczos for comparison
    im3_64_lan = im3_1080_f44.resize((64, 64), Image.Resampling.LANCZOS)
    im5_64_lan = im5_1080_f44.resize((64, 64), Image.Resampling.LANCZOS)
    m_stage1_lan = compute_metrics(np.array(im3_64_lan), np.array(im5_64_lan), roi_mask_64)

    results["stages"]["stage1_64x64"] = {
        **m_stage1,
        **c_stage1,
        "lanczos_comparison": m_stage1_lan,
        "resolution": [64, 64],
        "filter": "BOX (Area)",
    }
    print(f"Stage 1 (64x64 BOX): ROI_MAX_DELTA={m_stage1['roi_max_delta']}, ROI_MAE={m_stage1['roi_mae']:.4f}, Delta Weber={c_stage1['delta_weber_contrast']:.2f}")

    diff_64 = np.abs(arr5_64_f44.astype(float) - arr3_64_f44.astype(float))
    save_diff_heatmap(diff_64, os.path.join(diff_dir, "diff_stage1_64x64_f44.png"), "Stage 1: 64x64 (BOX) Frame 44 Delta |C5 - C3|")

    # =========================================================================
    # STAGE 2: Temporal Grid / Contact Sheets
    # =========================================================================
    print("\n--- [STAGE 2] Contact Sheets (GRID128 and GRID512) Audit ---")
    g128_3 = np.array(Image.open(os.path.join(kontakt_dir, "C3_GRID128.webp")))
    g128_5 = np.array(Image.open(os.path.join(kontakt_dir, "C5_GRID128.webp")))
    g512_3 = np.array(Image.open(os.path.join(kontakt_dir, "C3_GRID512.webp")))
    g512_5 = np.array(Image.open(os.path.join(kontakt_dir, "C5_GRID512.webp")))

    # Cell 11 is row 2, col 3:
    # In GRID128: cell size 32x32 -> row 2 [64:96], col 3 [96:128]
    # Ball inside cell 11: y[76:85], x[114:124]
    roi_mask_g128 = np.zeros((128, 128), dtype=bool)
    roi_mask_g128[76:85, 114:124] = True
    bg_mask_g128 = np.zeros((128, 128), dtype=bool)
    bg_mask_g128[66:74, 98:108] = True

    m_stage2_g128 = compute_metrics(g128_3, g128_5, roi_mask_g128)
    c_stage2_g128 = compute_contrast(g128_3, g128_5, roi_mask_g128, bg_mask_g128)

    # In GRID512: cell size 128x128 -> row 2 [256:384], col 3 [384:512]
    # Ball inside cell 11: y[308:345], x[455:495]
    roi_mask_g512 = np.zeros((512, 512), dtype=bool)
    roi_mask_g512[308:345, 455:495] = True
    bg_mask_g512 = np.zeros((512, 512), dtype=bool)
    bg_mask_g512[265:295, 395:430] = True

    m_stage2_g512 = compute_metrics(g512_3, g512_5, roi_mask_g512)
    c_stage2_g512 = compute_contrast(g512_3, g512_5, roi_mask_g512, bg_mask_g512)

    results["stages"]["stage2_grid128"] = {**m_stage2_g128, **c_stage2_g128, "format": "Contact_Sheet_128x128"}
    results["stages"]["stage2_grid512"] = {**m_stage2_g512, **c_stage2_g512, "format": "Contact_Sheet_512x512"}

    print(f"Stage 2 (GRID128 Cell 11): ROI_MAX_DELTA={m_stage2_g128['roi_max_delta']}, ROI_MAE={m_stage2_g128['roi_mae']:.4f}, Delta Weber={c_stage2_g128['delta_weber_contrast']:.2f}")
    print(f"Stage 2 (GRID512 Cell 11): ROI_MAX_DELTA={m_stage2_g512['roi_max_delta']}, ROI_MAE={m_stage2_g512['roi_mae']:.4f}, Delta Weber={c_stage2_g512['delta_weber_contrast']:.2f}")

    diff_g128 = np.abs(g128_5.astype(float) - g128_3.astype(float))
    diff_g512 = np.abs(g512_5.astype(float) - g512_3.astype(float))
    save_diff_heatmap(diff_g128, os.path.join(diff_dir, "diff_stage2_grid128.png"), "Stage 2: Contact Sheet 128x128 Delta |C5 - C3|")
    save_diff_heatmap(diff_g512, os.path.join(diff_dir, "diff_stage2_grid512.png"), "Stage 2: Contact Sheet 512x512 Delta |C5 - C3|")

    # =========================================================================
    # STAGE 3: Visual Carrier Encoding (E3-K12 Gram Projection)
    # =========================================================================
    print("\n--- [STAGE 3] Visual Carrier Encoding & Gram Mode Audit ---")
    # Load all 64 frames at 64x64
    all_64_c3 = [np.array(Image.open(os.path.join(c3_frames_dir, f"f{i:02d}.png")).convert("RGB").resize((64, 64), Image.Resampling.BOX)) for i in range(64)]
    all_64_c5 = [np.array(Image.open(os.path.join(c5_frames_dir, f"f{i:02d}.png")).convert("RGB").resize((64, 64), Image.Resampling.BOX)) for i in range(64)]
    arr_64_c3 = np.array(all_64_c3)
    arr_64_c5 = np.array(all_64_c5)

    # Gram projections
    P = compute_gram_polynomials_N_K(N=64, K=12)  # (12, 64)
    y3, _, _ = rgb_to_ycbcr(arr_64_c3)
    y5, _, _ = rgb_to_ycbcr(arr_64_c5)
    y3_c = y3 - 128.0
    y5_c = y5 - 128.0

    M3 = np.sum(y3_c * P[:, :, None, None], axis=1)  # (12, 64, 64)
    M5 = np.sum(y5_c * P[:, :, None, None], axis=1)  # (12, 64, 64)
    delta_M = M5 - M3

    # Mode energy spectrum and saturation analysis
    modes_report = {}
    print("  Gram Mode Spectrum & Saturation Diagnostics:")
    for k in range(12):
        d_k = delta_M[k]
        m3_k = M3[k]
        m5_k = M5[k]
        
        # Saturation check: does M_k / 35.0 exceed [-1.0, 1.0]?
        sat_c3_pct = float((np.abs(m3_k / 35.0) >= 1.0).sum() / 4096 * 100.0)
        sat_c5_pct = float((np.abs(m5_k / 35.0) >= 1.0).sum() / 4096 * 100.0)

        # ROI around frame 44 position [27:35, 38:47]
        roi_dk = d_k[27:35, 38:47]
        modes_report[f"mode_{k:02d}"] = {
            "mode_index": k,
            "full_max_delta": round(float(np.abs(d_k).max()), 3),
            "full_mean_delta": round(float(np.abs(d_k).mean()), 4),
            "roi_max_delta": round(float(np.abs(roi_dk).max()), 3),
            "roi_mean_delta": round(float(np.abs(roi_dk).mean()), 4),
            "l2_energy": round(float(np.linalg.norm(d_k)), 3),
            "saturation_c3_pct": round(sat_c3_pct, 2),
            "saturation_c5_pct": round(sat_c5_pct, 2),
            "m3_range": [round(float(m3_k.min()), 2), round(float(m3_k.max()), 2)],
            "m5_range": [round(float(m5_k.min()), 2), round(float(m5_k.max()), 2)],
        }
        print(f"    Mode {k:02d}: FullMax={np.abs(d_k).max():5.2f}, ROIMax={np.abs(roi_dk).max():5.2f}, Energy={np.linalg.norm(d_k):6.2f}, Saturation={sat_c3_pct:5.1f}%")
    results["gram_modes"] = modes_report

    # Encode carrier uncompressed
    carrier_raw_c3 = encode_carrier_E3_hybrid_scaling(arr_64_c3, K=12)
    carrier_raw_c5 = encode_carrier_E3_hybrid_scaling(arr_64_c5, K=12)

    # Carrier ROI: Quadrant T ball location [27:35, 64+38:64+47]
    roi_mask_carrier = np.zeros((128, 128), dtype=bool)
    roi_mask_carrier[27:35, 64+38:64+47] = True
    bg_mask_carrier = np.zeros((128, 128), dtype=bool)
    bg_mask_carrier[5:20, 64+5:64+20] = True

    m_stage3_raw = compute_metrics(carrier_raw_c3, carrier_raw_c5, roi_mask_carrier)
    c_stage3_raw = compute_contrast(carrier_raw_c3, carrier_raw_c5, roi_mask_carrier, bg_mask_carrier)
    results["stages"]["stage3_carrier_raw"] = {**m_stage3_raw, **c_stage3_raw, "format": "E3_K12_Raw"}
    print(f"Stage 3 (Carrier Raw): ROI_MAX_DELTA={m_stage3_raw['roi_max_delta']}, ROI_MAE={m_stage3_raw['roi_mae']:.4f}")

    diff_carrier_raw = np.abs(carrier_raw_c5.astype(float) - carrier_raw_c3.astype(float))
    save_diff_heatmap(diff_carrier_raw, os.path.join(diff_dir, "diff_stage3_carrier_raw.png"), "Stage 3: Carrier Raw Delta |C5 - C3|")

    # Lossless PNG Carrier
    buf3_png = io.BytesIO()
    buf5_png = io.BytesIO()
    Image.fromarray(carrier_raw_c3).save(buf3_png, format="PNG")
    Image.fromarray(carrier_raw_c5).save(buf5_png, format="PNG")
    buf3_png.seek(0); buf5_png.seek(0)
    carrier_png_c3 = np.array(Image.open(buf3_png))
    carrier_png_c5 = np.array(Image.open(buf5_png))

    m_stage3_png = compute_metrics(carrier_png_c3, carrier_png_c5, roi_mask_carrier)
    c_stage3_png = compute_contrast(carrier_png_c3, carrier_png_c5, roi_mask_carrier, bg_mask_carrier)
    results["stages"]["stage3_carrier_png"] = {**m_stage3_png, **c_stage3_png, "format": "E3_K12_Lossless_PNG"}
    save_diff_heatmap(np.abs(carrier_png_c5.astype(float) - carrier_png_c3.astype(float)), os.path.join(diff_dir, "diff_stage3_carrier_png.png"), "Stage 3: Carrier Lossless PNG Delta |C5 - C3|")

    # =========================================================================
    # STAGE 4: Codec Quantization & Compression (Lossy WebP Q80)
    # =========================================================================
    print("\n--- [STAGE 4] Lossy WebP (Q=80) Quantization Audit ---")
    buf3_webp = io.BytesIO()
    buf5_webp = io.BytesIO()
    Image.fromarray(carrier_raw_c3).save(buf3_webp, format="WEBP", quality=80)
    Image.fromarray(carrier_raw_c5).save(buf5_webp, format="WEBP", quality=80)
    buf3_webp.seek(0); buf5_webp.seek(0)
    carrier_webp_c3 = np.array(Image.open(buf3_webp))
    carrier_webp_c5 = np.array(Image.open(buf5_webp))

    m_stage4_webp = compute_metrics(carrier_webp_c3, carrier_webp_c5, roi_mask_carrier)
    c_stage4_webp = compute_contrast(carrier_webp_c3, carrier_webp_c5, roi_mask_carrier, bg_mask_carrier)

    # Per-Quadrant Breakdown in WebP
    quads = {
        "G_Base": (slice(0, 64), slice(0, 64)),
        "T_Temporal": (slice(0, 64), slice(64, 128)),
        "C_Chroma": (slice(64, 128), slice(0, 64)),
        "R_Neutral": (slice(64, 128), slice(64, 128)),
    }
    quad_report = {}
    diff_carrier_webp = np.abs(carrier_webp_c5.astype(float) - carrier_webp_c3.astype(float))
    for q_name, (ys, xs) in quads.items():
        qd = diff_carrier_webp[ys, xs]
        quad_report[q_name] = {
            "max_delta": round(float(qd.max()), 2),
            "mean_delta": round(float(qd.mean()), 4),
            "nonzero_pixel_pct": round(float((qd.max(axis=-1) > 0).sum() / 4096 * 100.0), 2),
        }
        print(f"  Quadrant {q_name:12s}: MaxDelta={qd.max():4.1f}, MeanDelta={qd.mean():6.4f}, NonzeroPixels={quad_report[q_name]['nonzero_pixel_pct']:5.1f}%")

    results["stages"]["stage4_carrier_webp"] = {
        **m_stage4_webp,
        **c_stage4_webp,
        "quadrant_breakdown": quad_report,
        "format": "E3_K12_Lossy_WebP_Q80",
    }
    print(f"Stage 4 (Carrier WebP Q80): ROI_MAX_DELTA={m_stage4_webp['roi_max_delta']}, ROI_MAE={m_stage4_webp['roi_mae']:.4f}")
    save_diff_heatmap(diff_carrier_webp, os.path.join(diff_dir, "diff_stage4_carrier_webp.png"), "Stage 4: Carrier Lossy WebP (Q80) Delta |C5 - C3|")

    # =========================================================================
    # SUMMARY TABLE & BENCHMARK COMPARISON
    # =========================================================================
    summary_rows = [
        {
            "stage": "Stage 0: 1080p Ground Truth (F44)",
            "format": "Uncompressed 1080p RGB",
            "roi_mae": m_stage0["roi_mae"],
            "roi_max_delta": m_stage0["roi_max_delta"],
            "pixel_equal_pct": m_stage0["roi_pixel_equal_pct"],
            "delta_weber": c_stage0["delta_weber_contrast"],
            "delta_michelson": c_stage0["delta_michelson_contrast"],
        },
        {
            "stage": "Stage 1: 64x64 Resampled (F44)",
            "format": "BOX (Area) Downsampling",
            "roi_mae": m_stage1["roi_mae"],
            "roi_max_delta": m_stage1["roi_max_delta"],
            "pixel_equal_pct": m_stage1["roi_pixel_equal_pct"],
            "delta_weber": c_stage1["delta_weber_contrast"],
            "delta_michelson": c_stage1["delta_michelson_contrast"],
        },
        {
            "stage": "Stage 2: GRID512 Contact Sheet",
            "format": "4x4 Grid 512x512 WebP (Cell 11)",
            "roi_mae": m_stage2_g512["roi_mae"],
            "roi_max_delta": m_stage2_g512["roi_max_delta"],
            "pixel_equal_pct": m_stage2_g512["roi_pixel_equal_pct"],
            "delta_weber": c_stage2_g512["delta_weber_contrast"],
            "delta_michelson": c_stage2_g512["delta_michelson_contrast"],
        },
        {
            "stage": "Stage 2: GRID128 Contact Sheet",
            "format": "4x4 Grid 128x128 WebP (Cell 11)",
            "roi_mae": m_stage2_g128["roi_mae"],
            "roi_max_delta": m_stage2_g128["roi_max_delta"],
            "pixel_equal_pct": m_stage2_g128["roi_pixel_equal_pct"],
            "delta_weber": c_stage2_g128["delta_weber_contrast"],
            "delta_michelson": c_stage2_g128["delta_michelson_contrast"],
        },
        {
            "stage": "Stage 3: E3-K12 Visual Carrier",
            "format": "128x128 Lossless PNG",
            "roi_mae": m_stage3_png["roi_mae"],
            "roi_max_delta": m_stage3_png["roi_max_delta"],
            "pixel_equal_pct": m_stage3_png["roi_pixel_equal_pct"],
            "delta_weber": c_stage3_png["delta_weber_contrast"],
            "delta_michelson": c_stage3_png["delta_michelson_contrast"],
        },
        {
            "stage": "Stage 4: E3-K12 Visual Carrier",
            "format": "128x128 Lossy WebP (Q=80)",
            "roi_mae": m_stage4_webp["roi_mae"],
            "roi_max_delta": m_stage4_webp["roi_max_delta"],
            "pixel_equal_pct": m_stage4_webp["roi_pixel_equal_pct"],
            "delta_weber": c_stage4_webp["delta_weber_contrast"],
            "delta_michelson": c_stage4_webp["delta_michelson_contrast"],
        },
    ]
    results["summary_table"] = summary_rows

    # Plot Gram energy spectrum
    plt.figure(figsize=(8, 4.5))
    modes = list(range(12))
    energies = [modes_report[f"mode_{k:02d}"]["l2_energy"] for k in modes]
    roi_maxs = [modes_report[f"mode_{k:02d}"]["roi_max_delta"] for k in modes]
    
    x = np.arange(12)
    width = 0.35
    plt.bar(x - width/2, energies, width, label="L2 Energy ||Delta M_k||", color="#4361ee")
    plt.bar(x + width/2, roi_maxs, width, label="ROI Max Delta", color="#f72585")
    plt.xlabel("Gram Polynomial Mode Index k", fontsize=10)
    plt.ylabel("Magnitude", fontsize=10)
    plt.title("EXP-028: Gram Mode Energy Distribution of 250ms Luminance Pulse", fontsize=11)
    plt.xticks(x, [f"k={k}" for k in modes])
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(diff_dir, "gram_modes_energy_spectrum.png"), dpi=200)
    plt.close()

    # Save metrics JSON
    metrics_json_path = os.path.join(output_dir, "pulse_survival_metrics.json")
    with open(metrics_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"\n[+] Saved complete metrics to: {metrics_json_path}")

    # Generate Markdown Summary Table
    md_table_path = os.path.join(output_dir, "summary_table.md")
    with open(md_table_path, "w", encoding="utf-8") as f:
        f.write("# EXP-028: Differential Signal Survival Summary Table\n\n")
        f.write("| Stufe / Format | Representation | ROI MAE | ROI Max Delta | C3-C5 Equal (%) | Delta Weber Contrast | Delta Michelson |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for r in summary_rows:
            f.write(f"| **{r['stage']}** | {r['format']} | {r['roi_mae']:.4f} | {r['roi_max_delta']:.1f} | {r['pixel_equal_pct']:.1f}% | {r['delta_weber']:+.2f} | {r['delta_michelson']:+.3f} |\n")
        f.write("\n### Gram Mode Energy Distribution (C5 - C3)\n\n")
        f.write("| Mode k | Basis Function | ROI Max Delta | Full Max Delta | L2 Energy | Saturation (C3) |\n")
        f.write("|---|---|---|---|---|---|\n")
        mode_names = [
            "P0 (Mean DC offset)",
            "P1 (Linear drift)",
            "P2 (Curvature / Bimodal)",
            "Walsh Subcarrier 1 (k=3)",
            "Walsh Subcarrier 2 (k=4)",
            "Walsh Subcarrier 3 (k=5)",
            "Walsh Subcarrier 4 (k=6)",
            "Walsh Subcarrier 5 (k=7)",
            "Walsh Subcarrier 6 (k=8)",
            "Walsh Subcarrier 7 (k=9)",
            "Walsh Subcarrier 8 (k=10)",
            "Walsh Subcarrier 9 (k=11)",
        ]
        for k in range(12):
            mr = modes_report[f"mode_{k:02d}"]
            f.write(f"| k={k:02d} | {mode_names[k]} | {mr['roi_max_delta']:5.2f} | {mr['full_max_delta']:5.2f} | {mr['l2_energy']:6.2f} | {mr['saturation_c3_pct']:.1f}% |\n")
    print(f"[+] Saved markdown summary table to: {md_table_path}")

    return results


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="EXP-028 Differential Pulse Survival Audit")
    parser.add_argument(
        "--delivery",
        default=os.environ.get("EXP027_DELIVERY_DIR", os.path.join("data", "delivery", "EXP-027")),
        help="Path to EXP-027 delivery directory containing frames_64 and kontaktboegen",
    )
    parser.add_argument(
        "--out",
        default=os.path.join("experiments", "2026", "EXP-028"),
        help="Path to output directory for EXP-028 audit artifacts",
    )
    args = parser.parse_args()
    
    # If default relative path does not exist, check fallback env or standard delivery location
    if not os.path.exists(args.delivery):
        fallback = os.path.join("..", "clip_generator", "projects", "swiftclip_exp027", "lieferung", "EXP-027")
        if os.path.exists(fallback):
            args.delivery = fallback
            
    run_exp028_audit(args.delivery, args.out)
