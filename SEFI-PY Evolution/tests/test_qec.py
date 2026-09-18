from qec.displacements import calculate_displacement
import numpy as np

def test_qec_displacement():
    pt = np.array([1.0, 1.0, 0.0])
    proj = np.array([1.0, 0.0, 0.0])
    N = np.array([0.0, 1.0, 0.0])
    B = np.array([0.0, 0.0, 1.0])
    dN, dB = calculate_displacement(pt, proj, N, B)
    assert dN == 1.0 and dB == 0.0