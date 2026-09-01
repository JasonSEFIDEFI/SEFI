"""
majority_check.py
-----------------
Independent QEC checking method using majority vote.

This provides a second error-detection pathway separate from stabilizers.
"""

def majority_vote_syndrome(qubits):
    """
    qubits: list of 3 state vectors, each [a, b]

    Returns:
        {
            "error_index": 0, 1, 2, or None,
            "logical_value": [1,0] or [0,1],
            "confidence": 1.0 or 0.66
        }
    """

    # Convert state vectors to classical bits for majority logic
    bits = []
    for q in qubits:
        # |0> = [1,0], |1> = [0,1]
        bits.append(0 if q[0] == 1 else 1)

    # Count occurrences
    zeros = bits.count(0)
    ones = bits.count(1)

    # Determine majority logical value
    logical_bit = 0 if zeros > ones else 1
    logical_value = [1,0] if logical_bit == 0 else [0,1]

    # Determine which qubit is wrong
    error_index = None
    for i, b in enumerate(bits):
        if b != logical_bit:
            error_index = i
            break

    # Confidence: 1.0 if unanimous, 0.66 if 2-of-3 majority
    confidence = 1.0 if zeros == 3 or ones == 3 else 0.66

    return {
        "error_index": error_index,
        "logical_value": logical_value,
        "confidence": confidence
    }
