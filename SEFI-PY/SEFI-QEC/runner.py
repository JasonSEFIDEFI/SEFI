"""
runner.py
---------
SEFI-QEC demo pipeline.
"""

from .logical_worldline import LogicalWorldline
from .physical_qubits import PhysicalQubits
from .stabilizers import StabilizerSet
from .syndrome import SyndromeExtractor
from .correction import Corrector
from .benchmark import run_qec_benchmark


def run_sefi_qec_demo():
    print("\n=== SEFI-QEC DEMO START ===\n")

    lw = LogicalWorldline()
    pq = PhysicalQubits(lw)
    print("Logical worldline:", lw.as_vector())
    print("Initial physical qubits:", pq.get_state())

    print("\nInjecting error: X on qubit 1")
    pq.inject_error(1, "X")

    stabs = StabilizerSet()
    stab_results = stabs.check(pq)
    print("Stabilizer results:", stab_results)

    synd = SyndromeExtractor(stabs)
    syndrome_info = synd.extract(pq)
    print("Syndrome:", syndrome_info)

    corr = Corrector(lw)
    corrected = corr.apply(pq, syndrome_info)
    print("Corrected qubits:", corrected.get_state())

    print("\nRunning benchmark (100 trials)...")
    result = run_qec_benchmark(100)
    print("Benchmark:", result)

    print("\n=== SEFI-QEC DEMO COMPLETE ===\n")
    return corrected
