import numpy as np
from sim.sim_engine import TorsionWaveform, run_torsion_sim


def helix(t):
    return np.array([np.cos(t), np.sin(t), t])


def demo_warp():
    tw = TorsionWaveform(mode="sin", amplitude=0.5, freq=3.0)
    run_torsion_sim(helix, tw, mode="tangent", lam=0.1,
                    t_min=0.0, t_max=10.0)


if __name__ == "__main__":
    demo_warp()
