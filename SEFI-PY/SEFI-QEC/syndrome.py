"""
syndrome.py
-----------
Extracts error syndromes from stabilizer violations.
"""

try:
    from .stabilizers import StabilizerSet
    from .physical_qubits import PhysicalQubits
except ImportError:  # pragma: no cover - standalone compatibility
    from stabilizers import StabilizerSet
    from physical_qubits import PhysicalQubits


class SyndromeExtractor:
    def __init__(self, stabilizers: StabilizerSet):
        self.stabilizers = stabilizers

    def extract(self, physical_qubits: PhysicalQubits):
        s = self.stabilizers.check(physical_qubits)

        z12 = s["Z1Z2"]
        z23 = s["Z2Z3"]

        if z12 == 0 and z23 == 0:
            return {"error_index": None, "error_type": None}
        if z12 == 1 and z23 == 0:
            return {"error_index": 0, "error_type": "X"}
        if z12 == 0 and z23 == 1:
            return {"error_index": 2, "error_type": "X"}
        if z12 == 1 and z23 == 1:
            return {"error_index": 1, "error_type": "X"}

        return {"error_index": None, "error_type": None}
