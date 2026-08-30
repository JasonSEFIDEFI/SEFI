# core/warp_expression.py

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
        """
        strength = self.sovereignty.sovereignty_strength()
        alignment = self.sovereignty.sovereignty_alignment()
        return blend(strength, alignment, 0.35)

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
