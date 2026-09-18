import numpy as np
from geometry.frenet import FrenetFrame
from qec.displacements import calculate_displacement
from qec.projection import project_to_manifold

class DEFIIntegrator:
    """
    Dynamical entity field integrator combining geometry and QEC projection.
    """
    def __init__(self, initial_position: np.ndarray, frame: FrenetFrame):
        self.pos = np.array(initial_position, dtype=float)
        self.frame = frame

    def step(self, kappa: float, tau: float, dt: float, noise_std: float = 0.0):
        # Forward geometric motion
        self.pos += self.frame.T * dt
        self.frame.step(kappa, tau, dt)
        
        # Inject perturbation noise if enabled
        if noise_std > 0:
            noise = np.random.normal(0, noise_std, size=3)
            self.pos += noise
            
            # Perform geometric correction mapping back onto the stability manifold
            d_N, d_B = calculate_displacement(self.pos, self.pos - noise, self.frame.N, self.frame.B)
            self.pos = project_to_manifold(self.pos, self.frame.N, self.frame.B, d_N, d_B)

        return self.pos.copy()