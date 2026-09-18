import numpy as np

def generate_helix(t_range: np.ndarray, radius: float = 1.0, pitch: float = 0.5):
    """
    Generates a 3D helical parametric curve: r(t) = [R*cos(t), R*sin(t), P*t]
    """
    x = radius * np.cos(t_range)
    y = radius * np.sin(t_range)
    z = pitch * t_range
    return np.column_stack([x, y, z])

def calculate_curvature_torsion(radius: float, pitch: float):
    """
    Analytic curvature (kappa) and torsion (tau) for a standard helix.
    """
    denom = radius**2 + pitch**2
    kappa = radius / denom
    tau = pitch / denom
    return kappa, tau