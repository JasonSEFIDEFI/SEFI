"""
runner.py
---------
SEFI-QEC demo pipeline.
"""

if __package__ in (None, ""):
    import sys
    from pathlib import Path

    package_dir = Path(__file__).resolve().parent
    repo_root = package_dir.parent
    for base in (str(package_dir), str(repo_root)):
        if base not in sys.path:
            sys.path.insert(0, base)

    from logical_worldline import LogicalWorldline
    from physical_qubits import PhysicalQubits
    from stabilizers import StabilizerSet
    from syndrome import SyndromeExtractor
    from correction import Corrector
    from benchmark import run_qec_benchmark
    from majority_check import majority_vote_syndrome
    from pauli_frame_check import pauli_frame_consistency
    from warp_residual_check import warp_residual_check
    from stabilizer_energy import stabilizer_energy_minimization
else:
    from .logical_worldline import LogicalWorldline
    from .physical_qubits import PhysicalQubits
    from .stabilizers import StabilizerSet
    from .syndrome import SyndromeExtractor
    from .correction import Corrector
    from .benchmark import run_qec_benchmark
    from .majority_check import majority_vote_syndrome
    from .pauli_frame_check import pauli_frame_consistency
    from .warp_residual_check import warp_residual_check
    from .stabilizer_energy import stabilizer_energy_minimization


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

    maj = majority_vote_syndrome(corrected.get_state())
    print("\nMajority-vote check:")
    print("Majority syndrome:", maj)

    applied_errors = ["I", "X", "I"]
    frame_result = pauli_frame_consistency(lw, corrected.get_state(), applied_errors)
    print("\nPauli-frame consistency:", frame_result)

    warp_vectors = [
        [0.0, 0.0, 0.0],
        [0.8, 0.1, 0.0],
        [0.0, 0.0, 0.0],
    ]
    print("\nWarp-residual check:")
    residual = warp_residual_check(lw.as_vector(), pq.get_state(), warp_vectors)
    print("Warp residual:", residual)

    print("\nStabilizer-energy minimization check:")
    energy_result = stabilizer_energy_minimization(
        lw.as_vector(),
        pq.get_state(),
        lambda states: stabs.check_states(states) if hasattr(stabs, "check_states") else stabs.check(pq),
    )
    print("Energy-minimization:", energy_result)

    print("\n=== SEFI-QEC DEMO COMPLETE ===\n")
    return corrected
