from core.field_origin import FieldOrigin
from core.field_authorship import FieldAuthorship
from core.field_sovereignty import FieldSovereignty
from core.warp_expression import WarpExpression
from core.warp_defi import WarpDEFI

def test_core_pipeline_values():
    origin = FieldOrigin([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    authorship = FieldAuthorship(origin)
    sovereignty = FieldSovereignty(authorship)
    expression = WarpExpression(sovereignty)
    defi = WarpDEFI(expression)

    assert origin.origin_strength() > 0
    assert authorship.authored_intensity() > 0
    assert sovereignty.sovereignty_strength() > 0
    assert expression.expression_intensity() > 0
    assert defi.defi_intensity() > 0
