# core/field_origin.py

from utils.geometry import magnitude, normalize, dot
from utils.stability import stable_ratio

class FieldOrigin:
    """
    FIELD ORIGIN:
    The foundational geometric state from which all SEFI field behavior emerges.
    It defines the raw position and momentum of the entity and provides
    primitive geometric measures used by higher layers.
    """

    def __init__(self, position, momentum):
        self.position = position
        self.momentum = momentum

    def origin_strength(self):
        """
        Strength is the magnitude of momentum.
        Represents raw geometric presence.
        """
        return magnitude(self.momentum)

    def origin_direction(self):
        """
        Direction is the normalized momentum vector.
        Represents the geometric orientation of the entity.
        """
        return normalize(self.momentum)

    def origin_alignment(self):
        """
        Alignment between position and momentum.
        Measures how coherently the entity's location and motion agree.
        """
        pos_dir = normalize(self.position)
        mom_dir = normalize(self.momentum)
        return dot(pos_dir, mom_dir)

    def origin_ratio(self):
        """
        Stable ratio between position magnitude and momentum magnitude.
        Used by higher layers to determine geometric balance.
        """
        pos_mag = magnitude(self.position)
        mom_mag = magnitude(self.momentum)
        return stable_ratio(pos_mag, mom_mag)
