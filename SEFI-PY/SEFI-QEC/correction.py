"""
correction.py
-------------
Applies correction based on extracted syndrome information.

In SEFI-QEC, correction is DEFI realignment:
restore the physical qubit's geometry to match the logical worldline.
"""

from .logical_worldline import LogicalWorldline
from .physical_qubits import PhysicalQubits


class Corrector:
    def __init__(self, logical_worldline: LogicalWorldline):
        """
        The logical worldline defines the stable configuration
        that physical qubits must be realigned to.
        """
        self.logical = logical_worldline

    def apply(self, physical_qubits: PhysicalQubits, syndrome_info: dict):
        """
        Apply correction based on syndrome information.

        syndrome_info:
            {
                "error_index": 0, 1, 2, or None
                "error_type": "X" or None
            }

        Correction strategy:
            - If error_index is None → nothing to correct
            - Otherwise → restore physical qubit to logical state
        """
        idx = syndrome_info.get("error_index")

        # No error detected
        if idx is None:
            return physical_qubits

        # Restore the qubit to the logical worldline state
        physical_qubits.qubits[idx] = self.logical.as_vector()[:]

        return physical_qubits
