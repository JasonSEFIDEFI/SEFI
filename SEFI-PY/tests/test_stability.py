from utils.stability import blend, stable_ratio

def test_blend():
    assert blend(0.0, 1.0, 0.5) == 0.5
    assert blend(2.0, 4.0, 0.25) == 2.5

def test_stable_ratio():
    assert stable_ratio(2.0, 1.0) > 1.0
    assert stable_ratio(0.0, 1.0) == 0.0
