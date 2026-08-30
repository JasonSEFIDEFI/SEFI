# sefi-core/curvature.py
import numpy as np

def curvature_from_worldline(worldline, t: np.ndarray) -> np.ndarray:
    """
    Compute curvature κ(t) for a SEFIWorldline instance.
    """
    dt = t[1] - t[0]
    r = worldline.r(t)

    dr = np.gradient(r, dt, axis=0)
    d2r = np.gradient(dr, dt, axis=0)

    cross = np.cross(dr, d2r)
    num = np.linalg.norm(cross, axis=1)
    den = np.linalg.norm(dr, axis=1) ** 3
    return num / np.maximum(den, 1e-9)
