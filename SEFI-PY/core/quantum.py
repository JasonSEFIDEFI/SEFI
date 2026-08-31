import numpy as np

class QuantumState:
    """
    ψ: state over worldline + warp configuration.
    """

    def __init__(self, basis, amplitudes):
        self.basis = basis      # list of configs
        self.amplitudes = np.asarray(amplitudes)  # complex

    def normalize(self):
        norm = np.linalg.norm(self.amplitudes)
        if norm == 0:
            return
        self.amplitudes /= norm

class QuantumOperator:
    """
    Linear operator on QuantumState (Hamiltonian, warp operator, etc.).
    """

    def __init__(self, matrix):
        self.matrix = np.asarray(matrix, dtype=complex)

    def apply(self, state: QuantumState):
        return QuantumState(state.basis, self.matrix @ state.amplitudes)

class QuantumEvolution:
    """
    Time evolution: ψ(t) = U(t) ψ(0)
    """

    def __init__(self, H: QuantumOperator):
        self.H = H

    def propagate(self, state: QuantumState, dt):
        U = np.eye(len(state.amplitudes), dtype=complex) - 1j * self.H.matrix * dt
        return QuantumState(state.basis, U @ state.amplitudes)
import numpy as np
from sim.world import Worldline
from core.warp_expression import WarpProfile, WarpEngine

class WarpConfig:
    """
    One classical configuration: (worldline, warp_profile, λ).
    """

    def __init__(self, r_func, waveform, mode="tangent", lam=0.0):
        self.worldline = Worldline(r_func)
        self.warp = WarpProfile(waveform.phi, mode=mode)
        self.engine = WarpEngine(self.worldline, self.warp, lam=lam)

class QuantumState:
    """
    Superposition over warp configurations.
    """

    def __init__(self, configs, amplitudes):
        self.configs = configs
        self.amplitudes = np.asarray(amplitudes, dtype=complex)

    def normalize(self):
        norm = np.linalg.norm(self.amplitudes)
        if norm != 0:
            self.amplitudes /= norm

class QuantumOperator:
    """
    Linear operator on QuantumState.
    """

    def __init__(self, matrix):
        self.matrix = np.asarray(matrix, dtype=complex)

    def apply(self, state: QuantumState):
        amps_new = self.matrix @ state.amplitudes
        return QuantumState(state.configs, amps_new)

class QuantumEvolution:
    """
    ψ(t + dt) ≈ (I - i H dt) ψ(t)
    """

    def __init__(self, H: QuantumOperator):
        self.H = H

    def step(self, state: QuantumState, dt):
        I = np.eye(len(state.amplitudes), dtype=complex)
        U = I - 1j * self.H.matrix * dt
        amps_new = U @ state.amplitudes
        new_state = QuantumState(state.configs, amps_new)
        new_state.normalize()
        return new_state
def warp_hamiltonian(configs, t):
    """
    Build a diagonal Hamiltonian from curvature/torsion energy.
    """
    n = len(configs)
    H = np.zeros((n, n), dtype=complex)
    for i, cfg in enumerate(configs):
        k0, k1, t0, t1 = cfg.engine.response(t)
        energy = (k1 - k0)**2 + (t1 - t0)**2
        H[i, i] = energy
    return QuantumOperator(H)
import numpy as np

def collapse_to_classical(state: QuantumState):
    """
    Sample one warp configuration from |ψ|².
    """
    probs = np.abs(state.amplitudes)**2
    probs = probs / probs.sum()

    idx = np.random.choice(len(probs), p=probs)
    return state.configs[idx]
