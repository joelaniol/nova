"""VLT Codec Stress Lab - Systematic Numerical Audit of Carrier Channel Bounds.

Standalone audit suite for E3-K12 Carrier codec addressing 5 fundamental questions:
1. Time-Reversal Invariance & Directionality (Parity of Gram modes).
2. Iso-Luminance Chromatic Blindness (Cross-color ambiguity & missing chroma modes).
3. Single-Frame Delta Transients (Sub-Nyquist detection threshold across time positions & amplitudes).
4. Saturation Boundaries & Normalization Divisor D (Clamping vs quantization noise trade-off).
5. Spatial Locality & Walsh Demultiplexing Crosstalk (Object size vs 2D Walsh orthogonality & WebP chroma subsampling).
"""

import os
import io
import json
from typing import Dict, Any, List, Tuple
import numpy as np
from PIL import Image

try:
    from reference_carrier_codec import (
        compute_gram_polynomials_N_K,
        generate_2d_orthogonal_block_basis,
        rgb_to_ycbcr,
        ycbcr_to_rgb,
        encode_carrier_E3_hybrid_scaling,
        decode_carrier_E3_hybrid_scaling,
    )
except ImportError:
    from scripts.reference_carrier_codec import (
        compute_gram_polynomials_N_K,
        generate_2d_orthogonal_block_basis,
        rgb_to_ycbcr,
        ycbcr_to_rgb,
        encode_carrier_E3_hybrid_scaling,
        decode_carrier_E3_hybrid_scaling,
    )


def compress_to_webp(img_array: np.ndarray, quality: int = 80) -> np.ndarray:
    """Helper to simulate WebP lossy compression in-memory."""
    im = Image.fromarray(img_array)
    buf = io.BytesIO()
    im.save(buf, format="WEBP", quality=quality)
    buf.seek(0)
    return np.array(Image.open(buf))


def compress_to_png(img_array: np.ndarray) -> np.ndarray:
    """Helper to simulate lossless PNG roundtrip in-memory."""
    im = Image.fromarray(img_array)
    buf = io.BytesIO()
    im.save(buf, format="PNG")
    buf.seek(0)
    return np.array(Image.open(buf))


# ==============================================================================
# TEST 1: Time-Reversal Parity & Invariance
# ==============================================================================
def run_test1_time_reversal() -> Dict[str, Any]:
    """Test 1: Forward vs. Backward Motion Parity.
    
    Verifies that even modes (0, 2, 4, 6, 8, 10) are symmetric and odd modes
    (1, 3, 5, 7, 9, 11) are antisymmetric: c_k(rev) = (-1)^k c_k.
    Measures carrier distance and decode parity.
    """
    N, H, W = 64, 64, 64
    K = 12
    P = compute_gram_polynomials_N_K(N=N, K=K)
    
    # Synthetic video: A circle traversing left-to-right
    video_fwd = np.full((N, H, W, 3), 128, dtype=np.uint8)
    y_grid, x_grid = np.mgrid[:H, :W]
    for t in range(N):
        cx = int(16 + (32 * t) / (N - 1))
        cy = 32
        mask = ((x_grid - cx) ** 2 + (y_grid - cy) ** 2) <= 12 ** 2
        video_fwd[t, mask] = [220, 220, 220]
        
    # Reverse video
    video_rev = video_fwd[::-1].copy()
    
    # Compute ground truth projection coefficients for both
    y_fwd = np.array([rgb_to_ycbcr(f)[0] for f in video_fwd]) - 128.0
    y_rev = np.array([rgb_to_ycbcr(f)[0] for f in video_rev]) - 128.0
    
    # Spatial average inside circle track
    M_fwd = np.sum(y_fwd * P[:, :, np.newaxis, np.newaxis], axis=1) # (K, H, W)
    M_rev = np.sum(y_rev * P[:, :, np.newaxis, np.newaxis], axis=1)
    
    # Mean coefficient over active region
    active_mask = np.mean(y_fwd, axis=0) > 10.0
    m_fwd_mean = [float(np.mean(M_fwd[k][active_mask])) for k in range(K)]
    m_rev_mean = [float(np.mean(M_rev[k][active_mask])) for k in range(K)]
    
    parity_errors = []
    for k in range(K):
        expected_parity = (-1) ** k
        actual_ratio = m_rev_mean[k] / m_fwd_mean[k] if abs(m_fwd_mean[k]) > 1e-6 else 1.0
        err = abs(actual_ratio - expected_parity)
        parity_errors.append(float(err))
        
    carrier_fwd = encode_carrier_E3_hybrid_scaling(video_fwd, K=K)
    carrier_rev = encode_carrier_E3_hybrid_scaling(video_rev, K=K)
    
    carrier_diff_png = np.abs(carrier_fwd.astype(float) - carrier_rev.astype(float))
    
    c_fwd_webp = compress_to_webp(carrier_fwd, quality=80)
    c_rev_webp = compress_to_webp(carrier_rev, quality=80)
    carrier_diff_webp = np.abs(c_fwd_webp.astype(float) - c_rev_webp.astype(float))
    
    # Quadrant breakdown
    quad_diffs = {
        "Quad_G_diff_mae": float(np.mean(carrier_diff_png[:64, :64])),
        "Quad_T_diff_mae": float(np.mean(carrier_diff_png[:64, 64:])),
        "Quad_C_diff_mae": float(np.mean(carrier_diff_png[64:, :64])),
        "Quad_R_diff_mae": float(np.mean(carrier_diff_png[64:, 64:])),
    }
    
    return {
        "m_fwd_mean": m_fwd_mean,
        "m_rev_mean": m_rev_mean,
        "max_parity_violation": float(np.max(parity_errors)),
        "carrier_mae_png": float(np.mean(carrier_diff_png)),
        "carrier_max_diff_png": int(np.max(carrier_diff_png)),
        "carrier_mae_webp": float(np.mean(carrier_diff_webp)),
        "carrier_max_diff_webp": int(np.max(carrier_diff_webp)),
        "quadrant_mae": quad_diffs,
        "is_directionally_separable": bool(np.max(carrier_diff_png) > 10),
    }


