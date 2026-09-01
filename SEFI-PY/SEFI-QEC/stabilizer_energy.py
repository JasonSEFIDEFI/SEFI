"""
stabilizer_energy.py
--------------------
Stabilizer-energy minimization QEC check.

Each stabilizer violation contributes +1 energy.
The best correction is the one that minimizes total stabilizer energy.
"""

try:
    from .pauli_ops import pauli_x, pauli_z, pauli_y
except ImportError:  # pragma: no cover - standalone compatibility
    from pauli_ops import pauli_x, pauli_z, pauli_y


def apply_pauli(state, error_type):
    if error_type == "X":
        return pauli_x(state)
    if error_type == "Z":
        return pauli_z(state)
    if error_type == "Y":
        return pauli_y(state)
    return state[:]  # identity


def stabilizer_energy(stabilizer_results):
    """
    stabilizer_results: {"Z1Z2": 0/1, "Z2Z3": 0/1}
    Energy = number of violated stabilizers.
    """
    return stabilizer_results["Z1Z2"] + stabilizer_results["Z2Z3"]


def stabilizer_energy_minimization(logical_vec, physical_states, stabilizer_checker):
    """
    Try all possible single-qubit corrections (I, X, Z, Y)
    and choose the one that minimizes stabilizer energy.

    Returns:
        {
            "best_error": ("I"|"X"|"Z"|"Y"),
            "best_index": 0|1|2|None,
            "best_energy": int,
            "energies": list of energies for all trials
        }
    """

    candidates = ["I", "X", "Z", "Y"]
    best_energy = 999
    best_error = None
    best_index = None

    energies = []

    for i in range(3):
        for e in candidates:
            # simulate correction
            trial = [p[:] for p in physical_states]
            trial[i] = apply_pauli(trial[i], e)

            # compute stabilizer energy
            stab = stabilizer_checker(trial)
            energy = stabilizer_energy(stab)
            energies.append((i, e, energy))

            if energy < best_energy:
                best_energy = energy
                best_error = e
                best_index = i

    return {
        "best_error": best_error,
        "best_index": best_index,
        "best_energy": best_energy,
        "energies": energies,
    }
