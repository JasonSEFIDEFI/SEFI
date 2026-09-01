"""
warp_mapping.py
---------------
Maps SEFI warp modes to QEC error types.
"""

def warp_to_error_mode(warp_vector):
    """
    warp_vector: [tangent, normal, binormal]
    """
    t, n, b = warp_vector

    if abs(t) > abs(n) and abs(t) > abs(b):
        return "X"
    if abs(n) > abs(t) and abs(n) > abs(b):
        return "Z"
    return "Y"
