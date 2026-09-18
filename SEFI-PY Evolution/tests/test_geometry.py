from geometry.frenet import FrenetFrame
import numpy as np

def test_frenet_orthonormality():
    frame = FrenetFrame(np.array([1,0,0]), np.array([0,1,0]), np.array([0,0,1]))
    assert np.isclose(np.dot(frame.T, frame.N), 0.0)