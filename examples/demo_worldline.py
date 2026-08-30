# examples/demo_worldline.py
import numpy as np
from sefi_geometry.trajectory_generator import generate_trajectory
from sefi_voxel.phase_compiler import compile_phase_pattern
from sefi_voxel.device_interface import send_phase_sequence

def main():
    # Time settings
    t_start, t_end, dt = 0.0, 10.0, 0.01
    t, r = generate_trajectory(t_start, t_end, dt)

    # Example transducer wave vectors (placeholder)
    M = 16
    k_vectors = np.random.randn(M, 3)  # replace with real geometry

    phases = compile_phase_pattern(r, k_vectors)

    # Send to hardware (replace 'COM3' with actual port)
    send_phase_sequence(port='COM3', phases=phases)

if __name__ == "__main__":
    main()
