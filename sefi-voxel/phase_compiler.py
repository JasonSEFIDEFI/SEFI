# sefi-voxel/phase_compiler.py
import numpy as np

def compile_phase_pattern(r: np.ndarray,
                          k_vectors: np.ndarray) -> np.ndarray:
    """
    r: (N, 3) positions
    k_vectors: (M, 3) wave vectors for M transducers
    returns phases: (N, M)
    """
    phases = -np.dot(r, k_vectors.T)
    return np.mod(phases, 2 * np.pi)
