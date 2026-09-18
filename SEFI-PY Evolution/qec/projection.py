import numpy as np

def project_to_manifold(trajectory_point: np.ndarray, N: np.ndarray, B: np.ndarray, d_N: float, d_B: float) -> np.ndarray:
    """
    Applies Geometric QEC Projection Mapping:
    gamma_corr(t) = gamma(t) - d_N * N - d_B * B
    """
    return trajectory_point - (d_N * N) - (d_B * B)