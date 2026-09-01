"""
physical_qubits.py
------------------
Physical qubits for the 3-qubit repetition code.
"""

try:
    from .logical_worldline import LogicalWorldline
    from .pauli_ops import pauli_x, pauli_z, pauli_y
except ImportError:  # pragma: no cover - standalone compatibility
    from logical_worldline import LogicalWorldline
    from pauli_ops import pauli_x, pauli_z, pauli_y


class PhysicalQubits:
    def __init__(self, logical_worldline: LogicalWorldline):
        self.logical = logical_worldline
        self.qubits = [logical_worldline.as_vector()[:] for _ in range(3)]

    def inject_error(self, index: int, error_type: str):
        if error_type == "X":
            self.qubits[index] = pauli_x(self.qubits[index])
        elif error_type == "Z":
            self.qubits[index] = pauli_z(self.qubits[index])
        elif error_type == "Y":
            self.qubits[index] = pauli_y(self.qubits[index])
        else:
            raise ValueError("Error type must be X, Z, or Y.")

        return {"index": index, "type": error_type}

    def get_state(self):
        return self.qubits
