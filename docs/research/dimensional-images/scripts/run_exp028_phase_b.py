"""EXP-028 Phase B: Adaptive Y0 Centering Counter-Experiment (E4-Y0 vs. E3-K12).

Tests the 4 pre-registered conditions across C3 (baseline) and C5 (pulsed twin):
- Condition A (E3_WebP):     E3-K12 (center 128, D=35), Lossy WebP Q80 (Reference)
- Condition B (E3_Lossless): E3-K12 (center 128, D=35), Lossless PNG (Compression Control)
- Condition C (E4_WebP):     E4-Y0 (center Y0,  D=35), Lossy WebP Q80 (Experimental)
- Condition D (E4_Lossless): E4-Y0 (center Y0,  D=35), Lossless PNG (Ablation Control)

Plus:
- Rigorous Signal-to-Noise / Differential Distortion Ratio on identical pixel sets.
- Verification of P1..P11 numerical invariance across centering schemes.
- Full decoder reconstructibility and Frame 44 pulse recovery audit.
- Multi-clip safety control across C1, C2, C3, C4, C5 (including C4 direction reversal).
"""

import os
import io
import json
from typing import Dict, Any, Tuple, List
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from scripts.reference_carrier_codec import (
    encode_carrier_E3_hybrid_scaling,
    encode_carrier_E4_Y0_hybrid_scaling,
    decode_carrier_E3_hybrid_scaling,
    decode_carrier_E4_Y0_hybrid_scaling,
    reconstruct_video_y_from_carrier,
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
    else:
        diff_max_ch = diff

    full_mae = float(diff.mean())
    full_max = float(diff.max())
    full_equal_pct = float((diff_max_ch == 0).sum() / diff_max_ch.size * 100.0)

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


def compute_rigorous_diff_snr(
    carrier_clean_c3: np.ndarray,
    carrier_clean_c5: np.ndarray,
    carrier_webp_c3: np.ndarray,
    carrier_webp_c5: np.ndarray,
    roi_mask: np.ndarray,
) -> Dict[str, float]:
    """Compute mathematically rigorous differential Signal-to-Noise Ratio on identical pixel sets.
    
    Signal: S = Carrier_clean(C5) - Carrier_clean(C3)
    WebP Signal: S_webp = Carrier_webp(C5) - Carrier_webp(C3)
    Compression Error / Noise: E = S_webp - S
    """
    S = carrier_clean_c5.astype(np.float64) - carrier_clean_c3.astype(np.float64)
    S_webp = carrier_webp_c5.astype(np.float64) - carrier_webp_c3.astype(np.float64)
    E = S_webp - S

    # Calculate over ROI
    S_roi = S[roi_mask]
    E_roi = E[roi_mask]

    sig_power = float(np.mean(S_roi ** 2))
    err_power = float(np.mean(E_roi ** 2))

    if err_power < 1e-12:
        snr_db = 999.0
        psnr_db = 999.0
    else:
        snr_db = float(10.0 * np.log10(max(sig_power, 1e-12) / err_power))
        psnr_db = float(10.0 * np.log10((255.0 ** 2) / err_power))

    # Full carrier metrics
    full_sig_power = float(np.mean(S ** 2))
    full_err_power = float(np.mean(E ** 2))
    full_snr_db = float(10.0 * np.log10(max(full_sig_power, 1e-12) / max(full_err_power, 1e-12))) if full_err_power > 0 else 999.0

    return {
        "roi_signal_power": round(sig_power, 4),
        "roi_error_power": round(err_power, 4),
        "roi_differential_snr_db": round(snr_db, 2),
        "roi_differential_psnr_db": round(psnr_db, 2),
        "full_differential_snr_db": round(full_snr_db, 2),
    }


def save_heatmap(data: np.ndarray, path: str, title: str, vmin: float = 0.0, vmax: float = None):
    """Save 2D array as a magma heatmap."""
    plt.figure(figsize=(6, 5))
    if data.ndim == 3:
        d = data.max(axis=-1)
    else:
        d = data
    if vmax is None:
        vmax = max(1.0, float(d.max()))
    im = plt.imshow(d, cmap="magma", vmin=vmin, vmax=vmax)
    plt.colorbar(im, fraction=0.046, pad=0.04, label="Delta")
    plt.title(title, fontsize=10)
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def run_phase_b_experiment(
    delivery_dir: str,
    output_dir: str,
) -> Dict[str, Any]:
    """Execute complete Phase B empirical evaluation."""
    os.makedirs(output_dir, exist_ok=True)
    plots_dir = os.path.join(output_dir, "phase_b_plots")
    os.makedirs(plots_dir, exist_ok=True)

    print("=" * 80)
    print("EXP-028 PHASE B: ADAPTIVE Y0 CENTERING AUDIT (E4-Y0 vs. E3-K12)")
    print(f"Source: {delivery_dir}")
    print(f"Output: {output_dir}")
    print("=" * 80)

    # 1. Load C3 and C5 64x64 frames
    c3_dir = os.path.join(delivery_dir, "frames_64", "C3")
    c5_dir = os.path.join(delivery_dir, "frames_64", "C5")

    frames_c3 = np.array([np.array(Image.open(os.path.join(c3_dir, f"f{i:02d}.png")).convert("RGB").resize((64, 64), Image.Resampling.BOX)) for i in range(64)])
    frames_c5 = np.array([np.array(Image.open(os.path.join(c5_dir, f"f{i:02d}.png")).convert("RGB").resize((64, 64), Image.Resampling.BOX)) for i in range(64)])

    y3, _, _ = rgb_to_ycbcr(frames_c3)
    y5, _, _ = rgb_to_ycbcr(frames_c5)

    P = compute_gram_polynomials_N_K(N=64, K=12)

    # Carrier ROI: Quadrant T ball location [27:35, 64+38:64+47]
    roi_mask_carrier = np.zeros((128, 128), dtype=bool)
    roi_mask_carrier[27:35, 64+38:64+47] = True

    # 2. Mathematical Projections
    # E3: Centering 128
    M3_e3 = np.sum((y3 - 128.0) * P[:, :, None, None], axis=1)
    M5_e3 = np.sum((y5 - 128.0) * P[:, :, None, None], axis=1)

    # E4: Centering Y0
    M3_e4 = np.sum((y3 - y3[0:1]) * P[:, :, None, None], axis=1)
    M5_e4 = np.sum((y5 - y5[0:1]) * P[:, :, None, None], axis=1)

    # Verify P1..P11 Invariance
    inv_c3 = float(np.max(np.abs(M3_e4[1:] - M3_e3[1:])))
    inv_c5 = float(np.max(np.abs(M5_e4[1:] - M5_e3[1:])))
    print(f"\n[+] P1..P11 Invariance Check: C3 max diff = {inv_c3:.2e}, C5 max diff = {inv_c5:.2e}")
    assert inv_c3 < 1e-10 and inv_c5 < 1e-10, "Mathematical invariance violated!"

    # 3. Encode Raw Carriers
    raw_e3_c3 = encode_carrier_E3_hybrid_scaling(frames_c3, K=12)
    raw_e3_c5 = encode_carrier_E3_hybrid_scaling(frames_c5, K=12)

    raw_e4_c3 = encode_carrier_E4_Y0_hybrid_scaling(frames_c3, K=12)
    raw_e4_c5 = encode_carrier_E4_Y0_hybrid_scaling(frames_c5, K=12)

    # 4. Generate Condition Formats (PNG & WebP Q80)
    def compress(arr: np.ndarray, fmt: str, quality: int = 80) -> Tuple[np.ndarray, int]:
        buf = io.BytesIO()
        im = Image.fromarray(arr)
        if fmt == "PNG":
            im.save(buf, format="PNG")
        elif fmt == "WEBP":
            im.save(buf, format="WEBP", quality=quality)
        size = buf.tell()
        buf.seek(0)
        return np.array(Image.open(buf)), size

    # Condition A: E3 WebP Q80
    c_a_c3, sz_a_c3 = compress(raw_e3_c3, "WEBP", quality=80)
    c_a_c5, sz_a_c5 = compress(raw_e3_c5, "WEBP", quality=80)

    # Condition B: E3 Lossless PNG
    c_b_c3, sz_b_c3 = compress(raw_e3_c3, "PNG")
    c_b_c5, sz_b_c5 = compress(raw_e3_c5, "PNG")

    # Condition C: E4-Y0 WebP Q80
    c_c_c3, sz_c_c3 = compress(raw_e4_c3, "WEBP", quality=80)
    c_c_c5, sz_c_c5 = compress(raw_e4_c5, "WEBP", quality=80)

    # Condition D: E4-Y0 Lossless PNG
    c_d_c3, sz_d_c3 = compress(raw_e4_c3, "PNG")
    c_d_c5, sz_d_c5 = compress(raw_e4_c5, "PNG")

    conditions = {
        "Condition_A_E3_WebP": {"c3": c_a_c3, "c5": c_a_c5, "sz_c3": sz_a_c3, "sz_c5": sz_a_c5, "codec": "E3-K12", "fmt": "WebP Q80"},
        "Condition_B_E3_Lossless": {"c3": c_b_c3, "c5": c_b_c5, "sz_c3": sz_b_c3, "sz_c5": sz_b_c5, "codec": "E3-K12", "fmt": "Lossless PNG"},
        "Condition_C_E4_WebP": {"c3": c_c_c3, "c5": c_c_c5, "sz_c3": sz_c_c3, "sz_c5": sz_c_c5, "codec": "E4-Y0", "fmt": "WebP Q80"},
        "Condition_D_E4_Lossless": {"c3": c_d_c3, "c5": c_d_c5, "sz_c3": sz_d_c3, "sz_c5": sz_d_c5, "codec": "E4-Y0", "fmt": "Lossless PNG"},
    }

    cond_results = {}
    print("\n--- 4 Conditions Differential Evaluation ---")
    quads = {
        "G_Base": (slice(0, 64), slice(0, 64)),
        "T_Temporal": (slice(0, 64), slice(64, 128)),
        "C_Chroma": (slice(64, 128), slice(0, 64)),
        "R_Neutral": (slice(64, 128), slice(64, 128)),
    }

    for name, cinfo in conditions.items():
        m = compute_metrics(cinfo["c3"], cinfo["c5"], roi_mask_carrier)
        diff = np.abs(cinfo["c5"].astype(float) - cinfo["c3"].astype(float))

        # Quadrant breakdown
        q_breakdown = {}
        for q_name, (ys, xs) in quads.items():
            qd = diff[ys, xs]
            q_breakdown[q_name] = {
                "max_delta": round(float(qd.max()), 2),
                "mean_delta": round(float(qd.mean()), 4),
                "nonzero_pct": round(float((qd.max(axis=-1) > 0).sum() / 4096 * 100.0), 2),
            }

        # Quadrant T Red channel (P0) pulse delta
        t_r_c3 = cinfo["c3"][:64, 64:, 0]
        t_r_c5 = cinfo["c5"][:64, 64:, 0]
        delta_t_r = np.abs(t_r_c5.astype(float) - t_r_c3.astype(float))
        roi_t_r = delta_t_r[27:35, 38:47]

        cond_results[name] = {
            "codec": cinfo["codec"],
            "format": cinfo["fmt"],
            "bytes_c3": cinfo["sz_c3"],
            "bytes_c5": cinfo["sz_c5"],
            "roi_metrics": m,
            "quadrant_breakdown": q_breakdown,
            "quadrant_T_red_max_delta": round(float(roi_t_r.max()), 2),
            "quadrant_T_red_mean_delta": round(float(roi_t_r.mean()), 4),
        }
        print(f"[{name:24s}] ROI MaxDelta={m['roi_max_delta']:4.1f}, ROI MAE={m['roi_mae']:6.4f}, Quad T Red MaxDelta={roi_t_r.max():4.1f}, Size={cinfo['sz_c5']} B")
        save_heatmap(diff, os.path.join(plots_dir, f"diff_{name}.png"), f"Phase B: {name} Delta |C5 - C3|")

    # 5. Rigorous Signal-to-Noise / Differential Distortion Ratios
    print("\n--- Rigorous Differential SNR / Error Evaluation ---")
    snr_e3 = compute_rigorous_diff_snr(c_b_c3, c_b_c5, c_a_c3, c_a_c5, roi_mask_carrier)
    snr_e4 = compute_rigorous_diff_snr(c_d_c3, c_d_c5, c_c_c3, c_c_c5, roi_mask_carrier)

    print(f"E3-K12: ROI Signal Power={snr_e3['roi_signal_power']:.2f}, Error Power={snr_e3['roi_error_power']:.2f}, Diff SNR={snr_e3['roi_differential_snr_db']:.2f} dB, Diff PSNR={snr_e3['roi_differential_psnr_db']:.2f} dB")
    print(f"E4-Y0:  ROI Signal Power={snr_e4['roi_signal_power']:.2f}, Error Power={snr_e4['roi_error_power']:.2f}, Diff SNR={snr_e4['roi_differential_snr_db']:.2f} dB, Diff PSNR={snr_e4['roi_differential_psnr_db']:.2f} dB")

    # 6. P0 Saturation Audit (Full and Ball ROI)
    sat_audit = {
        "E3_C3": {
            "full_sat_pct": round(float((np.abs(M3_e3[0] / 35.0) >= 1.0).mean() * 100.0), 2),
            "roi_sat_pct": round(float((np.abs(M3_e3[0][27:35, 38:47] / 35.0) >= 1.0).mean() * 100.0), 2),
            "m0_range": [round(float(M3_e3[0].min()), 1), round(float(M3_e3[0].max()), 1)],
        },
        "E3_C5": {
            "full_sat_pct": round(float((np.abs(M5_e3[0] / 35.0) >= 1.0).mean() * 100.0), 2),
            "roi_sat_pct": round(float((np.abs(M5_e3[0][27:35, 38:47] / 35.0) >= 1.0).mean() * 100.0), 2),
            "m0_range": [round(float(M5_e3[0].min()), 1), round(float(M5_e3[0].max()), 1)],
        },
        "E4_C3": {
            "full_sat_pct": round(float((np.abs(M3_e4[0] / 35.0) >= 1.0).mean() * 100.0), 2),
            "roi_sat_pct": round(float((np.abs(M3_e4[0][27:35, 38:47] / 35.0) >= 1.0).mean() * 100.0), 2),
            "m0_range": [round(float(M3_e4[0].min()), 1), round(float(M3_e4[0].max()), 1)],
        },
        "E4_C5": {
            "full_sat_pct": round(float((np.abs(M5_e4[0] / 35.0) >= 1.0).mean() * 100.0), 2),
            "roi_sat_pct": round(float((np.abs(M5_e4[0][27:35, 38:47] / 35.0) >= 1.0).mean() * 100.0), 2),
            "m0_range": [round(float(M5_e4[0].min()), 1), round(float(M5_e4[0].max()), 1)],
        },
    }
    print(f"\nP0 Saturation Summary: E3 Full={sat_audit['E3_C3']['full_sat_pct']}% -> E4 Full={sat_audit['E4_C3']['full_sat_pct']}%")

    # 7. Decoder Reconstructibility & Frame 44 Audit
    print("\n--- Decoder Reconstructibility Audit ---")
    recon_e3_c3 = reconstruct_video_y_from_carrier(c_b_c3, N=64, K=12, mode="E3")
    recon_e3_c5 = reconstruct_video_y_from_carrier(c_b_c5, N=64, K=12, mode="E3")

    recon_e4_c3 = reconstruct_video_y_from_carrier(c_d_c3, N=64, K=12, mode="E4")
    recon_e4_c5 = reconstruct_video_y_from_carrier(c_d_c5, N=64, K=12, mode="E4")

    # Compare reconstructed Frame 44
    gt_diff_f44 = np.abs(y5[44] - y3[44])
    recon_diff_f44_e3 = np.abs(recon_e3_c5[44] - recon_e3_c3[44])
    recon_diff_f44_e4 = np.abs(recon_e4_c5[44] - recon_e4_c3[44])

    roi_64 = np.zeros((64, 64), dtype=bool)
    roi_64[27:35, 38:47] = True

    recon_audit = {
        "ground_truth_f44": {
            "roi_max_delta": round(float(gt_diff_f44[roi_64].max()), 2),
            "roi_mae": round(float(gt_diff_f44[roi_64].mean()), 4),
        },
        "reconstructed_e3_f44": {
            "roi_max_delta": round(float(recon_diff_f44_e3[roi_64].max()), 2),
            "roi_mae": round(float(recon_diff_f44_e3[roi_64].mean()), 4),
            "error_vs_gt_mae": round(float(np.abs(recon_diff_f44_e3[roi_64] - gt_diff_f44[roi_64]).mean()), 4),
        },
        "reconstructed_e4_f44": {
            "roi_max_delta": round(float(recon_diff_f44_e4[roi_64].max()), 2),
            "roi_mae": round(float(recon_diff_f44_e4[roi_64].mean()), 4),
            "error_vs_gt_mae": round(float(np.abs(recon_diff_f44_e4[roi_64] - gt_diff_f44[roi_64]).mean()), 4),
        },
    }
    print(f"Frame 44 GT Diff:  ROI Max={recon_audit['ground_truth_f44']['roi_max_delta']}, ROI MAE={recon_audit['ground_truth_f44']['roi_mae']}")
    print(f"Recon E3 Diff:     ROI Max={recon_audit['reconstructed_e3_f44']['roi_max_delta']}, ROI MAE={recon_audit['reconstructed_e3_f44']['roi_mae']}")
    print(f"Recon E4 Diff:     ROI Max={recon_audit['reconstructed_e4_f44']['roi_max_delta']}, ROI MAE={recon_audit['reconstructed_e4_f44']['roi_mae']}")

    save_heatmap(recon_diff_f44_e3, os.path.join(plots_dir, "recon_f44_diff_e3.png"), "Reconstructed Frame 44 Delta (E3-K12)")
    save_heatmap(recon_diff_f44_e4, os.path.join(plots_dir, "recon_f44_diff_e4.png"), "Reconstructed Frame 44 Delta (E4-Y0)")
    save_heatmap(gt_diff_f44, os.path.join(plots_dir, "ground_truth_f44_diff.png"), "Ground Truth Frame 44 Delta (64x64 BOX)")

    # 8. Multi-Clip Safety Control (C1..C5)
    print("\n--- Multi-Clip Safety Control (C1..C5) ---")
    multi_clip_audit = {}
    for clip in ["C1", "C2", "C3", "C4", "C5"]:
        clip_dir = os.path.join(delivery_dir, "frames_64", clip)
        clip_frames = np.array([np.array(Image.open(os.path.join(clip_dir, f"f{i:02d}.png")).convert("RGB").resize((64, 64), Image.Resampling.BOX)) for i in range(64)])
        y_clip, _, _ = rgb_to_ycbcr(clip_frames)

        m_e3 = np.sum((y_clip - 128.0) * P[:, :, None, None], axis=1)
        m_e4 = np.sum((y_clip - y_clip[0:1]) * P[:, :, None, None], axis=1)

        sat_e3 = float((np.abs(m_e3[0] / 35.0) >= 1.0).mean() * 100.0)
        sat_e4 = float((np.abs(m_e4[0] / 35.0) >= 1.0).mean() * 100.0)
        sat_e4_pos = float(((m_e4[0] / 35.0) >= 1.0).mean() * 100.0)
        sat_e4_neg = float(((m_e4[0] / 35.0) <= -1.0).mean() * 100.0)

        # C4 Kinematics Preservation check:
        # Reconstruct C4 luminance and compare to input
        raw_e4_clip = encode_carrier_E4_Y0_hybrid_scaling(clip_frames, K=12)
        recon_y_clip = reconstruct_video_y_from_carrier(raw_e4_clip, N=64, K=12, mode="E4")
        mae_recon = float(np.abs(recon_y_clip - y_clip).mean())

        multi_clip_audit[clip] = {
            "e3_saturation_pct": round(sat_e3, 2),
            "e4_saturation_pct": round(sat_e4, 2),
            "e4_saturation_pos_pct": round(sat_e4_pos, 2),
            "e4_saturation_neg_pct": round(sat_e4_neg, 2),
            "e4_m0_range": [round(float(m_e4[0].min()), 1), round(float(m_e4[0].max()), 1)],
            "e4_reconstruction_mae": round(mae_recon, 4),
        }
        print(f"  {clip}: E3 Sat={sat_e3:5.1f}% -> E4 Sat={sat_e4:5.1f}% (Pos={sat_e4_pos:4.1f}%, Neg={sat_e4_neg:4.1f}%), Recon MAE={mae_recon:.4f}")

    # Assemble complete Phase B payload
    final_report = {
        "experiment_id": "EXP-028_PHASE_B",
        "description": "Adaptive Y0 Centering Counter-Experiment (E4-Y0 vs. E3-K12)",
        "invariance_check": {
            "p1_to_p11_max_abs_diff_c3": inv_c3,
            "p1_to_p11_max_abs_diff_c5": inv_c5,
            "invariance_passed": bool(inv_c3 < 1e-10 and inv_c5 < 1e-10),
        },
        "conditions": cond_results,
        "differential_snr": {
            "E3_K12": snr_e3,
            "E4_Y0": snr_e4,
        },
        "saturation_audit": sat_audit,
        "decoder_reconstruction_f44": recon_audit,
        "multi_clip_safety_control": multi_clip_audit,
    }

    # Save JSON results
    json_path = os.path.join(output_dir, "phase_b_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(final_report, f, indent=2)
    print(f"\n[+] Saved Phase B JSON results to: {json_path}")

    # Generate Markdown Summary
    md_path = os.path.join(output_dir, "phase_b_summary.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# EXP-028 Phase B: Adaptive Y0 Centering Evaluation Summary\n\n")
        f.write("## 1. Matrix der 4 Versuchsbedingungen (C5 vs. C3)\n\n")
        f.write("| Bedingung | Codec | Zentrierung | Format | Dateigröße (C5) | ROI Max Delta | ROI MAE | Quad T Red Max Delta |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        for cname, cdata in cond_results.items():
            rm = cdata["roi_metrics"]
            f.write(f"| **{cname}** | {cdata['codec']} | {'Y0 (Adaptiv)' if 'E4' in cname else '128 (Statisch)'} | {cdata['format']} | {cdata['bytes_c5']} B | {rm['roi_max_delta']:.1f} | {rm['roi_mae']:.4f} | {cdata['quadrant_T_red_max_delta']:.1f} |\n")
        
        f.write("\n## 2. Rigorose Signal-to-Noise / Fehler-Analyse (auf identischer ROI)\n\n")
        f.write("| Codec | ROI Signal Power | ROI WebP Error Power | Differential SNR (dB) | Differential PSNR (dB) |\n")
        f.write("|---|---|---|---|---|\n")
        f.write(f"| **E3-K12 (Statisch 128)** | {snr_e3['roi_signal_power']:.2f} | {snr_e3['roi_error_power']:.2f} | **{snr_e3['roi_differential_snr_db']:.2f} dB** | {snr_e3['roi_differential_psnr_db']:.2f} dB |\n")
        f.write(f"| **E4-Y0 (Adaptiv Y0)** | {snr_e4['roi_signal_power']:.2f} | {snr_e4['roi_error_power']:.2f} | **{snr_e4['roi_differential_snr_db']:.2f} dB** | {snr_e4['roi_differential_psnr_db']:.2f} dB |\n")

        f.write("\n## 3. P0 Sättigungsabbau über alle 5 Clips (Sicherheitskontrolle)\n\n")
        f.write("| Clip | E3-K12 Sättigung | E4-Y0 Sättigung (Gesamt) | E4 Positiv-Sättigung | E4 Negativ-Sättigung | E4 M0 Bereich | E4 Rekonstruktions-MAE |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for clip, cdata in multi_clip_audit.items():
            f.write(f"| **{clip}** | {cdata['e3_saturation_pct']:.1f}% | **{cdata['e4_saturation_pct']:.1f}%** | {cdata['e4_saturation_pos_pct']:.1f}% | {cdata['e4_saturation_neg_pct']:.1f}% | [{cdata['e4_m0_range'][0]}, {cdata['e4_m0_range'][1]}] | {cdata['e4_reconstruction_mae']:.4f} |\n")

        f.write("\n## 4. Frame 44 Rekonstruktion & Puls-Wiederherstellung\n\n")
        f.write(f"- **Ground Truth (64x64 Box):** ROI Max Delta = {recon_audit['ground_truth_f44']['roi_max_delta']}, ROI MAE = {recon_audit['ground_truth_f44']['roi_mae']}\n")
        f.write(f"- **E3-K12 Rekonstruktion:** ROI Max Delta = {recon_audit['reconstructed_e3_f44']['roi_max_delta']}, ROI MAE = {recon_audit['reconstructed_e3_f44']['roi_mae']} (Fehler vs GT: {recon_audit['reconstructed_e3_f44']['error_vs_gt_mae']})\n")
        f.write(f"- **E4-Y0 Rekonstruktion:**  ROI Max Delta = {recon_audit['reconstructed_e4_f44']['roi_max_delta']}, ROI MAE = {recon_audit['reconstructed_e4_f44']['roi_mae']} (Fehler vs GT: {recon_audit['reconstructed_e4_f44']['error_vs_gt_mae']})\n")

    print(f"[+] Saved Phase B Markdown summary to: {md_path}")
    return final_report


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="EXP-028 Phase B Counter-Experiment")
    parser.add_argument(
        "--delivery",
        default=os.environ.get("EXP027_DELIVERY_DIR", os.path.join("..", "clip_generator", "projects", "swiftclip_exp027", "lieferung", "EXP-027")),
        help="Path to EXP-027 delivery directory",
    )
    parser.add_argument(
        "--out",
        default=os.path.join("experiments", "2026", "EXP-028", "phase_b"),
        help="Path to output directory for Phase B",
    )
    args = parser.parse_args()
    if not os.path.exists(args.delivery):
        fallback = os.path.join("data", "delivery", "EXP-027")
        if os.path.exists(fallback):
            args.delivery = fallback
    run_phase_b_experiment(args.delivery, args.out)
