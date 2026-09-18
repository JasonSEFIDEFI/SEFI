import numpy as np

class FrenetFrame:
    """
    GWFM Worldline Frenet-Serret System:
    dT/dt = kappa * N
    dN/dt = -kappa * T + tau * B
    dB/dt = -tau * N
    """
    def __init__(self, T: np.ndarray, N: np.ndarray, B: np.ndarray):
        self.T = T / np.linalg.norm(T)
        self.N = N / np.linalg.norm(N)
        self.B = B / np.linalg.norm(B)

    def derivatives(self, kappa: float, tau: float):
        dT = kappa * self.N
        dN = -kappa * self.T + tau * self.B
        dB = -tau * self.N
        return dT, dN, dB

    def step(self, kappa: float, tau: float, dt: float):
        dT, dN, dB = self.derivatives(kappa, tau)
        self.T = self.T + dT * dt
        self.N = self.N + dN * dt
        self.B = self.B + dB * dt
        # Re-orthonormalize frame
        self.T /= np.linalg.norm(self.T)
        self.N /= np.linalg.norm(self.N)
        self.B /= np.linalg.norm(self.B)