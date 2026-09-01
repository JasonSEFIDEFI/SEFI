"""
physical_qubits.py
------------------
Implements the 3‑qubit repetition code physical layer.

Each physical qubit is a sample of the logical worldline.
Errors are modeled as local warp deviations (X, Z, Y).
"""

from .logical_worldline import LogicalWorldline


class PhysicalQubits:
    def __init__(self, logical_worldline: LogicalWorldline):
        """
        Encode the logical worldline into 3 physical qubits.
        Each physical qubit starts as a copy of the logical state vector.
        """
        self.logical = logical_worldline
        self.qubits = [logical_worldline.as_vector()[:] for _ in range(3)]

    def inject_error(self, index: int, error_type: str):
        """
        Inject an error into one of the physical qubits.

        error_type: 'X', 'Z', or 'Y'
        index: which qubit (0, 1, or 2)
        """
        if index not in [0, 1, 2]:
            raise ValueError("Physical qubit index must be 0, 1, or 2.")

        if error_type not in ["X", "Z", "Y"]:
            raise ValueError("Error type must be 'X', 'Z', or 'Y'.")

        # Placeholder: mark the error for syndrome extraction
        return {"index": index, "type": error_type}

    def get_state(self):
        """
        Returns the list of physical qubit state vectors.
        """
        return self.qubits
