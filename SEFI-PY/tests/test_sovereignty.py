from core.field_origin import FieldOrigin
from core.field_authorship import FieldAuthorship
from core.field_sovereignty import FieldSovereignty
from utils.geometry import magnitude

def test_sovereignty_vector_alignment():
    origin = FieldOrigin([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    authorship = FieldAuthorship(origin)
    sovereignty = FieldSovereignty(authorship)

    alignment = sovereignty.sovereignty_alignment()
    assert -1.0 <= alignment <= 1.0

def test_sovereignty_ratio():
    origin = FieldOrigin([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    authorship = FieldAuthorship(origin)
    sovereignty = FieldSovereignty(authorship)

    ratio = sovereignty.sovereignty_ratio()
    assert ratio >= 0.0
