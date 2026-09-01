"""
stabilizers.py
--------------
Real stabilizer parity checks for the 3-qubit repetition code.
"""

from .physical_qubits import PhysicalQubits


def z_parity(q1, q2):
    """
    Z-parity:
        +1 (syndrome 0) if states match (00 or 11)
        -1 (syndrome 1) if states differ (01 or 10)
    """
    return 0 if q1 == q2 else 1


class StabilizerSet:
    def __init__(self):
        self.stabilizers = ["Z1Z2", "Z2Z3"]

    def check(self, physical_qubits: PhysicalQubits):
        q = physical_qubits.get_state()
        return {
            "Z1Z2": z_parity(q[0], q[1]),
            "Z2Z3": z_parity(q[1], q[2])
        }
