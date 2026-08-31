from utils.geometry import normalize, dot, magnitude

def test_normalize_vector():
    v = [3.0, 4.0, 0.0]
    n = normalize(v)
    assert round(magnitude(n), 5) == 1.0

def test_dot_product():
    assert dot([1, 0, 0], [1, 0, 0]) == 1
    assert dot([1, 0, 0], [0, 1, 0]) == 0

def test_magnitude():
    assert magnitude([3, 4, 0]) == 5
import numpy as np
from sim.world import Worldline
from core.warp_expression import WarpProfile, WarpEngine
from sim.sim_engine import TorsionWaveform

# ---------------------------------------------------------
# Simple test worldline: helix
# r(t) = (cos t, sin t, t)
# ---------------------------------------------------------
def helix(t):
    return np.array([np.cos(t), np.sin(t), t])

wl = Worldline(helix)

# ---------------------------------------------------------
# Test 1: Tangent warp preserves curvature
# ---------------------------------------------------------
def test_tangent_warp_preserves_curvature():
    tw = TorsionWaveform(mode="sin", amplitude=0.5, freq=3)
    warp = WarpProfile(tw.phi, mode="tangent")
    engine = WarpEngine(wl, warp, lam=0.01)

    t = 1.0
    k0 = wl.curvature(t)
    k1 = engine.curvature_lambda(t)

    # Curvature should be preserved to first order
    assert np.isclose(k0, k1, atol=1e-3)

# ---------------------------------------------------------
# Test 2: Tangent warp modulates torsion
# ---------------------------------------------------------
def test_tangent_warp_modulates_torsion():
    tw = TorsionWaveform(mode="sin", amplitude=1.0, freq=5)
    warp = WarpProfile(tw.phi, mode="tangent")
    engine = WarpEngine(wl, warp, lam=0.1)

    t = 1.0
    t0 = wl.torsion(t)
    t1 = engine.torsion_lambda(t)

    # Torsion should change under tangent warp
    assert not np.isclose(t0, t1, atol=1e-3)

# ---------------------------------------------------------
# Test 3: Normal warp changes curvature
# ---------------------------------------------------------
def test_normal_warp_changes_curvature():
    tw = TorsionWaveform(mode="pulse", amplitude=1.0, center=1.0, width=0.2)
    warp = WarpProfile(tw.phi, mode="normal")
    engine = WarpEngine(wl, warp, lam=0.1)

    t = 1.0
    k0 = wl.curvature(t)
    k1 = engine.curvature_lambda(t)

    # Normal warp should modify curvature
    assert not np.isclose(k0, k1, atol=1e-3)

# ---------------------------------------------------------
# Test 4: Binormal warp changes torsion strongly
# ---------------------------------------------------------
def test_binormal_warp_changes_torsion():
    tw = TorsionWaveform(mode="chirp", amplitude=0.8, freq=2)
    warp = WarpProfile(tw.phi, mode="binormal")
    engine = WarpEngine(wl, warp, lam=0.1)

    t = 1.0
    t0 = wl.torsion(t)
    t1 = engine.torsion_lambda(t)

    # Binormal warp should significantly modify torsion
    assert abs(t1 - t0) > 1e-3

# ---------------------------------------------------------
# Test 5: Warp amplitude λ behaves like a 5D control axis
# ---------------------------------------------------------
def test_lambda_controls_warp_strength():
    tw = TorsionWaveform(mode="sin", amplitude=1.0, freq=4)
    warp = WarpProfile(tw.phi, mode="tangent")

    engine_small = WarpEngine(wl, warp, lam=0.01)
    engine_large = WarpEngine(wl, warp, lam=0.2)

    t = 1.0
    torsion_small = engine_small.torsion_lambda(t)
    torsion_large = engine_large.torsion_lambda(t)

    # Larger λ should produce larger torsion deviation
    assert abs(torsion_large - wl.torsion(t)) > abs(torsion_small - wl.torsion(t))
