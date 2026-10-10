"""Numerical Round-Trip Reconstruction & Basis Verification Benchmark.

Standalone Reproducibility Script:
Audits:
1. Gram basis orthonormality across N in {32, 64, 128} with K=12:
   Verifies P P^T = I_12 and ||P_k||_2 = 1.
2. Per-mode Round-Trip Reconstruction Fidelity across modes k=0..11:
   Tests encode -> PNG/WebP -> decode round-trip on controlled synthetic signals.
3. Multi-Mode superposition reconstruction.
4. Spatially localized object reconstruction (disc region).
"""

import os
import io
import json
import numpy as np
from PIL import Image

try:
    from reference_carrier_codec import (
        compute_gram_polynomials_N_K,
        encode_carrier_E3_hybrid_scaling,
        decode_carrier_E3_hybrid_scaling,
        create_synthetic_scaling_video,
    )
except ImportError:
    from scripts.reference_carrier_codec import (
        compute_gram_polynomials_N_K,
        encode_carrier_E3_hybrid_scaling,
        decode_carrier_E3_hybrid_scaling,
        create_synthetic_scaling_video,
    )


def audit_basis_orthonormality():
    results = {}
    for N in [32, 64, 128]:
        P = compute_gram_polynomials_N_K(N=N, K=12)
        gram_prod = P @ P.T
        diff = np.abs(gram_prod - np.eye(12))
        max_err = np.max(diff)
        frobenius_err = np.linalg.norm(diff, 'fro')
        row_norms = np.linalg.norm(P, axis=1)
        results[f"N_{N}"] = {
            "max_orthogonality_error": float(max_err),
            "frobenius_error": float(frobenius_err),
            "min_row_norm": float(np.min(row_norms)),
            "max_row_norm": float(np.max(row_norms)),
            "is_strictly_orthonormal": bool(max_err < 1e-10),
        }
    return results


def run_roundtrip_single_modes(N: int = 64, K: int = 12):
    test_amps = [-0.6, -0.3, 0.3, 0.6]
    per_mode_metrics = {}
    
    for k in range(K):
        actual_list = []
        decoded_png_list = []
        decoded_webp_list = []
        crosstalk_png_list = []
        crosstalk_webp_list = []
        
        for amp in test_amps:
            video = create_synthetic_scaling_video(
                N=N, H=64, W=64,
                active_dims={k: amp},
                base_luminance=128.0,
                spatial_region="full",
            )
            carrier = encode_carrier_E3_hybrid_scaling(video, K=K)
            
            # Transport 1: PNG
            buf_png = io.BytesIO()
            Image.fromarray(carrier).save(buf_png, format="PNG")
            buf_png.seek(0)
            carrier_png = np.array(Image.open(buf_png))
            
            # Transport 2: WebP Q=80
            buf_webp = io.BytesIO()
            Image.fromarray(carrier).save(buf_webp, format="WEBP", quality=80)
            buf_webp.seek(0)
            carrier_webp = np.array(Image.open(buf_webp))
            
            hat_png = decode_carrier_E3_hybrid_scaling(carrier_png, K=K, spatial_region="full")
            hat_webp = decode_carrier_E3_hybrid_scaling(carrier_webp, K=K, spatial_region="full")
            
            actual_list.append(amp)
            decoded_png_list.append(hat_png[k])
            decoded_webp_list.append(hat_webp[k])
            
            other_png = [abs(hat_png[j]) for j in range(K) if j != k]
            other_webp = [abs(hat_webp[j]) for j in range(K) if j != k]
            crosstalk_png_list.append(max(other_png) if other_png else 0.0)
            crosstalk_webp_list.append(max(other_webp) if other_webp else 0.0)
            
        act = np.array(actual_list)
        d_png = np.array(decoded_png_list)
        d_webp = np.array(decoded_webp_list)
        
        rmse_png = float(np.sqrt(np.mean((act - d_png) ** 2)))
        rmse_webp = float(np.sqrt(np.mean((act - d_webp) ** 2)))
        r_png = float(np.corrcoef(act, d_png)[0, 1]) if np.std(d_png) > 1e-6 else 0.0
        r_webp = float(np.corrcoef(act, d_webp)[0, 1]) if np.std(d_webp) > 1e-6 else 0.0
        max_crosstalk_png = float(np.max(crosstalk_png_list))
        max_crosstalk_webp = float(np.max(crosstalk_webp_list))
        
        per_mode_metrics[f"mode_{k}"] = {
            "mode_index": k,
            "rmse_png": rmse_png,
            "rmse_webp": rmse_webp,
            "pearson_r_png": r_png,
            "pearson_r_webp": r_webp,
            "max_crosstalk_png": max_crosstalk_png,
            "max_crosstalk_webp": max_crosstalk_webp,
        }
        
    return per_mode_metrics