# ==============================================================================
# TEST 2: Iso-Luminance Chromatic Blindness
# ==============================================================================
def run_test2_chromatic_blindness() -> Dict[str, Any]:
    """Test 2: Iso-Luminance Cross-Color Ambiguity.
    
    Constructs two scenes with IDENTICAL temporal luminance Y(t) trajectory
    but drastically different colors (pure red vs pure green vs pure blue).
    Tests if the E3-K12 carrier can differentiate them.
    """
    N, H, W = 64, 64, 64
    K = 12
    
    # We construct colors with identical BT.601 Luminance:
    # Y = 0.299 R + 0.587 G + 0.114 B
    # Target luminance: Y = 120.0
    # Color Red: R = 255, G = 60, B = 75 -> Y = 0.299*255 + 0.587*60 + 0.114*75 = 76.245 + 35.22 + 8.55 = 120.015
    # Color Green: R = 30, G = 175, B = 71 -> Y = 0.299*30 + 0.587*175 + 0.114*71 = 8.97 + 102.725 + 8.094 = 119.789 -> tweak G=175.4
    # Let's generate colors analytically:
    Y_target = 135.0
    
    # Red-dominant color
    c_red = np.array([240.0, 75.0, 85.0])
    y_r, cb_r, cr_r = rgb_to_ycbcr(c_red)
    
    # Find Green-dominant color with exact same Y
    # Y = 0.299*R + 0.587*G + 0.114*B
    # Let R=40, B=50 -> 0.299*40 + 0.114*50 = 11.96 + 5.7 = 17.66
    # G = (Y - 17.66) / 0.587
    g_val = (y_r - (0.299 * 40.0 + 0.114 * 50.0)) / 0.587
    c_green = np.array([40.0, g_val, 50.0])
    y_g, cb_g, cr_g = rgb_to_ycbcr(c_green)
    
    # Dynamic sequence: an oscillating disc
    y_grid, x_grid = np.mgrid[:H, :W]
    video_red = np.full((N, H, W, 3), 128, dtype=np.uint8)
    video_green = np.full((N, H, W, 3), 128, dtype=np.uint8)
    
    for t in range(N):
        cx = int(32 + 16 * np.sin(2 * np.pi * t / 32))
        cy = 32
        mask = ((x_grid - cx) ** 2 + (y_grid - cy) ** 2) <= 10 ** 2
        video_red[t, mask] = np.clip(np.round(c_red), 0, 255).astype(np.uint8)
        video_green[t, mask] = np.clip(np.round(c_green), 0, 255).astype(np.uint8)
        
    carrier_red = encode_carrier_E3_hybrid_scaling(video_red, K=K)
    carrier_green = encode_carrier_E3_hybrid_scaling(video_green, K=K)
    
    carrier_diff_png = np.abs(carrier_red.astype(float) - carrier_green.astype(float))
    
    # Test a mid-clip color change (Red -> Green at t=32) with CONSTANT Luminance
    video_swap = video_red.copy()
    for t in range(32, N):
        cx = int(32 + 16 * np.sin(2 * np.pi * t / 32))
        cy = 32
        mask = ((x_grid - cx) ** 2 + (y_grid - cy) ** 2) <= 10 ** 2
        video_swap[t, mask] = np.clip(np.round(c_green), 0, 255).astype(np.uint8)
        
    carrier_swap = encode_carrier_E3_hybrid_scaling(video_swap, K=K)
    carrier_diff_swap = np.abs(carrier_red.astype(float) - carrier_swap.astype(float))
    
    # Check Quad T and Quad C differences specifically
    quad_t_diff = float(np.mean(carrier_diff_swap[:64, 64:]))
    quad_c_diff = float(np.mean(carrier_diff_swap[64:, :64]))
    quad_g_diff = float(np.mean(carrier_diff_swap[:64, :64]))
    
    return {
        "luminance_y_red": float(y_r),
        "luminance_y_green": float(y_g),
        "luminance_delta": float(abs(y_r - y_g)),
        "static_colors_carrier_mae": float(np.mean(carrier_diff_png)),
        "static_colors_carrier_max_diff": int(np.max(carrier_diff_png)),
        "temporal_color_swap_carrier_mae": float(np.mean(carrier_diff_swap)),
        "temporal_color_swap_carrier_max_diff": int(np.max(carrier_diff_swap)),
        "quad_t_diff_on_color_swap": quad_t_diff,
        "quad_c_diff_on_color_swap": quad_c_diff,
        "quad_g_diff_on_color_swap": quad_g_diff,
        "is_completely_color_blind_in_T_and_C": bool(quad_t_diff < 0.1 and quad_c_diff < 0.1),
    }


