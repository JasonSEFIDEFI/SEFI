# core/warp_expression.py

import numpy as np
from utils.geometry import normalize, dot, magnitude
from utils.stability import blend, stable_ratio
from core.field_sovereignty import FieldSovereignty

class WarpExpression:
    """
    WARP:EXPRESSION:
    Dynamic expression of the sovereign field.
    This layer evolves the entity's identity through time,
    producing motion, behavior, and expressive geometry.
    """

    def __init__(self, sovereignty: FieldSovereignty):
        self.sovereignty = sovereignty

    def expression_vector(self):
        """
        The dynamic expression vector.
        Blends sovereignty vector with authored direction,
        weighted toward sovereignty (autonomy).
        """
        sov_vec = self.sovereignty.sovereignty_vector()
        auth_dir = self.sovereignty.authorship.authored_direction()
        return [blend(a, b, 0.6) for a, b in zip(sov_vec, auth_dir)]

    def expression_intensity(self):
        """
        Dynamic intensity of expression.
        Derived from sovereignty strength and sovereignty alignment.
        Maintain the sovereignty baseline so expressive dynamics do not reduce
        the already established field presence.
        """
        strength = self.sovereignty.sovereignty_strength()
        alignment = self.sovereignty.sovereignty_alignment()
        blended = blend(strength, alignment, 0.35)
        return max(strength, blended)

    def expression_alignment(self):
        """
        Alignment between expression vector and sovereignty vector.
        Measures how coherently the entity expresses its autonomous identity.
        """
        expr_vec = normalize(self.expression_vector())
        sov_vec = normalize(self.sovereignty.sovereignty_vector())
        return dot(expr_vec, sov_vec)

    def expression_ratio(self):
        """
        Stable ratio expressing how much dynamic expression
        amplifies or suppresses sovereignty.
        """
        expr_mag = magnitude(self.expression_vector())
        sov_mag = magnitude(self.sovereignty.sovereignty_vector())
        return stable_ratio(expr_mag, sov_mag)


class WarpProfile:
    """
    WarpProfile
    -----------
    Defines a SEFI warp field u(t) aligned to one of the
    Frenet–Serret directions: tangent, normal, or binormal.

    phi(t) is the scalar warp waveform.
    mode ∈ {"tangent", "normal", "binormal"} determines alignment.
    """

    def __init__(self, phi_func, mode="tangent"):
        """
        phi_func : callable(t) -> float
        mode     : "tangent", "normal", or "binormal"
        """
        self.phi = phi_func
        self.mode = mode.lower()

        if self.mode not in ("tangent", "normal", "binormal"):
            raise ValueError("WarpProfile mode must be tangent, normal, or binormal.")

    def u(self, worldline, t):
        """
        Compute the warp vector u(t) aligned to the chosen FS direction.
        """
        T, N, B = worldline.frenet_frame(t)

        if self.mode == "tangent":
            return self.phi(t) * T

        if self.mode == "normal":
            return self.phi(t) * N

        if self.mode == "binormal":
            return self.phi(t) * B


class WarpEngine:
    """
    WarpEngine
    ----------
    Applies a SEFI warp to a worldline using a WarpProfile.
    Produces warped curvature and torsion, enabling 5D control.

    r_lambda(t) = r(t) + λ * u(t)
    """

    def __init__(self, worldline, warp_profile, lam=0.0):
        """
        worldline     : Worldline object
        warp_profile  : WarpProfile object
        lam           : warp amplitude (5th-dimension control)
        """
        self.wl = worldline
        self.wp = warp_profile
        self.lam = lam

    # ---------------------------------------------------------
    # Warped worldline r_λ(t)
    # ---------------------------------------------------------
    def r_lambda(self, t):
        return self.wl.r(t) + self.lam * self.wp.u(self.wl, t)

    # ---------------------------------------------------------
    # Build a temporary worldline object for the warped curve
    # ---------------------------------------------------------
    def _wl_lambda(self):
        from sim.world import Worldline
        return Worldline(self.r_lambda)

    # ---------------------------------------------------------
    # Warped curvature κ_λ(t)
    # ---------------------------------------------------------
    def curvature_lambda(self, t):
        wl2 = self._wl_lambda()
        return wl2.curvature(t)

    # ---------------------------------------------------------
    # Warped torsion τ_λ(t)
    # ---------------------------------------------------------
    def torsion_lambda(self, t):
        wl2 = self._wl_lambda()
        return wl2.torsion(t)

    # ---------------------------------------------------------
    # Full warp response (κ, τ)
    # ---------------------------------------------------------
    def response(self, t):
        """
        Returns:
            (kappa_original, kappa_warped,
             torsion_original, torsion_warped)
        """
        k0 = self.wl.curvature(t)
        t0 = self.wl.torsion(t)

        k1 = self.curvature_lambda(t)
        t1 = self.torsion_lambda(t)

        return k0, k1, t0, t1
