"""
correction.py
-------------
Correction = DEFI realignment.
"""

try:
    from .logical_worldline import LogicalWorldline
    from .physical_qubits import PhysicalQubits
except ImportError:  # pragma: no cover - standalone compatibility
    from logical_worldline import LogicalWorldline
    from physical_qubits import PhysicalQubits


class Corrector:
    def __init__(self, logical_worldline: LogicalWorldline):
        self.logical = logical_worldline

    def apply(self, physical_qubits: PhysicalQubits, syndrome_info: dict):
        idx = syndrome_info.get("error_index")
        if idx is None:
            return physical_qubits

        physical_qubits.qubits[idx] = self.logical.as_vector()[:]
        return physical_qubits
