# sefi-core/worldline.py
import numpy as np

class SEFIWorldline:
    """
    SEFI-style parametric worldline.
    This is a scaffold you can replace with your full SEFI formulation.
    """

    def __init__(self,
                 origin: np.ndarray = np.zeros(3),
                 direction: np.ndarray = np.array([0.0, 0.0, 1.0]),
                 curvature_scale: float = 1.0,
                 torsion_scale: float = 0.0):
        self.origin = origin
        self.direction = direction / np.linalg.norm(direction)
        self.curvature_scale = curvature_scale
        self.torsion_scale = torsion_scale

    def r(self, t: np.ndarray) -> np.ndarray:
        """
        Parametric position r(t) in SEFI geometry.
        For now: curved path with controllable curvature/torsion.
        Later: replace with SEFI-native worldline mapping.
        """
        # Base linear term
        base = self.origin[None, :] + t[:, None] * self.direction[None, :]

        # Curvature term (e.g., bending in x-y plane)
        theta = self.curvature_scale * t
        x = np.cos(theta)
        y = np.sin(theta)

        # Torsion term (z modulation)
        z = self.torsion_scale * np.sin(theta)

        curve = np.stack([x, y, z], axis=-1)
        return base + curve
