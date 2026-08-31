import numpy as np
from core.quantum import WarpConfig, QuantumState, warp_hamiltonian, QuantumEvolution
from sim.sim_engine import TorsionWaveform

def helix(t):
    return np.array([np.cos(t), np.sin(t), t])

def test_quantum_warp_evolution():
    tw1 = TorsionWaveform(mode="sin", amplitude=0.5, freq=3.0)
    tw2 = TorsionWaveform(mode="pulse", amplitude=1.0, center=1.0, width=0.2)

    cfg1 = WarpConfig(helix, tw1, mode="tangent", lam=0.1)
    cfg2 = WarpConfig(helix, tw2, mode="normal", lam=0.2)

    configs = [cfg1, cfg2]
    amps = np.array([1.0 + 0j, 0.0 + 0j])
    state = QuantumState(configs, amps)
    state.normalize()

    H = warp_hamiltonian(configs, t=1.0)
    evo = QuantumEvolution(H)

    state2 = evo.step(state, dt=0.01)

    # amplitudes should change but remain normalized
    assert not np.allclose(state2.amplitudes, state.amplitudes)
    assert np.isclose(np.linalg.norm(state2.amplitudes), 1.0, atol=1e-6)
