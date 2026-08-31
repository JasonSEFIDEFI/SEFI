# sim/entity.py

from core.field_origin import FieldOrigin
from core.field_authorship import FieldAuthorship
from core.field_sovereignty import FieldSovereignty
from core.warp_expression import WarpExpression
from core.warp_defi import WarpDEFI

from sim.evolution import evolve_position, evolve_momentum
from sim.behavior import apply_behavior


class Entity:
    def __init__(self, position, momentum):
        """
        Basic SEFI-PY entity:
        - origin
        - authorship
        - sovereignty
        - expression
        - DEFI
        """
        self.origin = FieldOrigin(position, momentum)
        self.authorship = FieldAuthorship(self.origin)
        self.sovereignty = FieldSovereignty(self.authorship)
        self.expression = WarpExpression(self.sovereignty)
        self.defi = WarpDEFI(self.expression)

    def step(self, dt=0.1):
        """
        Full SEFI evolution step:
        1. Behavior layer (DEFI-driven)
        2. Momentum evolution
        3. Position evolution
        4. Rebuild SEFI layers after state change
        """
        apply_behavior(self, dt)
        evolve_momentum(self, dt)
        evolve_position(self, dt)

        # rebuild layers after evolution
        self.authorship = FieldAuthorship(self.origin)
        self.sovereignty = FieldSovereignty(self.authorship)
        self.expression = WarpExpression(self.sovereignty)
        self.defi = WarpDEFI(self.expression)