# ==============================================================================
# TEST 3: Single-Frame Impulse Sensitivity & Temporal Edge Bounds
# ==============================================================================
def run_test3_single_frame_impulse() -> Dict[str, Any]:
    """Test 3: Single-Frame Transient Detection Threshold.
    
    Sweeps a 1-frame impulse across time positions (n in 0..63) and amplitudes
    (A in 5..250). Checks if carrier retains the signal after 8-bit quantization
    and WebP lossy compression (Q=80).
    """
    N, H, W = 64, 64, 64
    K = 12
    
    baseline_video = np.full((N, H, W, 3), 128, dtype=np.uint8)
    carrier_base = encode_carrier_E3_hybrid_scaling(baseline_video, K=K)
    carrier_base_webp = compress_to_webp(carrier_base, quality=80)
    
    test_positions = [0, 1, 8, 16, 31, 32, 48, 56, 62, 63]
    test_amplitudes = [10, 25, 50, 100, 200]
    
    results_matrix = {}
    
    for t_pos in test_positions:
        results_matrix[f"t_{t_pos}"] = {}
        for amp in test_amplitudes:
            video_pulse = baseline_video.copy()
            # Flash the central 16x16 region
            video_pulse[t_pos, 24:40, 24:40] = np.clip(128 + amp, 0, 255).astype(np.uint8)
            
            c_png = encode_carrier_E3_hybrid_scaling(video_pulse, K=K)
            c_webp = compress_to_webp(c_png, quality=80)
            
            diff_png = np.max(np.abs(c_png.astype(float) - carrier_base.astype(float)))
            diff_webp = np.max(np.abs(c_webp.astype(float) - carrier_base_webp.astype(float)))
            
            results_matrix[f"t_{t_pos}"][f"amp_{amp}"] = {
                "max_diff_png": int(diff_png),
                "max_diff_webp": int(diff_webp),
                "detectable_png": bool(diff_png >= 3),
                "detectable_webp": bool(diff_webp >= 3),
            }
            
    # Measure boundary attenuation: compare t=0 vs t=32
    diff_t0_amp50 = results_matrix["t_0"]["amp_50"]["max_diff_png"]
    diff_t32_amp50 = results_matrix["t_32"]["amp_50"]["max_diff_png"]
    
    return {
        "sweep_results": results_matrix,
        "boundary_vs_mid_ratio_png": float(diff_t0_amp50 / max(1, diff_t32_amp50)),
        "min_detectable_amplitude_mid_png": min([amp for amp in test_amplitudes if results_matrix["t_32"][f"amp_{amp}"]["detectable_png"]]),
        "min_detectable_amplitude_mid_webp": min([amp for amp in test_amplitudes if results_matrix["t_32"][f"amp_{amp}"]["detectable_webp"]]),
    }


