import numpy as np
from core.quantum import WarpConfig, QuantumState, warp_hamiltonian, QuantumEvolution, collapse_to_classical
from sim.sim_engine import TorsionWaveform
from utils.draw3d import draw_3d


def helix(t):
    return np.array([np.cos(t), np.sin(t), t])


def demo_quantum():
    tw1 = TorsionWaveform(mode="sin", amplitude=0.5, freq=3.0)
    tw2 = TorsionWaveform(mode="pulse", amplitude=1.0, center=1.0, width=0.2)

    configs = [
        WarpConfig(helix, tw1, mode="tangent", lam=0.1),
        WarpConfig(helix, tw2, mode="normal", lam=0.2)
    ]

    amps = np.array([1.0 + 0j, 0.0 + 0j])
    state = QuantumState(configs, amps)
    state.normalize()

    H = warp_hamiltonian(configs, t=1.0)
    evo = QuantumEvolution(H)

    state = evo.step(state, dt=0.01)

    classical_cfg = collapse_to_classical(state)
    draw_3d(classical_cfg.worldline)


if __name__ == "__main__":
    demo_quantum()
