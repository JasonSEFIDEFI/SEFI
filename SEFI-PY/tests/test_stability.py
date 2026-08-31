# tests/test_stability.py

from utils.stability import blend, stable_ratio


def test_blend():
    # midpoint blend
    assert blend(0.0, 1.0, 0.5) == 0.5

    # weighted blend
    # 2 * 0.75 + 4 * 0.25 = 1.5 + 1.0 = 2.5
    assert blend(2.0, 4.0, 0.25) == 2.5


def test_stable_ratio():
    # normal ratio
    assert stable_ratio(2.0, 1.0) > 1.0

    # zero denominator protection
    assert stable_ratio(0.0, 1.0) == 0.0
