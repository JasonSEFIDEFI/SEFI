from sim.defi_integrator import DEFIIntegrator
from geometry.frenet import FrenetFrame
import numpy as np

def test_integrator_step():
    frame = FrenetFrame(np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1]))
    integrator = DEFIIntegrator(np.array([0,0,0]), frame)
    new_pos = integrator.step(kappa=0.1, tau=0.1, dt=1.0)
    assert new_pos[0] > 0