# sim/sim_engine.py

from config import SIM_CONFIG, ENTITY_CONFIGS

from sim.world import World
from sim.entity import Entity

from core.warp_expression import WarpProfile, WarpEngine
from sim.world import Worldline
from utils.plot import plot_response

import numpy as np


# ---------------------------------------------------------
# Main SEFI-SIM engine (entity-level field evolution)
# ---------------------------------------------------------

def run_sim():
    """
    Run a SEFI-SIM world with entities defined in ENTITY_CONFIGS
    and environment parameters from SIM_CONFIG.
    """
    world = World(
        global_field=SIM_CONFIG["global_field"],
        boundary_radius=SIM_CONFIG["boundary_radius"],
        ambient_intensity=SIM_CONFIG["ambient_intensity"]
    )

    # build entities from config
    for cfg in ENTITY_CONFIGS:
        e = Entity(
            position=cfg["position"],
            momentum=cfg["momentum"]
        )
        world.add(e)

    print("\n--- SEFI-SIM ---")

    for i in range(SIM_CONFIG["steps"]):
        world.step(SIM_CONFIG["dt"])
        print(f"Step {i+1}:")
        for idx, e in enumerate(world.entities):
            print(f"  E{idx+1} Pos={e.origin.position}, Mom={e.origin.momentum}")


# ---------------------------------------------------------
# Torsion waveform + warp response simulation
# ---------------------------------------------------------

class TorsionWaveform:
    """
    TorsionWaveform
    ----------------
    Defines φ(t), the torsion-driving scalar waveform used by WarpProfile.
    This is the 5th-dimension control signal.

    Supports:
        - sinusoidal ("sin")
        - pulse (Gaussian) ("pulse")
        - chirp (frequency sweep) ("chirp")
        - custom callable ("custom")
    """

    def __init__(self, mode="sin", amplitude=1.0, freq=1.0,
                 center=0.0, width=1.0, custom=None):
        """
        mode     : "sin", "pulse", "chirp", or "custom"
        amplitude: waveform amplitude
        freq     : frequency (for sin/chirp)
        center   : pulse center (for pulse)
        width    : pulse width (for pulse)
        custom   : callable(t) -> float (for custom mode)
        """
        self.mode = mode
        self.A = amplitude
        self.f = freq
        self.c = center
        self.w = width
        self.custom = custom

    def phi(self, t):
        if self.mode == "sin":
            return self.A * np.sin(self.f * t)

        if self.mode == "pulse":
            return self.A * np.exp(-((t - self.c) ** 2) / (2 * self.w ** 2))

        if self.mode == "chirp":
            return self.A * np.sin(self.f * t ** 2)

        if self.mode == "custom":
            if self.custom is None:
                raise ValueError("Custom waveform requires a callable.")
            return self.custom(t)

        raise ValueError("Invalid waveform mode.")


def run_torsion_sim(r_func, waveform, mode="tangent", lam=0.1,
                    t_min=0.0, t_max=10.0, n=500):
    """
    Run a torsion/curvature warp simulation on a single worldline.

    r_func   : callable(t) -> R^3, base worldline
    waveform : TorsionWaveform instance
    mode     : "tangent", "normal", "binormal"
    lam      : warp amplitude
    t_min    : start time
    t_max    : end time
    n        : number of samples
    """
    wl = Worldline(r_func)
    warp = WarpProfile(waveform.phi, mode=mode)
    engine = WarpEngine(wl, warp, lam=lam)
    plot_response(wl, engine, t_min=t_min, t_max=t_max, n=n)