# ==============================================================================
# TEST 4: Saturation Boundaries & Divisor D Parameter Sweep
# ==============================================================================
def run_test4_saturation_and_divisor_D() -> Dict[str, Any]:
    """Test 4: Dynamic Range Clamping vs Quantization Noise.
    
    Analyzes normalization divisor D across [10.0, 20.0, 35.0, 50.0, 75.0, 100.0]
    on small (A=15), medium (A=60), and extreme (A=220) multi-mode signals.
    Measures clamp saturation rate and reconstruction RMSE.
    """
    N, H, W = 64, 64, 64
    K = 12
    P = compute_gram_polynomials_N_K(N=N, K=K)
    
    divisors = [10.0, 20.0, 35.0, 50.0, 75.0, 100.0]
    amplitudes = [15.0, 60.0, 120.0, 220.0]
    
    sweep_data = {}
    
    for D in divisors:
        sweep_data[f"D_{int(D)}"] = {}
        for amp in amplitudes:
            # Create a multi-mode sinusoidal flash
            t_vec = np.linspace(0, 1, N)
            signal_1d = amp * np.sin(2 * np.pi * 3 * t_vec)
            
            # Theoretical projection
            M_true = np.sum(signal_1d * P, axis=1) # (K,)
            
            # Simulate normalization and 8-bit quantization with divisor D
            m_norm = np.clip(M_true / D, -1.0, 1.0)
            clamped_count = int(np.sum(np.abs(M_true / D) > 1.0))
            
            # Map to 8-bit uint8 range [0, 255] with scale 90.0
            u8_quant = np.clip(np.round(128.0 + m_norm * 90.0), 0, 255).astype(np.uint8)
            
            # Invert from uint8 back to continuous estimate
            m_hat = (u8_quant.astype(float) - 128.0) / 90.0 * D
            
            rmse = float(np.sqrt(np.mean((M_true - m_hat) ** 2)))
            max_abs_err = float(np.max(np.abs(M_true - m_hat)))
            
            sweep_data[f"D_{int(D)}"][f"amp_{int(amp)}"] = {
                "clamped_modes_count": clamped_count,
                "clamped_fraction": float(clamped_count / K),
                "rmse": rmse,
                "max_abs_err": max_abs_err,
            }
            
    # Find empirical collision between two distinct extreme bursts at D=35
    sigA = 220.0 * np.sin(2 * np.pi * 2 * np.linspace(0, 1, N))
    sigB = 240.0 * np.sin(2 * np.pi * 2 * np.linspace(0, 1, N))
    MA = np.sum(sigA * P, axis=1)
    MB = np.sum(sigB * P, axis=1)
    
    normA = np.clip(MA / 35.0, -1.0, 1.0)
    normB = np.clip(MB / 35.0, -1.0, 1.0)
    
    u8_A = np.clip(np.round(128.0 + normA * 90.0), 0, 255).astype(np.uint8)
    u8_B = np.clip(np.round(128.0 + normB * 90.0), 0, 255).astype(np.uint8)
    
    exact_collision = bool(np.array_equal(u8_A, u8_B))
    
    return {
        "divisor_sweep": sweep_data,
        "extreme_burst_collision_at_D35": exact_collision,
        "notes": "Smaller D increases small-signal SNR but triggers saturation collisions on high amplitudes. D=35 clamps signals exceeding ~35 energy units.",
    }


