# sefi-geometry/trajectory_generator.py
import numpy as np
from sefi_core.worldline import SEFIWorldline

def generate_sefi_trajectory(t_start: float,
                             t_end: float,
                             dt: float,
                             origin=None,
                             direction=None,
                             curvature_scale: float = 1.0,
                             torsion_scale: float = 0.0):
    """
    Generate a SEFI-style trajectory from a parametric worldline.
    Returns (t, r) where:
      t: (N,) time samples
      r: (N, 3) positions
    """
    t = np.arange(t_start, t_end, dt)

    if origin is None:
        origin = np.zeros(3)
    if direction is None:
        direction = np.array([0.0, 0.0, 1.0])

    wl = SEFIWorldline(origin=origin,
                       direction=direction,
                       curvature_scale=curvature_scale,
                       torsion_scale=torsion_scale)

    r = wl.r(t)
    return t, r
