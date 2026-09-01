"""
syndrome.py
-----------
Extracts error syndromes from stabilizer violations.

For the 3‑qubit repetition code:

    Z1Z2 = 1  → disagreement between qubit 1 and 2
    Z2Z3 = 1  → disagreement between qubit 2 and 3

Syndrome logic:
    - If only Z1Z2 violated → error on qubit 1
    - If only Z2Z3 violated → error on qubit 3
    - If both violated     → error on qubit 2
    - If none violated     → no error detected
"""

from .stabilizers import StabilizerSet
from .physical_qubits import PhysicalQubits


class SyndromeExtractor:
    def __init__(self, stabilizers: StabilizerSet):
        self.stabilizers = stabilizers

    def extract(self, physical_qubits: PhysicalQubits):
        """
        Extract syndrome information from stabilizer results.

        Returns:
            dict with:
                - error_index: 0, 1, 2, or None
                - error_type: placeholder ('X'), None if no error
        """
        s = self.stabilizers.check(physical_qubits)

        z12 = s["Z1Z2"]
        z23 = s["Z2Z3"]

        # No violations → no error
        if z12 == 0 and z23 == 0:
            return {"error_index": None, "error_type": None}

        # Only Z1Z2 violated → error on qubit 1
        if z12 == 1 and z23 == 0:
            return {"error_index": 0, "error_type": "X"}

        # Only Z2Z3 violated → error on qubit 3
        if z12 == 0 and z23 == 1:
            return {"error_index": 2, "error_type": "X"}

        # Both violated → error on qubit 2
        if z12 == 1 and z23 == 1:
            return {"error_index": 1, "error_type": "X"}

        # Fallback (should never happen)
        return {"error_index": None, "error_type": None}