# ==============================================================================
# TEST 5: Spatial Locality & Walsh Demultiplexing Crosstalk
# ==============================================================================
def run_test5_spatial_locality_and_crosstalk() -> Dict[str, Any]:
    """Test 5: Spatial Walsh Demultiplexing & Object Resolution Bounds.
    
    Evaluates whether localized objects (radii r in [1, 2, 4, 8, 16, 32]) preserve
    orthogonality across Walsh subcarriers, and tests WebP chroma subsampling effects.
    """
    H, W = 64, 64
    K = 12
    W_basis = generate_2d_orthogonal_block_basis((H, W), K=8)
    
    radii = [1, 2, 4, 8, 16, 32]
    crosstalk_by_radius = {}
    
    y_grid, x_grid = np.mgrid[:H, :W]
    
    for r in radii:
        mask = ((x_grid - 32) ** 2 + (y_grid - 32) ** 2) <= r ** 2
        mask_weight = np.sum(mask)
        
        # Test orthogonality of Walsh patterns strictly within the masked object area
        # For full image, W_i * W_j integrates to 0 (i != j) and 1 (i == j)
        num_walsh = 7 # indices 1..7
        gram_walsh_local = np.zeros((num_walsh, num_walsh))
        for i in range(num_walsh):
            for j in range(num_walsh):
                gram_walsh_local[i, j] = np.sum(W_basis[i + 1] * W_basis[j + 1] * mask) / mask_weight
                
        # Non-diagonal crosstalk
        off_diag = np.abs(gram_walsh_local - np.diag(np.diag(gram_walsh_local)))
        max_crosstalk = float(np.max(off_diag))
        mean_crosstalk = float(np.mean(off_diag))
        diag_min = float(np.min(np.diag(gram_walsh_local)))
        
        crosstalk_by_radius[f"radius_{r}"] = {
            "mask_pixel_count": int(mask_weight),
            "max_crosstalk": max_crosstalk,
            "mean_crosstalk": mean_crosstalk,
            "min_diagonal_energy": diag_min,
            "is_orthogonal": bool(max_crosstalk < 0.05),
        }
        
    # Test WebP 4:2:0 Chroma Subsampling impact on Quad C
    # Create test carrier with high-frequency Walsh pattern in Cr (Quad C)
    test_carrier = np.full((128, 128, 3), 128, dtype=np.uint8)
    # Inject Walsh mode 5 into Cr
    _, cb_clean, cr_clean = rgb_to_ycbcr(test_carrier[64:, :64])
    cr_modulated = np.clip(128.0 + 80.0 * W_basis[5], 0, 255)
    quad_C_rgb = ycbcr_to_rgb(np.full((64, 64), 128.0), cb_clean, cr_modulated)
    test_carrier[64:, :64] = quad_C_rgb
    
    carrier_webp_q80 = compress_to_webp(test_carrier, quality=80)
    _, _, cr_recovered_webp = rgb_to_ycbcr(carrier_webp_q80[64:, :64])
    
    # Measure attenuation of the Walsh carrier under WebP
    recovered_amp_webp = np.mean((cr_recovered_webp - 128.0) * W_basis[5])
    original_amp = 80.0
    webp_chroma_attenuation = float(recovered_amp_webp / original_amp)
    
    return {
        "crosstalk_by_radius": crosstalk_by_radius,
        "webp_chroma_carrier_recovery_ratio": webp_chroma_attenuation,
        "webp_chroma_attenuation_loss_pct": float((1.0 - webp_chroma_attenuation) * 100.0),
        "min_radius_for_walsh_orthogonality": min([r for r in radii if crosstalk_by_radius[f"radius_{r}"]["is_orthogonal"]] or [None]),
    }


