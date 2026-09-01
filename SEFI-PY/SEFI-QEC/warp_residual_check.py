"""
warp_residual_check.py
----------------------
Geometric warp-residual QEC check for SEFI-QEC.

This method evaluates how far each physical qubit's geometry has drifted
from the logical worldline, using SEFI warp vectors.
"""

import math


def vector_distance(v1, v2):
    """Euclidean distance between two 2D state vectors."""
    return math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)


def warp_residual_check(logical_vec, physical_states, warp_vectors):
    """
    logical_vec: [a, b]
    physical_states: list of 3 qubit state vectors
    warp_vectors: list of 3 warp vectors [tangent, normal, binormal]

    Returns:
        {
            "residuals": [float, float, float],
            "max_residual": float,
            "error_index": int or None,
        }
    """

    residuals = []

    for p, w in zip(physical_states, warp_vectors):
        # geometric deviation = distance + warp magnitude
        dist = vector_distance(logical_vec, p)
        warp_mag = abs(w[0]) + abs(w[1]) + abs(w[2])
        residuals.append(dist + warp_mag)

    max_res = max(residuals)
    error_index = residuals.index(max_res) if max_res > 0 else None

    return {
        "residuals": residuals,
        "max_residual": max_res,
        "error_index": error_index,
    }
