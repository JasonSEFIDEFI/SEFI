# sefi-core/layers.py
import numpy as np
from sefi_core.worldline import SEFIWorldline

def generate_layered_worldlines(t: np.ndarray,
                                layer_params: list[dict]) -> list[np.ndarray]:
    """
    Generate multiple SEFI worldlines for layered field constructs.
    layer_params: list of dicts with keys:
        origin, direction, curvature_scale, torsion_scale
    Returns: list of r_i(t) arrays, each (N, 3)
    """
    trajectories = []
    for params in layer_params:
        wl = SEFIWorldline(**params)
        trajectories.append(wl.r(t))
    return trajectories
