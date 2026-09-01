"""
pauli_frame_check.py
--------------------
Pauli-frame consistency check for SEFI-QEC.

We track the intended Pauli frame (what errors we *think* we've applied)
and compare it to the actual physical qubit states to detect mismatches.
"""

try:
    from .logical_worldline import LogicalWorldline
except ImportError:  # pragma: no cover - standalone compatibility
    from logical_worldline import LogicalWorldline


def pauli_frame_consistency(logical: LogicalWorldline, physical_states, applied_errors):
    """
    logical: LogicalWorldline
    physical_states: list of 3 state vectors [a, b]
    applied_errors: list of 3 error labels, e.g. ["I", "X", "Z"]

    Returns:
        {
            "consistent": bool,
            "mismatched_indices": [indices],
            "expected_states": [state vectors],
        }
    """

    # For now, "expected" = logical state with declared errors applied in frame,
    # but since we don't yet simulate full Pauli frames, we treat "I" as
    # "should match logical" and any non-"I" as "may differ".
    expected = []
    logical_vec = logical.as_vector()

    for e in applied_errors:
        if e == "I":
            expected.append(logical_vec[:])
        else:
            # Error present: we allow deviation, but still record logical baseline
            expected.append(logical_vec[:])

    mismatched = []
    for i, (p, exp) in enumerate(zip(physical_states, expected)):
        if p != exp:
            mismatched.append(i)

    return {
        "consistent": len(mismatched) == 0,
        "mismatched_indices": mismatched,
        "expected_states": expected,
    }
