"""
benchmark.py
------------
Runs QEC reliability tests over many trials.
"""

import importlib.util
import random
import sys
from pathlib import Path

try:
    from .logical_worldline import LogicalWorldline
    from .physical_qubits import PhysicalQubits
    from .stabilizers import StabilizerSet
    from .syndrome import SyndromeExtractor
    from .correction import Corrector
except ImportError:  # pragma: no cover - standalone compatibility
    qec_dir = Path(__file__).resolve().parent / "SEFI-QEC"
    modules = {
        "logical_worldline": qec_dir / "logical_worldline.py",
        "physical_qubits": qec_dir / "physical_qubits.py",
        "stabilizers": qec_dir / "stabilizers.py",
        "syndrome": qec_dir / "syndrome.py",
        "correction": qec_dir / "correction.py",
    }

    for name, path in modules.items():
        spec = importlib.util.spec_from_file_location(f"sefi_qec_{name}", path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Could not load SEFI-QEC module: {name}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[f"sefi_qec_{name}"] = module
        spec.loader.exec_module(module)

    LogicalWorldline = sys.modules["sefi_qec_logical_worldline"].LogicalWorldline
    PhysicalQubits = sys.modules["sefi_qec_physical_qubits"].PhysicalQubits
    StabilizerSet = sys.modules["sefi_qec_stabilizers"].StabilizerSet
    SyndromeExtractor = sys.modules["sefi_qec_syndrome"].SyndromeExtractor
    Corrector = sys.modules["sefi_qec_correction"].Corrector


def run_qec_benchmark(trials=1000):
    success = 0

    for _ in range(trials):
        lw = LogicalWorldline()
        pq = PhysicalQubits(lw)
        stabs = StabilizerSet()
        synd = SyndromeExtractor(stabs)
        corr = Corrector(lw)

        # random error
        idx = random.choice([0, 1, 2])
        etype = random.choice(["X", "Z", "Y"])
        pq.inject_error(idx, etype)

        syndrome_info = synd.extract(pq)
        corrected = corr.apply(pq, syndrome_info)

        if corrected.get_state() == [lw.as_vector()] * 3:
            success += 1

    return {
        "trials": trials,
        "success_rate": success / trials
    }
