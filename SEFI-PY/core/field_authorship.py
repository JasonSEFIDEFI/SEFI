# core/field_authorship.py

from utils.geometry import normalize, dot
from utils.stability import blend
from core.field_origin import FieldOrigin

class FieldAuthorship:
    """
    FIELD AUTHORSHIP:
    The layer where the entity expresses its geometric identity.
    It transforms origin data into communicable field structure.
    """

    def __init__(self, origin: FieldOrigin):
        self.origin = origin

    def authored_direction(self):
        """
        A refined direction that blends raw origin direction
        with positional influence.
        This expresses the entity's chosen geometric identity.
        """
        raw_dir = self.origin.origin_direction()
        pos_dir = normalize(self.origin.position)
        return [blend(r, p, 0.5) for r, p in zip(raw_dir, pos_dir)]

    def authored_intensity(self):
        """
        Intensity is derived from how aligned the position and momentum are.
        This expresses how strongly the entity asserts its identity.
        """
        raw_dir = self.origin.origin_direction()
        pos_dir = normalize(self.origin.position)
        alignment = dot(raw_dir, pos_dir)

        # Blend raw strength with alignment for expressive intensity
        return blend(self.origin.origin_strength(), alignment, 0.25)

    def authored_alignment(self):
        """
        Expressed alignment between authored direction and origin direction.
        This measures how coherently the entity expresses its identity.
        """
        raw_dir = self.origin.origin_direction()
        auth_dir = self.authored_direction()
        return dot(raw_dir, auth_dir)
