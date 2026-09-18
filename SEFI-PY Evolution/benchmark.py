import time
import numpy as np
from geometry.frenet import FrenetFrame
from sim.defi_integrator import DEFIIntegrator

def run_benchmark():
    frame = FrenetFrame(np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1]))
    integrator = DEFIIntegrator(np.array([0,0,0]), frame)
    
    start_time = time.time()
    for _ in range(10000):
        integrator.step(kappa=0.1, tau=0.05, dt=0.01, noise_std=0.001)
    end_time = time.time()
    
    print(f"Benchmark: Executed 10,000 DEFI integration steps in {end_time - start_time:.4f} seconds.")

if __name__ == "__main__":
    run_benchmark()