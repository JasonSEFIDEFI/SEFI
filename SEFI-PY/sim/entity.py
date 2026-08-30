# sim/entity.py

from core.field_origin import FieldOrigin
from core.field_authorship import FieldAuthorship
from core.field_sovereignty import FieldSovereignty
from core.warp_expression import WarpExpression
from core.warp_defi import WarpDEFI

class Entity:
    def __init__(self, position, momentum):
        self.origin = FieldOrigin(position, momentum)
        self.authorship = FieldAuthorship(self.origin)
        self.sovereignty = FieldSovereignty(self.authorship)
        self.expression = WarpExpression(self.sovereignty)
        self.defi = WarpDEFI(self.expression)

   from sim.evolution import evolve_position, evolve_momentum

from sim.evolution import evolve_position, evolve_momentum
from sim.behavior import apply_behavior

def step(self, dt=0.1):
    apply_behavior(self, dt)     # new behavioral layer
    evolve_momentum(self, dt)    # geometric evolution
    evolve_position(self, dt)    # spatial evolution

    # rebuild layers after evolution
    self.authorship = FieldAuthorship(self.origin)
    self.sovereignty = FieldSovereignty(self.authorship)
    self.expression = WarpExpression(self.sovereignty)
    self.defi = WarpDEFI(self.expression)


class Entity:
    def __init__(self, dna: EntityDNA):
        self.dna = dna

        self.origin = FieldOrigin(dna.position, dna.momentum)
        self.authorship = FieldAuthorship(self.origin)
        self.sovereignty = FieldSovereignty(self.authorship, bias=dna.sovereignty_bias)
        self.expression = WarpExpression(self.sovereignty, bias=dna.expression_bias)
        self.defi = WarpDEFI(self.expression, bias=dna.defi_bias)
from sim.evolution import evolve_position, evolve_momentum
from sim.behavior import apply_behavior