def main():
    print("=" * 70)
    print("VLT CODEC STRESS LAB - SYSTEMATIC CHANNEL BOUNDS AUDIT")
    print("=" * 70)
    
    print("\n--- Running Test 1: Time-Reversal Parity & Invariance ---")
    t1 = run_test1_time_reversal()
    print(f"  Max Parity Violation (|c_rev - (-1)^k c_fwd|): {t1['max_parity_violation']:.6e}")
    print(f"  Carrier Dist PNG (MAE): {t1['carrier_mae_png']:.2f}, Max Diff: {t1['carrier_max_diff_png']}")
    print(f"  Carrier Dist WebP (MAE): {t1['carrier_mae_webp']:.2f}, Max Diff: {t1['carrier_max_diff_webp']}")
    print(f"  Directional Separability: {t1['is_directionally_separable']}")
    print(f"  Quadrant breakdown (MAE): G={t1['quadrant_mae']['Quad_G_diff_mae']:.1f}, "
          f"T={t1['quadrant_mae']['Quad_T_diff_mae']:.1f}, "
          f"C={t1['quadrant_mae']['Quad_C_diff_mae']:.1f}")

    print("\n--- Running Test 2: Iso-Luminance Chromatic Blindness ---")
    t2 = run_test2_chromatic_blindness()
    print(f"  Luminance Delta between Red and Green targets: {t2['luminance_delta']:.4f}")
    print(f"  Static Colors Carrier MAE: {t2['static_colors_carrier_mae']:.4f}, Max: {t2['static_colors_carrier_max_diff']}")
    print(f"  Temporal Color Swap Carrier MAE: {t2['temporal_color_swap_carrier_mae']:.4f}, Max: {t2['temporal_color_swap_carrier_max_diff']}")
    print(f"  Quad T MAE on Color Swap: {t2['quad_t_diff_on_color_swap']:.4f}")
    print(f"  Quad C MAE on Color Swap: {t2['quad_c_diff_on_color_swap']:.4f}")
    print(f"  Quad G MAE on Color Swap: {t2['quad_g_diff_on_color_swap']:.4f}")
    print(f"  Complete Color Blindness in T & C: {t2['is_completely_color_blind_in_T_and_C']}")

    print("\n--- Running Test 3: Single-Frame Impulse Sensitivity ---")
    t3 = run_test3_single_frame_impulse()
    print(f"  Min Detectable Amplitude Mid-Window (PNG):  {t3['min_detectable_amplitude_mid_png']}")
    print(f"  Min Detectable Amplitude Mid-Window (WebP): {t3['min_detectable_amplitude_mid_webp']}")
    print(f"  Boundary-to-Mid Salience Ratio:             {t3['boundary_vs_mid_ratio_png']:.2f}")

    print("\n--- Running Test 4: Saturation Boundaries & Divisor D ---")
    t4 = run_test4_saturation_and_divisor_D()
    print(f"  Extreme Burst Collision at D=35: {t4['extreme_burst_collision_at_D35']}")
    print("  D=35 Clamping & RMSE summary:")
    for amp in [15, 60, 120, 220]:
        d35_res = t4['divisor_sweep']['D_35'][f'amp_{amp}']
        print(f"    Amp {amp:3d}: Clamped Modes={d35_res['clamped_modes_count']}/12, RMSE={d35_res['rmse']:.3f}")

    print("\n--- Running Test 5: Spatial Locality & Walsh Crosstalk ---")
    t5 = run_test5_spatial_locality_and_crosstalk()
    print(f"  Min Object Radius for Walsh Orthogonality: {t5['min_radius_for_walsh_orthogonality']} px")
    for r in [2, 4, 8, 16, 32]:
        print(f"    Radius {r:2d} px: Max Crosstalk={t5['crosstalk_by_radius'][f'radius_{r}']['max_crosstalk']:.4f}, "
              f"Orthogonal={t5['crosstalk_by_radius'][f'radius_{r}']['is_orthogonal']}")
    print(f"  WebP 4:2:0 Chroma Walsh Recovery: {t5['webp_chroma_carrier_recovery_ratio']:.2%}")
    print(f"  WebP Chroma Attenuation Loss:     {t5['webp_chroma_attenuation_loss_pct']:.2f}%")

    # Save complete structured results
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "stress_lab")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "vlt_stress_lab_results.json")
    
    full_report = {
        "suite": "VLT Codec Stress Lab",
        "version": "1.0",
        "description": "5-way numerical audit of E3-K12 channel and representation limits",
        "test1_time_reversal": t1,
        "test2_chromatic_blindness": t2,
        "test3_single_frame_impulse": t3,
        "test4_saturation_and_divisor_D": t4,
        "test5_spatial_walsh_crosstalk": t5,
    }
    
    with open(out_file, "w", encoding="utf-8", newline="\n") as f:
        json.dump(full_report, f, indent=2)
    print(f"\n[SUCCESS] Full stress lab results saved to: {out_file}")


if __name__ == "__main__":
    main()
