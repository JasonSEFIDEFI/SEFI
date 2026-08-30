# sefi-geometry/trajectory_generator.py
import numpy as np
from sefi_core.worldline import helix_worldline

def generate_trajectory(t_start: float,
                        t_end: float,
                        dt: float) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate a time-stamped trajectory from SEFI worldline.
    Returns (t, r) where:
      t: (N,) time samples
      r: (N, 3) positions
    """
    t = np.arange(t_start, t_end, dt)
    r = helix_worldline(t)
    return t, r
