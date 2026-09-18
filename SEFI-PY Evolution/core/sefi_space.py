import numpy as np
from core.constants import DEFAULT_ALPHA, DEFAULT_BETA, DEFAULT_GAMMA, DEFAULT_DELTA

class SEFISpace:
    """
    4D SEFI Space (SS) parameterizing Origin, Authorship, Sovereignty, and Warp dynamics.
    """
    def __init__(self, alpha=DEFAULT_ALPHA, beta=DEFAULT_BETA, gamma=DEFAULT_GAMMA, delta=DEFAULT_DELTA):
        self.metric = np.diag([alpha, beta, gamma, delta])

    def layer_field(self, O_val: float, A_val: float, S_val: float, W_val: float, kappa: float = 1.0) -> float:
        """
        Calculates SEFI Layered Field Identity:
        F(t) = O(r) + A(r, kappa) + S(r) + W(r)
        """
        return O_val + (A_val * kappa) + S_val + W_val

    def metric_distance(self, v1: np.ndarray, v2: np.ndarray) -> float:
        """
        Calculates interval ds^2 = diff^T * G * diff in SEFI Space.
        """
        diff = np.array(v1) - np.array(v2)
        return float(np.dot(diff.T, np.dot(self.metric, diff)))