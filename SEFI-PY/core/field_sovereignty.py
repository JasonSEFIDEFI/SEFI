# core/field_sovereignty.py

from utils.geometry import normalize, dot, magnitude
from utils.stability import blend, stable_ratio
from core.field_authorship import FieldAuthorship

class FieldSovereignty:
    """
    FIELD SOVEREIGNTY:
    Autonomous persistence and geometric self-governance.
    This layer stabilizes authored identity into a durable field presence.
    """

    def __init__(self, authorship: FieldAuthorship):
        self.authorship = authorship

    def sovereignty_vector(self):
        """
        A stabilized vector representing persistent identity.
        Blends origin direction with authored direction,
        weighted toward authored identity.
        """
        origin_dir = self.authorship.origin.origin_direction()
        authored_dir = self.authorship.authored_direction()
        return [blend(o, a, 0.7) for o, a in zip(origin_dir, authored_dir)]

    def sovereignty_strength(self):
        """
        Sovereignty strength is based on:
        - authored intensity
        - stability of alignment between origin and authored direction
        """
        authored_intensity = self.authorship.authored_intensity()

        origin_dir = self.authorship.origin.origin_direction()
        authored_dir = self.authorship.authored_direction()
        alignment = dot(origin_dir, authored_dir)

        return blend(authored_intensity, alignment, 0.4)

    def sovereignty_alignment(self):
        """
        Alignment between sovereignty vector and authored direction.
        Measures how coherently the entity maintains its identity.
        """
        sov_vec = self.sovereignty_vector()
        auth_dir = self.authorship.authored_direction()
        return dot(normalize(sov_vec), normalize(auth_dir))

    def sovereignty_ratio(self):
        """
        A stable ratio expressing how much the entity's authored identity
        governs its origin identity.
        """
        origin_mag = magnitude(self.authorship.origin.momentum)
        authored_mag = magnitude(self.authorship.authored_direction())
        return stable_ratio(authored_mag, origin_mag)
# tests/test_core.py

from core.field_origin import FieldOrigin
from core.field_authorship import FieldAuthorship
from core.field_sovereignty import FieldSovereignty
from core.warp_expression import WarpExpression
from core.warp_defi import WarpDEFI

def test_core_pipeline():
    origin = FieldOrigin([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    authorship = FieldAuthorship(origin)
    sovereignty = FieldSovereignty(authorship)
    expression = WarpExpression(sovereignty)
    defi = WarpDEFI(expression)

    o = origin.origin_strength()
    a = authorship.authored_intensity()
    s = sovereignty.sovereignty_strength()
    e = expression.expression_intensity()
    d = defi.defi_intensity()

    assert o > 0
    assert a > 0
    assert s > 0
    assert e > 0
    assert d > 0

    assert a >= o
    assert s >= a
    assert e >= s
    assert d >= e

    print("Core pipeline with sovereignty OK")
