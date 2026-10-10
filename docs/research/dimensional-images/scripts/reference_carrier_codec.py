"""Self-Contained Reference Implementation of the E3-K12 Visual Latent Transport Codec.

This standalone reference module implements the exact mathematical operations
described in METHODOLOGY.md without external project dependencies.
Required libraries: numpy, scipy, Pillow.
"""

from typing import Tuple, Dict, Any, Optional
import numpy as np


def rgb_to_ycbcr(rgb: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convert RGB image to ITU-R BT.601 YCbCr components."""
    rgb = rgb.astype(np.float64)
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = 128.0 - 0.168736 * r - 0.331264 * g + 0.5 * b
    cr = 128.0 + 0.5 * r - 0.418688 * g - 0.081312 * b
    return y, cb, cr


def ycbcr_to_rgb(y: np.ndarray, cb: np.ndarray, cr: np.ndarray) -> np.ndarray:
    """Convert ITU-R BT.601 YCbCr components to RGB uint8 array."""
    y = y.astype(np.float64)
    cb_shift = cb.astype(np.float64) - 128.0
    cr_shift = cr.astype(np.float64) - 128.0
    
    r = y + 1.402 * cr_shift
    g = y - 0.344136 * cb_shift - 0.714136 * cr_shift
    b = y + 1.772 * cb_shift
    
    rgb = np.stack([r, g, b], axis=-1)
    return np.clip(np.round(rgb), 0, 255).astype(np.uint8)


def compute_gram_polynomials_N_K(N: int = 64, K: int = 12) -> np.ndarray:
    """Compute discrete orthonormal Gram polynomials on N points up to degree K-1.
    
    Returns:
        P: Shape (K, N) float64 array satisfying P @ P.T = I_K.
    """
    assert 1 <= K <= N, f"K must be in [1, {N}], got {K}"
    t_norm = np.linspace(-1.0, 1.0, N, dtype=np.float64)
    V = np.column_stack([t_norm ** d for d in range(K)])
    Q, _ = np.linalg.qr(V)
    
    # Deterministic sign conventions:
    if Q[0, 0] < 0:
        Q[:, 0] = -Q[:, 0]
    if K > 1 and Q[-1, 1] < Q[0, 1]:
        Q[:, 1] = -Q[:, 1]
    if K > 2 and Q[0, 2] < 0:
        Q[:, 2] = -Q[:, 2]
    if K > 3 and Q[-1, 3] < 0:
        Q[:, 3] = -Q[:, 3]
    for d in range(4, K):
        if Q[-1, d] < 0:
            Q[:, d] = -Q[:, d]
            
    return Q.T  # Shape (K, N)


def generate_2d_orthogonal_block_basis(shape: Tuple[int, int] = (64, 64), K: int = 8) -> np.ndarray:
    """Generate 2D spatial orthogonal Walsh block basis patterns."""
    H, W = shape
    basis = np.zeros((K, H, W), dtype=np.float64)
    basis[0] = 1.0
    
    blocks = [
        (1, 2), (2, 1), (2, 2),
        (1, 4), (4, 1), (2, 4), (4, 2),
    ]
    for idx, (by, bx) in enumerate(blocks[:K-1]):
        pat = np.zeros((H, W), dtype=np.float64)
        sy, sx = H // by, W // bx
        for iy in range(by):
            for ix in range(bx):
                sign = 1.0 if ((iy + ix) % 2 == 0) else -1.0
                pat[iy*sy:(iy+1)*sy, ix*sx:(ix+1)*sx] = sign
        basis[idx + 1] = pat
        
    return basis


def encode_carrier_E3_hybrid_scaling(
    video_rgb: np.ndarray,
    K: int = 12,
) -> np.ndarray:
    """Encode video (N, H, W, 3) into single 128x128 E3-K12 Carrier Tile."""
    N, H, W, _ = video_rgb.shape
    P = compute_gram_polynomials_N_K(N=N, K=K)
    W_basis = generate_2d_orthogonal_block_basis((H, W), K=8)
    
    y_list, cb_list, cr_list = [], [], []
    for f in video_rgb:
        y, cb, cr = rgb_to_ycbcr(f)
        y_list.append(y)
        cb_list.append(cb)
        cr_list.append(cr)
        
    y_video = np.stack(y_list, axis=0)
    y_centered = y_video - 128.0
    
    # Compute temporal projections: M_k = sum_t y_centered(t) * P_k(t)
    M = np.sum(y_centered * P[:, :, np.newaxis, np.newaxis], axis=1)
    
    # Quad G: Base state Y0
    quad_G = np.zeros((64, 64, 3), dtype=np.uint8)
    y0_u8 = np.clip(y_list[0], 0, 255).astype(np.uint8)
    quad_G[..., 0] = y0_u8
    quad_G[..., 1] = y0_u8
    quad_G[..., 2] = y0_u8
    
    # Quad T (Kinematics):
    # Channel 0 (R): P0 (mean offset)
    # Channel 1 (G): P2 (curvature)
    # Channel 2 (B): Odd higher-order subcarriers (k=3, 5, 7, 9, 11)
    m0_norm = np.clip(M[0] / 35.0, -1.0, 1.0) if K > 0 else np.zeros((H, W))
    m2_norm = np.clip(M[2] / 35.0, -1.0, 1.0) if K > 2 else np.zeros((H, W))
    
    t_ch0 = np.clip(128.0 + m0_norm * 90.0, 0.0, 255.0).astype(np.uint8)
    t_ch1 = np.clip(128.0 + m2_norm * 90.0, 0.0, 255.0).astype(np.uint8)
    
    t_sub_mod = np.zeros((H, W), dtype=np.float64)
    odd_indices = [k for k in range(3, K) if k % 2 == 1]
    sub_amp_t = 80.0 / np.sqrt(max(1, len(odd_indices)))
    for idx_w, k_val in enumerate(odd_indices):
        m_norm = np.clip(M[k_val] / 35.0, -1.0, 1.0)
        t_sub_mod += m_norm * sub_amp_t * W_basis[idx_w + 1]
        
    t_ch2 = np.clip(128.0 + t_sub_mod, 0.0, 255.0).astype(np.uint8)
    quad_T = np.stack([t_ch0, t_ch1, t_ch2], axis=-1)
    
    # Quad C (False-color Chrominance Layer):
    # Cb: P1 (linear drift)
    # Cr: Even higher-order subcarriers (k=4, 6, 8, 10)
    m1_norm = np.clip(M[1] / 35.0, -1.0, 1.0) if K > 1 else np.zeros((H, W))
    cb_val = np.clip(128.0 + m1_norm * 90.0, 0.0, 255.0)
    
    c_sub_mod = np.zeros((H, W), dtype=np.float64)
    even_indices = [k for k in range(3, K) if k % 2 == 0]
    sub_amp_c = 80.0 / np.sqrt(max(1, len(even_indices)))
    for idx_w, k_val in enumerate(even_indices):
        m_norm = np.clip(M[k_val] / 35.0, -1.0, 1.0)
        c_sub_mod += m_norm * sub_amp_c * W_basis[idx_w + 1]
        
    cr_val = np.clip(128.0 + c_sub_mod, 0.0, 255.0)
    y_c = np.full((H, W), 128.0, dtype=np.float64)
    quad_C = ycbcr_to_rgb(y_c, cb_val, cr_val)
    
    # Quad R: Neutral baseline
    quad_R = np.full((64, 64, 3), 128, dtype=np.uint8)
    
    # 2x2 Assembly
    top_row = np.concatenate([quad_G, quad_T], axis=1)
    bot_row = np.concatenate([quad_C, quad_R], axis=1)
    mosaic_128 = np.concatenate([top_row, bot_row], axis=0)
    return mosaic_128


def decode_carrier_E3_hybrid_scaling(
    mosaic_128: np.ndarray,
    K: int = 12,
    spatial_region: str = "full",
) -> np.ndarray:
    """Demodulate normalized projection coefficients m_hat from E3 Carrier."""
    H, W = 64, 64
    W_basis = generate_2d_orthogonal_block_basis((H, W), K=8)
    
    quad_T = mosaic_128[:64, 64:].astype(np.float64)
    quad_C_rgb = mosaic_128[64:, :64]
    _, cb_val, cr_val = rgb_to_ycbcr(quad_C_rgb)
    cb_val = cb_val.astype(np.float64)
    cr_val = cr_val.astype(np.float64)
    
    coeffs = np.zeros(K, dtype=np.float64)
    
    y_grid, x_grid = np.mgrid[:H, :W]
    if spatial_region in ["center_circle", "disc_x32"]:
        dist = np.sqrt((x_grid - W // 2) ** 2 + (y_grid - H // 2) ** 2)
        mask = (dist <= 16).astype(np.float64)
    else:
        mask = np.ones((H, W), dtype=np.float64)
    mask_weight = np.sum(mask)
    
    # k=0 (P0 Mean): Channel 0 (Red) of Quad T
    if K > 0:
        coeffs[0] = (np.sum((quad_T[..., 0] - 128.0) * mask) / mask_weight) / 90.0
        
    # k=1 (P1 Drift): Cb channel of Quad C
    if K > 1:
        coeffs[1] = (np.sum((cb_val - 128.0) * mask) / mask_weight) / 90.0
        
    # k=2 (P2 Curvature): Channel 1 (Green) of Quad T
    if K > 2:
        coeffs[2] = (np.sum((quad_T[..., 1] - 128.0) * mask) / mask_weight) / 90.0
        
    # Odd modes in Quad T Channel 2 (Blue): k=3, 5, 7, 9, 11
    odd_indices = [k for k in range(3, K) if k % 2 == 1]
    sub_amp_t = 80.0 / np.sqrt(max(1, len(odd_indices)))
    t_ch2 = quad_T[..., 2] - 128.0
    for idx_w, k_val in enumerate(odd_indices):
        proj = np.mean(t_ch2 * W_basis[idx_w + 1])
        coeffs[k_val] = proj / sub_amp_t
        
    # Even modes in Quad C Cr channel: k=4, 6, 8, 10
    even_indices = [k for k in range(3, K) if k % 2 == 0]
    sub_amp_c = 80.0 / np.sqrt(max(1, len(even_indices)))
    cr_centered = cr_val - 128.0
    for idx_w, k_val in enumerate(even_indices):
        proj = np.mean(cr_centered * W_basis[idx_w + 1])
        coeffs[k_val] = proj / sub_amp_c
        
    return coeffs


def create_synthetic_scaling_video(
    N: int = 64,
    H: int = 64,
    W: int = 64,
    active_dims: Optional[Dict[int, float]] = None,
    base_luminance: float = 128.0,
    spatial_region: str = "full",
) -> np.ndarray:
    """Construct controlled synthetic N-frame video with specific Gram mode activations."""
    K = 12
    P = compute_gram_polynomials_N_K(N=N, K=K)
    
    y_grid, x_grid = np.mgrid[:H, :W]
    if spatial_region == "full":
        mask = np.ones((H, W), dtype=np.float64)
    elif spatial_region in ["center_circle", "disc_x32"]:
        cx, cy = W // 2, H // 2
        r = min(H, W) // 4
        dist = np.sqrt((x_grid - cx) ** 2 + (y_grid - cy) ** 2)
        mask = np.clip(1.0 - (dist - r) / 2.0, 0.0, 1.0)
    else:
        mask = np.ones((H, W), dtype=np.float64)
        
    video_y = np.full((N, H, W), base_luminance, dtype=np.float64)
    
    if active_dims:
        for k, amp in active_dims.items():
            if 0 <= k < K:
                scale = 35.0
                mod = amp * scale * P[k, :, np.newaxis, np.newaxis] * mask[np.newaxis, :, :]
                video_y += mod
                
    video_y = np.clip(video_y, 16.0, 235.0)
    
    video_rgb = np.zeros((N, H, W, 3), dtype=np.uint8)
    for t in range(N):
        y_channel = video_y[t]
        cb = np.full((H, W), 128.0, dtype=np.float64)
        cr = np.full((H, W), 128.0, dtype=np.float64)
        video_rgb[t] = ycbcr_to_rgb(y_channel, cb, cr)
        
    return video_rgb
