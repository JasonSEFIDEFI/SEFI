# core/warp_defi.py

from utils.geometry import normalize, dot, magnitude
from utils.stability import blend, stable_ratio
from core.warp_expression import WarpExpression

class WarpDEFI:
    """
    WARP:DEFI:
    Dynamic Entity Field Integration.
    The highest SEFI layer, where the entity actively manipulates
    its own field geometry. This layer integrates expression into
    actionable geometric behavior.
    """

    def __init__(self, expression: WarpExpression):
        self.expression = expression

    def defi_vector(self):
        """
        The integrated field vector.
        Blends expression vector with sovereignty vector,
        weighted toward expression (dynamic behavior).
        """
        expr_vec = self.expression.expression_vector()
        sov_vec = self.expression.sovereignty.sovereignty_vector()
        return [blend(s, e, 0.65) for s, e in zip(sov_vec, expr_vec)]

    def defi_intensity(self):
        """
        Integrated intensity of the field.
        Derived from:
        - expression intensity
        - expression alignment
        """
        intensity = self.expression.expression_intensity()
        alignment = self.expression.expression_alignment()
        return blend(intensity, alignment, 0.45)

    def defi_alignment(self):
        """
        Alignment between DEFI vector and expression vector.
        Measures how coherently the entity integrates its dynamic behavior.
        """
        defi_vec = normalize(self.defi_vector())
        expr_vec = normalize(self.expression.expression_vector())
        return dot(defi_vec, expr_vec)

    def defi_ratio(self):
        """
        Stable ratio expressing how much DEFI amplifies or suppresses
        dynamic expression relative to sovereignty.
        """
        defi_mag = magnitude(self.defi_vector())
        expr_mag = magnitude(self.expression.expression_vector())
        return stable_ratio(defi_mag, expr_mag)
