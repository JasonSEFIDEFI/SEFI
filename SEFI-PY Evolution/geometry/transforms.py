import numpy as np

def rotate_vector(vector: np.ndarray, axis: np.ndarray, angle: float) -> np.ndarray:
    """
    Rodrigues' rotation formula to rotate a vector around a given axis.
    """
    axis = axis / np.linalg.norm(axis)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    return vector * cos_a + np.cross(axis, vector) * sin_a + axis * np.dot(axis, vector) * (1 - cos_a)