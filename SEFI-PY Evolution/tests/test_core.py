from core.sefi_space import SEFISpace
import numpy as np

def test_sefi_metric_distance():
    ss = SEFISpace()
    v1 = np.array([1.0, 0.0, 0.0, 0.0])
    v2 = np.array([0.0, 0.0, 0.0, 0.0])
    assert ss.metric_distance(v1, v2) == 1.0