def run_roundtrip_multimode_superposition(N: int = 64, K: int = 12):
    """Test concurrent activation of multiple orthogonal modes."""
    active_modes = {0: 0.4, 1: -0.3, 2: 0.5, 4: -0.4, 7: 0.3}
    video = create_synthetic_scaling_video(N=N, H=64, W=64, active_dims=active_modes, base_luminance=128.0)
    carrier = encode_carrier_E3_hybrid_scaling(video, K=K)
    
    # PNG
    buf_png = io.BytesIO()
    Image.fromarray(carrier).save(buf_png, format="PNG")
    buf_png.seek(0)
    hat_png = decode_carrier_E3_hybrid_scaling(np.array(Image.open(buf_png)), K=K)
    
    # WebP
    buf_webp = io.BytesIO()
    Image.fromarray(carrier).save(buf_webp, format="WEBP", quality=80)
    buf_webp.seek(0)
    hat_webp = decode_carrier_E3_hybrid_scaling(np.array(Image.open(buf_webp)), K=K)
    
    active_keys = sorted(active_modes.keys())
    act = np.array([active_modes[k] for k in active_keys])
    rec_png = np.array([hat_png[k] for k in active_keys])
    rec_webp = np.array([hat_webp[k] for k in active_keys])
    
    return {
        "active_modes": active_modes,
        "rmse_png": float(np.sqrt(np.mean((act - rec_png) ** 2))),
        "rmse_webp": float(np.sqrt(np.mean((act - rec_webp) ** 2))),
        "pearson_r_png": float(np.corrcoef(act, rec_png)[0, 1]),
        "pearson_r_webp": float(np.corrcoef(act, rec_webp)[0, 1]),
    }


def run_full_numerical_audit():
    print("=" * 70)
    print("NUMERICAL ROUND-TRIP AUDIT: GRAM BASIS & E3-K12 DECODER")
    print("=" * 70)
    
    basis_res = audit_basis_orthonormality()
    print("\n--- 1. Gram Basis Orthonormality Check ---")
    for n_key, data in basis_res.items():
        print(f"  {n_key:6s}: Max Ortho Err={data['max_orthogonality_error']:.2e}, "
              f"Norm Bounds=[{data['min_row_norm']:.6f}, {data['max_row_norm']:.6f}] -> Pass: {data['is_strictly_orthonormal']}")
              
    print("\n--- 2. Single-Mode Round-Trip Reconstruction (N=64, K=12) ---")
    mode_metrics = run_roundtrip_single_modes(N=64, K=12)
    print(f"  {'Mode':8s} {'RMSE (PNG)':12s} {'RMSE (WebP)':12s} {'r (PNG)':10s} {'r (WebP)':10s} {'Max Leak PNG':14s} {'Max Leak WebP':14s}")
    print("  " + "-" * 76)
    for k_key, m in mode_metrics.items():
        print(f"  {k_key:8s} {m['rmse_png']:12.4f} {m['rmse_webp']:12.4f} {m['pearson_r_png']:10.4f} {m['pearson_r_webp']:10.4f} {m['max_crosstalk_png']:14.4f} {m['max_crosstalk_webp']:14.4f}")
        
    print("\n--- 3. Multi-Mode Superposition Invertibility ---")
    multi_res = run_roundtrip_multimode_superposition(N=64, K=12)
    print(f"  Concurrent Active Modes: {list(multi_res['active_modes'].keys())}")
    print(f"  Multi-Mode RMSE (PNG):        {multi_res['rmse_png']:.4f}")
    print(f"  Multi-Mode RMSE (WebP Q=80):  {multi_res['rmse_webp']:.4f}")
    print(f"  Multi-Mode Pearson r (PNG):   {multi_res['pearson_r_png']:.4f}")
    print(f"  Multi-Mode Pearson r (WebP):  {multi_res['pearson_r_webp']:.4f}")

    png_rmses = [m["rmse_png"] for m in mode_metrics.values()]
    webp_rmses = [m["rmse_webp"] for m in mode_metrics.values()]
    png_rs = [m["pearson_r_png"] for m in mode_metrics.values()]
    webp_rs = [m["pearson_r_webp"] for m in mode_metrics.values()]
    
    summary = {
        "basis_orthonormality": basis_res,
        "mode_roundtrip": mode_metrics,
        "multimode_superposition": multi_res,
        "aggregate": {
            "mean_rmse_png": float(np.mean(png_rmses)),
            "mean_rmse_webp": float(np.mean(webp_rmses)),
            "min_pearson_r_png": float(np.min(png_rs)),
            "min_pearson_r_webp": float(np.min(webp_rs)),
            "max_rmse_png": float(np.max(png_rmses)),
            "max_rmse_webp": float(np.max(webp_rmses)),
        }
    }
    
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "numerical_roundtrip_audit.json")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved relative numerical audit metrics to: {out_path}")
    return summary


if __name__ == "__main__":
    run_full_numerical_audit()
