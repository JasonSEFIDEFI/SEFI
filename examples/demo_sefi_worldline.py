# examples/demo_sefi_worldline.py
import numpy as np
from sefi_geometry.trajectory_generator import generate_sefi_trajectory
from sefi_voxel.phase_compiler import compile_phase_pattern
from sefi_voxel.device_interface import send_phase_sequence

def main():
    # Time settings
    t_start, t_end, dt = 0.0, 8.0, 0.005
    t, r = generate_sefi_trajectory(
        t_start=t_start,
        t_end=t_end,
        dt=dt,
        origin=np.array([0.0, 0.0, 0.0]),
        direction=np.array([0.0, 0.0, 1.0]),
        curvature_scale=1.5,
        torsion_scale=0.3
    )

    # Placeholder transducer geometry
    M = 32
    k_vectors = np.random.randn(M, 3)  # replace with real array geometry

    phases = compile_phase_pattern(r, k_vectors)

    # Send to hardware (replace 'COM3')
    send_phase_sequence(port='COM3', phases=phases)

if __name__ == "__main__":
    main()
