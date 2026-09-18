import numpy as np
from sim.defi_integrator import DEFIIntegrator
from geometry.frenet import FrenetFrame

class DEFISolver:
    """
    Batch trajectory solver over arbitrary time steps.
    """
    def __init__(self, integrator: DEFIIntegrator):
        self.integrator = integrator

    def solve(self, steps: int, kappa: float, tau: float, dt: float, noise_std: float = 0.0) -> np.ndarray:
        trajectory = []
        for _ in range(steps):
            pos = self.integrator.step(kappa, tau, dt, noise_std)
            trajectory.append(pos)
        return np.array(trajectory)