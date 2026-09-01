"""
logical_worldline.py
--------------------
Defines the logical qubit as a SEFI worldline.

In SEFI-QEC, the logical worldline represents the protected qubit.
All physical qubits are samples of this underlying geometric entity.
"""

class LogicalWorldline:
    def __init__(self, state=None):
        """
        Logical qubit state.
        Default is |0> represented as [1, 0].
        """
        self.state = state or [1, 0]

    def as_vector(self):
        """
        Returns the logical qubit state vector.
        """
        return self.state

    def describe(self):
        """
        Human-readable description for debugging and demos.
        """
        return "Logical worldline representing the protected qubit."
