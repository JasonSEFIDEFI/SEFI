from core.field_origin import FieldOrigin
from core.field_authorship import FieldAuthorship
from core.field_sovereignty import FieldSovereignty
from core.warp_expression import WarpExpression
from core.warp_defi import WarpDEFI

def demo():
    origin = FieldOrigin([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    authorship = FieldAuthorship(origin)
    sovereignty = FieldSovereignty(authorship)
    expression = WarpExpression(sovereignty)
    defi = WarpDEFI(expression)

    print("ORIGIN strength:", origin.origin_strength())
    print("AUTHORSHIP intensity:", authorship.authored_intensity())
    print("SOVEREIGNTY strength:", sovereignty.sovereignty_strength())
    print("EXPRESSION intensity:", expression.expression_intensity())
    print("DEFI intensity:", defi.defi_intensity())

if __name__ == "__main__":
    demo()

from sim.sim_engine import run_sim

if __name__ == "__main__":
    demo()      # your existing demo
    run_sim()   # SEFI-SIM starts here

from sim.sim_engine import run_sim

if __name__ == "__main__":
    run_sim()
