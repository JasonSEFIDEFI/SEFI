"""
stabilizers.py
--------------
Implements stabilizer checks for the 3‑qubit repetition code.

Stabilizers:
    Z1Z2
    Z2Z3

In SEFI-QEC, these represent sovereignty rules:
global invariants that detect local warp deviations.
"""

from .physical_qubits import PhysicalQubits


class StabilizerSet:
    def __init__(self):
        """
        Define the stabilizers for the 3‑qubit repetition code.
        """
        self.stabilizers = ["Z1Z2", "Z2Z3"]

    def check(self, physical_qubits: PhysicalQubits):
        """
        Check stabilizers by comparing physical qubits.

        For now, this is a placeholder:
        - If qubit[i] != qubit[j], mark stabilizer as violated (1)
        - If they match, mark stabilizer as satisfied (0)

        Returns:
            dict: {"Z1Z2": 0/1, "Z2Z3": 0/1}
        """
        q = physical_qubits.get_state()

        # Placeholder comparison: check if vectors differ
        z1z2 = 0 if q[0] == q[1] else 1
        z2z3 = 0 if q[1] == q[2] else 1

        return {"Z1Z2": z1z2, "Z2Z3": z2z3}
