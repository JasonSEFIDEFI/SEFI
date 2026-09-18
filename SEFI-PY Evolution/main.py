import numpy as np
from core.sefi_space import SEFISpace
from geometry.frenet import FrenetFrame
from sim.solver import DEFISolver
from sim.defi_integrator import DEFIIntegrator
from voxel.grid import VoxelGrid
from voxel.render import render_ascii_projection
from dna.encoder import DNAEncoder
from dna.mapping import sequence_to_curvature
from qec.syndrome import detect_syndrome

def main():
    print("==========================================")
    print("       SEFI-PY UNIFIED ENGINE START       ")
    print("==========================================")

    # 1. Core Space Initialization
    ss = SEFISpace()
    print(f"[+] SEFI Space Metric Initialized (4D diagonal)")

    # 2. DNA Encoding & Curvature Parameterization
    seq = "ATCGATCG"
    encoded_vecs = DNAEncoder.encode_sequence(seq)
    curvatures = sequence_to_curvature(encoded_vecs)
    print(f"[+] DNA Sequence '{seq}' encoded into {len(curvatures)} spatial states")

    # 3. Dynamic Integration
    frame = FrenetFrame(np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1]))
    integrator = DEFIIntegrator(initial_position=np.array([0.0, 0.0, 0.0]), frame=frame)
    solver = DEFISolver(integrator)

    trajectory = solver.solve(steps=20, kappa=curvatures[0], tau=0.05, dt=0.1, noise_std=0.02)
    print(f"[+] Trajectory generated ({len(trajectory)} points)")

    # 4. QEC Syndrome Evaluation
    syndrome = detect_syndrome(d_N=0.023, d_B=0.001)
    print(f"[+] QEC Status: {syndrome['error_type']} Error Detected")

    # 5. Voxel Discretization & ASCII Rendering
    grid = VoxelGrid(bounds=(-2, 2), resolution=12)
    grid.add_trajectory(trajectory)
    print("\n[+] 2D Voxel Density Projection:")
    print(render_ascii_projection(grid.grid))
    print("\n==========================================")
    print("       ENGINE EXECUTION COMPLETE          ")
    print("==========================================")

if __name__ == "__main__":
    main()