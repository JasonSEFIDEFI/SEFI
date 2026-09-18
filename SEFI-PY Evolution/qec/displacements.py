import numpy as np

def calculate_displacement(trajectory_point: np.ndarray, manifold_projection: np.ndarray, N: np.ndarray, B: np.ndarray):
    """
    Decomposes error vector into Normal (d_N) and Binormal (d_B) components:
    d(t) = d_N * N + d_B * B
    """
    displacement_vector = trajectory_point - manifold_projection
    d_N = np.dot(displacement_vector, N)
    d_B = np.dot(displacement_vector, B)
    return d_N, d_B