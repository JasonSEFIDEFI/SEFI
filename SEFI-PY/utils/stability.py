import numpy as np
from sim.world import Worldline


# ---------------------------------------------------------
# Basic stability helpers
# ---------------------------------------------------------

def clamp(value, low, high):
    """
    Clamp value into [low, high].
    """
    return max(low, min(value, high))


def stable_ratio(a, b, eps=1e-9):
    """
    Return a numerically stable ratio a/b with epsilon protection.
    Prevents blow-ups when b → 0.
    """
    return a / (b if abs(b) > eps else eps)


def blend(a, b, t):
    """
    Linear blend between a and b with clamped t ∈ [0, 1].
    """
    t = clamp(t, 0.0, 1.0)
    return (1 - t) * a + t * b


# ---------------------------------------------------------
# Worldline + warp stability helpers
# ---------------------------------------------------------

def acceleration_norm(worldline, t):
    """
    Return ||a(t)|| for a given worldline.
    """
    return np.linalg.norm(worldline.a(t))


def warp_stability(engine, t, max_increase=1.0):
    """
    Check that warp does not blow up acceleration too much at t.

    engine.wl      : original worldline
    engine.r_lambda: warped worldline function

    Returns True if:
        ||a_warp(t)|| <= ||a_orig(t)|| + max_increase
    """
    wl_orig = engine.wl
    wl_warp = Worldline(engine.r_lambda)

    a0 = np.linalg.norm(wl_orig.a(t))
    a1 = np.linalg.norm(wl_warp.a(t))

    return a1 <= a0 + max_increase
