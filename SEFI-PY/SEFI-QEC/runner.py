"""
runner.py
---------
SEFI-QEC demo pipeline.

This module ties together:
    - Logical worldline
    - Physical qubits (3-qubit repetition code)
    - Stabilizer checks
    - Syndrome extraction
    - Correction (DEFI realignment)

Running this demo shows the full QEC cycle.
"""

from .logical_worldline import LogicalWorldline
from .physical_qubits import PhysicalQubits
from .stabilizers import StabilizerSet
from .syndrome import SyndromeExtractor
from .correction import Corrector


def run_sefi_qec_demo():
    print("\n=== SEFI-QEC DEMO START ===\n")

    # 1. Logical worldline (protected qubit)
    lw = LogicalWorldline()
    print("Logical worldline state:", lw.as_vector())

    # 2. Encode into 3 physical qubits
    pq = PhysicalQubits(lw)
    print("Initial physical qubits:", pq.get_state())

    # 3. Inject an error (demo: X error on qubit 1)
    print("\nInjecting error: X on qubit 1")
    pq.inject_error(index=1, error_type="X")

    # 4. Stabilizer checks
    stabs = StabilizerSet()
    stab_results = stabs.check(pq)
    print("Stabilizer results:", stab_results)

    # 5. Syndrome extraction
    synd = SyndromeExtractor(stabs)
    syndrome_info = synd.extract(pq)
    print("Syndrome extracted:", syndrome_info)

    # 6. Correction
    corr = Corrector(lw)
    corrected = corr.apply(pq, syndrome_info)
    print("Corrected physical qubits:", corrected.get_state())

    print("\n=== SEFI-QEC DEMO COMPLETE ===\n")
    return corrected
