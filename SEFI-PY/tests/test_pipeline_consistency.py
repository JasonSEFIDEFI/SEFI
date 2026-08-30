from core.field_origin import FieldOrigin
from core.field_authorship import FieldAuthorship
from core.field_sovereignty import FieldSovereignty
from core.warp_expression import WarpExpression
from core.warp_defi import WarpDEFI

def test_pipeline_consistency():
    origin = FieldOrigin([1.0, 0.0, 0.0], [0.5, 0.5, 0.0])
    authorship = FieldAuthorship(origin)
    sovereignty = FieldSovereignty(authorship)
    expression = WarpExpression(sovereignty)
    defi = WarpDEFI(expression)

    # pipeline ordering must be monotonic
    o = origin.origin_strength()
    a = authorship.authored_intensity()
    s = sovereignty.sovereignty_strength()
    e = expression.expression_intensity()
    d = defi.defi_intensity()

    assert a >= o
    assert s >= a
    assert e >= s
    assert d >= e
