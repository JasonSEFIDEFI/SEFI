"""
benchmark.py
------------
Runs QEC reliability tests over many trials.
"""

import random
from .logical_worldline import LogicalWorldline
from .physical_qubits import PhysicalQubits
from .stabilizers import StabilizerSet
from .syndrome import SyndromeExtractor
from .correction import Corrector


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
